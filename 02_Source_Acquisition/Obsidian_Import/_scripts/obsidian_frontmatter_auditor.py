#!/usr/bin/env python3
"""Obsidian Frontmatter Auditor — CONN-OBS-01. Detects YAML frontmatter in vault notes."""
import os, json, re, argparse, datetime

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_dry_runs")
FM_RE = re.compile(r'^---\n(.*?)\n---', re.DOTALL)

def audit(vault_path=None):
    if not vault_path or not os.path.isdir(vault_path):
        print("[SKIP] No vault path provided"); return
    results = []
    for root, _, files in os.walk(vault_path):
        for f in files:
            if not f.endswith(".md"): continue
            fp = os.path.join(root, f)
            with open(fp, encoding="utf-8", errors="ignore") as fh: content = fh.read(2000)
            has_fm = bool(FM_RE.match(content))
            results.append({"file": os.path.relpath(fp, vault_path), "has_frontmatter": has_fm})
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out = os.path.join(OUTPUT_DIR, f"obsidian_frontmatter_{datetime.date.today()}.json")
    with open(out, "w") as f: json.dump({"total": len(results), "with_fm": sum(1 for r in results if r["has_frontmatter"]), "items": results}, f, indent=2)
    print(f"[OK] {len(results)} notes | {sum(1 for r in results if r['has_frontmatter'])} with frontmatter | Saved: {out}")

if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("--vault"); p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(); audit(args.vault)
