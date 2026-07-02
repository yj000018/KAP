#!/usr/bin/env python3
"""
Manus Metadata Census — CONN-MANUS-01
Dry-run: Fetches task metadata only. No task body ingestion.
Usage: python3 manus_metadata_census.py [--dry-run]
"""
import requests, json, os, time, argparse, datetime

API_KEY = os.environ.get("MANUS_API_KEY", "")
BASE = "https://api.manus.im/v2"
HEADERS = {"x-manus-api-key": API_KEY}
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_dry_runs")

NOISE_PATTERNS = ["wide research subtask", "new task"]

def fetch_metadata(limit=200):
    all_tasks, last_id, page = [], None, 0
    while len(all_tasks) < limit:
        params = {"limit": 100, "order": "desc"}
        if last_id: params["last_id"] = last_id
        r = requests.get(f"{BASE}/task.list", headers=HEADERS, params=params, timeout=20)
        if r.status_code != 200:
            print(f"[WARN] API {r.status_code}"); break
        items = r.json() if isinstance(r.json(), list) else r.json().get("data", [])
        if not items: break
        all_tasks.extend(items); page += 1
        new_last = items[-1].get("id")
        if len(items) < 100 or new_last == last_id: break
        last_id = new_last; time.sleep(0.3)
    return all_tasks

def run(dry_run=True):
    if not API_KEY:
        print("[SKIP] MANUS_API_KEY not set — access-limited dry-run"); return
    tasks = fetch_metadata()
    metadata = [{
        "task_id": t.get("id",""), "title": t.get("title",""),
        "created_at": t.get("created_at",""), "status": t.get("status",""),
        "is_noise": any(p in t.get("title","").lower() for p in NOISE_PATTERNS),
    } for t in tasks]
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out = os.path.join(OUTPUT_DIR, f"manus_census_dry_run_{datetime.date.today()}.json")
    with open(out, "w") as f: json.dump({"total": len(metadata), "items": metadata}, f, indent=2)
    noise = sum(1 for m in metadata if m["is_noise"])
    print(f"[OK] {len(metadata)} tasks | {noise} noise | Saved: {out}")

if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(); run(dry_run=True)
