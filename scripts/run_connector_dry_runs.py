#!/usr/bin/env python3
"""
KAP Connector Dry-Run Orchestrator
Gate: CONNECTOR-IMPLEMENTATION-GATE
Purpose: Run available connector dry-runs in safe mode. Skip connectors without credentials.
NEVER runs full acquisition.
"""
import os, json, datetime, subprocess, sys

KAP_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY_RUN_OUTPUT = os.path.join(KAP_ROOT, "04_Execution", "Dry_Runs", "CONNECTOR-DRY-RUN-SUMMARY.md")

CONNECTORS = [
    {"id": "CONN-MANUS-01",  "script": "02_Source_Acquisition/Manus/_scripts/manus_metadata_census.py",    "needs_creds": True,  "cred_env": "MANUS_API_KEY"},
    {"id": "CONN-OAI-01",    "script": "02_Source_Acquisition/ChatGPT/_scripts/chatgpt_export_schema_probe.py", "needs_creds": False, "cred_env": None},
    {"id": "CONN-OBS-01",    "script": "02_Source_Acquisition/Obsidian_Import/_scripts/obsidian_vault_scanner.py", "needs_creds": False, "cred_env": None},
    {"id": "CONN-GDRIVE-01", "script": "02_Source_Acquisition/GDrive/_scripts/gdrive_file_inventory.py",   "needs_creds": True,  "cred_env": "GDRIVE_OAUTH_TOKEN"},
    {"id": "CONN-NOTION-01", "script": "02_Source_Acquisition/Notion/_scripts/notion_workspace_inventory.py", "needs_creds": True, "cred_env": "NOTION_API_KEY"},
    {"id": "CONN-MEM0-01",   "script": "02_Source_Acquisition/Mem0_Export/_scripts/mem0_memory_schema_probe.py", "needs_creds": True, "cred_env": "MEM0_API_KEY"},
    {"id": "CONN-WEB-01",    "script": "02_Source_Acquisition/Web_References/_scripts/web_reference_metadata_probe.py", "needs_creds": False, "cred_env": None},
]

def run_dry_runs():
    results = []
    for c in CONNECTORS:
        cid = c["id"]
        script_path = os.path.join(KAP_ROOT, c["script"])
        if not os.path.exists(script_path):
            results.append({"id": cid, "status": "SKIP_SCRIPT_MISSING", "note": f"Script not found: {c['script']}"})
            continue
        if c["needs_creds"] and not os.environ.get(c["cred_env"], ""):
            results.append({"id": cid, "status": "SKIP_NO_CREDENTIALS", "note": f"Missing env var: {c['cred_env']}"})
            continue
        r = subprocess.run(["python3", script_path, "--dry-run"], cwd=KAP_ROOT, capture_output=True, text=True, timeout=30)
        status = "PASS" if r.returncode == 0 else "FAIL"
        results.append({"id": cid, "status": status, "note": r.stdout[:200] if r.stdout else r.stderr[:200]})

    # Write summary
    lines = [f"# Connector Dry-Run Summary\n\n**Date:** {datetime.date.today()}\n\n| Connector | Status | Notes |\n|---|---|---|"]
    for r in results:
        lines.append(f"| {r['id']} | {r['status']} | {r['note'][:80]} |")
    os.makedirs(os.path.dirname(DRY_RUN_OUTPUT), exist_ok=True)
    with open(DRY_RUN_OUTPUT, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Dry-run summary written to {DRY_RUN_OUTPUT}")
    for r in results:
        print(f"  {r['id']}: {r['status']}")

if __name__ == "__main__":
    run_dry_runs()
