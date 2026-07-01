#!/usr/bin/env python3
"""
KAP WP2-E2 Addendum — Manus Tasks Inventory
Collects all tasks via Manus API and classifies by priority.
"""
import json, os, time, requests
from pathlib import Path
from datetime import datetime

TOKEN = os.environ.get("MANUS_TOKEN", (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
    ".eyJlbWFpbCI6Inlhbm5pY2suam9sbGlldEBnbWFpbC5jb20iLCJleHAiOjE3ODM0MzEwOTMsImlhdCI6MTc3NTY1NTA5MywianRpIjoiY3dUOUxoOEtzNmNacEwzakVSaHozQyIsIm5hbWUiOiJZYW5uaWNrIEpvbGxpZXQiLCJvcmlnaW5hbF91c2VyX2lkIjoiIiwidGVhbV91aWQiOiIiLCJ0eXBlIjoidXNlciIsInVzZXJfaWQiOiIzMTA0MTk2NjMwMzIzODE4MzMifQ"
    ".88v6mbthCgzJQwUAc1-_wKYo-8uSdQ_qkro7C2cYVuM"
))
BASE_URL = "https://api.manus.im"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "connect-protocol-version": "1",
    "x-client-id": "SH6GDQiPhdFcHsaqh7U4Rm",
}
HEADERS_GET = {k: v for k, v in HEADERS.items() if k != "Content-Type"}

# Priority keywords
P0_KEYWORDS = ["yos", "kap", "kre", "memory", "manus pipeline", "notion exporter",
                "session extractor", "y-world", "living backbone", "cosa",
                "agent architecture", "memory pipeline", "lmp", "memory bridge",
                "session tree", "manus control", "brain map", "cognitive"]
P1_KEYWORDS = ["elysium", "kosmos", "oneshift", "civilizational", "archetype",
                "dashboard", "knowledge graph", "y-ecosystem", "universe",
                "youniverse", "satva", "odyssey", "ananda", "tana"]
P2_KEYWORDS = ["pev", "private equit", "deal radar", "travel", "future news",
                "layoff", "careglyph", "portfolio", "voixitalia", "ynot",
                "yantra", "ai portfolio", "finance", "media"]

def classify_priority(title: str) -> str:
    t = title.lower()
    for kw in P0_KEYWORDS:
        if kw in t:
            return "P0"
    for kw in P1_KEYWORDS:
        if kw in t:
            return "P1"
    for kw in P2_KEYWORDS:
        if kw in t:
            return "P2"
    return "P3"

def list_all_sessions():
    """Fetch all sessions (tasks) via pagination."""
    all_sessions = []
    offset = 0
    page_size = 100
    while True:
        try:
            resp = requests.post(
                f"{BASE_URL}/api/v1/session/list",
                headers=HEADERS,
                json={"filters": {}, "offset": offset, "limit": page_size},
                timeout=30
            )
            if resp.status_code != 200:
                print(f"  API error {resp.status_code}: {resp.text[:200]}")
                break
            data = resp.json()
            sessions = data.get("sessions", [])
            if not sessions:
                break
            all_sessions.extend(sessions)
            print(f"  Fetched {len(all_sessions)} sessions so far...")
            if len(sessions) < page_size:
                break
            offset += page_size
            time.sleep(0.3)
        except Exception as e:
            print(f"  Error: {e}")
            break
    return all_sessions

def main():
    out_dir = Path("/home/ubuntu/KAP/02_Source_Acquisition/WP2-E2_Addendum/manus_tasks")
    out_dir.mkdir(parents=True, exist_ok=True)

    print("Fetching Manus tasks...")
    sessions = list_all_sessions()
    print(f"Total tasks found: {len(sessions)}")

    # Classify and enrich
    tasks = []
    for s in sessions:
        title = s.get("title", "") or s.get("name", "") or ""
        uid = s.get("uid", s.get("id", ""))
        created = s.get("created_at", s.get("create_time", ""))
        updated = s.get("updated_at", s.get("update_time", ""))
        status = s.get("status", "unknown")
        priority = classify_priority(title)

        tasks.append({
            "uid": uid,
            "title": title,
            "status": status,
            "priority": priority,
            "created_at": created,
            "updated_at": updated,
            "source_id": f"KAP-TASK-{uid[:12]}",
            "canonical_status": "not_canonical",
            "acquisition_method": "manus_api_list",
            "date_captured": "2026-07-01",
            "raw": s
        })

    # Sort by priority then date
    priority_order = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
    tasks.sort(key=lambda x: (priority_order.get(x["priority"], 9), x.get("created_at", "") or ""))

    # Save full JSON
    with open(out_dir / "tasks_full.json", "w") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

    # Save summary (no raw)
    summary = [{k: v for k, v in t.items() if k != "raw"} for t in tasks]
    with open(out_dir / "tasks_summary.json", "w") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    # Stats
    from collections import Counter
    pcount = Counter(t["priority"] for t in tasks)
    scount = Counter(t["status"] for t in tasks)

    print(f"\nPriority breakdown: {dict(pcount)}")
    print(f"Status breakdown: {dict(scount)}")
    print(f"Output: {out_dir}")

    return tasks, pcount, scount

if __name__ == "__main__":
    main()
