# KAP Source State Registry

**Sprint:** WP1-R
**Generated:** 2026-07-02

This is the central ledger of all KAP source states.

| source_id | source_name | source_family | wp2_branch | source_status | baseline_status | delta_status | last_successful_run | last_seen_item_count | last_manifest_path | last_checksum_path | last_commit_hash | known_gaps | risk_level | next_action |
|---|---|---|---|---|---|---|---|---:|---|---|---|---|---|---|
| SRC-MANUS-01 | Manus Sessions API | SF-01 | WP2-MANUS | BASELINE_CAPTURED | PARTIAL_M8D_PENDING | NOT_READY | 2026-07-01 | 363 | /home/ubuntu/KAP/02_Source_Acquisition/WP2-M6B_Notion_Database_Extract/01_MANIFESTS/sprint_manifest.md |  |  | M8C residuals, Pagination bug | HIGH | Execute WP2-MANUS-FINAL |
| SRC-CHATGPT-01 | ChatGPT History | SF-01 | WP2-CHATGPT | DEFERRED | NOT_STARTED | NOT_READY |  | 0 |  |  |  | Manual export required | LOW | None |
| SRC-CLAUDE-01 | Claude History | SF-01 | WP2-CLAUDE | DEFERRED | NOT_STARTED | NOT_READY |  | 0 |  |  |  | Manual export required | LOW | None |
| SRC-GEMINI-01 | Gemini History | SF-01 | WP2-GEMINI | DEFERRED | NOT_STARTED | NOT_READY |  | 0 |  |  |  | Manual export required | LOW | None |
| SRC-GROK-01 | Grok History | SF-01 | WP2-GROK | DEFERRED | NOT_STARTED | NOT_READY |  | 0 |  |  |  | Manual export required | LOW | None |
| SRC-PERPLEXITY-01 | Perplexity History | SF-01 | WP2-PERPLEXITY | DEFERRED | NOT_STARTED | NOT_READY |  | 0 |  |  |  | Manual export required | LOW | None |
| SRC-NOTION-01 | Notion YOS Workspaces | SF-02 | WP2-NOTION | REOPEN_REQUIRED | NOT_STARTED | NOT_READY |  | 0 |  |  |  | Connector disabled in sandbox | HIGH | Enable Notion connector |
| SRC-MEM0-01 | Mem0 Global Context | SF-02 | WP2-MEM0 | REOPEN_REQUIRED | NOT_STARTED | NOT_READY |  | 0 |  |  |  | Connector disabled in sandbox | HIGH | Enable Mem0 connector |
| SRC-GITHUB-01 | YOS Monorepo | SF-03 | WP2-GITHUB | DISCOVERED | NOT_STARTED | NOT_READY |  | 0 |  |  |  | Needs clone and checksum | MEDIUM | Execute WP2-GITHUB |
| SRC-OBSIDIAN-01 | Y-WORLD Vault | SF-04 | WP2-OBSIDIAN | DISCOVERED | NOT_STARTED | NOT_READY |  | 229 |  |  |  | Embedded in YOS repo | LOW | Execute WP2-OBSIDIAN |
| SRC-LOCAL-FILES-01 | Manus Skills Directory | SF-04 | WP2-LOCAL-FILES | BASELINE_VERIFIED | COMPLETE | NOT_READY | 2026-06-25 | 59 | /home/ubuntu/KAP/02_Source_Acquisition/WP2-E1_Easy_Source_Harvest/manifest.json | /home/ubuntu/KAP/02_Source_Acquisition/WP2-E1_Easy_Source_Harvest/SHA256_manifest.md |  |  | LOW | None |
| SRC-WEBSITES-01 | Deployed YOS Websites | SF-05 | WP2-WEBSITES | BASELINE_VERIFIED | COMPLETE | NOT_READY | 2026-06-25 | 5 | /home/ubuntu/KAP/02_Source_Acquisition/WP2-E1_Easy_Source_Harvest/manifest.json | /home/ubuntu/KAP/02_Source_Acquisition/WP2-E1_Easy_Source_Harvest/SHA256_manifest.md |  |  | LOW | None |
| SRC-LOGS-TELEMETRY-01 | yOS Telemetry | SF-06 | WP2-LOGS-TELEMETRY | DEFERRED | NOT_STARTED | NOT_READY |  | 0 |  |  |  | No central log sink yet | LOW | None |
| SRC-HOME-AUTOMATION-01 | Home Assistant Logs | SF-07 | WP2-HOME-AUTOMATION | DEFERRED | NOT_STARTED | NOT_READY |  | 0 |  |  |  | Not configured | LOW | None |
| SRC-OTHER-01 | Emails and Calendar | SF-07 | WP2-OTHER | EXCLUDED | NOT_STARTED | NOT_READY |  | 0 |  |  |  | Out of scope | LOW | None |
