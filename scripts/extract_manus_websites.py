#!/usr/bin/env python3
"""
Extract website/deployment URLs from all Manus tasks.
Uses existing WP2-M4 task inventory if available, otherwise fetches from API.
"""
import subprocess, json, os, re, time

MANUS_KEY = "sk-TEKENLb_4FM1xUD0skvl7Y5bxdg_ZwSBn93f4UyT3obza8szuxS1v4AFcs5iokvaLur6obq0SlG80yIIr-Zu_rKeVdze"
ROOT = "/home/ubuntu/KAP/02_Source_Acquisition/WP2-M2B_Connector_Revalidation_Full_Manus_API_Harvest"
TASKS_DIR = ROOT + "/02_MANUS_API_TASKS"
WEB_DIR = ROOT + "/09_WEBSITE_LINKS_FROM_TASKS"
os.makedirs(TASKS_DIR, exist_ok=True)
os.makedirs(WEB_DIR, exist_ok=True)

# Check if we have existing full task list from WP2-M4
existing_tasks_path = "/home/ubuntu/KAP/02_Source_Acquisition/WP2-M4_Full_Manus_Tasks_Outputs_Capture"
all_tasks = []

# Try to load from existing WP2-M4 data
for fname in os.listdir(existing_tasks_path) if os.path.exists(existing_tasks_path) else []:
    if fname.endswith('.json') and 'inventory' in fname.lower():
        try:
            with open(os.path.join(existing_tasks_path, fname)) as f:
                data = json.load(f)
            if isinstance(data, list):
                all_tasks = data
                print(f"Loaded {len(all_tasks)} tasks from {fname}")
                break
            elif isinstance(data, dict) and 'tasks' in data:
                all_tasks = data['tasks']
                print(f"Loaded {len(all_tasks)} tasks from {fname}")
                break
        except:
            pass

# If no existing data, fetch from API
if not all_tasks:
    print("Fetching all tasks from Manus API...")
    cursor = None
    page = 0
    
    while True:
        page += 1
        url = "https://api.manus.im/v1/tasks?page_size=100"
        if cursor:
            url += f"&cursor={cursor}"
        
        cmd = ["curl", "-s", "--max-time", "30", "--retry", "2",
               "-H", f"x-manus-api-key: {MANUS_KEY}", url]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=45)
        
        try:
            data = json.loads(r.stdout)
        except:
            print(f"  Parse error page {page}")
            break
        
        tasks = data.get("tasks", data.get("data", []))
        all_tasks.extend(tasks)
        has_more = data.get("has_more", False)
        cursor = data.get("next_cursor", data.get("cursor"))
        print(f"  Page {page}: +{len(tasks)} (total={len(all_tasks)}, has_more={has_more})")
        
        if not has_more or not cursor or len(tasks) == 0:
            break
        time.sleep(0.3)
    
    # Save
    with open(os.path.join(TASKS_DIR, "manus_all_tasks_raw.json"), 'w') as f:
        json.dump({"total": len(all_tasks), "tasks": all_tasks}, f, indent=2, ensure_ascii=False)

print(f"\nTotal tasks to analyze: {len(all_tasks)}")

# Extract website URLs
URL_PATTERNS = [
    r'https?://[a-zA-Z0-9\-]+\.manus\.space[^\s"\'<>]*',
    r'https?://[a-zA-Z0-9\-]+\.vercel\.app[^\s"\'<>]*',
    r'https?://[a-zA-Z0-9\-]+\.netlify\.app[^\s"\'<>]*',
    r'https?://[a-zA-Z0-9\-]+\.pages\.dev[^\s"\'<>]*',
    r'https?://[a-zA-Z0-9\-]+\.github\.io[^\s"\'<>]*',
    r'https?://manus\.im/share/[^\s"\'<>]+',
    r'https?://manus\.im/app/[^\s"\'<>]+',
]

websites_found = []
github_links = []
notion_links = []

for t in all_tasks:
    task_id = t.get("id", t.get("task_id", ""))
    meta = t.get("metadata", {})
    title = meta.get("task_title", t.get("title", t.get("name", "")))
    task_url = meta.get("task_url", "")
    status = t.get("status", "")
    created = t.get("created_at", "")[:10]
    
    # Check all string fields for URLs
    task_str = json.dumps(t)
    
    for pattern in URL_PATTERNS:
        matches = re.findall(pattern, task_str)
        for url in set(matches):
            if "manus.im/app/" not in url:  # Skip task self-links
                websites_found.append({
                    "task_id": task_id,
                    "title": title[:80],
                    "url": url,
                    "status": status,
                    "created": created,
                    "confidence": "HIGH" if "manus.space" in url else "MEDIUM"
                })
    
    # GitHub links
    github_matches = re.findall(r'https?://github\.com/[^\s"\'<>]+', task_str)
    for url in set(github_matches):
        github_links.append({"task_id": task_id, "title": title[:80], "url": url, "created": created})
    
    # Notion links
    notion_matches = re.findall(r'https?://(?:www\.)?notion\.(?:so|com)/[^\s"\'<>]+', task_str)
    for url in set(notion_matches):
        notion_links.append({"task_id": task_id, "title": title[:80], "url": url, "created": created})

# Deduplicate
seen_urls = set()
unique_websites = []
for w in websites_found:
    if w['url'] not in seen_urls:
        seen_urls.add(w['url'])
        unique_websites.append(w)

print(f"\nWebsite URLs found: {len(unique_websites)}")
print(f"GitHub links: {len(github_links)}")
print(f"Notion links: {len(notion_links)}")

# Save
with open(os.path.join(WEB_DIR, "website_urls_all_tasks.json"), 'w') as f:
    json.dump(unique_websites, f, indent=2, ensure_ascii=False)

with open(os.path.join(WEB_DIR, "github_links_all_tasks.json"), 'w') as f:
    json.dump(github_links[:200], f, indent=2, ensure_ascii=False)

with open(os.path.join(WEB_DIR, "notion_links_all_tasks.json"), 'w') as f:
    json.dump(notion_links[:200], f, indent=2, ensure_ascii=False)

print("\nTop websites found:")
for w in unique_websites[:15]:
    print(f"  [{w['confidence']}] {w['url']}")
