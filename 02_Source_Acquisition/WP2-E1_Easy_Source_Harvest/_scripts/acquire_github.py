#!/usr/bin/env python3
"""
KAP WP2-E1 — GitHub Source Acquisition Script
Downloads targeted folders from yj000018 repos via GitHub API.
Records repo, branch, commit hash, original path, acquired path, checksum.
"""

import os
import sys
import json
import hashlib
import base64
import time
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import HTTPError

GITHUB_USER = "yj000018"
BASE_URL = "https://api.github.com"
OUTPUT_BASE = "/home/ubuntu/KAP/02_Source_Acquisition/WP2-E1_Easy_Source_Harvest"

# Rate limit handling
request_count = 0

def api_get(url, retries=3):
    """Make a GitHub API GET request with rate limit handling."""
    global request_count
    for attempt in range(retries):
        try:
            req = Request(url, headers={"User-Agent": "KAP-Harvester/1.0"})
            with urlopen(req, timeout=30) as resp:
                request_count += 1
                if request_count % 50 == 0:
                    time.sleep(2)  # Respect rate limits
                return json.loads(resp.read().decode())
        except HTTPError as e:
            if e.code == 403:
                print(f"  Rate limited. Waiting 60s... (attempt {attempt+1})")
                time.sleep(60)
            elif e.code == 404:
                return None
            else:
                print(f"  HTTP {e.code} on {url}")
                if attempt < retries - 1:
                    time.sleep(5)
                else:
                    return None
        except Exception as e:
            print(f"  Error: {e}")
            if attempt < retries - 1:
                time.sleep(5)
            else:
                return None
    return None


def get_commit_sha(repo, branch):
    """Get latest commit SHA for a branch."""
    url = f"{BASE_URL}/repos/{GITHUB_USER}/{repo}/branches/{branch}"
    data = api_get(url)
    if data:
        return data.get("commit", {}).get("sha", "unknown")
    return "unknown"


def download_file(repo, branch, filepath, output_dir):
    """Download a single file from GitHub."""
    url = f"{BASE_URL}/repos/{GITHUB_USER}/{repo}/contents/{filepath}?ref={branch}"
    data = api_get(url)
    if not data:
        return None
    
    if data.get("encoding") == "base64" and data.get("content"):
        content = base64.b64decode(data["content"])
        out_path = Path(output_dir) / filepath
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "wb") as f:
            f.write(content)
        return str(out_path)
    elif data.get("download_url"):
        # Large file - use download URL
        try:
            req = Request(data["download_url"], headers={"User-Agent": "KAP-Harvester/1.0"})
            with urlopen(req, timeout=60) as resp:
                content = resp.read()
            out_path = Path(output_dir) / filepath
            out_path.parent.mkdir(parents=True, exist_ok=True)
            with open(out_path, "wb") as f:
                f.write(content)
            return str(out_path)
        except Exception as e:
            print(f"  Download failed for {filepath}: {e}")
            return None
    return None


def download_folder(repo, branch, folder_path, output_dir, max_files=500):
    """Download all files in a folder recursively."""
    url = f"{BASE_URL}/repos/{GITHUB_USER}/{repo}/git/trees/{branch}?recursive=1"
    data = api_get(url)
    if not data or "tree" not in data:
        print(f"  ERROR: Could not get tree for {repo}/{branch}")
        return []
    
    # Filter files in target folder
    target_files = [
        item["path"] for item in data["tree"]
        if item["type"] == "blob" and item["path"].startswith(folder_path)
    ]
    
    if len(target_files) > max_files:
        print(f"  WARNING: {len(target_files)} files in {folder_path}, limiting to {max_files}")
        target_files = target_files[:max_files]
    
    downloaded = []
    for i, filepath in enumerate(target_files):
        if i % 10 == 0:
            print(f"  Downloading {i+1}/{len(target_files)}: {filepath[:60]}...")
        result = download_file(repo, branch, filepath, output_dir)
        if result:
            downloaded.append({
                "original_path": filepath,
                "acquired_path": result,
                "checksum": compute_checksum(result)
            })
        time.sleep(0.5)  # Be gentle with API
    
    return downloaded


def compute_checksum(filepath):
    """Compute SHA-256 checksum."""
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def acquire_target(repo, branch, folder_path, capsule_name, max_files=500):
    """Acquire a target folder and generate metadata."""
    print(f"\n{'='*60}")
    print(f"Acquiring: {repo}/{branch} → {folder_path}")
    print(f"Capsule: {capsule_name}")
    print(f"{'='*60}")
    
    output_dir = f"{OUTPUT_BASE}/{capsule_name}"
    os.makedirs(output_dir, exist_ok=True)
    
    # Get commit SHA
    commit_sha = get_commit_sha(repo, branch)
    print(f"  Commit: {commit_sha[:12]}")
    
    # Download files
    downloaded = download_folder(repo, branch, folder_path, output_dir, max_files)
    
    # Save acquisition metadata
    metadata = {
        "source_id": f"KAP-ACQ-E1-{capsule_name}",
        "repo": f"{GITHUB_USER}/{repo}",
        "branch": branch,
        "commit_sha": commit_sha,
        "folder_path": folder_path,
        "capsule_name": capsule_name,
        "acquisition_date": "2026-07-01",
        "files_acquired": len(downloaded),
        "files": downloaded
    }
    
    meta_path = f"{output_dir}/_ACQUISITION_META.json"
    with open(meta_path, "w") as f:
        json.dump(metadata, f, indent=2)
    
    print(f"  Acquired: {len(downloaded)} files")
    print(f"  Metadata: {meta_path}")
    
    return metadata


if __name__ == "__main__":
    targets = [
        # High-value: YOS master branch
        ("YOS", "master", "concepts/", "github_yos_master/concepts"),
        ("YOS", "master", "context_packs/", "github_yos_master/context_packs"),
        ("YOS", "master", "yos-governance/Decisions/", "github_yos_master/ADRs"),
        # High-value: YOS main branch - Y-WORLD vault
        ("YOS", "main", "yos-vault/knowledge/Y-WORLD/60_Y-OS/", "github_yos_main/Y-WORLD_60_Y-OS"),
        ("YOS", "main", "yos-vault/knowledge/Y-WORLD/00_System/", "github_yos_main/Y-WORLD_00_System"),
        ("YOS", "main", "yos-vault/knowledge/Y-WORLD/02_Maps/", "github_yos_main/Y-WORLD_02_Maps"),
        ("YOS", "main", "yos-vault/knowledge/Y-WORLD/50_Projects/", "github_yos_main/Y-WORLD_50_Projects"),
    ]
    
    all_results = []
    for repo, branch, folder, capsule in targets:
        result = acquire_target(repo, branch, folder, capsule)
        all_results.append(result)
    
    # Save global manifest
    manifest_path = f"{OUTPUT_BASE}/_registry/acquisition_manifest_phase1.json"
    os.makedirs(os.path.dirname(manifest_path), exist_ok=True)
    with open(manifest_path, "w") as f:
        json.dump(all_results, f, indent=2)
    
    print(f"\n{'='*60}")
    print(f"PHASE 1 COMPLETE")
    total_files = sum(r["files_acquired"] for r in all_results)
    print(f"Total files acquired: {total_files}")
    print(f"Manifest: {manifest_path}")
    print(f"{'='*60}")
