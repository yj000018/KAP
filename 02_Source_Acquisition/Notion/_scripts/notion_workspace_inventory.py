#!/usr/bin/env python3
"""
Notion Workspace Inventory — CONN-NOTION-01
Lists databases and pages metadata. No page body ingestion.
Requires: NOTION_API_KEY env var.
"""
import os, json, datetime

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_dry_runs")

def inventory():
    api_key = os.environ.get("NOTION_API_KEY","")
    if not api_key: print("[SKIP] NOTION_API_KEY not set — access-limited dry-run"); return
    try:
        import requests
        headers = {"Authorization": f"Bearer {api_key}", "Notion-Version": "2022-06-28", "Content-Type": "application/json"}
        r = requests.post("https://api.notion.com/v1/search", headers=headers,
                          json={"filter": {"value": "database", "property": "object"}, "page_size": 100}, timeout=15)
        if r.status_code != 200: print(f"[FAIL] {r.status_code}: {r.text[:200]}"); return
        dbs = r.json().get("results", [])
        items = [{"id": d.get("id",""), "title": (d.get("title") or [{}])[0].get("plain_text","") if d.get("title") else d.get("id",""),
                  "created_time": d.get("created_time",""), "url": d.get("url","")} for d in dbs]
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        out = os.path.join(OUTPUT_DIR, f"notion_inventory_{datetime.date.today()}.json")
        with open(out, "w") as f: json.dump({"total": len(items), "items": items}, f, indent=2, ensure_ascii=False)
        print(f"[OK] {len(items)} databases | Saved: {out}")
    except ImportError: print("[FAIL] requests not installed")

if __name__ == "__main__": inventory()
