#!/usr/bin/env python3
"""
Fetch ALL Mem0 memories for user_id=yannick.
316 total, paginated 100/page.
"""
import subprocess, json, os, time

TOKEN = "m0-AaySh4Tbbwf2DA5TpXzqcBJSiDnFRIlFrF695fJE"
USER_ID = "yannick"
OUT_DIR = "/home/ubuntu/KAP/02_Source_Acquisition/WP2-M2B_Connector_Revalidation_Full_Manus_API_Harvest/06_MEM0_EXPORT"
os.makedirs(OUT_DIR, exist_ok=True)

all_memories = []
page = 1
page_size = 100

while True:
    cmd = ["curl", "-s", "--max-time", "30", "--retry", "2",
           "-H", f"Authorization: Token {TOKEN}",
           f"https://api.mem0.ai/v1/memories/?user_id={USER_ID}&page={page}&page_size={page_size}"]
    
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=45)
    
    if r.returncode != 0 or not r.stdout.strip():
        print(f"  ERROR: curl failed page {page}")
        break
    
    try:
        data = json.loads(r.stdout)
    except:
        print(f"  ERROR: JSON parse failed page {page}: {r.stdout[:200]}")
        break
    
    if isinstance(data, list):
        memories = data
        has_more = len(data) == page_size
    elif isinstance(data, dict):
        memories = data.get("results", data.get("memories", []))
        total = data.get("count", data.get("total", 0))
        has_more = len(all_memories) + len(memories) < total
    else:
        print(f"  ERROR: unexpected format: {str(data)[:100]}")
        break
    
    all_memories.extend(memories)
    print(f"  Page {page}: +{len(memories)} (total={len(all_memories)}, has_more={has_more})")
    
    if not has_more or len(memories) == 0:
        break
    
    page += 1
    time.sleep(0.3)

# Save raw
raw_path = os.path.join(OUT_DIR, "mem0_full_raw.json")
with open(raw_path, 'w') as f:
    json.dump({"user_id": USER_ID, "total": len(all_memories), "memories": all_memories}, f, indent=2, ensure_ascii=False)

print(f"\n=== TOTAL MEM0 MEMORIES: {len(all_memories)} ===")

# Save CSV summary
csv_path = os.path.join(OUT_DIR, "mem0_summary.csv")
with open(csv_path, 'w') as f:
    f.write("id,created_at,updated_at,memory_preview,categories,source\n")
    for m in all_memories:
        mid = m.get("id", "")
        created = m.get("created_at", "")[:19] if m.get("created_at") else ""
        updated = m.get("updated_at", "")[:19] if m.get("updated_at") else ""
        memory = m.get("memory", "").replace(",", ";").replace("\n", " ")[:120]
        cats = ";".join(m.get("categories", []))
        source = str(m.get("metadata", {}).get("source", "")).replace(",", ";")
        f.write(f"{mid},{created},{updated},{memory},{cats},{source}\n")

print(f"CSV: {csv_path}")
print("\nFirst 10 memories:")
for m in all_memories[:10]:
    mem_text = m.get("memory", "")[:100]
    created = m.get("created_at", "")[:10]
    print(f"  [{created}] {mem_text}")
