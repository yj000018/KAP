#!/usr/bin/env python3
"""Notion Page Hierarchy Mapper — CONN-NOTION-01. Maps parent/child page relationships."""
import os, json, datetime

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_dry_runs")

def map_hierarchy():
    api_key = os.environ.get("NOTION_API_KEY","")
    if not api_key: print("[SKIP] NOTION_API_KEY not set"); return
    try:
        import requests
        headers = {"Authorization": f"Bearer {api_key}", "Notion-Version": "2022-06-28", "Content-Type": "application/json"}
        r = requests.post("https://api.notion.com/v1/search", headers=headers, json={"page_size": 100}, timeout=15)
        if r.status_code != 200: print(f"[FAIL] {r.status_code}"); return
        pages = r.json().get("results", [])
        hierarchy = [{"id": p.get("id",""), "type": p.get("object",""), "parent_type": p.get("parent",{}).get("type",""),
                      "parent_id": p.get("parent",{}).get("database_id") or p.get("parent",{}).get("page_id",""),
                      "url": p.get("url","")} for p in pages]
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        out = os.path.join(OUTPUT_DIR, f"notion_hierarchy_{datetime.date.today()}.json")
        with open(out, "w") as f: json.dump({"total": len(hierarchy), "items": hierarchy}, f, indent=2)
        print(f"[OK] {len(hierarchy)} pages mapped | Saved: {out}")
    except ImportError: print("[FAIL] requests not installed")

if __name__ == "__main__": map_hierarchy()
