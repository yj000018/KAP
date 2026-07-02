# KAP-ARCH-1-PATCH — Connector Design Gate

**Purpose:** Validate that sources/connectors/pipelines are designed before executing acquisition.

## Source Family Table

| source_family | connector_status | pipeline_status | reuse_decision | extraction_allowed_now | reason | next_design_action |
|---|---|---|---|---|---|---|
| Manus Sessions | TESTED_WORKING | DESIGNED_READY_TO_TEST | Reuse v3 | NO | Awaiting Architect review of PATCH | Finalize UID extraction protocol |
| Manus Skills | TESTED_WORKING | DESIGNED_READY_TO_TEST | Reuse | NO | Awaiting Architect review of PATCH | Map local vs remote skills |
| Manus Websites | UNKNOWN_REVIEW_REQUIRED | PARTIAL_BLOCKER | TBD | NO | Awaiting Architect review of PATCH | Define scraping vs source code strategy |
| Manus Internal Knowledge | TESTED_WORKING | DESIGNED_READY_TO_TEST | Reuse | NO | Awaiting Architect review of PATCH | Distillation protocol definition |
| Manus Tasks | TESTED_WORKING | DESIGNED_READY_TO_TEST | Reuse | NO | Awaiting Architect review of PATCH | Define filtering strategy |
| Notion legacy | TESTED_WORKING | PARTIAL_BLOCKER | TBD | NO | Awaiting Architect review of PATCH | Frozen, define decommission plan |
| GitHub KAP | TESTED_WORKING | DESIGNED_READY_TO_TEST | Reuse | NO | Awaiting Architect review of PATCH | - |
| GitHub yOS/MyOS | TESTED_WORKING | DESIGNED_READY_TO_TEST | Reuse | NO | Awaiting Architect review of PATCH | - |
| Obsidian vaults | UNKNOWN_REVIEW_REQUIRED | PARTIAL_BLOCKER | TBD | NO | Awaiting Architect review of PATCH | Define read-only vs write rules |
| Mem0 | TESTED_WORKING | DESIGNED_READY_TO_TEST | Reuse | NO | Awaiting Architect review of PATCH | Semantic only, no raw ingestion |
| ChatGPT exports | TESTED_WORKING | DESIGNED_READY_TO_TEST | Reuse | NO | Awaiting Architect review of PATCH | Define JSON parsing strategy |
| Claude exports | TESTED_WORKING | DESIGNED_READY_TO_TEST | Reuse | NO | Awaiting Architect review of PATCH | Define JSON parsing strategy |
| Gemini | UNKNOWN_REVIEW_REQUIRED | PARTIAL_BLOCKER | TBD | NO | Awaiting Architect review of PATCH | Check export formats |
| Grok | UNKNOWN_REVIEW_REQUIRED | PARTIAL_BLOCKER | TBD | NO | Awaiting Architect review of PATCH | Check export formats |
| Perplexity | UNKNOWN_REVIEW_REQUIRED | PARTIAL_BLOCKER | TBD | NO | Awaiting Architect review of PATCH | Check export formats |
| local project folders | UNKNOWN_REVIEW_REQUIRED | PARTIAL_BLOCKER | TBD | NO | Awaiting Architect review of PATCH | Define file filtering |
| project assets/logos/docs | UNKNOWN_REVIEW_REQUIRED | PARTIAL_BLOCKER | TBD | NO | Awaiting Architect review of PATCH | Define media handling |
| Readwise | UNKNOWN_REVIEW_REQUIRED | PARTIAL_BLOCKER | TBD | NO | Awaiting Architect review of PATCH | API integration design |
| YouTube playlists/favorites | UNKNOWN_REVIEW_REQUIRED | PARTIAL_BLOCKER | TBD | NO | Awaiting Architect review of PATCH | API integration design |
| email/calendar | UNKNOWN_REVIEW_REQUIRED | PARTIAL_BLOCKER | TBD | NO | Awaiting Architect review of PATCH | Privacy and filtering rules |
| Home Assistant | DEFERRED_TELEMETRY | DEFERRED_TELEMETRY | Deferred | NO | Awaiting Architect review of PATCH | - |
| sensors/telemetry | DEFERRED_TELEMETRY | DEFERRED_TELEMETRY | Deferred | NO | Awaiting Architect review of PATCH | - |
| browser history | UNKNOWN_REVIEW_REQUIRED | PARTIAL_BLOCKER | TBD | NO | Awaiting Architect review of PATCH | Privacy and filtering rules |
| shell history | UNKNOWN_REVIEW_REQUIRED | PARTIAL_BLOCKER | TBD | NO | Awaiting Architect review of PATCH | Filtering rules |
| secrets/tokens | RESTRICTED_SECRET_SURFACE | EXCLUDED_BY_POLICY | Excluded | NO | Awaiting Architect review of PATCH | Security policy |
