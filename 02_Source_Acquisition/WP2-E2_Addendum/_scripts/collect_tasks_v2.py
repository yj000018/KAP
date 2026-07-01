#!/usr/bin/env python3
"""
KAP WP2-E2 Addendum — Manus Tasks Inventory v2
Tries multiple API endpoints to find the correct one.
"""
import json, os, time, requests
from pathlib import Path

TOKEN = os.environ.get("MANUS_TOKEN", (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
    ".eyJlbWFpbCI6Inlhbm5pY2suam9sbGlldEBnbWFpbC5jb20iLCJleHAiOjE3ODM0MzEwOTMsImlhdCI6MTc3NTY1NTA5MywianRpIjoiY3dUOUxoOEtzNmNacEwzakVSaHozQyIsIm5hbWUiOiJZYW5uaWNrIEpvbGxpZXQiLCJvcmlnaW5hbF91c2VyX2lkIjoiIiwidGVhbV91aWQiOiIiLCJ0eXBlIjoidXNlciIsInVzZXJfaWQiOiIzMTA0MTk2NjMwMzIzODE4MzMifQ"
    ".88v6mbthCgzJQwUAc1-_wKYo-8uSdQ_qkro7C2cYVuM"
))

HEADERS_BASE = {
    "Authorization": f"Bearer {TOKEN}",
    "connect-protocol-version": "1",
    "x-client-id": "SH6GDQiPhdFcHsaqh7U4Rm",
}

# Try different endpoint patterns
ENDPOINTS_TO_TRY = [
    ("GET",  "https://api.manus.im/api/v1/tasks", {}),
    ("POST", "https://api.manus.im/api/v1/tasks/list", {"offset": 0, "limit": 100}),
    ("GET",  "https://api.manus.im/api/v1/task/list", {}),
    ("POST", "https://api.manus.im/api/v1/task/list", {"offset": 0, "limit": 100}),
    ("GET",  "https://api.manus.im/api/v1/sessions", {}),
    ("POST", "https://api.manus.im/api/v1/sessions/list", {"offset": 0, "limit": 100}),
    ("GET",  "https://api.manus.im/api/v1/user/tasks", {}),
    ("GET",  "https://api.manus.im/api/v1/user/sessions", {}),
    ("POST", "https://api.manus.im/api/v1/session/list", {"filters": {}, "offset": 0, "limit": 100}),
]

def try_endpoints():
    results = {}
    for method, url, body in ENDPOINTS_TO_TRY:
        try:
            headers = dict(HEADERS_BASE)
            if method == "POST":
                headers["Content-Type"] = "application/json"
                resp = requests.post(url, headers=headers, json=body, timeout=15)
            else:
                resp = requests.get(url, headers=headers, timeout=15)
            
            print(f"  [{method}] {url} → {resp.status_code}")
            if resp.status_code == 200:
                data = resp.json()
                print(f"    Keys: {list(data.keys()) if isinstance(data, dict) else f'list({len(data)})'}")
                results[url] = {"status": resp.status_code, "data": data}
            elif resp.status_code not in [404, 405]:
                print(f"    Body: {resp.text[:150]}")
        except Exception as e:
            print(f"  [{method}] {url} → ERROR: {e}")
        time.sleep(0.3)
    return results

# Also try the manus-api skill approach
def try_manus_skill_api():
    """Try the approach from manus-api skill."""
    try:
        # Check if manus-api skill has endpoint info
        skill_path = Path("/home/ubuntu/skills/manus-api/SKILL.md")
        if skill_path.exists():
            content = skill_path.read_text()
            print("\n--- manus-api SKILL.md excerpt ---")
            # Find API endpoint info
            for line in content.split('\n'):
                if any(kw in line.lower() for kw in ['endpoint', 'api.manus', 'base_url', 'task', 'session']):
                    print(f"  {line}")
    except Exception as e:
        print(f"  Error reading manus-api skill: {e}")

if __name__ == "__main__":
    print("=== Testing Manus API endpoints ===")
    results = try_endpoints()
    try_manus_skill_api()
    
    # Save results
    out = Path("/home/ubuntu/KAP/02_Source_Acquisition/WP2-E2_Addendum/manus_tasks")
    out.mkdir(parents=True, exist_ok=True)
    with open(out / "api_probe_results.json", "w") as f:
        # Remove non-serializable data
        safe = {k: {"status": v["status"]} for k, v in results.items()}
        json.dump(safe, f, indent=2)
    
    print(f"\nSuccessful endpoints: {[k for k,v in results.items() if v['status']==200]}")
