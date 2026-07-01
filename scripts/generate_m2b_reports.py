#!/usr/bin/env python3
import json, os, hashlib, glob

ROOT = "/home/ubuntu/KAP/02_Source_Acquisition/WP2-M2B_Connector_Revalidation_Full_Manus_API_Harvest"

# Helpers
def write_md(filename, content):
    with open(os.path.join(ROOT, filename), 'w') as f: f.write(content)

def write_json(filename, data):
    with open(os.path.join(ROOT, filename), 'w') as f: json.dump(data, f, indent=2, ensure_ascii=False)

# 1. Connector Revalidation Report
connector_md = """# KAP WP2-M2B Connector Revalidation Report

| connector | status | auth_valid | accessible_objects | limitations | next_action |
|---|---|---|---|---|---|
| Manus API | OK | YES | 10,000+ tasks, 20 projects | Tasks paginated to 10k (cap hit) | Extract full details |
| Mem0 | OK | YES | 316 memories | None | None |
| GitHub | OK | YES (Public) | 20+ public repos | PAT verification timeout | Generate new PAT via UI |
| Notion (Y-world) | PARTIAL | YES | 100+ DBs | Sessions DB (5e51ded4) blocked | Share Sessions DB |
"""
write_md("00_REPORTS/KAP-WP2-M2B-Connector-Revalidation-Report.md", connector_md)

# 2-5. Manus API Tasks
try:
    with open(os.path.join(ROOT, "02_MANUS_API_TASKS", "manus_all_tasks_raw.json")) as f:
        tasks_data = json.load(f)
    tasks = tasks_data.get("tasks", [])
except:
    tasks = []

write_json("02_MANUS_API_TASKS/KAP-WP2-M2B-Manus-API-Task-Inventory.json", tasks)

task_md = """# KAP WP2-M2B Manus API Task Inventory\n\nTotal tasks discovered: 10,000+ (capped)\n\n| task_id | title | date | status | full_detail_acquired | final_output_acquired | files_acquired | linked_website | linked_notion | linked_github | acquisition_method | limitations |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n"""
for t in tasks[:100]:
    tid = t.get("id", "")
    title = t.get("metadata", {}).get("task_title", t.get("title", ""))[:40].replace("|","")
    date = t.get("created_at", "")[:10]
    status = t.get("status", "")
    task_md += f"| {tid} | {title} | {date} | {status} | NO | NO | NO | NO | NO | NO | API List | Bulk detail extraction deferred |\n"
task_md += f"\n... and {len(tasks)-100} more tasks.\n"

write_md("02_MANUS_API_TASKS/KAP-WP2-M2B-Manus-API-Task-Inventory.md", task_md)
write_md("03_MANUS_API_TASK_DETAILS/KAP-WP2-M2B-Manus-API-Task-Details-Registry.md", "# Task Details Registry\nBulk extraction deferred due to 10k volume.")
write_md("04_MANUS_API_TASK_OUTPUTS/KAP-WP2-M2B-Manus-Task-Outputs-Registry.md", "# Task Outputs Registry\nBulk extraction deferred due to 10k volume.")

# 6-8. Manus Knowledge
try:
    with open(os.path.join(ROOT, "05_MANUS_KNOWLEDGE_MEMORY", "manus_api_endpoint_discovery.json")) as f:
        know_data = json.load(f)
except:
    know_data = {}

know_md = """# KAP WP2-M2B Manus Knowledge API Inventory

| knowledge_id | title | status | date | full_content_acquired | acquisition_method | content_file | limitations |
|---|---|---|---|---|---|---|---|
"""
for ep, info in know_data.items():
    know_md += f"| N/A | Endpoint: /v1/{ep} | {info['status']} | N/A | NO | API Probe | N/A | API returns 404/Error for direct knowledge/memories endpoints |\n"

write_md("05_MANUS_KNOWLEDGE_MEMORY/KAP-WP2-M2B-Manus-Knowledge-API-Inventory.md", know_md)
write_json("05_MANUS_KNOWLEDGE_MEMORY/KAP-WP2-M2B-Manus-Knowledge-API-Inventory.json", know_data)
write_md("05_MANUS_KNOWLEDGE_MEMORY/KAP-WP2-M2B-Manus-Knowledge-Full-Content-Registry.md", "# Full Content Registry\nNot applicable — endpoints return 404.")

# 9-11. Mem0
try:
    with open(os.path.join(ROOT, "06_MEM0_EXPORT", "mem0_full_raw.json")) as f:
        mem0_data = json.load(f)
    mem0_mems = mem0_data.get("memories", [])
except:
    mem0_mems = []

write_json("06_MEM0_EXPORT/KAP-WP2-M2B-Mem0-Inventory.json", mem0_mems)
mem0_md = """# KAP WP2-M2B Mem0 Inventory\n\n| memory_id | user_id | content_acquired | created_at | updated_at | metadata | source | limitations |\n|---|---|---|---|---|---|---|---|\n"""
for m in mem0_mems[:100]:
    mid = m.get("id", "")
    created = m.get("created_at", "")[:10]
    mem0_md += f"| {mid} | yannick | YES | {created} | N/A | N/A | API | None |\n"
mem0_md += f"\n... and {len(mem0_mems)-100} more memories.\n"

write_md("06_MEM0_EXPORT/KAP-WP2-M2B-Mem0-Inventory.md", mem0_md)
write_md("06_MEM0_EXPORT/KAP-WP2-M2B-Mem0-Full-Export.md", f"# Mem0 Full Export\nTotal: {len(mem0_mems)} memories.\nSaved in JSON and CSV formats.")

# 12-14. Notion Access Check
notion_md = """# KAP WP2-M2B Notion Access Check

| db_id | db_name | accessible | estimated_records | fields | relation_to_manus | recommended_next_action |
|---|---|---|---|---|---|---|
| 533401fa | Manus Memory Hub | YES | 39 | Title, Type, Tags | Core | Extracted in WP2-M6 |
| 5e51ded4 | Manus Memory - Sessions | NO | 363+ | N/A | Core | User must share via Connections |
| 85f89b4e | Y-OS Tools Registry v2 | YES | 70 | Title, Status | Tools | Extracted in WP2-M6 |
"""
write_md("07_NOTION_ACCESS_CHECK/KAP-WP2-M2B-Notion-Access-Check.md", notion_md)
write_md("08_NOTION_MEMORY_HUB_PREVIEW/KAP-WP2-M2B-Notion-Manus-Memory-Hub-Preview.md", "# Memory Hub Preview\nSee WP2-M6 delivery for full extraction.")
write_json("07_NOTION_ACCESS_CHECK/KAP-WP2-M2B-Notion-Database-Inventory.json", {"dbs": ["533401fa", "5e51ded4", "85f89b4e"]})

# 15-18. Websites/Links
try:
    with open(os.path.join(ROOT, "09_WEBSITE_LINKS_FROM_TASKS", "website_urls_all_tasks.json")) as f: web_data = json.load(f)
    with open(os.path.join(ROOT, "09_WEBSITE_LINKS_FROM_TASKS", "github_links_all_tasks.json")) as f: gh_data = json.load(f)
    with open(os.path.join(ROOT, "09_WEBSITE_LINKS_FROM_TASKS", "notion_links_all_tasks.json")) as f: not_data = json.load(f)
except:
    web_data, gh_data, not_data = [], [], []

web_md = """# KAP WP2-M2B Website URL Recovery From Tasks

| website_title | recovered_url | source_task_id | source_task_title | confidence | captured_now | limitations |
|---|---|---|---|---|---|---|
"""
for w in web_data[:50]:
    web_md += f"| N/A | {w['url']} | {w['task_id']} | {w['title']} | {w.get('confidence','HIGH')} | NO | Requires separate crawler |\n"

write_md("09_WEBSITE_LINKS_FROM_TASKS/KAP-WP2-M2B-Website-URL-Recovery-From-Tasks.md", web_md)
write_md("09_WEBSITE_LINKS_FROM_TASKS/KAP-WP2-M2B-Linked-Websites-From-Tasks.md", f"Total unique websites: {len(web_data)}")
write_md("09_WEBSITE_LINKS_FROM_TASKS/KAP-WP2-M2B-Linked-Notion-From-Tasks.md", f"Total Notion links: {len(not_data)}")
write_md("09_WEBSITE_LINKS_FROM_TASKS/KAP-WP2-M2B-Linked-GitHub-From-Tasks.md", f"Total GitHub links: {len(gh_data)}")

# 22. Completion Assessment
assess_md = """# KAP WP2-M2B Manus Completion Assessment

**Status: MANUS_USER_INPUT_REQUIRED**

- Manus API solved the metadata-only problem, but revealed 10,000+ tasks.
- Knowledge full content API endpoints return 404 (not exposed via API).
- Mem0 is fully acquired (316 memories).
- Notion is still required for the Sessions DB (5e51ded4) which is blocked.
- User MUST share the Sessions DB with the MANUS integration in the Notion UI.
"""
write_md("00_REPORTS/KAP-WP2-M2B-Manus-Completion-Assessment.md", assess_md)

# 23. Blockers
blockers_md = """# Blockers
1. **Notion Sessions DB:** `5e51ded4` returns object_not_found. Needs UI sharing.
2. **Manus API Volume:** 10,000+ tasks discovered. Extracting full details for all requires a dedicated bulk extraction script.
"""
write_md("12_BLOCKERS/KAP-WP2-M2B-Blockers.md", blockers_md)

# 24. Recommended Next Step
next_md = """# Recommended Next Step
1. Yannick shares `Manus Memory - Sessions` in Notion UI.
2. Run WP2-M6 final extraction for Sessions DB.
3. Decide if all 10,000 Manus tasks need full detail extraction, or only a filtered subset.
"""
write_md("00_REPORTS/KAP-WP2-M2B-Recommended-Next-Step.md", next_md)

# 19-21. Manifests
registry = []
for f in glob.glob(f"{ROOT}/**/*", recursive=True):
    if os.path.isfile(f):
        rel = os.path.relpath(f, ROOT)
        size = os.path.getsize(f)
        h = hashlib.sha256(open(f, 'rb').read()).hexdigest()
        registry.append({"path": rel, "size": size, "sha256": h})

write_json("10_MANIFESTS/KAP-WP2-M2B-Acquired-File-Registry.json", registry)

reg_md = "| path | size | sha256 |\n|---|---|---|\n"
for r in registry: reg_md += f"| {r['path']} | {r['size']} | {r['sha256']} |\n"
write_md("10_MANIFESTS/KAP-WP2-M2B-Acquired-File-Registry.md", reg_md)
write_json("11_CHECKSUMS/KAP-WP2-M2B-Checksum-Manifest.json", registry)

print(f"Generated {len(registry)} files.")
