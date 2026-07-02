# KAP Global Source Freeze Map

**Sprint:** WP1-R
**Generated:** 2026-07-02

This map defines which sources are active, frozen, deferred, or blocked, dictating readiness for WP3.

| source_id | source_name | wp2_branch | current_decision | reason | wp3_blocking | next_required_action |
|---|---|---|---|---|---|---|
| SRC-MANUS-01 | Manus Sessions API | WP2-MANUS | REOPEN_REQUIRED_BEFORE_WP3 | M8C/M8D-PATCH residuals still pending | YES | Execute WP2-MANUS-FINAL |
| SRC-CHATGPT-01 | ChatGPT History | WP2-CHATGPT | DEFER_AFTER_WP3 | Not critical for baseline, manual export required | NO | None |
| SRC-CLAUDE-01 | Claude History | WP2-CLAUDE | DEFER_AFTER_WP3 | Not critical for baseline, manual export required | NO | None |
| SRC-GEMINI-01 | Gemini History | WP2-GEMINI | DEFER_AFTER_WP3 | Not critical for baseline, manual export required | NO | None |
| SRC-GROK-01 | Grok History | WP2-GROK | DEFER_AFTER_WP3 | Not critical for baseline, manual export required | NO | None |
| SRC-PERPLEXITY-01 | Perplexity History | WP2-PERPLEXITY | DEFER_AFTER_WP3 | Not critical for baseline, manual export required | NO | None |
| SRC-NOTION-01 | Notion YOS Workspaces | WP2-NOTION | REOPEN_REQUIRED_BEFORE_WP3 | Connector disabled, high-value source | YES | Enable connector, execute WP2-NOTION |
| SRC-MEM0-01 | Mem0 Global Context | WP2-MEM0 | REOPEN_REQUIRED_BEFORE_WP3 | Connector disabled, high-value source | YES | Enable connector, execute WP2-MEM0 |
| SRC-GITHUB-01 | YOS Monorepo | WP2-GITHUB | REOPEN_REQUIRED_BEFORE_WP3 | Needs clone and checksum, high-value source | YES | Execute WP2-GITHUB |
| SRC-OBSIDIAN-01 | Y-WORLD Vault | WP2-OBSIDIAN | REOPEN_REQUIRED_BEFORE_WP3 | Embedded in YOS repo, high-value source | YES | Execute WP2-OBSIDIAN |
| SRC-LOCAL-FILES-01 | Manus Skills Directory | WP2-LOCAL-FILES | FREEZE_FOR_WP3 | Baseline captured via WP2-E1 | NO | None |
| SRC-WEBSITES-01 | Deployed YOS Websites | WP2-WEBSITES | FREEZE_FOR_WP3 | Baseline captured via WP2-E1 | NO | None |
| SRC-LOGS-TELEMETRY-01 | yOS Telemetry | WP2-LOGS-TELEMETRY | DEFER_AFTER_WP3 | No central log sink yet | NO | None |
| SRC-HOME-AUTOMATION-01 | Home Assistant Logs | WP2-HOME-AUTOMATION | DEFER_AFTER_WP3 | Not configured | NO | None |
| SRC-OTHER-01 | Emails and Calendar | WP2-OTHER | EXCLUDED | Out of scope | NO | None |
