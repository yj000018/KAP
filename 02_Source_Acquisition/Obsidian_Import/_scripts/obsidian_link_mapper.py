#!/usr/bin/env python3
"""Obsidian Link Mapper — CONN-OBS-01. Maps [[wikilinks]] across vault notes."""
import os, json, re, argparse, datetime

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_dry_runs")
WIKILINK_RE = re.compile(r'\[\[([^\]]+)\]\]')

def map_links(vault_path=None):
    if not vault_path or not os.path.isdir(vault_path):
        print("[SKIP] No vault path provided"); return
    link_map = {}
    for root, _, files in os.walk(vault_path):
        for f in files:
            if not f.endswith(".md"): continue
            fp = os.path.join(root, f)
            rel = os.path.relpath(fp, vault_path)
            with open(fp, encoding="utf-8", errors="ignore") as fh: content = fh.read()
            links = WIKILINK_RE.findall(content)
            if links: link_map[rel] = links
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out = os.path.join(OUTPUT_DIR, f"obsidian_links_{datetime.date.today()}.json")
    with open(out, "w") as f: json.dump({"total_files_with_links": len(link_map), "map": link_map}, f, indent=2)
    print(f"[OK] {len(link_map)} files with wikilinks | Saved: {out}")

if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("--vault"); p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(); map_links(args.vault)
