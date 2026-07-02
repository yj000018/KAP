#!/usr/bin/env python3
"""
Notion Full Census — KAP
Pagine l'API Notion pour récupérer toutes les pages + databases accessibles via KAP-Executor
"""
import requests, json, os

NOTION_TOKEN = os.environ.get("NOTION_TOKEN", "")
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

def get_title(obj):
    if obj.get('object') == 'page':
        props = obj.get('properties', {})
        for k, v in props.items():
            if v.get('type') == 'title':
                return ''.join([t.get('plain_text','') for t in v.get('title',[])])
        # Fallback: check title key directly
        title_obj = obj.get('title', [])
        if title_obj:
            return ''.join([t.get('plain_text','') for t in title_obj])
    elif obj.get('object') == 'database':
        return ''.join([t.get('plain_text','') for t in obj.get('title',[])])
    return '(untitled)'

def paginate_search(query="", filter_type=None):
    results = []
    cursor = None
    body = {"page_size": 100}
    if query:
        body["query"] = query
    if filter_type:
        body["filter"] = {"value": filter_type, "property": "object"}
    
    while True:
        if cursor:
            body["start_cursor"] = cursor
        resp = requests.post("https://api.notion.com/v1/search", headers=HEADERS, json=body)
        data = resp.json()
        if resp.status_code != 200:
            print(f"Error: {resp.status_code} — {data.get('message')}")
            break
        results.extend(data.get('results', []))
        if not data.get('has_more'):
            break
        cursor = data.get('next_cursor')
    return results

# Récupérer tout
print("Fetching all pages...")
all_pages = paginate_search(filter_type="page")
print(f"Pages: {len(all_pages)}")

print("Fetching all databases...")
all_dbs = paginate_search(filter_type="database")
print(f"Databases: {len(all_dbs)}")

# Classifier par workspace ROOT
workspace_map = {
    "KOSMOS": [],
    "Y-OS": [],
    "ELYSIUM": [],
    "Y-WORLD": [],
    "YANNICK": [],
    "UNCLASSIFIED": []
}

root_ids = {}

# Identifier les ROOTs
for p in all_pages:
    title = get_title(p)
    if "KOSMOS ROOT" in title:
        root_ids["KOSMOS"] = p['id']
    elif "Y-OS ROOT" in title:
        root_ids["Y-OS"] = p['id']
    elif "ELYSIUM ROOT" in title:
        root_ids["ELYSIUM"] = p['id']
    elif "Y-World ROOT" in title or "Y-WORLD ROOT" in title:
        root_ids["Y-WORLD"] = p['id']
    elif "Yannick ROOT" in title:
        root_ids["YANNICK"] = p['id']

print(f"\nROOT IDs found: {json.dumps(root_ids, indent=2)}")

# Sauvegarder le census complet
census = {
    "total_pages": len(all_pages),
    "total_databases": len(all_dbs),
    "root_ids": root_ids,
    "pages": [{"id": p['id'], "title": get_title(p), "parent": p.get('parent',{}), "url": p.get('url','')} for p in all_pages],
    "databases": [{"id": d['id'], "title": get_title(d), "parent": d.get('parent',{}), "url": d.get('url','')} for d in all_dbs]
}

with open("/tmp/notion_census.json", "w") as f:
    json.dump(census, f, indent=2)

print(f"\nCensus saved: {len(all_pages)} pages + {len(all_dbs)} databases")
print(f"Total objects: {len(all_pages) + len(all_dbs)}")

# Afficher les databases (sources KAP prioritaires)
print("\n=== DATABASES (KAP priority sources) ===")
for d in all_dbs:
    print(f"  [DB] {get_title(d)} — {d['id'][:8]}...")
EOF
