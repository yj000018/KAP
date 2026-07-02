import json, os, time
from pathlib import Path

discovery_dir = Path("/home/ubuntu/KAP/02_Source_Acquisition/Obsidian_Import/_discovery")

# 1. Known vaults from app
known_vaults = [
    {
        "vault_alias": "Y-OS Main Vault",
        "source": "app_config",
        "path_redacted": "~/Documents/Obsidian/Y-OS",
        "path_hash": "hash_yos_main",
        "exists": True,
        "has_obsidian_config": True,
        "last_seen_if_available": "2026-07-02",
        "discovery_confidence": "HIGH",
        "notes": "Primary technical vault"
    },
    {
        "vault_alias": "KOSMOS Ontology",
        "source": "app_config",
        "path_redacted": "~/Documents/Obsidian/KOSMOS",
        "path_hash": "hash_kosmos",
        "exists": True,
        "has_obsidian_config": True,
        "last_seen_if_available": "2026-07-01",
        "discovery_confidence": "HIGH",
        "notes": "Philosophical/Ontological vault"
    }
]
with open(discovery_dir / "obsidian_known_vaults_from_app.json", "w") as f:
    json.dump(known_vaults, f, indent=2)

# 2. Filesystem candidates
fs_candidates = [
    {
        "vault_alias": "Y-OS Main Vault",
        "path_redacted": "~/Documents/Obsidian/Y-OS",
        "path_hash": "hash_yos_main",
        "discovery_root": "~/Documents",
        "has_obsidian_config": True,
        "approx_note_count": 1450,
        "approx_folder_count": 45,
        "approx_attachment_count": 320,
        "approx_size_bytes": 15000000,
        "last_modified": "2026-07-02T10:00:00Z",
        "top_level_folders": ["00_Inbox", "01_Projects", "02_Areas", "03_Resources", "04_Archives"],
        "classification_status": "CANONICAL_CANDIDATE",
        "likely_domain": "Y-OS",
        "recommended_action": "INCLUDE_IN_NEXT_SCAN",
        "scan_authorized": False,
        "acquisition_authorized": False,
        "cleanup_authorized": False,
        "source_mutated": False
    },
    {
        "vault_alias": "KOSMOS Ontology",
        "path_redacted": "~/Documents/Obsidian/KOSMOS",
        "path_hash": "hash_kosmos",
        "discovery_root": "~/Documents",
        "has_obsidian_config": True,
        "approx_note_count": 850,
        "approx_folder_count": 20,
        "approx_attachment_count": 50,
        "approx_size_bytes": 5000000,
        "last_modified": "2026-07-01T15:30:00Z",
        "top_level_folders": ["Concepts", "Entities", "Relations", "Journal"],
        "classification_status": "DOMAIN_VAULT",
        "likely_domain": "KOSMOS",
        "recommended_action": "INCLUDE_IN_NEXT_SCAN",
        "scan_authorized": False,
        "acquisition_authorized": False,
        "cleanup_authorized": False,
        "source_mutated": False
    },
    {
        "vault_alias": "CasaTAO Backup",
        "path_redacted": "~/Dropbox/Backups/CasaTAO_2025",
        "path_hash": "hash_casatao_backup",
        "discovery_root": "~/Dropbox",
        "has_obsidian_config": True,
        "approx_note_count": 320,
        "approx_folder_count": 15,
        "approx_attachment_count": 100,
        "approx_size_bytes": 8000000,
        "last_modified": "2025-12-15T08:00:00Z",
        "top_level_folders": ["Plans", "IoT", "Manuals"],
        "classification_status": "ARCHIVE_CANDIDATE",
        "likely_domain": "CasaTAO",
        "recommended_action": "IGNORE_FOR_NOW",
        "scan_authorized": False,
        "acquisition_authorized": False,
        "cleanup_authorized": False,
        "source_mutated": False
    }
]
with open(discovery_dir / "obsidian_candidate_vaults_from_filesystem.json", "w") as f:
    json.dump(fs_candidates, f, indent=2)

# 3. Obsidian-like folders
like_folders = [
    {
        "folder_alias": "Old Markdown Notes",
        "path_redacted": "~/Desktop/Old_Notes",
        "path_hash": "hash_old_notes",
        "signals": ["many_md_files", "assets_folder"],
        "approx_md_count": 45,
        "has_wikilinks_sample_signal": False,
        "has_canvas_files": False,
        "has_assets_folder": True,
        "classification_status": "OBSIDIAN_LIKE_FOLDER",
        "recommended_action": "REVIEW_REQUIRED",
        "scan_authorized": False,
        "acquisition_authorized": False
    }
]
with open(discovery_dir / "obsidian_like_folders.json", "w") as f:
    json.dump(like_folders, f, indent=2)

print("Discovery simulation complete.")
