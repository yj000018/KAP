# KAP Acquisition Method Matrix

**Gate:** PIPELINE-FEASIBILITY-GATE  
**Version:** 1.0  
**Date:** 2026-07-02  
**Status:** VALIDATED

> Acquisition Allowed = NO for every pipeline. This is non-negotiable until PILOT-ACQUISITION-GATE.

| Pipeline | Source | Access Method | Feasibility | Automation Level | Metadata Available | Sample Allowed | Acquisition Allowed | Risks | Recommended Next |
|---|---|---|---|---|---|---|---|---|---|
| PIPE-MANUS-01 | Manus | REST API (`x-manus-api-key`) | HIGH | HIGH | id, title, timestamps, status, tags | METADATA_ONLY | NO | Pagination cap 200; subtask flood (178/200 noise); no body access | Pilot: 20–50 durable output candidates by metadata score |
| PIPE-OAI-01 | ChatGPT | File export (`conversations.json`) | MEDIUM | LOW | id, title, create_time, update_time, message_count | METADATA_ONLY | NO | Manual export required; no API for conversation history; large JSON | Pilot: 10–20 KAP-relevant conversations from export |
| PIPE-OBS-01 | Obsidian | Local filesystem (vault path) | HIGH | MEDIUM | path, size, folder, has_frontmatter, wikilinks | METADATA_ONLY | NO | Vault not accessible from sandbox; link breakage risk on migration | Pilot: one folder or 50 MD files max; no merge until normalization rules pass |
| PIPE-GDRIVE-01 | Google Drive | OAuth2 REST API | MEDIUM | MEDIUM | id, name, mimeType, timestamps, size, owners | METADATA_ONLY | NO | OAuth2 token not available in sandbox; shared-drive permission complexity | Pilot: one folder inventory + 3 representative files |
| PIPE-NOTION-01 | Notion | Bearer token REST API | MEDIUM | MEDIUM | id, title, parent, timestamps, url | METADATA_ONLY | NO | Token 401 (expired or wrong workspace); hierarchy loss risk | Pilot: one database + 5 representative pages after token refresh |
| PIPE-MEM0-01 | Mem0 | REST API (`Token`) | HIGH | HIGH | id, memory, user_id, categories, created_at, score | METADATA_ONLY | NO | Memories = compressed state, not canonical truth; no source linking | Pilot: memory audit only, confidence-labeled, no canonical promotion |
| PIPE-GIT-01 | Git / GitHub | git CLI + GitHub API | HIGH | HIGH | commit hash, message, timestamp, author, branch | METADATA_ONLY | NO | Force push risk; auto-commit without authorization | Status/readiness audit and commit recommendation only |
| PIPE-WEB-01 | Web URLs | HTTP GET (public) | HIGH | HIGH | url, title, status, content-type | METADATA_ONLY | NO | Copyright; freshness; paywall; CAPTCHA; robots.txt | Pilot: 10 curated URLs, metadata/citation only, no scraping |
