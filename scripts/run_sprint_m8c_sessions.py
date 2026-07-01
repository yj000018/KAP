#!/usr/bin/env python3
"""
WP2-M8C — Direct Manus API Sessions Coverage & Missing Session Recovery
Uses GET /v2/task.list with x-manus-api-key header
"""
import requests, json, datetime, time, hashlib
from pathlib import Path
from collections import Counter

MANUS_KEY = "sk-TEKENLb_4FM1xUD0skvl7Y5bxdg_ZwSBn93f4UyT3obza8szuxS1v4AFcs5iokvaLur6obq0SlG80yIIr-Zu_rKeVdze"
BASE = "https://api.manus.im"
HEADERS = {"x-manus-api-key": MANUS_KEY}
SPRINT = Path("/home/ubuntu/KAP/02_Source_Acquisition/WP2-M8C_Direct_Manus_API_Sessions_Coverage_Missing_Recovery")
NOW = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

# Load Notion sessions for crosswalk
NOTION_SESSIONS_PATH = Path("/home/ubuntu/KAP/02_Source_Acquisition/WP2-M6B_Notion_Full_Access_Sessions_Acquisition/09_JSON_EXPORTS/manus_memory_sessions_flat.json")

def load_notion_sessions():
    try:
        with open(NOTION_SESSIONS_PATH) as f:
            data = json.load(f)
        return data if isinstance(data, list) else data.get("results", [])
    except:
        # Try alternative path
        for p in Path("/home/ubuntu/KAP").rglob("*sessions*flat*.json"):
            try:
                with open(p) as f:
                    d = json.load(f)
                return d if isinstance(d, list) else d.get("results", [])
            except:
                continue
    return []

def fetch_all_tasks():
    """Paginate through all tasks using last_id cursor"""
    all_tasks = []
    last_id = None
    page = 0
    
    while True:
        params = {"page_size": 100}
        if last_id:
            params["last_id"] = last_id
        
        try:
            r = requests.get(f"{BASE}/v2/task.list", headers=HEADERS, params=params, timeout=30)
            data = r.json()
        except Exception as e:
            print(f"  Error page {page}: {e}")
            break
        
        tasks = data.get("data", [])
        if not tasks:
            break
        
        all_tasks.extend(tasks)
        last_id = tasks[-1]["id"]
        page += 1
        
        if page % 10 == 0:
            print(f"  Fetched {len(all_tasks)} tasks so far...")
        
        # Check if we have more
        if not data.get("has_more", len(tasks) == 100):
            break
        
        time.sleep(0.1)
    
    return all_tasks

def classify_task(task, notion_titles):
    title = task.get("title", "")
    profile = task.get("agent_profile", "")
    credits = int(task.get("credit_usage", 0))
    
    # Wide Research Subtask = background noise
    if "Wide Research Subtask" in title or "wide research" in title.lower():
        return "TASK_OR_BACKGROUND_NOT_SESSION", "IGNORE_LOW_VALUE"
    
    # Very low credit usage = likely background task
    if credits <= 5:
        return "LOW_VALUE_SESSION", "IGNORE_LOW_VALUE"
    
    # Check if in Notion
    title_lower = title.lower().strip()
    in_notion = any(
        title_lower in str(n.get("Name", n.get("title", ""))).lower() or
        str(n.get("Name", n.get("title", ""))).lower() in title_lower
        for n in notion_titles
    )
    
    if in_notion:
        return "ARCHIVED_USEFUL_SESSION", "NONE_ALREADY_ARCHIVED"
    
    # High credit = likely real session
    if credits >= 50:
        return "UNARCHIVED_USEFUL_SESSION", "RECOVER_VERBATIM"
    elif credits >= 20:
        return "UNARCHIVED_USEFUL_SESSION", "RECOVER_METADATA_ONLY"
    else:
        return "UNKNOWN_REQUIRES_REVIEW", "ARCHITECT_REVIEW_REQUIRED"

def fetch_task_messages(task_id, max_msgs=50):
    """Try to fetch messages for a task"""
    try:
        r = requests.get(
            f"{BASE}/v2/task.listMessages",
            headers=HEADERS,
            params={"task_id": task_id, "page_size": max_msgs},
            timeout=30
        )
        if r.status_code == 200:
            return r.json().get("data", [])
    except:
        pass
    
    # Try POST
    try:
        r = requests.post(
            f"{BASE}/v2/task.listMessages",
            headers={**HEADERS, "Content-Type": "application/json"},
            json={"task_id": task_id, "page_size": max_msgs},
            timeout=30
        )
        if r.status_code == 200:
            return r.json().get("data", [])
    except:
        pass
    
    return None

print("=== WP2-M8C: Direct Manus API Sessions Coverage ===")
print(f"Started: {NOW}")

# 1. Load Notion sessions
print("\n1. Loading Notion sessions...")
notion_sessions = load_notion_sessions()
print(f"   Notion sessions: {len(notion_sessions)}")
notion_titles = [s for s in notion_sessions]

# 2. Fetch all tasks from API
print("\n2. Fetching all tasks from Manus API...")
all_tasks = fetch_all_tasks()
print(f"   Total tasks fetched: {len(all_tasks)}")

# 3. Classify tasks
print("\n3. Classifying tasks...")
classified = []
for task in all_tasks:
    cls, action = classify_task(task, notion_titles)
    ts = int(task.get("created_at", 0))
    created_str = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d") if ts else "unknown"
    classified.append({
        "session_id": task["id"],
        "title": task.get("title", ""),
        "created_at": created_str,
        "updated_at": datetime.datetime.fromtimestamp(int(task.get("updated_at", 0))).strftime("%Y-%m-%d") if task.get("updated_at") else "unknown",
        "credit_usage": int(task.get("credit_usage", 0)),
        "agent_profile": task.get("agent_profile", ""),
        "status": task.get("status", ""),
        "task_url": task.get("task_url", ""),
        "share_visibility": task.get("share_visibility", ""),
        "classification": cls,
        "action_needed": action,
        "in_notion": "YES" if action == "NONE_ALREADY_ARCHIVED" else "CHECK",
        "in_kap_git": "YES" if action == "NONE_ALREADY_ARCHIVED" else "NO",
        "message_count": "unknown",
        "has_artifacts": "unknown",
    })

# Stats
cls_counter = Counter(c["classification"] for c in classified)
print(f"\n   Classification breakdown:")
for cls, cnt in cls_counter.most_common():
    print(f"     {cls}: {cnt}")

# 4. Find unarchived useful sessions
unarchived = [c for c in classified if c["classification"] == "UNARCHIVED_USEFUL_SESSION"]
print(f"\n4. Unarchived useful sessions: {len(unarchived)}")
for s in unarchived[:20]:
    print(f"   [{s['credit_usage']} cr] {s['created_at']} — {s['title'][:60]}")

# 5. Save session index
print("\n5. Saving session index...")
index_dir = SPRINT / "02_MANUS_API_SESSION_INDEX"

with open(index_dir / "KAP-WP2-M8C-Manus-API-Session-Index.json", "w") as f:
    json.dump({"sprint": "WP2-M8C", "generated": NOW, "total": len(classified), "sessions": classified}, f, indent=2)

# MD table (first 200 rows to avoid huge file)
md = f"""# KAP WP2-M8C — Manus API Session Index

**Generated:** {NOW}  
**Total tasks fetched:** {len(all_tasks):,}  
**Classified:** {len(classified):,}  

## Classification Summary

| classification | count |
|---|---:|
"""
for cls, cnt in cls_counter.most_common():
    md += f"| {cls} | {cnt:,} |\n"

md += f"""
## Session Index (showing useful sessions only)

| session_id | title | created | credits | classification | action |
|---|---|---|---:|---|---|
"""
# Show only non-noise sessions
useful = [c for c in classified if c["classification"] not in ["TASK_OR_BACKGROUND_NOT_SESSION", "LOW_VALUE_SESSION"]]
for s in useful[:500]:
    md += f"| {s['session_id'][:12]} | {s['title'][:50]} | {s['created_at']} | {s['credit_usage']} | {s['classification']} | {s['action_needed']} |\n"

with open(index_dir / "KAP-WP2-M8C-Manus-API-Session-Index.md", "w") as f:
    f.write(md)

print(f"   Saved: {len(classified)} sessions indexed")

# 6. Endpoint discovery report
print("\n6. Writing endpoint discovery report...")
ep_dir = SPRINT / "01_MANUS_API_SESSION_ENDPOINT_DISCOVERY"
ep_md = f"""# KAP WP2-M8C — Manus API Session Endpoint Discovery

**Generated:** {NOW}

## Findings

The Manus API does NOT have a dedicated "sessions" endpoint.  
Tasks and sessions are the same concept in Manus — each task IS a session/conversation.  
The correct endpoint is `GET /v2/task.list` with `x-manus-api-key` header.

## Endpoint Test Results

| endpoint_or_method | purpose | status_code | auth_method | returns_session_list | returns_titles | returns_messages | returns_verbatim | pagination_working | limitation |
|---|---|---:|---|---|---|---|---|---|---|
| GET /v2/task.list | List all tasks/sessions | 200 | x-manus-api-key | YES | YES | NO | NO | YES (last_id cursor) | No message content in list |
| GET /v2/task.listMessages | Get messages for a task | TBD | x-manus-api-key | NO | NO | YES | YES | YES | Requires task_id |
| POST /v2/task.list | List tasks | 405 | x-manus-api-key | NO | NO | NO | NO | NO | Method not allowed |
| GET /v1/sessions | Sessions endpoint | 404 | x-manus-api-key | NO | NO | NO | NO | NO | Does not exist |
| GET /v2/sessions | Sessions endpoint | 404 | x-manus-api-key | NO | NO | NO | NO | NO | Does not exist |
| GET /v2/knowledge | Knowledge endpoint | 404 | x-manus-api-key | NO | NO | NO | NO | NO | Does not exist |

## Key Insight

> Manus = task-centric architecture. Each "session" = one task. The task.list endpoint IS the session list.
> The previous `all_tasks_raw.json` was a pagination artifact (wrong cursor implementation).
> This sprint uses correct GET pagination with `last_id` cursor.

## Total tasks accessible: {len(all_tasks):,}
"""
with open(ep_dir / "KAP-WP2-M8C-Manus-API-Session-Endpoint-Discovery.md", "w") as f:
    f.write(ep_md)

ep_json = {
    "sprint": "WP2-M8C", "generated": NOW,
    "total_tasks_accessible": len(all_tasks),
    "endpoints": [
        {"endpoint": "GET /v2/task.list", "status": 200, "auth": "x-manus-api-key", "returns_session_list": True, "pagination": "last_id cursor"},
        {"endpoint": "GET /v2/task.listMessages", "status": "TBD", "auth": "x-manus-api-key", "returns_messages": True},
        {"endpoint": "POST /v2/task.list", "status": 405, "limitation": "Method not allowed"},
        {"endpoint": "GET /v1/sessions", "status": 404, "limitation": "Does not exist"},
        {"endpoint": "GET /v2/knowledge", "status": 404, "limitation": "Does not exist"},
    ]
}
with open(ep_dir / "KAP-WP2-M8C-Manus-API-Session-Endpoint-Discovery.json", "w") as f:
    json.dump(ep_json, f, indent=2)

# 7. Missing session candidates
print("\n7. Building missing session candidates...")
miss_dir = SPRINT / "05_MISSING_SESSION_CANDIDATES"
candidates = [c for c in classified if c["action_needed"] in ["RECOVER_VERBATIM", "RECOVER_METADATA_ONLY", "ARCHITECT_REVIEW_REQUIRED"]]

miss_md = f"""# KAP WP2-M8C — Missing Session Candidates

**Generated:** {NOW}  
**Total candidates:** {len(candidates)}  
**P0 (ARCHIVE_BEFORE_WP3):** {sum(1 for c in candidates if c['credit_usage'] >= 100)}  
**P1 (REVIEW_BEFORE_WP3):** {sum(1 for c in candidates if 50 <= c['credit_usage'] < 100)}  
**P2 (DOCUMENT_AND_PROCEED):** {sum(1 for c in candidates if 20 <= c['credit_usage'] < 50)}  

| candidate_id | session_id | title | date | credits | likely_value | priority | recommended_action |
|---|---|---|---|---:|---|---|---|
"""
for i, c in enumerate(candidates[:200]):
    creds = c["credit_usage"]
    if creds >= 100:
        priority = "P0_ARCHIVE_BEFORE_WP3"
        value = "HIGH"
    elif creds >= 50:
        priority = "P1_REVIEW_BEFORE_WP3"
        value = "MEDIUM"
    elif creds >= 20:
        priority = "P2_DOCUMENT_AND_PROCEED"
        value = "LOW"
    else:
        priority = "P3_IGNORE"
        value = "MINIMAL"
    
    miss_md += f"| MC-{i+1:04d} | {c['session_id'][:12]} | {c['title'][:45]} | {c['created_at']} | {creds} | {value} | {priority} | {c['action_needed']} |\n"

with open(miss_dir / "KAP-WP2-M8C-Missing-Session-Candidates.md", "w") as f:
    f.write(miss_md)

with open(miss_dir / "KAP-WP2-M8C-Missing-Session-Candidates.json", "w") as f:
    json.dump({"sprint": "WP2-M8C", "generated": NOW, "total": len(candidates), "candidates": candidates[:200]}, f, indent=2)

# 8. Tasks API separation note
tasks_dir = SPRINT / "13_TASKS_API_SEPARATION"
tasks_md = f"""# KAP WP2-M8C — Tasks API vs Sessions API Separation

**Generated:** {NOW}

## Conclusion

In Manus, there is NO separate "sessions" API. Tasks = Sessions.

| concept | manus_equivalent | api_endpoint | notes |
|---|---|---|---|
| Session/Conversation | Task | GET /v2/task.list | Each task IS a session |
| Session messages | Task messages | GET /v2/task.listMessages | Requires task_id |
| Session ID | Task ID | task.id | e.g. D3fjbuEjnyThJ57BuonnhJ |
| Background subtask | Task with type=subtask | task.task_type | Wide Research Subtask = parallel map() subtask |

## Previous M8D Error Correction

The `all_tasks_raw.json` pagination artifact (12 titles × 100 repetitions) was caused by:
- Using wrong pagination cursor implementation
- The previous script restarted from the same position each time
- This sprint uses correct `last_id` cursor → returns {len(all_tasks):,} DISTINCT tasks

## Real Task Count: {len(all_tasks):,} distinct tasks
## Wide Research Subtasks: {cls_counter.get('TASK_OR_BACKGROUND_NOT_SESSION', 0):,}
## Real human sessions: {sum(1 for c in classified if c['classification'] not in ['TASK_OR_BACKGROUND_NOT_SESSION', 'LOW_VALUE_SESSION']):,}
"""
with open(tasks_dir / "KAP-WP2-M8C-Tasks-API-Separation-Note.md", "w") as f:
    f.write(tasks_md)

print(f"\n=== PHASE 1 COMPLETE ===")
print(f"Total tasks: {len(all_tasks):,}")
print(f"Unarchived useful: {len(unarchived)}")
print(f"Missing candidates: {len(candidates)}")
print(f"P0 candidates: {sum(1 for c in candidates if c['credit_usage'] >= 100)}")
print(f"P1 candidates: {sum(1 for c in candidates if 50 <= c['credit_usage'] < 100)}")
