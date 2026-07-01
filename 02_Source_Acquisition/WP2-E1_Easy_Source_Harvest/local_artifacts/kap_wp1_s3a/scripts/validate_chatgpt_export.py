#!/usr/bin/env python3
"""
KAP WP1-S3A — ChatGPT Export Validation Script
Validates exported Markdown files for fidelity, structure, and completeness.
Usage: python3 validate_chatgpt_export.py <export_folder>
"""

import os
import sys
import hashlib
import re
import json
from pathlib import Path
from datetime import datetime


def compute_checksum(filepath: str) -> str:
    """Compute SHA-256 checksum for a file."""
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def analyze_markdown(filepath: str) -> dict:
    """Analyze a Markdown file for structural elements."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")
    
    analysis = {
        "file": os.path.basename(filepath),
        "path": filepath,
        "checksum_sha256": compute_checksum(filepath),
        "size_bytes": os.path.getsize(filepath),
        "total_lines": len(lines),
        "total_chars": len(content),
        "headings": len(re.findall(r"^#{1,6}\s", content, re.MULTILINE)),
        "code_blocks": len(re.findall(r"```", content)) // 2,
        "tables": len(re.findall(r"^\|.*\|$", content, re.MULTILINE)),
        "latex_inline": len(re.findall(r"\$[^$]+\$", content)),
        "latex_block": len(re.findall(r"\$\$[^$]+\$\$", content, re.DOTALL)),
        "links": len(re.findall(r"\[.*?\]\(.*?\)", content)),
        "images": len(re.findall(r"!\[.*?\]\(.*?\)", content)),
        "user_messages": len(re.findall(r"^(##?\s*User|>\s*\*\*User)", content, re.MULTILINE)),
        "assistant_messages": len(re.findall(r"^(##?\s*(Assistant|ChatGPT)|>\s*\*\*(Assistant|ChatGPT))", content, re.MULTILINE)),
        "has_metadata_header": bool(re.search(r"^(---|# Conversation)", content[:500])),
        "has_timestamps": bool(re.search(r"\d{4}[/-]\d{2}[/-]\d{2}", content[:1000])),
        "encoding_issues": bool(re.search(r"[\ufffd\x00-\x08\x0b\x0c\x0e-\x1f]", content)),
        "empty_code_blocks": len(re.findall(r"```\s*\n\s*```", content)),
        "broken_tables": 0,
    }

    # Check for broken tables (rows with inconsistent column count)
    table_rows = re.findall(r"^\|.*\|$", content, re.MULTILINE)
    if table_rows:
        col_counts = [row.count("|") for row in table_rows]
        if col_counts:
            expected = col_counts[0]
            analysis["broken_tables"] = sum(1 for c in col_counts if c != expected)

    return analysis


def run_fidelity_checks(analysis: dict) -> list:
    """Run fidelity checks on the analysis results."""
    issues = []

    if analysis["encoding_issues"]:
        issues.append("CRITICAL: Encoding issues detected (replacement chars or control chars)")
    if analysis["empty_code_blocks"] > 0:
        issues.append(f"WARNING: {analysis['empty_code_blocks']} empty code block(s) found")
    if analysis["broken_tables"] > 0:
        issues.append(f"WARNING: {analysis['broken_tables']} table row(s) with inconsistent columns")
    if analysis["total_lines"] < 5:
        issues.append("WARNING: File appears very short (< 5 lines)")
    if analysis["user_messages"] == 0 and analysis["assistant_messages"] == 0:
        issues.append("INFO: No clear user/assistant message markers detected")
    if not analysis["has_metadata_header"]:
        issues.append("INFO: No metadata header detected")

    return issues


def validate_folder(folder_path: str) -> dict:
    """Validate all Markdown files in a folder."""
    folder = Path(folder_path)
    if not folder.exists():
        return {"error": f"Folder not found: {folder_path}"}

    md_files = list(folder.glob("**/*.md"))
    if not md_files:
        return {"error": f"No .md files found in {folder_path}"}

    results = {
        "validation_timestamp": datetime.now().isoformat(),
        "folder": str(folder),
        "total_files": len(md_files),
        "files": [],
        "summary": {
            "total_size_bytes": 0,
            "total_lines": 0,
            "total_code_blocks": 0,
            "total_tables": 0,
            "files_with_issues": 0,
            "critical_issues": 0,
            "warnings": 0,
        }
    }

    for md_file in sorted(md_files):
        analysis = analyze_markdown(str(md_file))
        issues = run_fidelity_checks(analysis)
        
        file_result = {
            "analysis": analysis,
            "issues": issues,
            "status": "PASS" if not any("CRITICAL" in i for i in issues) else "FAIL"
        }
        results["files"].append(file_result)

        # Update summary
        results["summary"]["total_size_bytes"] += analysis["size_bytes"]
        results["summary"]["total_lines"] += analysis["total_lines"]
        results["summary"]["total_code_blocks"] += analysis["code_blocks"]
        results["summary"]["total_tables"] += analysis["tables"] // 3  # approximate table count
        if issues:
            results["summary"]["files_with_issues"] += 1
        results["summary"]["critical_issues"] += sum(1 for i in issues if "CRITICAL" in i)
        results["summary"]["warnings"] += sum(1 for i in issues if "WARNING" in i)

    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 validate_chatgpt_export.py <export_folder>")
        print("  Validates ChatGPT Markdown exports for KAP WP1-S3A")
        sys.exit(1)

    folder = sys.argv[1]
    results = validate_folder(folder)

    if "error" in results:
        print(f"ERROR: {results['error']}")
        sys.exit(1)

    # Output JSON report
    output_path = os.path.join(folder, "KAP_validation_report.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    # Print summary
    print(f"\n{'='*60}")
    print(f"KAP WP1-S3A — ChatGPT Export Validation Report")
    print(f"{'='*60}")
    print(f"Folder: {results['folder']}")
    print(f"Files validated: {results['total_files']}")
    print(f"Total size: {results['summary']['total_size_bytes']:,} bytes")
    print(f"Total lines: {results['summary']['total_lines']:,}")
    print(f"Code blocks: {results['summary']['total_code_blocks']}")
    print(f"Tables: {results['summary']['total_tables']}")
    print(f"{'='*60}")
    print(f"Files with issues: {results['summary']['files_with_issues']}")
    print(f"Critical issues: {results['summary']['critical_issues']}")
    print(f"Warnings: {results['summary']['warnings']}")
    print(f"{'='*60}")

    for file_result in results["files"]:
        status = file_result["status"]
        name = file_result["analysis"]["file"]
        size = file_result["analysis"]["size_bytes"]
        print(f"  [{status}] {name} ({size:,} bytes)")
        for issue in file_result["issues"]:
            print(f"        → {issue}")

    print(f"\nFull report: {output_path}")
    
    # Exit code
    if results["summary"]["critical_issues"] > 0:
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
