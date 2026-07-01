#!/usr/bin/env python3
"""
KAP WP2-E1 — GitHub Source Acquisition v2
Uses git sparse-checkout for efficient folder acquisition.
Falls back to API with URL encoding for files with spaces.
"""

import os
import sys
import json
import hashlib
import subprocess
import time
from pathlib import Path
from urllib.parse import quote

GITHUB_USER = "yj000018"
OUTPUT_BASE = "/home/ubuntu/KAP/02_Source_Acquisition/WP2-E1_Easy_Source_Harvest"


def compute_checksum(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def git_clone_sparse(repo, branch, folders, output_dir):
    """Clone repo with sparse checkout for specific folders."""
    clone_dir = f"/tmp/kap_clone_{repo}_{branch.replace('/', '_')}"
    
    # Clean previous attempt
    subprocess.run(["rm", "-rf", clone_dir], capture_output=True)
    
    # Sparse clone
    url = f"https://github.com/{GITHUB_USER}/{repo}.git"
    
    print(f"  Cloning {repo} ({branch}) sparse...")
    result = subprocess.run(
        ["git", "clone", "--filter=blob:none", "--no-checkout", "--single-branch",
         "--branch", branch, url, clone_dir],
        capture_output=True, text=True, timeout=120
    )
    
    if result.returncode != 0:
        print(f"  Clone failed: {result.stderr[:200]}")
        return None, None
    
    # Setup sparse checkout
    subprocess.run(
        ["git", "-C", clone_dir, "sparse-checkout", "init", "--cone"],
        capture_output=True, text=True
    )
    
    # Set folders
    subprocess.run(
        ["git", "-C", clone_dir, "sparse-checkout", "set"] + folders,
        capture_output=True, text=True
    )
    
    # Checkout
    result = subprocess.run(
        ["git", "-C", clone_dir, "checkout"],
        capture_output=True, text=True, timeout=120
    )
    
    if result.returncode != 0:
        print(f"  Checkout failed: {result.stderr[:200]}")
        return None, None
    
    # Get commit SHA
    result = subprocess.run(
        ["git", "-C", clone_dir, "rev-parse", "HEAD"],
        capture_output=True, text=True
    )
    commit_sha = result.stdout.strip() if result.returncode == 0 else "unknown"
    
    # Copy folders to output
    acquired_files = []
    for folder in folders:
        src = Path(clone_dir) / folder
        if src.exists():
            dst = Path(output_dir) / folder
            dst.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run(["cp", "-r", str(src), str(dst)], capture_output=True)
            
            # Index acquired files
            for f in dst.rglob("*"):
                if f.is_file() and not f.name.startswith(".git"):
                    acquired_files.append({
                        "original_path": str(f.relative_to(Path(output_dir))),
                        "acquired_path": str(f),
                        "size_bytes": f.stat().st_size,
                        "checksum": compute_checksum(str(f))
                    })
    
    # Cleanup
    subprocess.run(["rm", "-rf", clone_dir], capture_output=True)
    
    return commit_sha, acquired_files


def acquire_batch(repo, branch, folders, capsule_name):
    """Acquire a batch of folders from a repo/branch."""
    print(f"\n{'='*60}")
    print(f"ACQUIRING: {repo}/{branch}")
    print(f"Folders: {folders}")
    print(f"Capsule: {capsule_name}")
    print(f"{'='*60}")
    
    output_dir = f"{OUTPUT_BASE}/{capsule_name}"
    os.makedirs(output_dir, exist_ok=True)
    
    commit_sha, acquired_files = git_clone_sparse(repo, branch, folders, output_dir)
    
    if acquired_files is None:
        print(f"  FAILED - could not acquire")
        return {"status": "FAILED", "capsule": capsule_name}
    
    metadata = {
        "source_id": f"KAP-ACQ-E1-{capsule_name.replace('/', '-')}",
        "repo": f"{GITHUB_USER}/{repo}",
        "branch": branch,
        "commit_sha": commit_sha,
        "folders": folders,
        "capsule_name": capsule_name,
        "acquisition_date": "2026-07-01",
        "files_acquired": len(acquired_files),
        "total_size_bytes": sum(f["size_bytes"] for f in acquired_files),
        "status": "SUCCESS",
        "files": acquired_files
    }
    
    meta_path = f"{output_dir}/_ACQUISITION_META.json"
    with open(meta_path, "w") as f:
        json.dump(metadata, f, indent=2)
    
    print(f"  ✓ Acquired: {len(acquired_files)} files ({metadata['total_size_bytes']:,} bytes)")
    return metadata


def main():
    all_results = []
    
    # Batch 1: YOS master - concepts, context_packs, ADRs
    result = acquire_batch(
        "YOS", "master",
        ["concepts", "context_packs", "yos-governance/Decisions"],
        "github_yos_master"
    )
    all_results.append(result)
    
    # Batch 2: YOS main - Y-WORLD vault key folders
    result = acquire_batch(
        "YOS", "main",
        ["yos-vault/knowledge/Y-WORLD/60_Y-OS",
         "yos-vault/knowledge/Y-WORLD/00_System",
         "yos-vault/knowledge/Y-WORLD/02_Maps",
         "yos-vault/knowledge/Y-WORLD/50_Projects",
         "yos-vault/knowledge/Y-WORLD/30_Knowledge",
         "yos-vault/knowledge/Y-WORLD/07_Agent_Operations"],
        "github_yos_main"
    )
    all_results.append(result)
    
    # Batch 3: YOS main - agents and governance
    result = acquire_batch(
        "YOS", "main",
        ["yos-agents/manus", "yos-governance"],
        "github_yos_main_agents"
    )
    all_results.append(result)
    
    # Batch 4: elysium-civilizational-ontology - pattern library
    result = acquire_batch(
        "elysium-civilizational-ontology", "main",
        ["07_YOS_PATTERN_LIBRARY", "YOS_PROGRAM_OS", "00_PROGRAM_OFFICE", "99_FINAL_REPORTS"],
        "github_elysium"
    )
    all_results.append(result)
    
    # Save global manifest
    manifest_path = f"{OUTPUT_BASE}/_registry/acquisition_manifest.json"
    os.makedirs(os.path.dirname(manifest_path), exist_ok=True)
    with open(manifest_path, "w") as f:
        json.dump(all_results, f, indent=2)
    
    print(f"\n{'='*60}")
    print(f"ALL BATCHES COMPLETE")
    total = sum(r.get("files_acquired", 0) for r in all_results if r.get("status") == "SUCCESS")
    print(f"Total files acquired: {total}")
    print(f"Manifest: {manifest_path}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
