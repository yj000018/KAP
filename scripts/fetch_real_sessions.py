#!/usr/bin/env python3
"""
Fetch real Manus sessions — skip Wide Research Subtasks entirely.
Stop after finding 200 real sessions OR hitting rate limit.
Max 150 API calls to stay safe.
"""
import requests, json, time, datetime
from pathlib import Path

MANUS_KEY = "sk-TEKENLb_4FM1xUD0skvl7Y5bxdg_ZwSBn93f4UyT3obza8szuxS1v4AFcs5iokvaLur6obq0SlG80yIIr-Zu_rKeVdze"
BASE = "https://api.manus.im"
HEADERS = {"x-manus-api-key": MANUS_KEY}

SKIP_TITLES = {"Wide Research Subtask", "wide research subtask"}
MAX_CALLS = 150
TARGET_REAL = 200

real_sessions = []
last_id = None
call_count = 0
page = 0

print("Fetching real sessions (skipping Wide Research Subtasks)...")

while call_count < MAX_CALLS and len(real_sessions) < TARGET_REAL:
    params = {"page_size": 20}
    if last_id:
        params["last_id"] = last_id

    try:
        r = requests.get(f"{BASE}/v2/task.list", headers=HEADERS, params=params, timeout=10)
    except Exception as e:
        print(f"  Network error: {e}")
        time.sleep(5)
        continue

    call_count += 1

    if r.status_code == 429 or (r.status_code == 200 and "rate_limit" in r.text.lower()):
        print(f"  Rate limit hit at call {call_count}. Waiting 60s...")
        time.sleep(60)
        continue

    if r.status_code != 200:
        print(f"  Error {r.status_code}: {r.text[:200]}")
        break

    data = r.json()
    if not data.get("ok", True) and "rate" in str(data).lower():
        print(f"  Rate limit (ok=false) at call {call_count}. Waiting 60s...")
        time.sleep(60)
        continue

    tasks = data.get("data", [])
    has_more = data.get("has_more", False)

    if not tasks:
        print("  No more tasks.")
        break

    last_id = tasks[-1].get("id")
    page += 1

    wide_count = 0
    real_count = 0
    for t in tasks:
        title = t.get("title", "")
        credits = t.get("credit_usage", 0)
        if "Wide Research" in title or "Subtask" in title or credits <= 4:
            wide_count += 1
            continue
        real_count += 1
        real_sessions.append({
            "id": t.get("id"),
            "title": title,
            "status": t.get("status"),
            "credit_usage": credits,
            "created_at": t.get("created_at", ""),
            "task_url": t.get("task_url", ""),
        })

    print(f"  Page {page} (call {call_count}): {wide_count} wide, {real_count} real | total real: {len(real_sessions)}")

    if not has_more:
        print("  No more pages.")
        break

    # Small delay to avoid rate limit
    time.sleep(0.5)

# Save results
OUT = Path("/home/ubuntu/KAP/02_Source_Acquisition/WP2-M8C_Direct_Manus_API_Sessions_Coverage_Missing_Recovery")
OUT.mkdir(parents=True, exist_ok=True)

result = {
    "generated": datetime.datetime.now().isoformat(),
    "total_real_sessions": len(real_sessions),
    "api_calls_used": call_count,
    "pages_fetched": page,
    "sessions": real_sessions
}

with open(OUT / "02_MANUS_API_SESSION_INDEX" / "KAP-WP2-M8C-Real-Sessions-Only.json", "w") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

# Markdown table
lines = [
    "# KAP WP2-M8C — Real Manus Sessions (Non-Wide-Research)\n",
    f"**Generated:** {result['generated']}  \n",
    f"**Total real sessions found:** {len(real_sessions)}  \n",
    f"**API calls used:** {call_count}  \n\n",
    "| # | title | credits | date | url |\n",
    "|---|---|---:|---|---|\n"
]
for i, s in enumerate(real_sessions, 1):
    date = s['created_at'][:10] if s['created_at'] else ''
    url = s['task_url'] or ''
    lines.append(f"| {i} | {s['title'][:60]} | {s['credit_usage']} | {date} | [link]({url}) |\n")

with open(OUT / "02_MANUS_API_SESSION_INDEX" / "KAP-WP2-M8C-Real-Sessions-Only.md", "w") as f:
    f.writelines(lines)

print(f"\n=== DONE ===")
print(f"Real sessions found: {len(real_sessions)}")
print(f"API calls used: {call_count}")
print(f"Saved to: {OUT}/02_MANUS_API_SESSION_INDEX/")
