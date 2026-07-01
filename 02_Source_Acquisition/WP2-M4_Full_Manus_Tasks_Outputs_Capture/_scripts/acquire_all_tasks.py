#!/usr/bin/env python3
"""
KAP WP2-M4 — Full Manus Tasks Acquisition
Acquires all 2392 task metadata, classifies by project/domain, extracts linked websites
"""
import requests, json, os, hashlib, re
from datetime import datetime
from pathlib import Path

MANUS = "sk-TEKENLb_4FM1xUD0skvl7Y5bxdg_ZwSBn93f4UyT3obza8szuxS1v4AFcs5iokvaLur6obq0SlG80yIIr-Zu_rKeVdze"
M4ROOT = Path("/home/ubuntu/KAP/02_Source_Acquisition/WP2-M4_Full_Manus_Tasks_Outputs_Capture")

# Project name mapping (from API)
PROJECTS = {
    "9GjP3A95mkVdcWbXKJmQQX": "Y-OS",
    "DeoQgC2KePiJrzHGH5xGYa": "MDMA-ONENESS",
    "GPsAbGNxGGdEdUKknsfRn5": "mac-root",
    "jipiV8WJS6hyCh9FW2MTLU": "Y-Life",
    "N4Bmkkd87EMvLQiptozZ8M": "eia",
    "XoXfPkktwg3P67up5FMmKG": "VISUAL-REALITY",
    "dFVGvbFJ9iR4NUEgVDwBzH": "MEDIA-CREA",
    "9Jn9dnhtjDL8ERjyijv5Fj": "ELYSIUM",
    "nSfXw9MBovFvxuTvtUQyy4": "LUDIVINE",
    "KkbgmW9PGcVHXCkPhWbV2q": "FULL-MAC-ACCESS",
    "iLuFWy8LyLjaV5LJCBQgrd": "archives",
    "NsUBejjCJaeUbbWMxr8dye": "Y-ONE",
    "o6UZWvrbKd9HiBNNnCtVVm": "LightWay",
    "6ooCyNCA3LtXLR9LjmQnvV": "KAP",
    "TgKTXckuquNUhNTpf6cTbh": "MAGIC-AI",
    "BvaDD4T2s54TsyQCiJo8Xw": "Odyssey",
    "REpSwLtfVYiWbZVuj3cE6C": "GEN5",
    "bL6ZPrH59xoaYXxY8HVdxZ": "Y-World",
    "GeNvwGBvdyBGDN65g2zTEp": "HOME-AUTOMATION",
    "gGoVizty5NhxjYoKGXZqqW": "PRECIPITATION",
}

# Priority classification by title keywords
P0_KEYWORDS = ["kap", "yos", "y-os", "memory", "notion", "mem0", "context", "pipeline", 
                "session", "manus", "skill", "living backbone", "cosa", "agent", "llm", 
                "routing", "program os", "mop", "adr", "knowledge assimilation"]
P1_KEYWORDS = ["elysium", "kosmos", "oneshift", "civilization", "awakening", "divine", 
                "archetype", "knowledge graph", "website", "youniverse", "y-world"]
P2_KEYWORDS = ["finance", "health", "real estate", "travel", "app", "prototype", "personal"]

def classify_priority(title, project_name):
    title_lower = (title or "").lower()
    proj_lower = (project_name or "").lower()
    combined = title_lower + " " + proj_lower
    
    if any(kw in combined for kw in P0_KEYWORDS):
        return "P0"
    if any(kw in combined for kw in P1_KEYWORDS):
        return "P1"
    if any(kw in combined for kw in P2_KEYWORDS):
        return "P2"
    return "P3"

def get_domain(title, project_name):
    title_lower = (title or "").lower()
    proj = (project_name or "").lower()
    if "kap" in title_lower or "kap" in proj: return "KAP"
    if "yos" in title_lower or "y-os" in title_lower or proj in ["y-os", "y-life"]: return "yOS"
    if "elysium" in title_lower or "elysium" in proj: return "ELYSIUM"
    if "memory" in title_lower or "notion" in title_lower or "mem0" in title_lower: return "MEMORY"
    if "website" in title_lower or "youniverse" in title_lower: return "WEBSITES"
    if "mac" in title_lower or "mac" in proj: return "MAC"
    if "health" in title_lower or "mdma" in proj: return "HEALTH"
    if "finance" in title_lower: return "FINANCE"
    if "real estate" in title_lower: return "REAL-ESTATE"
    return "GENERAL"

# --- STEP 1: Paginate all tasks ---
print("Paginating all tasks...")
all_tasks = []
cursor = None
page = 0
while True:
    params = {"page_size": 100}
    if cursor:
        params["after"] = cursor
    r = requests.get("https://api.manus.im/v1/tasks", headers={"x-manus-api-key": MANUS}, params=params, timeout=20)
    if r.status_code != 200:
        print(f"Error page {page}: {r.status_code}")
        break
    data = r.json()
    batch = data.get("data", [])
    all_tasks.extend(batch)
    page += 1
    if page % 5 == 0:
        print(f"  Page {page}: {len(all_tasks)} tasks...")
    if not data.get("has_more") or not batch:
        break
    cursor = batch[-1]["id"]
    if page > 300:
        break

print(f"Total tasks: {len(all_tasks)}")

# --- STEP 2: Get project task assignments ---
print("Getting project task assignments...")
project_tasks = {}
for proj_id, proj_name in PROJECTS.items():
    r = requests.get(f"https://api.manus.im/v1/projects/{proj_id}", 
                      headers={"x-manus-api-key": MANUS}, timeout=10)
    if r.status_code == 200:
        pd = r.json()
        # Check if project has task list
        task_ids = pd.get("task_ids", [])
        project_tasks[proj_id] = task_ids

# Build task-to-project map from metadata
task_project_map = {}
for task in all_tasks:
    meta = task.get("metadata", {})
    task_url = meta.get("task_url", "")
    # Check if task URL contains project info
    for proj_id, proj_name in PROJECTS.items():
        if proj_id in task_url:
            task_project_map[task["id"]] = proj_name
            break

# --- STEP 3: Classify and enrich tasks ---
print("Classifying tasks...")
enriched_tasks = []
linked_websites = []
domain_counts = {}
priority_counts = {"P0": 0, "P1": 0, "P2": 0, "P3": 0}

for i, task in enumerate(all_tasks):
    meta = task.get("metadata", {})
    title = meta.get("task_title", "")
    task_url = meta.get("task_url", "")
    project_name = task_project_map.get(task["id"], "")
    
    priority = classify_priority(title, project_name)
    domain = get_domain(title, project_name)
    
    priority_counts[priority] = priority_counts.get(priority, 0) + 1
    domain_counts[domain] = domain_counts.get(domain, 0) + 1
    
    # Check for website links in title
    website_url = None
    if "manus.space" in title.lower() or "manus.space" in task_url.lower():
        website_url = task_url
        linked_websites.append({"task_id": task["id"], "title": title, "url": website_url})
    
    enriched = {
        "task_id": task["id"],
        "title": title,
        "date": datetime.fromtimestamp(int(task.get("created_at", 0))).strftime("%Y-%m-%d") if task.get("created_at") else "",
        "status": task.get("status", ""),
        "model": task.get("model", ""),
        "credit_usage": task.get("credit_usage", 0),
        "priority": priority,
        "domain": domain,
        "project": project_name,
        "task_url": task_url,
        "full_text_acquired": "No",
        "final_output_acquired": "No",
        "files_acquired": "No",
        "linked_website": website_url or "",
        "acquisition_method": "API_METADATA",
        "limitations": "No /messages or /files endpoint in API v1"
    }
    enriched_tasks.append(enriched)

# --- STEP 4: Save outputs ---
print("Saving outputs...")

# Full JSON
with open(M4ROOT / "01_TASK_INVENTORY/KAP-WP2-M4-Full-Tasks-Inventory.json", "w") as f:
    json.dump(enriched_tasks, f, indent=2)

# Checksums
with open(M4ROOT / "08_CHECKSUMS/tasks_inventory_checksum.txt", "w") as f:
    data_str = json.dumps(enriched_tasks, sort_keys=True)
    f.write(f"SHA256: {hashlib.sha256(data_str.encode()).hexdigest()}\n")
    f.write(f"Task count: {len(enriched_tasks)}\n")
    f.write(f"Generated: {datetime.now().isoformat()}\n")

# Linked websites
with open(M4ROOT / "04_LINKED_WEBSITES/linked_websites.json", "w") as f:
    json.dump(linked_websites, f, indent=2)

print(f"\n=== RESULTS ===")
print(f"Total tasks: {len(enriched_tasks)}")
print(f"Priority breakdown: {priority_counts}")
print(f"Domain breakdown: {domain_counts}")
print(f"Linked websites found: {len(linked_websites)}")

# Print sample P0 tasks
p0_tasks = [t for t in enriched_tasks if t["priority"] == "P0"]
print(f"\nP0 tasks ({len(p0_tasks)}):")
for t in p0_tasks[:20]:
    print(f"  [{t['domain']}] {t['title'][:70]}")

if __name__ == "__main__":
    pass
