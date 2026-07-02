# Connector Contract — CONN-NOTION-01

**Source:** Notion  **Gate:** CONNECTOR-IMPLEMENTATION-GATE

| Field | Value |
|---|---|
| 1. Source Identity | Notion — `https://notion.so` |
| 2. Scope | Database/page metadata inventory; no page body ingestion |
| 3. Authentication | Bearer token via `NOTION_API_KEY` env var |
| 4. Data Types | Page/database metadata (id, title, parent, timestamps, url) |
| 5. Metadata Fields | id, title, type, parent_type, parent_id, created_time, url |
| 6. Extraction Method | Notion API v1 `/search` endpoint |
| 7. Transformation | Hierarchy mapping (parent/child relationships) |
| 8. Storage Targets | `_dry_runs/` only during this gate |
| 9. Deduplication | By page `id` |
| 10. Validation | JSON schema `notion_page_metadata.schema.json` |
| 11. Failure Modes | Log API errors; skip on 403 |
| 12. Security/Privacy | API key via env var only; never committed |
| 13. Git Persistence | Index JSON committed; credentials excluded |
| 14. Acquisition Boundary | **NO** — metadata only; no page body ingestion |
| 15. Review Gate | PILOT-ACQUISITION-GATE (future) |
| 16. Next Allowed Action | Dry-run inventory; full import requires PILOT-ACQUISITION-GATE |
