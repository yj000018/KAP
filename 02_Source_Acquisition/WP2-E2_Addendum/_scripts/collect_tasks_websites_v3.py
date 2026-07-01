#!/usr/bin/env python3
"""
KAP WP2-E2 Addendum — Manus Tasks + Websites Inventory v3
Uses Manus API v2 with x-manus-api-key auth.
Base URL: https://api.manus.ai
"""
import json, os, time, requests, hashlib
from pathlib import Path
from datetime import datetime

API_KEY = os.environ.get("MANUS_API_KEY", "")
BASE = "https://api.manus.ai"
HEADERS = {"x-manus-api-key": API_KEY}

OUT = Path("/home/ubuntu/KAP/02_Source_Acquisition/WP2-E2_Addendum")
TASKS_DIR = OUT / "manus_tasks"
WEB_DIR = OUT / "manus_websites"
TASKS_DIR.mkdir(parents=True, exist_ok=True)
WEB_DIR.mkdir(parents=True, exist_ok=True)
(WEB_DIR / "screenshots").mkdir(exist_ok=True)
(WEB_DIR / "html_snapshots").mkdir(exist_ok=True)
(WEB_DIR / "source_links").mkdir(exist_ok=True)
(WEB_DIR / "checksums").mkdir(exist_ok=True)
(WEB_DIR / "notes").mkdir(exist_ok=True)

# Priority keywords
P0_KW = ["yos", "kap", "kre", "memory", "manus pipeline", "notion exporter",
         "session extractor", "y-world", "living backbone", "cosa",
         "agent architecture", "memory pipeline", "lmp", "memory bridge",
         "session tree", "manus control", "brain map", "cognitive", "y-os",
         "youniverse", "y-ecosystem", "control panel", "activity dashboard",
         "voice", "universe", "core brain", "architecture", "memory layer"]
P1_KW = ["elysium", "kosmos", "oneshift", "civilizational", "archetype",
         "dashboard", "knowledge graph", "satva", "odyssey", "ananda",
         "tana", "mirror", "gratitude", "life odyssey", "awakening"]
P2_KW = ["pev", "private equit", "deal radar", "travel", "future news",
         "layoff", "careglyph", "portfolio", "voixitalia", "ynot",
         "yantra", "ai portfolio", "finance", "media", "clinic", "cafe"]

def classify(title: str) -> str:
    t = title.lower()
    for kw in P0_KW:
        if kw in t: return "P0"
    for kw in P1_KW:
        if kw in t: return "P1"
    for kw in P2_KW:
        if kw in t: return "P2"
    return "P3"

def api_get(path, params=None):
    try:
        r = requests.get(f"{BASE}{path}", headers=HEADERS, params=params, timeout=20)
        return r.status_code, r.json() if r.headers.get("content-type","").startswith("application/json") else {}
    except Exception as e:
        return 0, {"error": str(e)}

def collect_tasks():
    print("\n=== COLLECTING TASKS ===")
    all_tasks = []
    page_token = None
    page = 0
    while True:
        params = {"limit": 100}
        if page_token:
            params["page_token"] = page_token
        status, data = api_get("/v2/task.list", params)
        print(f"  Page {page}: status={status}, keys={list(data.keys()) if isinstance(data,dict) else type(data)}")
        if status != 200:
            print(f"  Error: {data}")
            break
        if not data.get("ok"):
            print(f"  API error: {data}")
            break
        tasks = data.get("data", [])
        all_tasks.extend(tasks)
        print(f"  Got {len(tasks)} tasks (total: {len(all_tasks)})")
        page_token = data.get("next_page_token")
        if not page_token or not tasks:
            break
        page += 1
        time.sleep(0.3)
    return all_tasks

def collect_websites_from_tasks(tasks):
    """For each task, check if it has a website."""
    print("\n=== CHECKING WEBSITES ===")
    websites = []
    for t in tasks:
        task_id = t.get("id") or t.get("task_id") or t.get("uid", "")
        title = t.get("title", "")
        if not task_id:
            continue
        status, data = api_get("/v2/website.status", {"task_id": task_id})
        if status == 200 and data.get("ok"):
            site = data.get("data", {})
            if site:
                site["_task_id"] = task_id
                site["_task_title"] = title
                site["_priority"] = classify(title)
                websites.append(site)
                print(f"  ✅ Website found: {title[:50]} → {site.get('site_urls', ['?'])[0] if site.get('site_urls') else '?'}")
        time.sleep(0.2)
    return websites

def snapshot_website(site: dict, idx: int):
    """Capture HTML snapshot of a website."""
    urls = site.get("site_urls", [])
    if not urls:
        return None
    url = urls[0]
    title = site.get("_task_title", f"site_{idx}")
    safe_title = "".join(c if c.isalnum() or c in "-_" else "_" for c in title[:40])
    
    try:
        r = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        if r.status_code == 200:
            html_path = WEB_DIR / "html_snapshots" / f"{safe_title}.html"
            html_path.write_text(r.text, encoding="utf-8")
            checksum = hashlib.sha256(r.content).hexdigest()
            (WEB_DIR / "checksums" / f"{safe_title}.sha256").write_text(f"{checksum}  {url}\n")
            return {"url": url, "html_path": str(html_path), "checksum": checksum, "size_bytes": len(r.content)}
    except Exception as e:
        print(f"    Snapshot failed for {url}: {e}")
    return None

def main():
    if not API_KEY:
        print("ERROR: MANUS_API_KEY not set")
        return

    # 1. Collect tasks
    tasks = collect_tasks()
    print(f"\nTotal tasks: {len(tasks)}")

    if not tasks:
        print("No tasks found via API. Saving empty results.")
        with open(TASKS_DIR / "tasks_summary.json", "w") as f:
            json.dump({"total": 0, "tasks": [], "error": "API returned no tasks"}, f, indent=2)
        return

    # 2. Classify tasks
    enriched = []
    for t in tasks:
        title = t.get("title", "") or ""
        enriched.append({
            "source_id": f"KAP-TASK-{(t.get('id','')[:12])}",
            "uid": t.get("id") or t.get("task_id") or t.get("uid", ""),
            "title": title,
            "status": t.get("status", "unknown"),
            "priority": classify(title),
            "created_at": t.get("created_at", ""),
            "updated_at": t.get("updated_at", ""),
            "project_id": t.get("project_id", ""),
            "canonical_status": "not_canonical",
            "acquisition_method": "manus_api_v2",
            "date_captured": "2026-07-01",
            "visibility": t.get("visibility", "unknown"),
        })

    from collections import Counter
    pcount = Counter(t["priority"] for t in enriched)
    scount = Counter(t["status"] for t in enriched)

    with open(TASKS_DIR / "tasks_summary.json", "w") as f:
        json.dump({"total": len(enriched), "priority_breakdown": dict(pcount),
                   "status_breakdown": dict(scount), "tasks": enriched}, f, indent=2, ensure_ascii=False)

    print(f"Priority: {dict(pcount)}")
    print(f"Status: {dict(scount)}")

    # 3. Collect websites
    websites = collect_websites_from_tasks(tasks)
    print(f"\nWebsites found: {len(websites)}")

    # 4. Snapshot P0/P1 websites
    website_inventory = []
    for i, site in enumerate(websites):
        priority = site.get("_priority", "P3")
        snapshot = None
        if priority in ("P0", "P1"):
            print(f"  Snapshotting [{priority}]: {site.get('_task_title','')[:50]}")
            snapshot = snapshot_website(site, i)
            time.sleep(0.5)

        urls = site.get("site_urls", [])
        entry = {
            "source_id": f"KAP-WEB-{str(i+1).zfill(3)}",
            "title": site.get("_task_title", ""),
            "url": urls[0] if urls else "",
            "all_urls": urls,
            "visibility": site.get("visibility", "unknown"),
            "publish_status": site.get("publish_status", "unknown"),
            "task_id": site.get("_task_id", ""),
            "priority": priority,
            "website_id": site.get("website_id", ""),
            "published_version_id": site.get("published_version_id", ""),
            "canonical_status": "not_canonical",
            "acquisition_method": "manus_api_v2_website_status",
            "date_captured": "2026-07-01",
            "html_snapshot": snapshot.get("html_path") if snapshot else None,
            "checksum": snapshot.get("checksum") if snapshot else None,
            "snapshot_size_bytes": snapshot.get("size_bytes") if snapshot else None,
        }
        website_inventory.append(entry)

    with open(WEB_DIR / "website_inventory.json", "w") as f:
        json.dump(website_inventory, f, indent=2, ensure_ascii=False)

    print(f"\nDone. Tasks: {len(enriched)}, Websites: {len(website_inventory)}")
    return enriched, website_inventory

if __name__ == "__main__":
    main()
