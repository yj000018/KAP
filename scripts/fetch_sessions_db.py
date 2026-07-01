#!/usr/bin/env python3
"""
Fetch ALL entries from Manus Memory Sessions DB.
Uses curl with extended timeout (60s) per page.
"""
import subprocess, json, os, time

TOKEN = "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"
DB_ID = "5e51ded4-0b46-4a68-acc2-4e90886a2499"
OUT_DIR = "/home/ubuntu/KAP/02_Source_Acquisition/WP2-M6_Notion_Memory_Hub_Bridge/raw"

all_results = []
cursor = None
page = 0

while True:
    page += 1
    body = {"page_size": 100}
    if cursor:
        body["start_cursor"] = cursor
    
    cmd = ["curl", "-s", "--max-time", "60", "--retry", "2",
           "-X", "POST",
           "-H", f"Authorization: Bearer {TOKEN}",
           "-H", "Notion-Version: 2022-06-28",
           "-H", "Content-Type: application/json",
           "-d", json.dumps(body),
           f"https://api.notion.com/v1/databases/{DB_ID}/query"]
    
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    
    if r.returncode != 0 or not r.stdout.strip():
        print(f"  ERROR: curl failed page {page}")
        break
    
    try:
        data = json.loads(r.stdout)
    except json.JSONDecodeError:
        print(f"  ERROR: JSON parse failed page {page}")
        break
    
    if data.get("object") == "error":
        print(f"  ERROR: {data['code']} — {data['message']}")
        break
    
    results = data.get("results", [])
    all_results.extend(results)
    has_more = data.get("has_more", False)
    cursor = data.get("next_cursor")
    print(f"  Page {page}: +{len(results)} (total={len(all_results)}, has_more={has_more})")
    
    if not has_more or not cursor:
        break
    time.sleep(0.5)

# Save raw
out_path = os.path.join(OUT_DIR, "Manus_Memory_Sessions_raw.json")
with open(out_path, 'w') as f:
    json.dump({"db_id": DB_ID, "label": "Manus_Memory_Sessions", "total": len(all_results), "results": all_results}, f, indent=2, ensure_ascii=False)

print(f"\n=== TOTAL SESSIONS: {len(all_results)} ===")

# Extract titles for preview
def get_title(r):
    props = r.get("properties", {})
    for k in ["Name", "Title", "Session Title", "title"]:
        if k in props:
            arr = props[k].get("title", props[k].get("rich_text", []))
            if arr:
                return arr[0].get("plain_text", "")
    return "(untitled)"

def get_prop(r, key):
    props = r.get("properties", {})
    if key not in props:
        return ""
    v = props[key]
    ptype = v.get("type", "")
    if ptype == "select":
        s = v.get("select")
        return s.get("name", "") if s else ""
    elif ptype == "multi_select":
        return ", ".join(i.get("name", "") for i in v.get("multi_select", []))
    elif ptype in ("title", "rich_text"):
        arr = v.get(ptype, [])
        return " ".join(t.get("plain_text", "") for t in arr)
    elif ptype == "date":
        d = v.get("date")
        return d.get("start", "") if d else ""
    return ""

# Save summary CSV
csv_path = os.path.join(OUT_DIR, "Manus_Memory_Sessions_summary.csv")
with open(csv_path, 'w') as f:
    f.write("created,title,type,status,tags\n")
    for r in all_results:
        created = r.get("created_time", "")[:10]
        title = get_title(r).replace(",", ";").replace("\n", " ")[:100]
        stype = get_prop(r, "Type").replace(",", ";")
        status = get_prop(r, "Status").replace(",", ";")
        tags = get_prop(r, "Tags").replace(",", ";")
        f.write(f"{created},{title},{stype},{status},{tags}\n")

print(f"Summary CSV: {csv_path}")
print("\nFirst 20 sessions:")
for r in all_results[:20]:
    print(f"  [{r.get('created_time','')[:10]}] {get_title(r)[:80]}")
