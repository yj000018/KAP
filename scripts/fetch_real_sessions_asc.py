#!/usr/bin/env python3
"""
Fetch real Manus sessions using order=asc (oldest first = real sessions).
Stop when hitting Wide Research Subtasks (means we've reached recent noise).
Max 50 API calls — very conservative.
"""
import requests, json, time, datetime
from pathlib import Path

MANUS_KEY = "sk-TEKENLb_4FM1xUD0skvl7Y5bxdg_ZwSBn93f4UyT3obza8szuxS1v4AFcs5iokvaLur6obq0SlG80yIIr-Zu_rKeVdze"
BASE = "https://api.manus.im"
HEADERS = {"x-manus-api-key": MANUS_KEY}

MAX_CALLS = 50
real_sessions = []
last_id = None
call_count = 0
page = 0
stop_reason = "max_calls"

print("Fetching real sessions (order=asc, oldest first)...")

while call_count < MAX_CALLS:
    params = {"page_size": 20, "order": "asc"}
    if last_id:
        params["last_id"] = last_id

    try:
        r = requests.get(f"{BASE}/v2/task.list", headers=HEADERS, params=params, timeout=10)
    except Exception as e:
        print(f"  Network error: {e}")
        time.sleep(5)
        continue

    call_count += 1

    if r.status_code == 429 or (r.status_code == 200 and '"rate_limit"' in r.text):
        print(f"  Rate limit at call {call_count}. Stopping.")
        stop_reason = "rate_limit"
        break

    if not r.ok:
        print(f"  Error {r.status_code}: {r.text[:200]}")
        break

    data = r.json()
    if not data.get("ok", True):
        err = data.get("error", {})
        if "rate" in str(err).lower():
            print(f"  Rate limit (ok=false) at call {call_count}. Stopping.")
            stop_reason = "rate_limit"
            break
        print(f"  API error: {err}")
        break

    tasks = data.get("data", [])
    has_more = data.get("has_more", False)

    if not tasks:
        stop_reason = "no_more_tasks"
        break

    last_id = tasks[-1].get("id")
    page += 1

    wide_count = 0
    real_count = 0
    all_wide = True

    for t in tasks:
        title = t.get("title", "")
        credits = t.get("credit_usage", 0)
        is_wide = "Wide Research" in title or ("Subtask" in title and credits <= 4)

        if is_wide:
            wide_count += 1
        else:
            all_wide = False
            real_count += 1
            real_sessions.append({
                "id": t.get("id"),
                "title": title,
                "status": t.get("status"),
                "credit_usage": credits,
                "created_at": t.get("created_at", ""),
                "task_url": t.get("task_url", ""),
            })

    print(f"  Page {page} (call {call_count}): {real_count} real, {wide_count} wide | total: {len(real_sessions)}")

    # If entire page is Wide Research, we've hit the noise zone — stop
    if all_wide:
        print("  Full page of Wide Research Subtasks — reached noise zone. Stopping.")
        stop_reason = "reached_wide_research_zone"
        break

    if not has_more:
        stop_reason = "no_more_pages"
        break

    time.sleep(0.3)

# Save results
OUT = Path("/home/ubuntu/KAP/02_Source_Acquisition/WP2-M8C_Direct_Manus_API_Sessions_Coverage_Missing_Recovery/02_MANUS_API_SESSION_INDEX")
OUT.mkdir(parents=True, exist_ok=True)

result = {
    "generated": datetime.datetime.now().isoformat(),
    "method": "order=asc (oldest first)",
    "stop_reason": stop_reason,
    "total_real_sessions": len(real_sessions),
    "api_calls_used": call_count,
    "pages_fetched": page,
    "sessions": real_sessions
}

with open(OUT / "KAP-WP2-M8C-Real-Sessions-ASC.json", "w") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

# Markdown table
lines = [
    "# KAP WP2-M8C — Real Manus Sessions (order=asc, oldest first)\n\n",
    f"**Generated:** {result['generated']}  \n",
    f"**Method:** order=asc — oldest sessions first  \n",
    f"**Stop reason:** {stop_reason}  \n",
    f"**Total real sessions:** {len(real_sessions)}  \n",
    f"**API calls used:** {call_count}  \n\n",
    "| # | title | credits | date | url |\n",
    "|---|---|---:|---|---|\n"
]
for i, s in enumerate(real_sessions, 1):
    date = s['created_at'][:10] if s['created_at'] else ''
    url = s['task_url'] or ''
    title = s['title'][:65].replace('|', '/')
    lines.append(f"| {i} | {title} | {s['credit_usage']} | {date} | [link]({url}) |\n")

with open(OUT / "KAP-WP2-M8C-Real-Sessions-ASC.md", "w") as f:
    f.writelines(lines)

print(f"\n=== DONE ===")
print(f"Real sessions found: {len(real_sessions)}")
print(f"API calls used: {call_count}")
print(f"Stop reason: {stop_reason}")

# Show first 30
print("\nFirst 30 real sessions:")
for s in real_sessions[:30]:
    print(f"  [{s['credit_usage']}cr] {s['title'][:65]} ({s['created_at'][:10]})")
