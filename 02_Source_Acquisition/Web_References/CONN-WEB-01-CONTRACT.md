# Connector Contract — CONN-WEB-01

**Source:** Web References  **Gate:** CONNECTOR-IMPLEMENTATION-GATE

| Field | Value |
|---|---|
| 1. Source Identity | Public web URLs |
| 2. Scope | URL metadata probe + citation policy validation. No full text dumps. |
| 3. Authentication | None — public URLs only |
| 4. Data Types | URL metadata (title, status, content-type) |
| 5. Metadata Fields | url, title, status, valid, issues |
| 6. Extraction Method | HTTP GET with title extraction; no scraping |
| 7. Transformation | Citation policy validation (HTTPS, domain blocklist) |
| 8. Storage Targets | `_dry_runs/` only during this gate |
| 9. Deduplication | By URL |
| 10. Validation | JSON schema `web_reference_metadata.schema.json` |
| 11. Failure Modes | Log HTTP errors; skip on timeout |
| 12. Security/Privacy | No login, no CAPTCHA bypass, no paywall bypass |
| 13. Git Persistence | Index JSON committed |
| 14. Acquisition Boundary | **NO** — metadata only; no full text ingestion |
| 15. Review Gate | PILOT-ACQUISITION-GATE (future) |
| 16. Next Allowed Action | Dry-run probe; full text requires PILOT-ACQUISITION-GATE |
