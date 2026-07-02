# KAP Pipeline Feasibility Dry-Run Notes

**Gate:** PIPELINE-FEASIBILITY-GATE  
**Version:** 1.0  
**Date:** 2026-07-02

---

## Probe 1 — Manus Metadata Census

| Field | Value |
|---|---|
| Probe Name | manus_metadata_census dry-run |
| Pipeline | PIPE-MANUS-01 |
| Method | REST API `GET /v2/task.list` with cursor pagination |
| Input | `MANUS_API_KEY` env var |
| Credentials Used | YES — `x-manus-api-key` header |
| Output Type | JSON metadata index |
| Sample Size | 200 tasks (API max) |
| Result | SUCCESS — 200 tasks retrieved; 178 noise (Wide Research Subtasks); 22 real sessions |
| Limits | Max 200 per call; subtask flood; no body access |
| Corpus Acquired? | NO |
| Output File | `02_Source_Acquisition/Manus/_dry_runs/manus_census_dry_run_2026-07-02.json` |
| Confirmation | No WP3 acquisition. No body ingestion. Metadata only. |

---

## Probe 2 — Notion Workspace Inventory

| Field | Value |
|---|---|
| Probe Name | notion_workspace_inventory dry-run |
| Pipeline | PIPE-NOTION-01 |
| Method | Notion API v1 `/search` endpoint |
| Input | `NOTION_API_KEY` env var |
| Credentials Used | YES — Bearer token |
| Output Type | N/A — probe failed |
| Sample Size | 0 |
| Result | FAIL — 401 Unauthorized. Token expired or wrong workspace. |
| Limits | Token invalid; workspace confusion (Yannick / y-World / namaste-welfare) |
| Corpus Acquired? | NO |
| Output File | None — probe failed |
| Confirmation | No WP3 acquisition. No body ingestion. Access gap documented in GAP-001. |

---

## Probe 3 — Mem0 Memory Schema Probe

| Field | Value |
|---|---|
| Probe Name | mem0_memory_schema_probe dry-run |
| Pipeline | PIPE-MEM0-01 |
| Method | Mem0 REST API `GET /v1/memories/` |
| Input | `MEM0_API_KEY` env var |
| Credentials Used | YES — Token header |
| Output Type | JSON schema + 10 memory facts |
| Sample Size | 10 memories |
| Result | SUCCESS — Schema: `['id', 'memory', 'user_id', 'metadata', 'categories', 'created_at', 'updated_at', 'expiration_date', 'structured_attributes']` |
| Limits | Memories = compressed state; no source linking; confidence scores not always present |
| Corpus Acquired? | NO |
| Output File | `02_Source_Acquisition/Mem0_Export/_dry_runs/mem0_schema_probe_2026-07-02.json` |
| Confirmation | No WP3 acquisition. No canonicalization. Metadata only. |

---

## Probe 4 — Web Reference Metadata Probe

| Field | Value |
|---|---|
| Probe Name | web_reference_metadata_probe dry-run |
| Pipeline | PIPE-WEB-01 |
| Method | HTTP GET (public URLs) |
| Input | Sample URLs: manus.im, notion.so, obsidian.md |
| Credentials Used | NO |
| Output Type | JSON metadata (url, title, status) |
| Sample Size | 3 URLs |
| Result | SUCCESS — 3 URLs probed; titles extracted |
| Limits | Public URLs only; no paywall/CAPTCHA |
| Corpus Acquired? | NO |
| Output File | `02_Source_Acquisition/Web_References/_dry_runs/web_probe_2026-07-02.json` |
| Confirmation | No WP3 acquisition. No scraping. Metadata only. |

---

## Probe 5 — Git Status Audit

| Field | Value |
|---|---|
| Probe Name | git status / remote / log audit |
| Pipeline | PIPE-GIT-01 |
| Method | `git status`, `git remote -v`, `git log --oneline` |
| Input | Local KAP repository |
| Credentials Used | YES — GitHub PAT (push/pull) |
| Output Type | Terminal output |
| Sample Size | N/A |
| Result | SUCCESS — Remote configured (github.com/yj000018/KAP); HEAD at `dda1940`; active commits |
| Limits | Auto-commit forbidden without authorization |
| Corpus Acquired? | NO |
| Output File | N/A — git metadata only |
| Confirmation | No destructive operations. No force push. Status audit only. |

---

## Access-Limited Probes (Not Executed)

| Probe | Pipeline | Reason | Gap ID |
|---|---|---|---|
| chatgpt_export_schema_probe | PIPE-OAI-01 | No `conversations.json` available | GAP-002 |
| obsidian_vault_scanner | PIPE-OBS-01 | Vault path not accessible from sandbox | GAP-003 |
| gdrive_file_inventory | PIPE-GDRIVE-01 | No `GDRIVE_OAUTH_TOKEN` available | GAP-004 |
