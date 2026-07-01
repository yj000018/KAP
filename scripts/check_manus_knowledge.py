#!/usr/bin/env python3
"""
Check Manus API for Knowledge/Memory endpoints beyond tasks.
Also extract website URLs from task details.
"""
import subprocess, json, os, time

MANUS_KEY = "sk-TEKENLb_4FM1xUD0skvl7Y5bxdg_ZwSBn93f4UyT3obza8szuxS1v4AFcs5iokvaLur6obq0SlG80yIIr-Zu_rKeVdze"
ROOT = "/home/ubuntu/KAP/02_Source_Acquisition/WP2-M2B_Connector_Revalidation_Full_Manus_API_Harvest"
os.makedirs(ROOT + "/05_MANUS_KNOWLEDGE_MEMORY", exist_ok=True)

def manus_get(endpoint, params=""):
    url = f"https://api.manus.im/v1/{endpoint}"
    if params:
        url += f"?{params}"
    cmd = ["curl", "-s", "--max-time", "20", "--retry", "2",
           "-H", f"x-manus-api-key: {MANUS_KEY}", url]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    try:
        return json.loads(r.stdout)
    except:
        return {"error": r.stdout[:200]}

# Test known and potential endpoints
endpoints_to_test = [
    ("knowledge", "page_size=100"),
    ("memories", "page_size=100"),
    ("knowledge/items", "page_size=100"),
    ("projects", "page_size=100"),
    ("files", "page_size=100"),
    ("artifacts", "page_size=100"),
    ("config", ""),
    ("user", ""),
    ("me", ""),
    ("profile", ""),
    ("settings", ""),
    ("websites", "page_size=100"),
    ("deployments", "page_size=100"),
]

results = {}
print("=== Manus API Endpoint Discovery ===")
for ep, params in endpoints_to_test:
    data = manus_get(ep, params)
    if "error" in data and len(data) == 1:
        status = f"ERROR: {data['error'][:80]}"
    elif data.get("object") == "error" or data.get("code") in ("not_found", "unauthorized", "forbidden"):
        status = f"NOT_FOUND/BLOCKED: {data.get('message','?')[:80]}"
    elif isinstance(data, list):
        status = f"OK (list): {len(data)} items"
    elif isinstance(data, dict):
        keys = list(data.keys())[:8]
        count = data.get("total", data.get("count", data.get("page_size", "?")))
        status = f"OK (dict): keys={keys}, count={count}"
    else:
        status = f"UNKNOWN: {str(data)[:80]}"
    
    results[ep] = {"endpoint": ep, "status": status, "data_sample": str(data)[:200]}
    print(f"  /v1/{ep}: {status}")
    time.sleep(0.2)

# Save results
out_path = os.path.join(ROOT, "05_MANUS_KNOWLEDGE_MEMORY", "manus_api_endpoint_discovery.json")
with open(out_path, 'w') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"\nSaved: {out_path}")

# Now check tasks endpoint for website URLs in metadata
print("\n=== Checking tasks for website/deployment URLs ===")
data = manus_get("tasks", "page_size=100")
tasks = data.get("tasks", data.get("data", []))
print(f"  Got {len(tasks)} tasks in first page")

websites_found = []
for t in tasks:
    task_id = t.get("id", t.get("task_id", ""))
    title = t.get("title", t.get("name", ""))
    # Check various fields for URLs
    for field in ["website_url", "deployment_url", "url", "preview_url", "output_url", "site_url"]:
        url = t.get(field, "")
        if url and url.startswith("http"):
            websites_found.append({"task_id": task_id, "title": title, "url": url, "field": field})
    # Check metadata
    meta = t.get("metadata", t.get("extra", {}))
    if isinstance(meta, dict):
        for k, v in meta.items():
            if isinstance(v, str) and v.startswith("http") and ("manus" in v or "vercel" in v or "netlify" in v or ".space" in v or ".app" in v):
                websites_found.append({"task_id": task_id, "title": title, "url": v, "field": f"metadata.{k}"})

print(f"  Website URLs found in first 100 tasks: {len(websites_found)}")
for w in websites_found[:10]:
    print(f"    [{w['task_id']}] {w['title'][:50]} -> {w['url']}")

# Save
web_path = os.path.join(ROOT, "09_WEBSITE_LINKS_FROM_TASKS", "website_urls_from_tasks_p1.json")
os.makedirs(os.path.dirname(web_path), exist_ok=True)
with open(web_path, 'w') as f:
    json.dump(websites_found, f, indent=2, ensure_ascii=False)
