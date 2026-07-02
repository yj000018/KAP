#!/usr/bin/env python3
"""
Obsidian Vault Scanner — CONN-OBS-01
Scans a local Obsidian vault directory for .md files. No merge or mutation.
Usage: python3 obsidian_vault_scanner.py [--vault /path/to/vault] [--dry-run]
"""
import os, json, argparse, datetime

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_dry_runs")

def scan(vault_path=None):
    if not vault_path or not os.path.isdir(vault_path):
        print("[SKIP] No vault path provided or path not found — access-limited dry-run"); return
    notes = []
    for root, _, files in os.walk(vault_path):
        for f in files:
            if f.endswith(".md"):
                fp = os.path.join(root, f)
                rel = os.path.relpath(fp, vault_path)
                size = os.path.getsize(fp)
                notes.append({"path": rel, "size_bytes": size, "folder": os.path.dirname(rel)})
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out = os.path.join(OUTPUT_DIR, f"obsidian_scan_{datetime.date.today()}.json")
    with open(out, "w") as f: json.dump({"total": len(notes), "vault": vault_path, "items": notes}, f, indent=2)
    print(f"[OK] {len(notes)} notes found | Saved: {out}")

if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("--vault"); p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(); scan(args.vault)
