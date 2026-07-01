#!/usr/bin/env python3
"""
KAP WP2-E1 — GitHub Secondary Targets Acquisition
Acquires yos-scripts, manus-enhancer, y-menu, elysium-book, one-galaxy
"""

import os
import sys
import json
import hashlib
import subprocess
from pathlib import Path

GITHUB_USER = "yj000018"
OUTPUT_BASE = "/home/ubuntu/KAP/02_Source_Acquisition/WP2-E1_Easy_Source_Harvest/github_secondary"


def compute_checksum(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def clone_full_repo(repo, branch="main", capsule_name=None):
    """Clone entire repo (small repos only)."""
    if capsule_name is None:
        capsule_name = repo
    
    print(f"\n{'='*60}")
    print(f"ACQUIRING: {repo}/{branch} (full clone)")
    print(f"{'='*60}")
    
    clone_dir = f"/tmp/kap_clone_{repo}"
    output_dir = f"{OUTPUT_BASE}/{capsule_name}"
    
    subprocess.run(["rm", "-rf", clone_dir], capture_output=True)
    os.makedirs(output_dir, exist_ok=True)
    
    url = f"https://github.com/{GITHUB_USER}/{repo}.git"
    result = subprocess.run(
        ["git", "clone", "--single-branch", "--branch", branch, "--depth", "1", url, clone_dir],
        capture_output=True, text=True, timeout=120
    )
    
    if result.returncode != 0:
        # Try without specifying branch (use default)
        result = subprocess.run(
            ["git", "clone", "--depth", "1", url, clone_dir],
            capture_output=True, text=True, timeout=120
        )
        if result.returncode != 0:
            print(f"  FAILED: {result.stderr[:200]}")
            return {"status": "FAILED", "repo": repo}
    
    # Get commit SHA
    result = subprocess.run(
        ["git", "-C", clone_dir, "rev-parse", "HEAD"],
        capture_output=True, text=True
    )
    commit_sha = result.stdout.strip() if result.returncode == 0 else "unknown"
    
    # Get actual branch name
    result = subprocess.run(
        ["git", "-C", clone_dir, "branch", "--show-current"],
        capture_output=True, text=True
    )
    actual_branch = result.stdout.strip() if result.returncode == 0 else branch
    
    # Remove .git folder and copy content
    subprocess.run(["rm", "-rf", f"{clone_dir}/.git"], capture_output=True)
    subprocess.run(["cp", "-r", f"{clone_dir}/.", output_dir], capture_output=True)
    
    # Index files
    acquired_files = []
    for f in Path(output_dir).rglob("*"):
        if f.is_file():
            acquired_files.append({
                "original_path": str(f.relative_to(Path(output_dir))),
                "acquired_path": str(f),
                "size_bytes": f.stat().st_size,
                "checksum": compute_checksum(str(f))
            })
    
    metadata = {
        "source_id": f"KAP-ACQ-E1-{capsule_name}",
        "repo": f"{GITHUB_USER}/{repo}",
        "branch": actual_branch,
        "commit_sha": commit_sha,
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
    
    # Cleanup
    subprocess.run(["rm", "-rf", clone_dir], capture_output=True)
    
    print(f"  ✓ Acquired: {len(acquired_files)} files ({metadata['total_size_bytes']:,} bytes)")
    return metadata


def main():
    os.makedirs(OUTPUT_BASE, exist_ok=True)
    all_results = []
    
    # Secondary repos (small, full clone)
    repos = [
        ("yos-scripts", "main"),
        ("manus-enhancer", "main"),
        ("y-menu", "main"),
        ("elysium-book", "main"),
        ("one-galaxy", "main"),
    ]
    
    for repo, branch in repos:
        result = clone_full_repo(repo, branch)
        all_results.append(result)
    
    # Save manifest
    manifest_path = f"{OUTPUT_BASE}/_ACQUISITION_META.json"
    with open(manifest_path, "w") as f:
        json.dump(all_results, f, indent=2)
    
    print(f"\n{'='*60}")
    print(f"SECONDARY TARGETS COMPLETE")
    total = sum(r.get("files_acquired", 0) for r in all_results if r.get("status") == "SUCCESS")
    failed = sum(1 for r in all_results if r.get("status") == "FAILED")
    print(f"Total files acquired: {total}")
    print(f"Failed repos: {failed}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
