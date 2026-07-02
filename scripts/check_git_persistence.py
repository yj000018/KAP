#!/usr/bin/env python3
"""
KAP Git Persistence Checker
Gate: CONNECTOR-IMPLEMENTATION-GATE
Purpose: Verify KAP is in a Git repo, list untracked/modified files, recommend commit message.
"""
import subprocess, os, sys

KAP_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run(cmd):
    r = subprocess.run(cmd, cwd=KAP_ROOT, capture_output=True, text=True)
    return r.stdout.strip(), r.returncode

def check():
    _, rc = run(["git", "rev-parse", "--is-inside-work-tree"])
    if rc != 0:
        print("[FAIL] Not inside a Git repository"); sys.exit(1)
    print("[OK] Inside Git repository")
    status, _ = run(["git", "status", "--short"])
    if status:
        lines = status.split("\n")
        print(f"[INFO] {len(lines)} untracked/modified files:")
        for l in lines[:20]: print(f"  {l}")
        if len(lines) > 20: print(f"  ... and {len(lines)-20} more")
        print(f"\n[RECOMMEND] git add -A && git commit -m 'KAP: connector-implementation-gate'")
    else:
        print("[OK] Working tree clean — all files committed")
    log, _ = run(["git", "log", "--oneline", "-5"])
    print(f"\n[LAST 5 COMMITS]\n{log}")

if __name__ == "__main__":
    check()
