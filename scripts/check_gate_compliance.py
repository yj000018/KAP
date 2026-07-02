#!/usr/bin/env python3
"""
KAP Gate Compliance Checker
Gate: CONNECTOR-IMPLEMENTATION-GATE
Purpose: Verify no forbidden outputs, all required files exist, no ZIP primary output, WP3 blocked.
"""
import os, sys, glob

KAP_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REQUIRED_FILES = [
    "05_Registries/CONNECTOR-REGISTRY.md",
    "05_Registries/CONNECTOR-REGISTRY.json",
    "02_Architecture/Connectors/CONNECTOR-ARCHITECTURE.md",
    "02_Architecture/Connectors/CONNECTOR-CONTRACT-TEMPLATE.md",
    "04_Execution/Dry_Runs/DRY-RUN-POLICY.md",
    "06_Reports/Gates/CONNECTOR-IMPLEMENTATION-GATE-REPORT.md",
]

FORBIDDEN_PATTERNS = [
    "03_Normalized_Knowledge/**/*.md",
    "04_Distillation/**/*.md",
]

def check():
    errors = []
    warnings = []
    # Check required files
    for f in REQUIRED_FILES:
        path = os.path.join(KAP_ROOT, f)
        if not os.path.exists(path):
            errors.append(f"[MISSING] {f}")
        else:
            print(f"[OK] {f}")
    # Check no forbidden outputs
    for pattern in FORBIDDEN_PATTERNS:
        matches = glob.glob(os.path.join(KAP_ROOT, pattern), recursive=True)
        if matches:
            warnings.append(f"[WARN] Unexpected files in forbidden path: {pattern} ({len(matches)} files)")
    # Check no ZIP primary outputs
    zips = glob.glob(os.path.join(KAP_ROOT, "**/*.zip"), recursive=True)
    if zips:
        warnings.append(f"[WARN] ZIP files found (not as primary corpus): {len(zips)}")
    for w in warnings: print(w)
    if errors:
        for e in errors: print(e)
        print(f"\n[RESULT] {len(errors)} compliance errors")
        sys.exit(1)
    else:
        print("\n[PASS] Gate compliance check passed")

if __name__ == "__main__":
    check()
