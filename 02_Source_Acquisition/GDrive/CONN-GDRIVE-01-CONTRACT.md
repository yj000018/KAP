# Connector Contract — CONN-GDRIVE-01

**Source:** Google Drive  **Gate:** CONNECTOR-IMPLEMENTATION-GATE

| Field | Value |
|---|---|
| 1. Source Identity | Google Drive — `https://drive.google.com` |
| 2. Scope | File metadata inventory; no file download |
| 3. Authentication | OAuth2 token via `GDRIVE_OAUTH_TOKEN` env var |
| 4. Data Types | File metadata (id, name, mimeType, timestamps, size, owners) |
| 5. Metadata Fields | id, name, mimeType, createdTime, modifiedTime, size, owners |
| 6. Extraction Method | Google Drive API v3 `files.list` |
| 7. Transformation | MIME-to-export-strategy mapping |
| 8. Storage Targets | `_dry_runs/` only during this gate |
| 9. Deduplication | By file `id` |
| 10. Validation | JSON schema `gdrive_file_metadata.schema.json` |
| 11. Failure Modes | Log API errors; skip on 403/404 |
| 12. Security/Privacy | OAuth token via env var only; never committed to Git |
| 13. Git Persistence | Index JSON committed; credentials excluded |
| 14. Acquisition Boundary | **NO** — metadata only; no file download |
| 15. Review Gate | PILOT-ACQUISITION-GATE (future) |
| 16. Next Allowed Action | Dry-run inventory; download requires PILOT-ACQUISITION-GATE |
