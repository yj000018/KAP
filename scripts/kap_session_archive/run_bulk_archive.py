#!/usr/bin/env python3
"""
KAP Bulk Archive Pipeline
- Fetches all accessible Manus sessions via API
- Skips sessions already marked with ✓ or check variants in title
- Skips sessions already in KAP Git (by UID)
- Generates MD session card via LLM
- Commits to Git
- Adds ✓ prefix to title in Manus after successful archiving
"""

import os, sys, json, time, re, subprocess, requests
from pathlib import Path
from openai import OpenAI

# Config
API_KEY = "sk-TEKENLb_4FM1xUD0skvl7Y5bxdg_ZwSBn93f4UyT3obza8szuxS1v4AFcs5iokvaLur6obq0SlG80yIIr-Zu_rKeVdze"
BASE = "https://api.manus.im/v2"
HEADERS = {"x-manus-api-key": API_KEY}
KAP_DIR = Path("/home/ubuntu/KAP/03_Archived_Sessions/YOS")
KAP_ROOT = Path("/home/ubuntu/KAP")

# LLM client (sandbox proxy)
client = OpenAI()
MODEL = "claude-sonnet-4-5"

# Check characters to detect already-archived sessions
CHECK_CHARS = ["✓", "✔", "☑", "✅", "Check ", "check "]

SKIP_PATTERNS = ["Wide Research Subtask", "Parallel Research Subtask", "Research Subtask"]

def is_already_archived(title):
    """Check if session title already has a check mark."""
    for c in CHECK_CHARS:
        if title.startswith(c) or title.endswith(c.strip()):
            return True
    return False

def get_check_char_used(sessions):
    """Detect which check character is already in use."""
    for s in sessions:
        title = s.get("title", "")
        for c in CHECK_CHARS:
            if title.startswith(c):
                return c
    return "✓ "  # default

def card_exists(uid):
    """Check if session card already exists in KAP."""
    return (KAP_DIR / f"{uid}_session_card.md").exists()

def fetch_messages(task_id, limit=100):
    """Fetch messages for a task."""
    r = requests.get(f"{BASE}/task.listMessages",
                     headers=HEADERS,
                     params={"task_id": task_id, "limit": limit, "order": "asc"},
                     timeout=20)
    if r.status_code != 200:
        return []
    data = r.json()
    if isinstance(data, dict):
        inner = data.get("data", data)
        if isinstance(inner, list):
            return inner
        return inner.get("items", [])
    return data if isinstance(data, list) else []

def build_transcript(messages):
    """Build a readable transcript from messages."""
    lines = []
    for m in messages:
        role = m.get("role", m.get("type", "unknown"))
        content = ""
        if isinstance(m.get("content"), str):
            content = m["content"]
        elif isinstance(m.get("content"), list):
            for block in m["content"]:
                if isinstance(block, dict) and block.get("type") == "text":
                    content += block.get("text", "")
        if content.strip():
            lines.append(f"[{role.upper()}]: {content.strip()[:500]}")
    return "\n\n".join(lines[:30])  # max 30 turns

def generate_card(uid, title, transcript):
    """Generate session card via LLM."""
    prompt = f"""You are a KAP session archivist. Generate a structured session card in Markdown for this Manus session.

Session ID: {uid}
Session Title: {title}

Transcript (excerpt):
{transcript}

Generate a session card with these sections:
# {title}
**UID:** {uid}
**Date:** [extract from transcript or use today]
**Project:** [main project]
**Themes:** [2-4 key themes]

## Executive Summary
[2-3 sentences]

## What Was Done
[bullet list]

## Key Decisions
[bullet list]

## Outputs Produced
[bullet list]

## Open Questions / Next Steps
[bullet list]

## Resume Hint
[1 sentence for next agent to continue]
"""
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1500
    )
    return resp.choices[0].message.content

def update_title(task_id, new_title):
    """Update task title in Manus."""
    r = requests.post(f"{BASE}/task.update",
                      headers={**HEADERS, "Content-Type": "application/json"},
                      json={"task_id": task_id, "title": new_title},
                      timeout=15)
    return r.status_code == 200

def git_commit(uid, title):
    """Add and commit the session card to Git."""
    try:
        subprocess.run(["git", "add", f"03_Archived_Sessions/YOS/{uid}_session_card.md"],
                       cwd=KAP_ROOT, check=True, capture_output=True)
        msg = f"KAP: archive session {uid[:12]} — {title[:50]}"
        subprocess.run(["git", "commit", "-m", msg],
                       cwd=KAP_ROOT, check=True, capture_output=True)
        return True
    except Exception as e:
        print(f"  Git error: {e}")
        return False

def main():
    KAP_DIR.mkdir(parents=True, exist_ok=True)

    # Fetch all accessible sessions
    print("Fetching sessions from API...")
    all_sessions = []
    last_id = None
    page = 0

    while page < 50:
        params = {"limit": 100, "order": "desc"}
        if last_id:
            params["last_id"] = last_id
        r = requests.get(f"{BASE}/task.list", headers=HEADERS, params=params, timeout=20)
        if r.status_code != 200:
            print(f"API error: {r.status_code}")
            break
        raw = r.json()
        if isinstance(raw, list):
            items = raw
            has_more = len(items) == 100
        elif isinstance(raw, dict):
            inner = raw.get("data", raw)
            items = inner.get("items", inner) if isinstance(inner, dict) else inner
            has_more = inner.get("has_more", False) if isinstance(inner, dict) else len(items) == 100
        else:
            break

        if not items:
            break

        for item in items:
            title = item.get("title", "")
            if not any(skip in title for skip in SKIP_PATTERNS):
                all_sessions.append(item)

        new_last_id = items[-1].get("id") if items else None
        print(f"  Page {page+1}: {len(all_sessions)} real sessions so far")

        if not has_more or new_last_id == last_id:
            break
        last_id = new_last_id
        page += 1
        time.sleep(0.3)

    print(f"\nTotal real sessions found: {len(all_sessions)}")

    # Detect check character in use
    check_char = get_check_char_used(all_sessions)
    print(f"Check character in use: '{check_char.strip()}'")

    # Categorize
    already_archived = [s for s in all_sessions if is_already_archived(s.get("title", ""))]
    to_process = [s for s in all_sessions if not is_already_archived(s.get("title", ""))
                  and not card_exists(s.get("id", ""))]
    already_in_kap = [s for s in all_sessions if not is_already_archived(s.get("title", ""))
                      and card_exists(s.get("id", ""))]

    print(f"\nAlready archived (✓ in title): {len(already_archived)}")
    print(f"Already in KAP Git (no ✓): {len(already_in_kap)}")
    print(f"To process: {len(to_process)}")

    # Process
    processed = []
    failed = []

    for i, session in enumerate(to_process):
        uid = session.get("id")
        title = session.get("title", "Untitled")
        print(f"\n[{i+1}/{len(to_process)}] Processing: {title[:60]}...")

        # Fetch messages
        messages = fetch_messages(uid)
        if not messages:
            print(f"  No messages accessible — skipping")
            failed.append({"uid": uid, "title": title, "reason": "no_messages"})
            continue

        transcript = build_transcript(messages)

        # Generate card
        try:
            card = generate_card(uid, title, transcript)
        except Exception as e:
            print(f"  LLM error: {e}")
            failed.append({"uid": uid, "title": title, "reason": f"llm_error: {e}"})
            continue

        # Save card
        card_path = KAP_DIR / f"{uid}_session_card.md"
        card_path.write_text(card)
        print(f"  Card saved: {card_path.name}")

        # Git commit
        committed = git_commit(uid, title)
        print(f"  Git commit: {'OK' if committed else 'FAILED'}")

        # Update title with check
        new_title = f"{check_char}{title}" if not title.startswith(check_char) else title
        title_updated = update_title(uid, new_title)
        print(f"  Title updated to '{new_title[:50]}': {'OK' if title_updated else 'FAILED'}")

        processed.append({
            "uid": uid,
            "title": title,
            "new_title": new_title,
            "card_path": str(card_path),
            "committed": committed,
            "title_updated": title_updated
        })
        time.sleep(1)

    # Git push
    print("\nPushing to GitHub...")
    try:
        subprocess.run(["git", "push", "origin", "main"],
                       cwd=KAP_ROOT, check=True, capture_output=True)
        print("Push: OK")
    except Exception as e:
        print(f"Push failed: {e}")

    # Report
    print("\n" + "="*60)
    print("BULK ARCHIVE REPORT")
    print("="*60)
    print(f"Total sessions seen:        {len(all_sessions)}")
    print(f"Already archived (✓):       {len(already_archived)}")
    print(f"Already in KAP Git:         {len(already_in_kap)}")
    print(f"Processed this run:         {len(processed)}")
    print(f"Failed:                     {len(failed)}")

    if processed:
        print("\n✓ PROCESSED:")
        for p in processed:
            status = "✓" if p["committed"] else "⚠"
            print(f"  {status} {p['uid'][:12]} | {p['title'][:60]}")

    if failed:
        print("\n✗ FAILED:")
        for f in failed:
            print(f"  ✗ {f['uid'][:12]} | {f['title'][:50]} | {f['reason']}")

    # Save report
    report = {
        "total_seen": len(all_sessions),
        "already_archived": len(already_archived),
        "already_in_kap": len(already_in_kap),
        "processed": processed,
        "failed": failed,
        "check_char_used": check_char.strip()
    }
    report_path = KAP_ROOT / "03_Archived_Sessions/YOS/bulk_archive_report.json"
    report_path.write_text(json.dumps(report, indent=2))
    print(f"\nReport saved: {report_path}")

if __name__ == "__main__":
    main()
