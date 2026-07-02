#!/usr/bin/env python3
"""
KAP Connector Registry Validator
Gate: CONNECTOR-IMPLEMENTATION-GATE
Purpose: Validate CONNECTOR-REGISTRY.json — check IDs, required fields, acquisition state, script/schema presence.
"""
import json, os, sys

KAP_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY_PATH = os.path.join(KAP_ROOT, "05_Registries", "CONNECTOR-REGISTRY.json")

REQUIRED_FIELDS = ["connector_id","source_system","status","owner_agent","target_branches","acquisition_auth","last_validation","risks","notes"]
VALID_STATUSES = ["DESIGNED","IMPLEMENTED_DRY_RUN_READY","PARTIAL_IMPLEMENTATION_ACCESS_LIMITED","BLOCKED_NEEDS_CREDENTIALS","BLOCKED_NEEDS_SCOPE_DECISION"]

def validate():
    if not os.path.exists(REGISTRY_PATH):
        print(f"[FAIL] Registry not found: {REGISTRY_PATH}"); sys.exit(1)
    with open(REGISTRY_PATH) as f:
        reg = json.load(f)
    connectors = reg.get("connectors", [])
    print(f"[INFO] {len(connectors)} connectors found")
    errors = []
    for c in connectors:
        cid = c.get("connector_id","?")
        for field in REQUIRED_FIELDS:
            if field not in c:
                errors.append(f"[{cid}] Missing field: {field}")
        if c.get("acquisition_auth","") != "NO":
            errors.append(f"[{cid}] CRITICAL: acquisition_auth != NO")
        # Check script folder exists
        target = c.get("target_branches","")
        script_folder = os.path.join(KAP_ROOT, target.strip("/"), "_scripts")
        if not os.path.isdir(script_folder):
            errors.append(f"[{cid}] Missing script folder: {script_folder}")
        schema_folder = os.path.join(KAP_ROOT, target.strip("/"), "_schemas")
        if not os.path.isdir(schema_folder):
            errors.append(f"[{cid}] Missing schema folder: {schema_folder}")
    if errors:
        for e in errors: print(e)
        print(f"\n[RESULT] {len(errors)} issues found")
    else:
        print("[PASS] All connectors valid")

if __name__ == "__main__":
    validate()
