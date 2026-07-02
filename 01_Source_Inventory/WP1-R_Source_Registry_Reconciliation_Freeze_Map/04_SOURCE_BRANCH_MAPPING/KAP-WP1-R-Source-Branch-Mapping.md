# KAP Source Branch Mapping

**Sprint:** WP1-R
**Generated:** 2026-07-02

This map assigns every known source surface to its correct WP2 branch.

| source_surface | source_family | wp2_branch | corpus_value | acquisition_status | delta_requirement | notes |
|---|---|---|---|---|---|---|
| Manus Sessions API | SF-01 | WP2-MANUS | PRIMARY_CORPUS | BASELINE_IN_PROGRESS | YES | Pending M8C residuals |
| Manus Tasks API | SF-01 | WP2-MANUS | OPERATIONAL_METADATA | DEFERRED | NO | Low priority compared to sessions |
| Manus Internal Knowledge / Personalization | SF-01 | WP2-MANUS | PRIMARY_CORPUS | DEFERRED | YES | Needs specific extraction method |
| Manus Skills | SF-04 | WP2-LOCAL-FILES | PRIMARY_CORPUS | BASELINE_CAPTURED | YES | Captured via WP2-E1 |
| Manus Websites | SF-05 | WP2-WEBSITES | SECONDARY_CORPUS | BASELINE_CAPTURED | YES | Captured via WP2-E1 |
| Manus remote filesystem /home/ubuntu | SF-04 | WP2-LOCAL-FILES | PRIMARY_CORPUS | PARTIAL | YES | KAP and skills covered, rest deferred |
| Notion Manus Memory Sessions | SF-02 | WP2-NOTION | PRIMARY_CORPUS | BLOCKED | YES | Connector disabled |
| Notion project spaces | SF-02 | WP2-NOTION | PRIMARY_CORPUS | BLOCKED | YES | Connector disabled |
| Mem0 existing memories | SF-02 | WP2-MEM0 | PRIMARY_CORPUS | BLOCKED | YES | Connector disabled |
| GitHub KAP repo | SF-03 | WP2-GITHUB | PRIMARY_CORPUS | DISCOVERED | YES | Needs clone |
| Obsidian / vaults if known | SF-04 | WP2-OBSIDIAN | PRIMARY_CORPUS | DISCOVERED | YES | Embedded in YOS repo |
| ChatGPT conversations/exports | SF-01 | WP2-CHATGPT | SECONDARY_CORPUS | DEFERRED | NO | Manual export required |
| Claude conversations/exports | SF-01 | WP2-CLAUDE | SECONDARY_CORPUS | DEFERRED | NO | Manual export required |
| Gemini conversations/exports | SF-01 | WP2-GEMINI | SECONDARY_CORPUS | DEFERRED | NO | Manual export required |
| Grok conversations/exports | SF-01 | WP2-GROK | SECONDARY_CORPUS | DEFERRED | NO | Manual export required |
| Perplexity conversations/exports | SF-01 | WP2-PERPLEXITY | SECONDARY_CORPUS | DEFERRED | NO | Manual export required |
| local files/folders | SF-04 | WP2-LOCAL-FILES | PRIMARY_CORPUS | PARTIAL | YES | Covered by specific targeting |
| websites/deployed artifacts | SF-05 | WP2-WEBSITES | SECONDARY_CORPUS | BASELINE_CAPTURED | YES | Captured via WP2-E1 |
| logs/telemetry | SF-06 | WP2-LOGS-TELEMETRY | OPERATIONAL_METADATA | DEFERRED | NO | Out of scope for now |
| home automation future logs | SF-07 | WP2-HOME-AUTOMATION | FUTURE_OPTIONAL_SOURCE | DEFERRED | NO | Out of scope for now |
| emails/calendar | SF-07 | WP2-OTHER | RESTRICTED_SECRET_SURFACE | EXCLUDED | NO | Explicitly excluded |
| browser/shell history | SF-07 | WP2-OTHER | NON_CORPUS_NOISE | EXCLUDED | NO | Excluded by default |
