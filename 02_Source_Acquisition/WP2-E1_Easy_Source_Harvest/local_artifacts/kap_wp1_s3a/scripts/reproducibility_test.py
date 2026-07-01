#!/usr/bin/env python3
"""
KAP WP1-S3A — Reproducibility Test
Exports the same conversation twice and compares checksums.
Usage: python3 reproducibility_test.py <file_a> <file_b>
"""

import sys
import hashlib
import difflib
from pathlib import Path


def compute_checksum(filepath: str) -> str:
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def compare_exports(file_a: str, file_b: str) -> dict:
    """Compare two exports of the same conversation."""
    path_a = Path(file_a)
    path_b = Path(file_b)

    if not path_a.exists():
        return {"error": f"File A not found: {file_a}"}
    if not path_b.exists():
        return {"error": f"File B not found: {file_b}"}

    checksum_a = compute_checksum(file_a)
    checksum_b = compute_checksum(file_b)

    with open(file_a, "r", encoding="utf-8") as f:
        content_a = f.readlines()
    with open(file_b, "r", encoding="utf-8") as f:
        content_b = f.readlines()

    # Compute diff
    diff = list(difflib.unified_diff(content_a, content_b, 
                                      fromfile=path_a.name, 
                                      tofile=path_b.name, 
                                      lineterm=""))

    result = {
        "file_a": file_a,
        "file_b": file_b,
        "checksum_a": checksum_a,
        "checksum_b": checksum_b,
        "identical": checksum_a == checksum_b,
        "lines_a": len(content_a),
        "lines_b": len(content_b),
        "diff_lines": len(diff),
        "verdict": "REPRODUCIBLE" if checksum_a == checksum_b else "NOT_REPRODUCIBLE"
    }

    if not result["identical"]:
        # Show first 20 diff lines
        result["diff_sample"] = diff[:20]

    return result


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 reproducibility_test.py <file_a> <file_b>")
        print("  Compare two exports of the same conversation for reproducibility.")
        sys.exit(1)

    result = compare_exports(sys.argv[1], sys.argv[2])

    if "error" in result:
        print(f"ERROR: {result['error']}")
        sys.exit(1)

    print(f"\n{'='*60}")
    print(f"KAP WP1-S3A — Reproducibility Test")
    print(f"{'='*60}")
    print(f"File A: {result['file_a']} ({result['lines_a']} lines)")
    print(f"File B: {result['file_b']} ({result['lines_b']} lines)")
    print(f"Checksum A: {result['checksum_a']}")
    print(f"Checksum B: {result['checksum_b']}")
    print(f"Identical: {result['identical']}")
    print(f"Verdict: {result['verdict']}")
    print(f"{'='*60}")

    if not result["identical"]:
        print(f"\nDiff ({result['diff_lines']} lines differ):")
        for line in result.get("diff_sample", []):
            print(f"  {line}")

    sys.exit(0 if result["identical"] else 1)


if __name__ == "__main__":
    main()
