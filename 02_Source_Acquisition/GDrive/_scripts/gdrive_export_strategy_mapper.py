#!/usr/bin/env python3
"""GDrive Export Strategy Mapper — CONN-GDRIVE-01. Maps MIME types to export strategies."""
MIME_EXPORT_MAP = {
    "application/vnd.google-apps.document": {"export": "text/markdown", "ext": ".md"},
    "application/vnd.google-apps.spreadsheet": {"export": "text/csv", "ext": ".csv"},
    "application/vnd.google-apps.presentation": {"export": "application/pdf", "ext": ".pdf"},
    "application/vnd.google-apps.drawing": {"export": "image/png", "ext": ".png"},
    "application/pdf": {"export": "direct_download", "ext": ".pdf"},
    "image/jpeg": {"export": "direct_download", "ext": ".jpg"},
    "image/png": {"export": "direct_download", "ext": ".png"},
}
if __name__ == "__main__":
    import json; print(json.dumps(MIME_EXPORT_MAP, indent=2))
