# KAP Pipeline Feasibility Registry

**Gate:** PIPELINE-FEASIBILITY-GATE  
**Version:** 1.0  
**Date:** 2026-07-02

---

## PIPE-MANUS-01

| Field | Value |
|---|---|
| Pipeline ID | PIPE-MANUS-01 |
| Related Connector | CONN-MANUS-01 |
| Source System | Manus |
| Access Method | REST API — `GET /v2/task.list` with `x-manus-api-key` header |
| Validation Status | VALIDATED |
| Credential Requirement | `MANUS_API_KEY` env var — available |
| Tested | YES |
| Evidence Level | METADATA_PROBED |
| Known Limits | Max 200 tasks per API call; 178/200 are Wide Research Subtasks (noise); no task body via metadata endpoint |
| Risks | Subtask flood; pagination cap; no semantic content without body fetch |
| Recommended Pilot | 20–50 metadata-ranked durable output candidates only. No full task import. |
| Acquisition Allowed | NO |

---

## PIPE-OAI-01

| Field | Value |
|---|---|
| Pipeline ID | PIPE-OAI-01 |
| Related Connector | CONN-OAI-01 |
| Source System | ChatGPT / OpenAI Conversations |
| Access Method | File export — `conversations.json` from chat.openai.com/settings |
| Validation Status | ACCESS_LIMITED |
| Credential Requirement | No API key; manual export required |
| Tested | NO — export file not available in sandbox |
| Evidence Level | DOCUMENTED_ONLY |
| Known Limits | Manual export step; no programmatic API for conversation history; large JSON files |
| Risks | Large JSON parsing; no project-level classification in export; attachment asset pointers may be broken |
| Recommended Pilot | 10–20 selected KAP-relevant exported conversations. Full provenance, no broad import. |
| Acquisition Allowed | NO |

---

## PIPE-OBS-01

| Field | Value |
|---|---|
| Pipeline ID | PIPE-OBS-01 |
| Related Connector | CONN-OBS-01 |
| Source System | Obsidian / Local Markdown |
| Access Method | Local filesystem — `--vault /path/to/vault` |
| Validation Status | ACCESS_LIMITED |
| Credential Requirement | Vault path — not accessible from sandbox |
| Tested | NO — vault not mounted in sandbox |
| Evidence Level | DOCUMENTED_ONLY |
| Known Limits | Vault not accessible from sandbox; wikilinks break on move; attachments scattered |
| Risks | Link breakage; attachment loss; duplicate notes; no frontmatter standard |
| Recommended Pilot | One small vault folder or 50 Markdown files max. No merge until normalization rules pass. |
| Acquisition Allowed | NO |

---

## PIPE-GDRIVE-01

| Field | Value |
|---|---|
| Pipeline ID | PIPE-GDRIVE-01 |
| Related Connector | CONN-GDRIVE-01 |
| Source System | Google Drive |
| Access Method | OAuth2 REST API — Google Drive API v3 |
| Validation Status | ACCESS_LIMITED |
| Credential Requirement | `GDRIVE_OAUTH_TOKEN` — not available in sandbox |
| Tested | NO — OAuth2 token not available |
| Evidence Level | DOCUMENTED_ONLY |
| Known Limits | OAuth2 setup requires GCP project; token expiry; shared-drive permission complexity |
| Risks | Permission changes; OAuth expiry; large file downloads; MIME type diversity |
| Recommended Pilot | One folder inventory + 3 representative files. No broad download. |
| Acquisition Allowed | NO |

---

## PIPE-NOTION-01

| Field | Value |
|---|---|
| Pipeline ID | PIPE-NOTION-01 |
| Related Connector | CONN-NOTION-01 |
| Source System | Notion |
| Access Method | Bearer token REST API — Notion API v1 |
| Validation Status | BLOCKED_BY_ACCESS |
| Credential Requirement | `NOTION_API_KEY` — 401 Unauthorized (token expired or wrong workspace) |
| Tested | YES — probe attempted, returned 401 |
| Evidence Level | BLOCKED_BY_ACCESS |
| Known Limits | Token 401; integration must be granted access per workspace; hierarchy loss risk |
| Risks | Hierarchy loss; relation breakage; block-level content loss; workspace confusion (Yannick vs y-World) |
| Recommended Pilot | One database + 5 representative pages after token refresh and workspace clarification. |
| Acquisition Allowed | NO |

---

## PIPE-MEM0-01

| Field | Value |
|---|---|
| Pipeline ID | PIPE-MEM0-01 |
| Related Connector | CONN-MEM0-01 |
| Source System | Mem0 / Memory Systems |
| Access Method | REST API — `GET /v1/memories/` with `Token` header |
| Validation Status | VALIDATED |
| Credential Requirement | `MEM0_API_KEY` — available |
| Tested | YES |
| Evidence Level | METADATA_PROBED |
| Known Limits | Memories are compressed state; no source linking; confidence scores not always present |
| Risks | State drift; no canonical truth; contradictions undetectable without source |
| Recommended Pilot | Memory audit only, confidence-labeled, no canonical truth promotion. |
| Acquisition Allowed | NO |

---

## PIPE-GIT-01

| Field | Value |
|---|---|
| Pipeline ID | PIPE-GIT-01 |
| Related Connector | N/A — native Git CLI |
| Source System | Git / GitHub |
| Access Method | git CLI + GitHub API (PAT) |
| Validation Status | VALIDATED |
| Credential Requirement | GitHub PAT — available |
| Tested | YES |
| Evidence Level | METADATA_PROBED |
| Known Limits | Auto-commit without authorization is forbidden; force push forbidden |
| Risks | Accidental destructive operations; commit message quality |
| Recommended Pilot | Status/readiness audit and commit recommendation only. No auto-commit unless authorized. |
| Acquisition Allowed | NO |

---

## PIPE-WEB-01

| Field | Value |
|---|---|
| Pipeline ID | PIPE-WEB-01 |
| Related Connector | CONN-WEB-01 |
| Source System | Web URLs / References |
| Access Method | HTTP GET (public URLs only) |
| Validation Status | VALIDATED |
| Credential Requirement | None |
| Tested | YES |
| Evidence Level | METADATA_PROBED |
| Known Limits | Public URLs only; no paywall/CAPTCHA bypass; robots.txt compliance required |
| Risks | Copyright; freshness decay; CAPTCHA; paywall; robots.txt restrictions |
| Recommended Pilot | 10 curated URLs, metadata/citation only, no scraping. |
| Acquisition Allowed | NO |
