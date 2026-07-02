#!/usr/bin/env python3
"""
GDrive File Inventory — CONN-GDRIVE-01
Lists file metadata from Google Drive. No file download.
Requires: GDRIVE_OAUTH_TOKEN env var or service account JSON.
"""
import os, json, argparse, datetime

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_dry_runs")

def inventory():
    token = os.environ.get("GDRIVE_OAUTH_TOKEN","")
    if not token:
        print("[SKIP] GDRIVE_OAUTH_TOKEN not set — access-limited dry-run")
        print("[INFO] Set up OAuth2 via Google Cloud Console, then export GDRIVE_OAUTH_TOKEN"); return
    try:
        import requests
        headers = {"Authorization": f"Bearer {token}"}
        r = requests.get("https://www.googleapis.com/drive/v3/files",
                         headers=headers, params={"pageSize": 100, "fields": "files(id,name,mimeType,createdTime,modifiedTime,size,owners)"}, timeout=15)
        if r.status_code != 200: print(f"[FAIL] API {r.status_code}: {r.text[:200]}"); return
        files = r.json().get("files", [])
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        out = os.path.join(OUTPUT_DIR, f"gdrive_inventory_{datetime.date.today()}.json")
        with open(out, "w") as f: json.dump({"total": len(files), "items": files}, f, indent=2)
        print(f"[OK] {len(files)} files inventoried | Saved: {out}")
    except ImportError: print("[FAIL] requests not installed")

if __name__ == "__main__": inventory()
