#!/usr/bin/env python3
"""
Enhanced extraction of Notion DB entries with proper property handling.
Produces human-readable summary files per database.
"""
import json, os, sys

RAW_DIR = "/home/ubuntu/KAP/02_Source_Acquisition/WP2-M6_Notion_Memory_Hub_Bridge/raw"
OUT_DIR = "/home/ubuntu/KAP/02_Source_Acquisition/WP2-M6_Notion_Memory_Hub_Bridge"


def extract_prop(val):
    """Extract value from any Notion property type."""
    ptype = val.get("type", "")
    if ptype in ("title", "rich_text"):
        arr = val.get(ptype, [])
        return " ".join(t.get("plain_text", "") for t in arr).strip()
    elif ptype == "select":
        sel = val.get("select")
        return sel.get("name", "") if sel else ""
    elif ptype == "multi_select":
        items = val.get("multi_select", [])
        return [i.get("name", "") for i in items]
    elif ptype == "date":
        d = val.get("date")
        return d.get("start", "") if d else ""
    elif ptype == "url":
        return val.get("url", "") or ""
    elif ptype == "checkbox":
        return val.get("checkbox", False)
    elif ptype == "number":
        return val.get("number")
    elif ptype == "unique_id":
        uid = val.get("unique_id", {})
        prefix = uid.get("prefix", "")
        num = uid.get("number", "")
        return f"{prefix}-{num}" if prefix else str(num)
    elif ptype == "last_edited_time":
        return val.get("last_edited_time", "")
    elif ptype == "created_time":
        return val.get("created_time", "")
    elif ptype == "relation":
        rels = val.get("relation", [])
        return [r.get("id", "") for r in rels]
    elif ptype == "formula":
        formula = val.get("formula", {})
        ftype = formula.get("type", "")
        return formula.get(ftype, "")
    elif ptype == "rollup":
        rollup = val.get("rollup", {})
        rtype = rollup.get("type", "")
        if rtype == "array":
            return [extract_prop(item) for item in rollup.get("array", [])]
        return rollup.get(rtype, "")
    elif ptype == "people":
        people = val.get("people", [])
        return [p.get("name", p.get("id", "")) for p in people]
    elif ptype == "files":
        files = val.get("files", [])
        return [f.get("name", "") for f in files]
    elif ptype == "email":
        return val.get("email", "") or ""
    elif ptype == "phone_number":
        return val.get("phone_number", "") or ""
    elif ptype == "status":
        s = val.get("status")
        return s.get("name", "") if s else ""
    return ""


def process_db(label):
    raw_path = os.path.join(RAW_DIR, f"{label}_raw.json")
    if not os.path.exists(raw_path):
        print(f"  SKIP: {raw_path} not found")
        return []
    
    with open(raw_path) as f:
        data = json.load(f)
    
    results = data.get("results", [])
    entries = []
    
    for r in results:
        props = r.get("properties", {})
        extracted = {}
        for k, v in props.items():
            val = extract_prop(v)
            if val not in ("", [], None, False):
                extracted[k] = val
        
        entry = {
            "id": r.get("id"),
            "created": r.get("created_time", "")[:10],
            "edited": r.get("last_edited_time", "")[:10],
            "url": r.get("url", ""),
            "properties": extracted
        }
        entries.append(entry)
    
    return entries


def write_markdown_table(entries, label, db_id):
    """Write a markdown summary of the database."""
    lines = [f"# {label}\n", f"**DB ID:** `{db_id}`  \n**Total entries:** {len(entries)}\n\n"]
    
    if not entries:
        lines.append("_Empty database_\n")
        return "\n".join(lines)
    
    # Determine key columns based on what's present
    all_keys = set()
    for e in entries:
        all_keys.update(e["properties"].keys())
    
    # Priority columns
    priority = ["Tool Name", "Name", "Title", "Session Title", "Type", "Status", "Category", 
                "Tags", "Source", "Date", "Tool Type", "Pricing", "Source URL"]
    cols = [k for k in priority if k in all_keys]
    # Add remaining (up to 8 total)
    for k in sorted(all_keys):
        if k not in cols and len(cols) < 8:
            cols.append(k)
    
    lines.append("| # | Created | " + " | ".join(cols) + " |\n")
    lines.append("|---|---------|" + "|".join(["---"] * len(cols)) + "|\n")
    
    for i, e in enumerate(entries, 1):
        props = e["properties"]
        row_vals = []
        for col in cols:
            v = props.get(col, "")
            if isinstance(v, list):
                v = ", ".join(str(x) for x in v)
            v = str(v)[:50].replace("|", "\\|").replace("\n", " ")
            row_vals.append(v)
        lines.append(f"| {i} | {e['created']} | " + " | ".join(row_vals) + " |\n")
    
    return "".join(lines)


DATABASES = {
    "Manus_Memory_Hub": "533401fa-1702-4d9d-a60e-5433cac72fe1",
    "SSA_Session_Synthetic_Archive": "ebafd590-ce92-45c7-9fe7-068f7ca6d415",
    "YOS_Tools_Registry_v2": "85f89b4e-847d-4cbe-a931-0ffdf11b60f2",
    "YOS_Tools_Registry_v1": "92f217a0-59fd-4d05-aaa3-4460ccbad58d",
    "KOR_Knowledge_Object_Repository": "f2c0bc6c-54cd-46ee-a663-f7b2952fc967",
    "YOS_Archives": "31235e21-8cf8-8126-9212-f5a0eebadce0",
}

os.makedirs(OUT_DIR, exist_ok=True)

all_stats = {}

for label, db_id in DATABASES.items():
    print(f"\nProcessing: {label}")
    entries = process_db(label)
    
    # Save enhanced summary JSON
    enhanced_path = os.path.join(RAW_DIR, f"{label}_enhanced.json")
    with open(enhanced_path, 'w') as f:
        json.dump({"db_id": db_id, "label": label, "total": len(entries), "entries": entries}, f, indent=2, ensure_ascii=False)
    
    # Save markdown table
    md_content = write_markdown_table(entries, label, db_id)
    md_path = os.path.join(OUT_DIR, f"{label}.md")
    with open(md_path, 'w') as f:
        f.write(md_content)
    
    all_stats[label] = {"db_id": db_id, "total": len(entries), "md": md_path}
    print(f"  -> {len(entries)} entries, saved to {label}.md")

print("\n=== EXTRACTION COMPLETE ===")
for label, stats in all_stats.items():
    print(f"  {label}: {stats['total']} entries")
