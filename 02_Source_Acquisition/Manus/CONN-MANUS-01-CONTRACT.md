# Connector Contract — CONN-MANUS-01

**Source:** Manus  **Gate:** CONNECTOR-IMPLEMENTATION-GATE

| Field | Value |
|---|---|
| 1. Source Identity | Manus AI Platform — `https://manus.im` |
| 2. Scope | Metadata census, durable output detection, no full task body ingestion |
| 3. Authentication | `x-manus-api-key` header, env var `MANUS_API_KEY` |
| 4. Data Types | Task metadata (id, title, timestamps, status, tags) |
| 5. Metadata Fields | task_id, title, created_at, updated_at, status, project, tags, url, has_attachments |
| 6. Extraction Method | REST API `GET /v2/task.list` with cursor pagination |
| 7. Transformation | Filter noise (subtasks), score KAP relevance, flag durable candidates |
| 8. Storage Targets | `_dry_runs/` and `_census/` only during this gate |
| 9. Deduplication | By `task_id` |
| 10. Validation | JSON schema `manus_session_metadata.schema.json` |
| 11. Failure Modes | K5 staggered retry; log and skip on persistent failure |
| 12. Security/Privacy | API key via env var only; no key in committed files |
| 13. Git Persistence | All outputs committed to KAP GitHub |
| 14. Acquisition Boundary | **NO** — metadata only; no task body ingestion |
| 15. Review Gate | PILOT-ACQUISITION-GATE (future) |
| 16. Next Allowed Action | Dry-run census only; full acquisition requires PILOT-ACQUISITION-GATE |
