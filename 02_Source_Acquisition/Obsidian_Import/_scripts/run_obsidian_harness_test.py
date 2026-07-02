#!/usr/bin/env python3
"""
run_obsidian_harness_test.py
KAP Obsidian Harness Runner — FAKE VAULT ONLY

SAFETY: This runner ONLY operates on the fake test vault.
Real vault path is FORBIDDEN. Any other path causes a safe failure.

Acquisition Allowed: NO
Real Vault Execution Allowed: NO
Source Mutation: NO
"""

import os
import sys
import json
import hashlib
import re
from pathlib import Path
from datetime import datetime, timezone

# ─── SAFETY CONSTANTS ────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
OBSIDIAN_BASE = SCRIPT_DIR.parent
ALLOWED_VAULT = OBSIDIAN_BASE / "_tests" / "fake_vault"
INDEXES_DIR = OBSIDIAN_BASE / "_indexes"
DRY_RUNS_DIR = OBSIDIAN_BASE / "_dry_runs"

# KAP Branch classifier rules
BRANCH_RULES = [
    (["KOSMOS", "Cosmos", "Ontology", "Metaphysics"], "KOSMOS/"),
    (["Y-OS", "yOS", "WireOS", "Agent", "Automation", "Memory"], "Y-OS/"),
    (["CasaTAO", "House", "Home AI", "Frigate", "Coral", "Vision"], "CasaTAO/"),
    (["ELYSIUM"], "ELYSIUM/"),
    (["YOUniverse", "Y World", "Private"], "YOUniverse/"),
]

ATTACHMENT_EXTENSIONS = {
    "image": [".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp"],
    "pdf": [".pdf"],
    "audio": [".mp3", ".wav", ".ogg", ".m4a", ".flac"],
    "video": [".mp4", ".mov", ".avi", ".mkv", ".webm"],
    "document": [".docx", ".xlsx", ".pptx", ".odt", ".csv"],
}

# ─── SAFETY CHECK ─────────────────────────────────────────────────────────────
def check_vault_safety(vault_path: Path) -> None:
    vault_path = vault_path.resolve()
    allowed = ALLOWED_VAULT.resolve()
    if not str(vault_path).startswith(str(allowed)):
        print(f"[SAFETY FAIL] Vault path '{vault_path}' is NOT under allowed fake vault path.")
        print(f"[SAFETY FAIL] Allowed path: {allowed}")
        print("[SAFETY FAIL] This harness runner may ONLY run against the fake test vault.")
        sys.exit(1)
    print(f"[SAFETY OK] Vault path validated: {vault_path}")

# ─── MODULE 1: VAULT SCANNER ──────────────────────────────────────────────────
def scan_vault(vault_path: Path) -> list:
    notes = []
    for md_file in sorted(vault_path.rglob("*.md")):
        stat = md_file.stat()
        content = md_file.read_text(encoding="utf-8", errors="replace")
        content_hash = hashlib.md5(content.encode()).hexdigest()
        
        # Extract frontmatter
        fm_present = content.startswith("---")
        fm_fields = {}
        tags = []
        title = md_file.stem
        if fm_present:
            fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
            if fm_match:
                for line in fm_match.group(1).split("\n"):
                    if ":" in line:
                        k, _, v = line.partition(":")
                        fm_fields[k.strip()] = v.strip()
                if "title" in fm_fields:
                    title = fm_fields["title"]
                if "tags" in fm_fields:
                    raw_tags = fm_fields["tags"].strip("[]").split(",")
                    tags = [t.strip() for t in raw_tags if t.strip()]
        
        # Extract wikilinks
        wikilinks_out = re.findall(r"\[\[([^\]]+)\]\]", content)
        wikilinks_out = [w.split("|")[0].strip() for w in wikilinks_out]
        
        # Extract attachment refs
        attachments = re.findall(r"!\[\[([^\]]+)\]\]", content)
        attachments += re.findall(r"!\[.*?\]\(([^)]+)\)", content)
        
        # Classify KAP branch
        candidate_branch = "REVIEW_REQUIRED"
        confidence = "LOW"
        reason = "No matching pattern"
        text_to_check = title + " " + " ".join(tags) + " " + str(md_file.parts)
        for keywords, branch in BRANCH_RULES:
            for kw in keywords:
                if kw.lower() in text_to_check.lower():
                    candidate_branch = branch
                    confidence = "HIGH"
                    reason = f"Keyword match: '{kw}'"
                    break
            if candidate_branch != "REVIEW_REQUIRED":
                break
        
        rel = md_file.relative_to(vault_path)
        notes.append({
            "source_path": str(md_file),
            "relative_path": str(rel),
            "filename": md_file.name,
            "title": title,
            "created_at": datetime.fromtimestamp(stat.st_ctime, tz=timezone.utc).isoformat(),
            "modified_at": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
            "size_bytes": stat.st_size,
            "content_hash": content_hash,
            "frontmatter_present": fm_present,
            "frontmatter_fields": fm_fields,
            "tags": tags,
            "wikilinks_out": wikilinks_out,
            "wikilinks_in": [],
            "attachments": attachments,
            "candidate_kap_branch": candidate_branch,
            "classification_confidence": confidence,
            "classification_reason": reason,
            "duplicate_candidate": False,
            "import_authorized": False,
            "source_mutated": False,
        })
    
    # Backfill wikilinks_in
    all_titles = {n["title"]: n["relative_path"] for n in notes}
    all_filenames = {n["filename"].replace(".md", ""): n["relative_path"] for n in notes}
    for note in notes:
        for other in notes:
            for wl in other["wikilinks_out"]:
                wl_base = wl.split("/")[-1]
                if wl_base == note["title"] or wl_base == note["filename"].replace(".md", ""):
                    if other["relative_path"] not in note["wikilinks_in"]:
                        note["wikilinks_in"].append(other["relative_path"])
    
    return notes

# ─── MODULE 2: FRONTMATTER AUDITOR ───────────────────────────────────────────
def audit_frontmatter(notes: list) -> list:
    audit = []
    for note in notes:
        audit.append({
            "relative_path": note["relative_path"],
            "title": note["title"],
            "frontmatter_present": note["frontmatter_present"],
            "frontmatter_fields": list(note["frontmatter_fields"].keys()),
            "has_title": "title" in note["frontmatter_fields"],
            "has_tags": "tags" in note["frontmatter_fields"],
            "has_created": "created" in note["frontmatter_fields"],
            "has_modified": "modified" in note["frontmatter_fields"],
            "tags_count": len(note["tags"]),
            "import_authorized": False,
            "source_mutated": False,
        })
    return audit

# ─── MODULE 3: LINK MAPPER + BROKEN LINK DETECTOR ────────────────────────────
def map_links_and_detect_broken(notes: list, vault_path: Path) -> tuple:
    all_note_paths = set()
    for note in notes:
        all_note_paths.add(note["title"])
        all_note_paths.add(note["filename"].replace(".md", ""))
        all_note_paths.add(note["relative_path"].replace(".md", ""))
    
    link_graph = []
    broken_links = []
    
    for note in notes:
        for wl in note["wikilinks_out"]:
            wl_base = wl.split("/")[-1]
            is_attachment = any(wl.endswith(ext) for exts in ATTACHMENT_EXTENSIONS.values() for ext in exts)
            resolved = wl_base in all_note_paths or wl in all_note_paths
            
            entry = {
                "source_note": note["relative_path"],
                "link_text": wl,
                "link_type": "attachment_embed" if is_attachment else "wikilink",
                "resolved": resolved,
                "candidate_targets": [p for p in all_note_paths if wl_base.lower() in p.lower()],
                "requires_review": not resolved,
                "import_authorized": False,
                "source_mutated": False,
            }
            link_graph.append(entry)
            if not resolved:
                broken_links.append(entry)
    
    return link_graph, broken_links

# ─── MODULE 4: ATTACHMENT INVENTORY ──────────────────────────────────────────
def inventory_attachments(notes: list, vault_path: Path) -> list:
    # Collect all referenced attachments
    referenced = {}
    for note in notes:
        for att in note["attachments"]:
            att_base = Path(att).name
            if att_base not in referenced:
                referenced[att_base] = []
            referenced[att_base].append(note["relative_path"])
    
    # Scan all non-MD files
    inventory = []
    for asset_file in sorted(vault_path.rglob("*")):
        if asset_file.is_file() and asset_file.suffix.lower() != ".md":
            stat = asset_file.stat()
            rel = asset_file.relative_to(vault_path)
            fname = asset_file.name
            refs = referenced.get(fname, [])
            
            # Determine type
            ext = asset_file.suffix.lower()
            asset_type = "unknown"
            for atype, exts in ATTACHMENT_EXTENSIONS.items():
                if ext in exts:
                    asset_type = atype
                    break
            
            inventory.append({
                "asset_path": str(asset_file),
                "relative_path": str(rel),
                "filename": fname,
                "extension": ext,
                "asset_type": asset_type,
                "size_bytes": stat.st_size,
                "referenced_by": refs,
                "reference_count": len(refs),
                "is_orphan": len(refs) == 0,
                "source_mutated": False,
                "import_authorized": False,
            })
    
    return inventory

# ─── MODULE 5: DUPLICATE DETECTOR ────────────────────────────────────────────
def detect_duplicates(notes: list) -> list:
    from collections import defaultdict
    
    groups = defaultdict(list)
    
    # Group by content hash
    for note in notes:
        groups[("hash", note["content_hash"])].append(note)
    
    # Group by normalized title
    for note in notes:
        norm_title = re.sub(r"[^a-z0-9]", "", note["title"].lower())
        groups[("norm_title", norm_title)].append(note)
    
    # Group by filename (without extension)
    for note in notes:
        fname_base = note["filename"].replace(".md", "").lower()
        groups[("filename", fname_base)].append(note)
    
    candidates = []
    group_id = 1
    seen_pairs = set()
    
    for (dup_type, key), group_notes in groups.items():
        if len(group_notes) > 1:
            pair_key = frozenset(n["relative_path"] for n in group_notes)
            if pair_key in seen_pairs:
                continue
            seen_pairs.add(pair_key)
            
            confidence = "HIGH" if dup_type == "hash" else "MEDIUM" if dup_type == "norm_title" else "LOW"
            
            candidates.append({
                "candidate_group_id": f"DUP-{group_id:03d}",
                "duplicate_type": dup_type,
                "key": key,
                "confidence": confidence,
                "notes": [n["relative_path"] for n in group_notes],
                "titles": [n["title"] for n in group_notes],
                "recommended_action": "MANUAL_REVIEW",
                "merge_authorized": False,
            })
            group_id += 1
            
            # Mark notes as duplicate candidates
            for note in notes:
                if note["relative_path"] in [n["relative_path"] for n in group_notes]:
                    note["duplicate_candidate"] = True
    
    return candidates

# ─── MODULE 6: DRY-RUN IMPORT MAPPER ─────────────────────────────────────────
def dry_run_import_map(notes: list, duplicates: list) -> list:
    dup_paths = set()
    for d in duplicates:
        for p in d["notes"]:
            dup_paths.add(p)
    
    preview = []
    for note in notes:
        requires_review = (
            note["classification_confidence"] == "LOW" or
            note["duplicate_candidate"] or
            not note["frontmatter_present"]
        )
        
        preview.append({
            "source_path": note["source_path"],
            "relative_path": note["relative_path"],
            "title": note["title"],
            "candidate_kap_branch": note["candidate_kap_branch"],
            "classification_confidence": note["classification_confidence"],
            "classification_reason": note["classification_reason"],
            "frontmatter_present": note["frontmatter_present"],
            "duplicate_candidate": note["duplicate_candidate"],
            "requires_review": requires_review,
            "import_authorized": False,
            "source_mutated": False,
        })
    
    return preview

# ─── MAIN RUNNER ──────────────────────────────────────────────────────────────
def main():
    vault_path = ALLOWED_VAULT
    
    print("\n" + "="*60)
    print("KAP OBSIDIAN HARNESS RUNNER — FAKE VAULT ONLY")
    print("="*60)
    print(f"Date: {datetime.now(tz=timezone.utc).isoformat()}")
    print(f"Vault: {vault_path}")
    
    # Safety check
    check_vault_safety(vault_path)
    
    if not vault_path.exists():
        print(f"[FAIL] Fake vault not found at {vault_path}")
        sys.exit(1)
    
    INDEXES_DIR.mkdir(parents=True, exist_ok=True)
    DRY_RUNS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Run all modules
    print("\n[1/6] Scanning vault...")
    notes = scan_vault(vault_path)
    print(f"  → {len(notes)} notes found")
    
    print("[2/6] Auditing frontmatter...")
    fm_audit = audit_frontmatter(notes)
    fm_with = sum(1 for f in fm_audit if f["frontmatter_present"])
    print(f"  → {fm_with}/{len(fm_audit)} notes have frontmatter")
    
    print("[3/6] Mapping links + detecting broken links...")
    link_graph, broken_links = map_links_and_detect_broken(notes, vault_path)
    print(f"  → {len(link_graph)} links total, {len(broken_links)} broken")
    
    print("[4/6] Inventorying attachments...")
    attachments = inventory_attachments(notes, vault_path)
    orphans = sum(1 for a in attachments if a["is_orphan"])
    print(f"  → {len(attachments)} assets, {orphans} orphans")
    
    print("[5/6] Detecting duplicates...")
    duplicates = detect_duplicates(notes)
    print(f"  → {len(duplicates)} duplicate groups found")
    
    print("[6/6] Building dry-run import map...")
    import_map = dry_run_import_map(notes, duplicates)
    needs_review = sum(1 for i in import_map if i["requires_review"])
    print(f"  → {len(import_map)} notes mapped, {needs_review} require review")
    
    # Write outputs
    meta = {
        "source": "fake_vault",
        "vault_path": str(vault_path),
        "real_vault_scanned": False,
        "import_authorized": False,
        "source_mutated": False,
        "generated_at": datetime.now(tz=timezone.utc).isoformat(),
    }
    
    outputs = {
        INDEXES_DIR / "obsidian_note_index.json": notes,
        INDEXES_DIR / "obsidian_frontmatter_audit.json": fm_audit,
        INDEXES_DIR / "obsidian_link_graph.json": link_graph,
        INDEXES_DIR / "obsidian_broken_links.json": broken_links,
        INDEXES_DIR / "obsidian_attachment_index.json": attachments,
        INDEXES_DIR / "obsidian_duplicate_candidates.json": duplicates,
        DRY_RUNS_DIR / "obsidian_import_map_preview.json": import_map,
    }
    
    for path, data in outputs.items():
        payload = {"_meta": meta, "data": data}
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  [SAVED] {path.relative_to(OBSIDIAN_BASE)}")
    
    # Summary
    print("\n" + "="*60)
    print("HARNESS TEST COMPLETE")
    print(f"  Notes scanned:      {len(notes)}")
    print(f"  With frontmatter:   {fm_with}")
    print(f"  Links total:        {len(link_graph)}")
    print(f"  Broken links:       {len(broken_links)}")
    print(f"  Assets:             {len(attachments)}")
    print(f"  Orphan assets:      {orphans}")
    print(f"  Duplicate groups:   {len(duplicates)}")
    print(f"  Needs review:       {needs_review}")
    print(f"  Source mutated:     False")
    print(f"  Import authorized:  False")
    print(f"  Real vault scanned: False")
    print("="*60)
    
    return {
        "notes": len(notes),
        "fm_with": fm_with,
        "links": len(link_graph),
        "broken": len(broken_links),
        "assets": len(attachments),
        "orphans": orphans,
        "duplicates": len(duplicates),
        "needs_review": needs_review,
    }

if __name__ == "__main__":
    main()
