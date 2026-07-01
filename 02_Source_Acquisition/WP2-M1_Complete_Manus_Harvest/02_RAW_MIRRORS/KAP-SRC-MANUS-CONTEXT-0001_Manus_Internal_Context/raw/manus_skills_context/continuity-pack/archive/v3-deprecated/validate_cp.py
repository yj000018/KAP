#!/usr/bin/env python3
"""
yOS Continuity Pack Validator
Checks structural completeness and assigns a quality score (0-10).
Usage: python3 validate_cp.py <path_to_cp.md>
"""

import sys
import os
import re


def validate_cp(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    total_checks = 0
    passed_checks = 0
    issues = []

    # --- Section presence checks ---
    required_sections = [
        (r"##\s*0\.\s*Transfer Header", "0. Transfer Header"),
        (r"##\s*Source Metadata", "Source Metadata"),
        (r"##\s*1\.\s*Executive Handover", "1. Executive Handover"),
        (r"##\s*2\.\s*Strategic Context", "2. Strategic Context"),
        (r"##\s*3\.\s*Scope & Boundaries", "3. Scope & Boundaries"),
        (r"##\s*4\.\s*Current Architecture", "4. Current Architecture"),
        (r"##\s*5\.\s*Decision Register", "5. Decision Register"),
        (r"##\s*6\.\s*Terminology Register", "6. Terminology Register"),
        (r"##\s*7\.\s*Work Done", "7. Work Done / Not Done"),
        (r"##\s*8\.\s*Open Questions", "8. Open Questions"),
        (r"##\s*9\.\s*Risks", "9. Risks / Issues / Ambiguities"),
        (r"##\s*10\.\s*Backlog", "10. Backlog / Recommended Next Work"),
        (r"##\s*11\.\s*Reference Map", "11. Reference Map"),
        (r"##\s*12\.\s*Resume Instructions", "12. Resume Instructions"),
    ]

    for pattern, name in required_sections:
        total_checks += 1
        if re.search(pattern, content, re.IGNORECASE):
            passed_checks += 1
        else:
            issues.append(f"Missing section: {name}")

    # --- Transfer Header field checks ---
    header_fields = [
        "CP Type", "Source Scope", "Target Use", "Intended Receiver",
        "Current State", "Continuity Depth", "Confidence Level",
        "Handover Mode", "What the receiver must do",
        "What the receiver must not do", "Next Recommended Action"
    ]

    for field in header_fields:
        total_checks += 1
        if re.search(re.escape(field), content, re.IGNORECASE):
            passed_checks += 1
        else:
            issues.append(f"Missing Transfer Header field: {field}")

    # --- Executive Handover field checks ---
    handover_fields = [
        "Where are we", "Why does this exist",
        "What are we trying to accomplish",
        "What has already been done", "What remains to be done",
        "What should the receiver do now",
        "What should the receiver not reopen"
    ]

    for field in handover_fields:
        total_checks += 1
        if re.search(re.escape(field), content, re.IGNORECASE):
            passed_checks += 1
        else:
            issues.append(f"Missing Executive Handover field: {field}")

    # --- Source Metadata checks ---
    source_fields = [
        "Source Session Name", "Source LLM", "Source Date",
        "Source Confidence", "Source Completeness"
    ]

    for field in source_fields:
        total_checks += 1
        if re.search(re.escape(field), content, re.IGNORECASE):
            passed_checks += 1
        else:
            issues.append(f"Missing Source Metadata field: {field}")

    # --- Receiver Instruction check ---
    total_checks += 1
    if re.search(r"Receiver Instruction|handover_mode|Absorb it as transferred context|execute the Next Recommended Action", content, re.IGNORECASE):
        passed_checks += 1
    else:
        issues.append("Missing Receiver Instruction block")

    # --- Calculate score ---
    ratio = passed_checks / total_checks if total_checks > 0 else 0
    score = round(ratio * 10, 1)

    # --- Output ---
    print("=" * 60)
    print("  yOS Continuity Pack Validation Report")
    print("=" * 60)
    print(f"  File: {file_path}")
    print(f"  Checks passed: {passed_checks}/{total_checks}")
    print(f"  Quality Score: {score}/10")
    print()

    if score >= 10:
        print("  Rating: EXCELLENT — Production-grade")
    elif score >= 8:
        print("  Rating: STRONG — Clear and transferable")
    elif score >= 6:
        print("  Rating: USABLE — Functional but fragile")
    else:
        print("  Rating: INCOMPLETE — Not ready for transfer")

    if issues:
        print()
        print("  Issues found:")
        for issue in issues:
            print(f"    - {issue}")

    print("=" * 60)
    sys.exit(0 if score >= 6 else 1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 validate_cp.py <path_to_cp.md>")
        sys.exit(1)

    validate_cp(sys.argv[1])
