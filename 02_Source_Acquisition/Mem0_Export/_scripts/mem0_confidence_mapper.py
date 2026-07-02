#!/usr/bin/env python3
"""Mem0 Confidence Mapper — CONN-MEM0-01. Maps memory facts with confidence scores. Memories are compressed state, not source of truth."""
import os, json, datetime

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_dry_runs")

def map_confidence():
    api_key = os.environ.get("MEM0_API_KEY","")
    if not api_key: print("[SKIP] MEM0_API_KEY not set"); return
    try:
        import requests
        headers = {"Authorization": f"Token {api_key}"}
        r = requests.get("https://api.mem0.ai/v1/memories/", headers=headers, params={"user_id": "yannick", "limit": 100}, timeout=15)
        if r.status_code != 200: print(f"[FAIL] {r.status_code}"); return
        memories = r.json() if isinstance(r.json(), list) else r.json().get("results", [])
        mapped = [{"id": m.get("id",""), "memory": m.get("memory",""), "score": m.get("score", None),
                   "confidence": "HIGH" if m.get("score",0) and m.get("score",0) > 0.8 else "MEDIUM" if m.get("score",0) and m.get("score",0) > 0.5 else "LOW",
                   "warning": "Compressed state — not canonical truth without source backing"} for m in memories]
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        out = os.path.join(OUTPUT_DIR, f"mem0_confidence_{datetime.date.today()}.json")
        with open(out, "w") as f: json.dump({"total": len(mapped), "items": mapped}, f, indent=2, ensure_ascii=False)
        print(f"[OK] {len(mapped)} memories mapped | Saved: {out}")
    except ImportError: print("[FAIL] requests not installed")

if __name__ == "__main__": map_confidence()
