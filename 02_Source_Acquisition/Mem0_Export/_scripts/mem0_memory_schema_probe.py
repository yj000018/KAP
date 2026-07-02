#!/usr/bin/env python3
"""
Mem0 Memory Schema Probe — CONN-MEM0-01
Fetches a sample of memory facts to inspect schema. No canonicalization.
Requires: MEM0_API_KEY env var.
"""
import os, json, datetime

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_dry_runs")

def probe():
    api_key = os.environ.get("MEM0_API_KEY","")
    if not api_key: print("[SKIP] MEM0_API_KEY not set — access-limited dry-run"); return
    try:
        import requests
        headers = {"Authorization": f"Token {api_key}"}
        r = requests.get("https://api.mem0.ai/v1/memories/", headers=headers, params={"user_id": "yannick", "limit": 10}, timeout=15)
        if r.status_code != 200: print(f"[FAIL] {r.status_code}: {r.text[:200]}"); return
        memories = r.json() if isinstance(r.json(), list) else r.json().get("results", [])
        schema = list(memories[0].keys()) if memories else []
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        out = os.path.join(OUTPUT_DIR, f"mem0_schema_probe_{datetime.date.today()}.json")
        with open(out, "w") as f: json.dump({"total_sample": len(memories), "schema_fields": schema}, f, indent=2)
        print(f"[OK] {len(memories)} memories sampled | Schema: {schema} | Saved: {out}")
    except ImportError: print("[FAIL] requests not installed")

if __name__ == "__main__": probe()
