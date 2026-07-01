#!/usr/bin/env python3
"""
Fetch ALL pages from a Notion database with full pagination.
Uses curl subprocess to avoid SSL EOF issues in sandbox.
"""
import subprocess, json, sys, os, time

TOKEN = "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"

def fetch_db(db_id, label=""):
    """Fetch all entries from a Notion database, returning list of results."""
    all_results = []
    cursor = None
    page = 0
    
    while True:
        page += 1
        body = {"page_size": 100}
        if cursor:
            body["start_cursor"] = cursor
        
        cmd = [
            "curl", "-s", "--retry", "2",
            "-X", "POST",
            "-H", f"Authorization: Bearer {TOKEN}",
            "-H", "Notion-Version: 2022-06-28",
            "-H", "Content-Type: application/json",
            "-d", json.dumps(body),
            f"https://api.notion.com/v1/databases/{db_id}/query"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode != 0:
            print(f"  ERROR: curl failed for {db_id}", file=sys.stderr)
            break
        
        try:
            data = json.loads(result.stdout)
        except json.JSONDecodeError as e:
            print(f"  ERROR: JSON parse failed: {e}", file=sys.stderr)
            break
        
        if data.get("object") == "error":
            print(f"  ERROR: {data.get('code')} - {data.get('message')}", file=sys.stderr)
            break
        
        results = data.get("results", [])
        all_results.extend(results)
        has_more = data.get("has_more", False)
        cursor = data.get("next_cursor")
        
        print(f"  [{label}] Page {page}: +{len(results)} entries (total={len(all_results)}, has_more={has_more})", file=sys.stderr)
        
        if not has_more or not cursor:
            break
        
        time.sleep(0.3)  # Rate limit courtesy
    
    return all_results


def extract_title(page):
    """Extract title from a Notion page/entry."""
    props = page.get("properties", {})
    for key in ["Name", "Title", "Session Title", "title", "name"]:
        if key in props:
            prop = props[key]
            arr = prop.get("title", prop.get("rich_text", []))
            if arr:
                return arr[0].get("plain_text", "")
    return "(untitled)"


def extract_all_text(page):
    """Extract all text content from page properties."""
    props = page.get("properties", {})
    extracted = {}
    for key, val in props.items():
        ptype = val.get("type", "")
        if ptype in ("title", "rich_text"):
            arr = val.get(ptype, [])
            text = " ".join(t.get("plain_text", "") for t in arr)
            if text:
                extracted[key] = text
        elif ptype == "select":
            sel = val.get("select")
            if sel:
                extracted[key] = sel.get("name", "")
        elif ptype == "multi_select":
            items = val.get("multi_select", [])
            if items:
                extracted[key] = [i.get("name", "") for i in items]
        elif ptype == "date":
            d = val.get("date")
            if d:
                extracted[key] = d.get("start", "")
        elif ptype == "url":
            u = val.get("url")
            if u:
                extracted[key] = u
        elif ptype == "checkbox":
            extracted[key] = val.get("checkbox", False)
        elif ptype == "number":
            n = val.get("number")
            if n is not None:
                extracted[key] = n
    return extracted


DATABASES = {
    "533401fa-1702-4d9d-a60e-5433cac72fe1": "Manus_Memory_Hub",
    "ebafd590-ce92-45c7-9fe7-068f7ca6d415": "SSA_Session_Synthetic_Archive",
    "85f89b4e-847d-4cbe-a931-0ffdf11b60f2": "YOS_Tools_Registry_v2",
    "92f217a0-59fd-4d05-aaa3-4460ccbad58d": "YOS_Tools_Registry_v1",
    "f2c0bc6c-54cd-46ee-a663-f7b2952fc967": "KOR_Knowledge_Object_Repository",
    "31235e21-8cf8-8126-9212-f5a0eebadce0": "YOS_Archives",
}

if __name__ == "__main__":
    output_dir = sys.argv[1] if len(sys.argv) > 1 else "/home/ubuntu/KAP/02_Source_Acquisition/WP2-M6_Notion_Memory_Hub_Bridge/raw"
    os.makedirs(output_dir, exist_ok=True)
    
    summary = {}
    
    for db_id, label in DATABASES.items():
        print(f"\n=== Fetching: {label} ({db_id}) ===", file=sys.stderr)
        results = fetch_db(db_id, label)
        
        # Save raw JSON
        raw_path = os.path.join(output_dir, f"{label}_raw.json")
        with open(raw_path, 'w') as f:
            json.dump({"db_id": db_id, "label": label, "total": len(results), "results": results}, f, indent=2, ensure_ascii=False)
        
        # Save extracted summary
        extracted = []
        for r in results:
            entry = {
                "id": r.get("id"),
                "created_time": r.get("created_time"),
                "last_edited_time": r.get("last_edited_time"),
                "url": r.get("url"),
                "title": extract_title(r),
                "properties": extract_all_text(r)
            }
            extracted.append(entry)
        
        summary_path = os.path.join(output_dir, f"{label}_summary.json")
        with open(summary_path, 'w') as f:
            json.dump({"db_id": db_id, "label": label, "total": len(extracted), "entries": extracted}, f, indent=2, ensure_ascii=False)
        
        summary[label] = {
            "db_id": db_id,
            "total_entries": len(results),
            "raw_file": raw_path,
            "summary_file": summary_path
        }
        
        print(f"  -> Saved {len(results)} entries to {label}_raw.json + {label}_summary.json")
    
    # Save global summary
    summary_path = os.path.join(output_dir, "ACQUISITION_SUMMARY.json")
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    print(f"\n=== DONE ===")
    for label, info in summary.items():
        print(f"  {label}: {info['total_entries']} entries")
    print(f"\nSummary: {summary_path}")
