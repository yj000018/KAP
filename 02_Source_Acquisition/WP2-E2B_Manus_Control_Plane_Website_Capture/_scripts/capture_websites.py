#!/usr/bin/env python3
"""
KAP WP2-E2B — Manus Deployed Websites Capture
Captures metadata + HTML + text for P0/P1 deployed sites.
"""
import requests, hashlib, json, os, time
from pathlib import Path
from datetime import datetime

ROOT = Path("/home/ubuntu/KAP/02_Source_Acquisition/WP2-E2B_Manus_Control_Plane_Website_Capture")
WEB_DIR = ROOT / "02_RAW_MIRRORS/KAP-SRC-MANUS-WEBSITES-0001_Manus_Deployed_Websites"
CONTENT_DIR = ROOT / "02_RAW_MIRRORS/KAP-SRC-MANUS-WEBSITE-CONTENT-0001_Website_Content_Capture"
HTML_DIR = ROOT / "06_HTML_SNAPSHOTS"
TEXT_DIR = ROOT / "07_TEXT_EXTRACTS"
SS_DIR = ROOT / "05_SCREENSHOTS"

for d in [WEB_DIR, CONTENT_DIR, HTML_DIR, TEXT_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# Known deployed Manus sites (from Library page + task titles)
# These are inferred from task titles with [✓] and "Deploy/Build website" keywords
KNOWN_SITES = [
    {
        "id": "KAP-WEB-001",
        "title": "Human Awakening Lab Website",
        "task": "[✓] Human Awakening Lab Website Deployment with Unified Architecture",
        "priority": "P1",
        "url_candidates": [
            "https://human-awakening-lab.manus.space",
            "https://humanawakeninglab.manus.space",
        ]
    },
    {
        "id": "KAP-WEB-002",
        "title": "Unified Planetary Transformation Ecosystem",
        "task": "[✓] Deploy Unified Planetary Transformation Ecosystem Website",
        "priority": "P1",
        "url_candidates": [
            "https://planetary-transformation.manus.space",
            "https://unified-planetary.manus.space",
        ]
    },
    {
        "id": "KAP-WEB-003",
        "title": "Multi-Agent LLM Analysis App",
        "task": "[✓] Create and Deploy Multi-Agent LLM Analysis App",
        "priority": "P0",
        "url_candidates": [
            "https://multi-agent-llm.manus.space",
            "https://llm-analysis.manus.space",
        ]
    },
    {
        "id": "KAP-WEB-004",
        "title": "AI-Powered Iris Analysis Web App",
        "task": "[✓] Build AI-Powered Iris Analysis Web App",
        "priority": "P1",
        "url_candidates": [
            "https://iris-analysis.manus.space",
            "https://ai-iris.manus.space",
        ]
    },
    {
        "id": "KAP-WEB-005",
        "title": "Multilingual Spiritual Library Platform",
        "task": "[✓] Finalizing Multilingual Spiritual Library Platform Launch",
        "priority": "P1",
        "url_candidates": [
            "https://spiritual-library.manus.space",
            "https://librairie-spirituelle.manus.space",
        ]
    },
    {
        "id": "KAP-WEB-006",
        "title": "GPT-Manus Command Bridge",
        "task": "[✓] GPT-Manus Command Bridge Script Deployment and Configuration",
        "priority": "P0",
        "url_candidates": [
            "https://gpt-manus-bridge.manus.space",
        ]
    },
    {
        "id": "KAP-WEB-007",
        "title": "ynot.cafe domain",
        "task": "[✓] Domain accessibility check for ynot.cafe",
        "priority": "P2",
        "url_candidates": [
            "https://ynot.cafe",
        ]
    },
]

HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

def safe_name(title):
    return "".join(c if c.isalnum() or c in "-_" else "_" for c in title[:40])

def capture_site(site):
    result = {**site, "captured_at": datetime.utcnow().isoformat() + "Z",
              "live_url": None, "status_code": None, "html_path": None,
              "text_path": None, "checksum": None, "size_bytes": None}
    
    for url in site.get("url_candidates", []):
        try:
            r = requests.get(url, headers=HEADERS, timeout=10, allow_redirects=True)
            if r.status_code == 200:
                result["live_url"] = r.url
                result["status_code"] = 200
                result["size_bytes"] = len(r.content)
                result["checksum"] = hashlib.sha256(r.content).hexdigest()
                
                sname = safe_name(site["title"])
                html_path = HTML_DIR / f"{sname}.html"
                html_path.write_bytes(r.content)
                result["html_path"] = str(html_path)
                
                # Extract text
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(r.content, 'html.parser')
                text = soup.get_text(separator='\n', strip=True)
                text_path = TEXT_DIR / f"{sname}.txt"
                text_path.write_text(text[:50000], encoding='utf-8')
                result["text_path"] = str(text_path)
                result["text_preview"] = text[:500]
                
                print(f"  ✅ {site['title']}: {r.url} ({len(r.content)} bytes)")
                break
            else:
                result["status_code"] = r.status_code
                print(f"  ⚠️  {url}: HTTP {r.status_code}")
        except Exception as e:
            print(f"  ❌ {url}: {e}")
    
    if not result["live_url"]:
        result["status"] = "NOT_FOUND"
        print(f"  ❌ {site['title']}: all URLs failed")
    
    return result

def main():
    print("=== KAP WP2-E2B — Website Capture ===")
    results = []
    for site in KNOWN_SITES:
        print(f"\n[{site['priority']}] {site['title']}")
        r = capture_site(site)
        results.append(r)
        time.sleep(0.5)
    
    found = [r for r in results if r.get("live_url")]
    not_found = [r for r in results if not r.get("live_url")]
    
    print(f"\n=== RESULTS ===")
    print(f"Found: {len(found)}/{len(results)}")
    
    with open(WEB_DIR / "website_inventory.json", 'w') as f:
        json.dump({
            "total": len(results),
            "found": len(found),
            "not_found": len(not_found),
            "sites": results,
            "note": "URLs inferred from task titles — Manus API v2 blocked (no API key). Direct URL probing used.",
            "captured_at": datetime.utcnow().isoformat() + "Z"
        }, f, indent=2, ensure_ascii=False)
    
    print(f"Saved to {WEB_DIR}/website_inventory.json")
    return results

if __name__ == "__main__":
    main()
