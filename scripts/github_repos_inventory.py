#!/usr/bin/env python3
"""Extract full GitHub repos inventory from API response."""
import json

with open('/tmp/gh_repos_p1.json') as f:
    repos = json.load(f)

print(f"Total repos: {len(repos)}\n")
print(f"{'#':>2} | {'Name':40s} | {'Visibility':10s} | {'Language':12s} | {'Updated':10s} | {'Description'}")
print("-" * 140)

for i, r in enumerate(repos, 1):
    name = r.get('name', '?')
    vis = 'private' if r.get('private') else 'public'
    lang = r.get('language') or '-'
    updated = r.get('updated_at', '')[:10]
    desc = (r.get('description') or '-')[:80]
    print(f"{i:>2} | {name:40s} | {vis:10s} | {lang:12s} | {updated} | {desc}")

# Also check if there are repos visible from screenshots but missing from API
screenshot_repos = [
    "YOS", "KAP", "yos-llm-pipeline", "eia-awakening-petal", "yos-bus",
    "yos-scripts", "Y-WORLD", "yos-manus-client", "casa-tao-nest",
    "elysium-civilizational-ontology", "yos-cockpit", "one-galaxy",
    "relevance-ai-workforce", "yos-voice-vision", "yos-continuity-protocol",
    "y-menu", "manus-enhancer", "yos-userscripts", "future-news-project",
    "elysium-book", "y-llm-exporter", "civilizational-awakening",
    "yos-governance", "yos-skills", "yos-project", "YMap", "Y-Browser-Admin",
    "daylog-mvp", "daylog", "yos-voice-gateway", "youniverse", "pulse-app",
    "remotion-project", "UniversalChatThemeCanon", "desktop-tutorial", "yannick"
]

api_names = {r['name'] for r in repos}
missing = [n for n in screenshot_repos if n not in api_names]
if missing:
    print(f"\n⚠️  Repos visible in screenshots but NOT returned by this PAT ({len(missing)}):")
    for m in missing:
        print(f"   - {m}")
    print("\n→ This PAT may have limited scope. Consider using the newer PAT (ghp_PZalt6Au...) or checking token permissions.")
