#!/usr/bin/env python3
"""
Manus Durable Output Detector — CONN-MANUS-01
Identifies tasks likely to contain durable artifacts (files, code, docs).
Dry-run only: no task body ingestion.
"""
import requests, json, os, time, datetime

API_KEY = os.environ.get("MANUS_API_KEY", "")
BASE = "https://api.manus.im/v2"
HEADERS = {"x-manus-api-key": API_KEY}
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_dry_runs")

DURABLE_KEYWORDS = ["KAP","yOS","ELYSIUM","pipeline","connector","architecture","gate","registry","factsheet","script","report","schema","roadmap","memory","Notion","GitHub","Obsidian"]
NOISE_PATTERNS = ["wide research subtask","new task","parallel research"]

def detect():
    if not API_KEY: print("[SKIP] MANUS_API_KEY not set"); return
    all_tasks, last_id = [], None
    while True:
        params = {"limit": 100, "order": "desc"}
        if last_id: params["last_id"] = last_id
        r = requests.get(f"{BASE}/task.list", headers=HEADERS, params=params, timeout=20)
        if r.status_code != 200: break
        items = r.json() if isinstance(r.json(), list) else r.json().get("data", [])
        if not items: break
        all_tasks.extend(items)
        new_last = items[-1].get("id")
        if len(items) < 100 or new_last == last_id: break
        last_id = new_last; time.sleep(0.3)

    candidates = []
    for t in all_tasks:
        title = t.get("title","")
        if any(p in title.lower() for p in NOISE_PATTERNS): continue
        score = sum(1 for k in DURABLE_KEYWORDS if k.lower() in title.lower())
        if score >= 1:
            candidates.append({"task_id": t.get("id",""), "title": title, "score": score,
                                "url": f"https://manus.im/app/{t.get('id','')}"})
    candidates.sort(key=lambda x: x["score"], reverse=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out = os.path.join(OUTPUT_DIR, f"durable_candidates_{datetime.date.today()}.json")
    with open(out, "w") as f: json.dump({"total": len(candidates), "items": candidates}, f, indent=2, ensure_ascii=False)
    print(f"[OK] {len(candidates)} durable candidates found | Saved: {out}")
    for c in candidates[:10]: print(f"  [{c['score']}] {c['task_id'][:8]}... | {c['title'][:70]}")

if __name__ == "__main__": detect()
