#!/usr/bin/env python3
"""
KAP Archive Pipeline — Enhanced v3
Single-file factsheet: YAML metadata + Session Card + Verbatim Archive
Output: {uid}_factsheet.md
"""

import os, sys, json, time, re, subprocess, requests, datetime
from pathlib import Path
from openai import OpenAI

# Config
API_KEY = os.environ.get("MANUS_API_KEY", "")
BASE = "https://api.manus.im/v2"
HEADERS = {"x-manus-api-key": API_KEY}
KAP_DIR = Path("/home/ubuntu/KAP/03_Archived_Sessions/YOS")
KAP_ROOT = Path("/home/ubuntu/KAP")

# LLM
client = OpenAI()
MODEL = "claude-sonnet-4-6"

CHECK_CHARS = ["[✓]", "✓", "✔", "☑", "✅"]
SKIP_TITLE_PATTERNS = ["Wide Research Subtask", "Parallel Research Subtask", "Research Subtask"]

# ─── CARD PROMPT ──────────────────────────────────────────────────────────────
CARD_PROMPT = """You are a KAP session archivist for Y-OS (Yannick's cognitive operating system).
Analyze this Manus session and produce a structured Session Card.

Session UID: {uid}
Session Title: {title}
Date: {date}
Session URL: https://manus.im/app/{uid}

Transcript (up to 30 turns):
{transcript}

Generate ONLY the Session Card section below (no YAML, no verbatim — those are added separately).
Use EXACTLY this structure:

## 📋 SESSION CARD

### 🧭 Executive Summary
[3 sentences max. Dense. What happened, what was produced, what matters.]

### 🎯 Context & Intent
[Why this session existed. What the user wanted to achieve.]

### ✅ What Was Done
[Numbered list of concrete actions taken]

### 💡 Key Insights
[Bullet list: key decisions made + important learnings/discoveries]

### 📦 Outputs Produced
[Bullet list with type prefix: **[website]**, **[doc]**, **[script]**, **[data]**, **[skill]**, **[design]**]
[Format: **[type]** `filename/URL`: description]

### ⚠️ Open Items & Blockers
[Bullet list. Mark uncertainty with [INCERTAIN]]

### 🔁 Next Steps
[Numbered list of actionable next steps]

### 🔗 Links & References
[Bullet list of all URLs, file paths, referenced sessions, artifacts]
[Format: - 🌐 URL | 📁 file | 🔗 session:{uid} | 📄 artifact]

### 🧠 Resume Hint
[Single sentence. What the next agent needs to know to continue without losing context.]

### 🏷️ Tags
`tag-1` `tag-2` `tag-3` `tag-4` `tag-5`
[4-6 kebab-case tags]

---
ALSO extract these fields for metadata (return as a JSON block at the very end, after ---METADATA---):
{{
  "inferred_title": "clean descriptive title (max 80 chars)",
  "project": "main project name",
  "language": "fr|en|mixed",
  "depth": "quick|moderate|substantial|deep",
  "length": "short|medium|long",
  "llm_used": "inferred LLM if mentioned, else unknown",
  "referenced_sessions": ["uid1", "uid2"],
  "referenced_artifacts": ["filename1", "url1"],
  "referenced_urls": ["url1", "url2"],
  "input_files": ["file1"]
}}
"""

# ─── HELPERS ──────────────────────────────────────────────────────────────────
def is_already_archived(title):
    t = title.strip()
    for c in CHECK_CHARS:
        if t.startswith(c) or t.endswith(c.strip()):
            return True
    return False

def is_subtask(title):
    for p in SKIP_TITLE_PATTERNS:
        if p.lower() in title.lower():
            return True
    return False

def factsheet_exists(uid):
    return (KAP_DIR / f"{uid}_factsheet.md").exists()

def fetch_messages(task_id, limit=100):
    r = requests.get(f"{BASE}/task.listMessages",
                     headers=HEADERS,
                     params={"task_id": task_id, "limit": limit, "order": "asc"},
                     timeout=20)
    if r.status_code != 200:
        return []
    data = r.json()
    if isinstance(data, list):
        return data
    return data.get("messages", data.get("data", {}).get("messages", []) if isinstance(data.get("data"), dict) else data.get("data", []))

def build_transcript(messages):
    lines = []
    for m in messages:
        mtype = m.get("type", "")
        content = ""
        ts = m.get("timestamp", "")
        ts_str = ""
        if ts:
            try:
                ts_int = int(ts)
                if ts_int > 1e12:
                    ts_int //= 1000
                ts_str = datetime.datetime.fromtimestamp(ts_int).strftime("%Y-%m-%d %H:%M")
            except:
                pass

        if mtype in ("user_message", "human_message"):
            inner = m.get("user_message") or m.get("human_message") or {}
            if isinstance(inner, dict):
                content = inner.get("content", "")
            elif isinstance(inner, str):
                content = inner
            if isinstance(content, list):
                content = " ".join(b.get("text", "") for b in content if isinstance(b, dict))
            role = "USER"
        elif mtype == "assistant_message":
            inner = m.get("assistant_message", {})
            content = inner.get("content", "") if isinstance(inner, dict) else str(inner)
            role = "MANUS"
        else:
            continue

        if content and str(content).strip():
            prefix = f"[{ts_str}] " if ts_str else ""
            lines.append(f"**{prefix}{role}:** {str(content).strip()[:800]}")

    return "\n\n".join(lines)

def extract_date(messages):
    for m in messages:
        ts = m.get("timestamp")
        if ts:
            try:
                ts_int = int(ts)
                if ts_int > 1e12:
                    ts_int //= 1000
                return datetime.datetime.fromtimestamp(ts_int).strftime("%Y-%m-%d")
            except:
                pass
    return datetime.date.today().isoformat()

def generate_card_and_meta(uid, title, transcript, date):
    prompt = CARD_PROMPT.format(uid=uid, title=title, transcript=transcript[:8000], date=date)
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2500
    )
    content = resp.choices[0].message.content
    if not content:
        raise ValueError("LLM returned empty content")

    # Split card from metadata JSON
    card_part = content
    meta = {}
    if "---METADATA---" in content:
        parts = content.split("---METADATA---", 1)
        card_part = parts[0].strip()
        try:
            json_str = parts[1].strip()
            # Extract JSON block
            json_match = re.search(r'\{.*\}', json_str, re.DOTALL)
            if json_match:
                meta = json.loads(json_match.group())
        except:
            pass

    return card_part, meta

def build_factsheet(uid, title, date, card_part, meta, transcript, messages):
    """Assemble the 3-layer factsheet."""
    session_url = f"https://manus.im/app/{uid}"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    # Use inferred title if available and better than UID
    display_title = meta.get("inferred_title") or title
    if display_title == uid:
        display_title = title

    # ── Layer 1: YAML front matter (metadata) ──
    yaml_meta = f"""---
uid: {uid}
session_url: {session_url}
session_title: "{display_title}"
date: {date}
project: "{meta.get('project', 'unknown')}"
language: {meta.get('language', 'unknown')}
depth: {meta.get('depth', 'unknown')}
length: {meta.get('length', 'unknown')}
llm_used: {meta.get('llm_used', 'unknown')}
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: {now}
referenced_sessions: {json.dumps(meta.get('referenced_sessions', []))}
referenced_artifacts: {json.dumps(meta.get('referenced_artifacts', []))}
referenced_urls: {json.dumps(meta.get('referenced_urls', []))}
input_files: {json.dumps(meta.get('input_files', []))}
message_count: {len(messages)}
---"""

    # ── Layer 2: Session Card ──
    header = f"# {display_title}\n\n> **Session:** [{uid}]({session_url}) | **Date:** {date} | **Project:** {meta.get('project', '—')} | **Language:** {meta.get('language', '—')}\n"

    # ── Layer 3: Verbatim Archive ──
    verbatim = f"""---

## 📜 VERBATIM ARCHIVE

> Raw transcript — {len(messages)} messages — {date}

{transcript}
"""

    return f"{yaml_meta}\n\n{header}\n{card_part}\n\n{verbatim}"

def update_title(task_id, new_title):
    r = requests.post(f"{BASE}/task.update",
                      headers={**HEADERS, "Content-Type": "application/json"},
                      json={"task_id": task_id, "title": new_title},
                      timeout=15)
    return r.status_code == 200

def git_commit(uid, title):
    try:
        subprocess.run(["git", "add", f"03_Archived_Sessions/YOS/{uid}_factsheet.md"],
                       cwd=KAP_ROOT, check=True, capture_output=True)
        msg = f"KAP: factsheet {uid[:12]} — {title[:50]}"
        subprocess.run(["git", "commit", "-m", msg],
                       cwd=KAP_ROOT, check=True, capture_output=True)
        return True
    except Exception as e:
        print(f"  Git error: {e}")
        return False

# ─── MAIN PROCESS ─────────────────────────────────────────────────────────────
def process_session(uid, title):
    print(f"\n→ {title[:65]}")
    print(f"  UID: {uid}")

    if is_already_archived(title):
        print(f"  SKIP — [✓] already in title")
        return {"uid": uid, "title": title, "status": "skipped_check"}

    if is_subtask(title):
        print(f"  SKIP — subtask")
        return {"uid": uid, "title": title, "status": "skipped_subtask"}

    if factsheet_exists(uid):
        print(f"  SKIP — factsheet already exists")
        return {"uid": uid, "title": title, "status": "skipped_exists"}

    # Fetch messages
    messages = fetch_messages(uid)
    if not messages:
        print(f"  FAIL — no messages accessible")
        return {"uid": uid, "title": title, "status": "failed_no_messages"}

    print(f"  Messages: {len(messages)}")
    transcript = build_transcript(messages)
    date = extract_date(messages)

    # Generate card + metadata
    try:
        card_part, meta = generate_card_and_meta(uid, title, transcript, date)
    except Exception as e:
        print(f"  FAIL — LLM: {e}")
        return {"uid": uid, "title": title, "status": f"failed_llm: {e}"}

    # Use inferred title if better
    display_title = meta.get("inferred_title") or title
    if display_title and display_title != uid:
        print(f"  Title: {display_title[:60]}")
    else:
        display_title = title

    # Assemble factsheet
    factsheet = build_factsheet(uid, display_title, date, card_part, meta, transcript, messages)

    # Save
    KAP_DIR.mkdir(parents=True, exist_ok=True)
    path = KAP_DIR / f"{uid}_factsheet.md"
    path.write_text(factsheet, encoding="utf-8")
    print(f"  Saved: {path.name}")

    # Git commit
    committed = git_commit(uid, display_title)
    print(f"  Git: {'OK' if committed else 'FAILED'}")

    # Update Manus title with [✓] prefix
    new_title = f"[✓] {display_title}"
    title_updated = update_title(uid, new_title)
    print(f"  Manus title → '[✓] {display_title[:45]}': {'OK' if title_updated else 'FAILED'}")

    return {
        "uid": uid,
        "title": display_title,
        "new_title": new_title,
        "date": date,
        "factsheet_path": str(path),
        "committed": committed,
        "title_updated": title_updated,
        "status": "processed"
    }

# ─── ENTRY POINT ──────────────────────────────────────────────────────────────
def main():
    targets = sys.argv[1:]
    if not targets:
        print("Usage: python3 run_pipeline_enhanced.py <uid_or_url> [...]")
        sys.exit(1)

    # Extract UIDs from URLs
    uids = []
    for t in targets:
        uid = t.rstrip("/").split("/")[-1] if "manus.im/app/" in t else t.strip()
        uids.append(uid)

    print(f"KAP Archive Pipeline — Enhanced v3 (Factsheet)")
    print(f"Sessions: {len(uids)}")
    print("=" * 60)

    # Resolve titles from task.list
    uid_to_title = {}
    last_id = None
    for _ in range(20):
        params = {"limit": 100, "order": "desc"}
        if last_id:
            params["last_id"] = last_id
        r = requests.get(f"{BASE}/task.list", headers=HEADERS, params=params, timeout=20)
        if r.status_code != 200:
            break
        raw = r.json()
        items = raw if isinstance(raw, list) else (raw.get("data") if isinstance(raw.get("data"), list) else raw.get("data", {}).get("items", []) if isinstance(raw.get("data"), dict) else [])
        if not items:
            break
        for item in items:
            iid = item.get("id", "")
            if iid in uids:
                uid_to_title[iid] = item.get("title", iid)
        if all(u in uid_to_title for u in uids):
            break
        new_last = items[-1].get("id") if items else None
        has_more = (raw.get("has_more", False) if isinstance(raw, dict) else len(items) == 100)
        if not has_more or new_last == last_id:
            break
        last_id = new_last
        time.sleep(0.2)

    results = []
    for uid in uids:
        title = uid_to_title.get(uid, uid)
        result = process_session(uid, title)
        results.append(result)
        time.sleep(1)

    # Push
    print("\nPushing to GitHub...")
    try:
        subprocess.run(["git", "push", "origin", "main"], cwd=KAP_ROOT, check=True, capture_output=True)
        print("Push: OK")
    except Exception as e:
        print(f"Push failed: {e}")

    # Summary
    print("\n" + "=" * 60)
    processed = [r for r in results if r["status"] == "processed"]
    skipped   = [r for r in results if r["status"].startswith("skipped")]
    failed    = [r for r in results if r["status"].startswith("failed")]
    print(f"Processed: {len(processed)} | Skipped: {len(skipped)} | Failed: {len(failed)}")
    for r in processed:
        print(f"  ✓ {r['uid'][:12]} | {r['title'][:55]}")
    for r in skipped:
        print(f"  ↷ {r['uid'][:12]} | {r['title'][:45]} [{r['status']}]")
    for r in failed:
        print(f"  ✗ {r['uid'][:12]} | {r['title'][:45]} [{r['status']}]")

    # Save report
    report = KAP_ROOT / "03_Archived_Sessions/YOS/pipeline_report.json"
    report.write_text(json.dumps(results, indent=2, ensure_ascii=False))
    print(f"\nReport: {report}")

if __name__ == "__main__":
    main()
