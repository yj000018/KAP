#!/usr/bin/env python3
"""
ChatGPT Export Schema Probe — CONN-OAI-01
Inspects the structure of a ChatGPT conversations.json export file (no API needed).
Usage: python3 chatgpt_export_schema_probe.py [--file path/to/conversations.json] [--dry-run]
"""
import json, os, sys, argparse, datetime

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_dry_runs")

def probe(filepath=None):
    if not filepath or not os.path.exists(filepath):
        print("[SKIP] No conversations.json provided — access-limited dry-run")
        print("[INFO] To use: export ChatGPT data from https://chat.openai.com/settings, then run:")
        print("       python3 chatgpt_export_schema_probe.py --file /path/to/conversations.json")
        return
    with open(filepath) as f: data = json.load(f)
    if isinstance(data, list): convs = data
    elif isinstance(data, dict): convs = data.get("conversations", [data])
    else: print("[FAIL] Unexpected format"); return
    sample = convs[0] if convs else {}
    print(f"[SCHEMA] Fields: {list(sample.keys())}")
    print(f"[INFO] Total conversations: {len(convs)}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out = os.path.join(OUTPUT_DIR, f"chatgpt_schema_probe_{datetime.date.today()}.json")
    with open(out, "w") as f:
        json.dump({"total": len(convs), "schema_fields": list(sample.keys()), "sample_titles": [c.get("title","") for c in convs[:10]]}, f, indent=2)
    print(f"[OK] Schema probe saved: {out}")

if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("--file"); p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(); probe(args.file)
