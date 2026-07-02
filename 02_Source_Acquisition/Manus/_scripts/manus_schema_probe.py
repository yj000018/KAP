#!/usr/bin/env python3
"""Manus Schema Probe — CONN-MANUS-01. Inspects the API response schema for a single task."""
import requests, json, os

API_KEY = os.environ.get("MANUS_API_KEY", "")
BASE = "https://api.manus.im/v2"
HEADERS = {"x-manus-api-key": API_KEY}

def probe():
    if not API_KEY: print("[SKIP] MANUS_API_KEY not set"); return
    r = requests.get(f"{BASE}/task.list", headers=HEADERS, params={"limit": 1}, timeout=10)
    if r.status_code != 200: print(f"[FAIL] {r.status_code}"); return
    items = r.json() if isinstance(r.json(), list) else r.json().get("data", [])
    if not items: print("[WARN] No tasks found"); return
    print("[SCHEMA]", json.dumps(list(items[0].keys()), indent=2))

if __name__ == "__main__": probe()
