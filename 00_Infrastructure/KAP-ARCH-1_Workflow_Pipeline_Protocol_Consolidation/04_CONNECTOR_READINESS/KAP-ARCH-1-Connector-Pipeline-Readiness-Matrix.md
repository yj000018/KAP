# KAP-ARCH-1: Connector & Pipeline Readiness Matrix

**Program:** KAP
**Sprint:** KAP-ARCH-1
**Date:** 2026-07-02

## Overview
This matrix determines the readiness of connectors and pipelines for every relevant source or source family. It identifies what is working, what is blocked, what is deferred, and what is excluded by policy.

## Readiness Matrix

| source_or_family | phase | domain | connector_or_tool | pipeline | readiness_status | blocker_or_risk | next_decision |
|---|---|---|---|---|---|---|---|
| Manus Sessions API | Phase 1 | yOS/MyOS | Manus API | Archive Pipeline | PARTIAL_BLOCKER | API limits pagination to 200 | Use My Browser Mac |
| Manus Skills | Phase 1 | yOS/MyOS | Filesystem | Not started | DESIGNED_READY_TO_TEST | None | Run WP2-MANUS |
| Manus Websites | Phase 1 | yOS/MyOS | Filesystem | Not started | DESIGNED_READY_TO_TEST | None | Run WP2-MANUS |
| Manus Internal Knowledge | Phase 1 | yOS/MyOS | Filesystem | Not started | DESIGNED_READY_TO_TEST | None | Run WP2-MANUS |
| Manus Tasks API | Phase 1 | yOS/MyOS | Manus API | Archive Pipeline | PARTIAL_BLOCKER | API limits pagination to 200 | Use My Browser Mac |
| GitHub KAP repo | Phase 1 | System | Git CLI | Clone Pipeline | TESTED_WORKING | None | Ready |
| GitHub yOS / MyOS repos | Phase 1 | System | Git CLI | Clone Pipeline | DESIGNED_READY_TO_TEST | None | Run WP2-GITHUB |
| Notion legacy | Phase 1 | System | Notion API | Notion-to-Git | DESIGNED_READY_TO_TEST | None | Run WP2-NOTION |
| Mem0 | Phase 2 | Memory | Mem0 API | Mem0 Sync | TESTED_WORKING | None | Run WP5 |
| Obsidian / vaults | Phase 1 | System | Filesystem | Vault Indexing | DESIGNED_READY_TO_TEST | None | Run WP3 |
| ChatGPT exports | Phase 1 | AI History | File upload | TBD | DESIGNED_READY_TO_TEST | None | Schedule sprint |
| Claude exports | Phase 1 | AI History | File upload | TBD | DESIGNED_READY_TO_TEST | None | Schedule sprint |
| Gemini | Phase 1 | AI History | TBD | TBD | DISABLED_BY_NON_USE | Quality/usage too low | Do not ingest |
| Grok | Phase 1 | AI History | TBD | TBD | DISABLED_BY_NON_USE | Quality/usage too low | Do not ingest |
| Perplexity | Phase 1 | AI History | TBD | TBD | DESIGNED_READY_TO_TEST | API limits | Schedule sprint |
| local files / project folders | Phase 1 | Projects | Filesystem | TBD | DESIGNED_READY_TO_TEST | None | Schedule sprint |
| project assets / logos / docs | Phase 1 | Projects | Filesystem | TBD | DESIGNED_READY_TO_TEST | None | Schedule sprint |
| Readwise | Phase 3 | YOUniverse | API | TBD | DEFERRED_YOUNIVERSE | None | Defer to Phase 3 |
| YouTube playlists / favorites | Phase 3 | YOUniverse | API | TBD | DEFERRED_YOUNIVERSE | None | Defer to Phase 3 |
| emails / calendar | Phase 3 | YOUniverse | Gmail/Cal API | 2-Phase Funnel | DEFERRED_YOUNIVERSE | None | Defer to Phase 3 |
| Home Assistant logs | Phase 4 | Telemetry | API | Telemetry Pipeline | DEFERRED_TELEMETRY | None | Defer to Phase 4 |
| sensors / monitoring streams | Phase 4 | Telemetry | API | Telemetry Pipeline | DEFERRED_TELEMETRY | None | Defer to Phase 4 |
| browser history | Phase 1 | Telemetry | TBD | TBD | EXCLUDED_BY_POLICY | Privacy/Noise | Exclude unless requested |
| shell history | Phase 1 | Telemetry | TBD | TBD | EXCLUDED_BY_POLICY | Privacy/Noise | Exclude unless requested |
| secrets / tokens | Phase 1 | Security | None | None | EXCLUDED_BY_POLICY | Security | Never ingest |

## Key Decisions
1. **Manus API Limitations:** The Manus Sessions API is partially blocked due to a 200-item pagination limit. The official workaround is using My Browser on Mac.
2. **Deferred Sources:** All personal data (Readwise, YouTube, Emails, Calendar) is deferred to Phase 3 (YOUniverse). Telemetry is deferred to Phase 4.
3. **Excluded Sources:** Browser history, shell history, and secrets are strictly excluded by policy.
4. **Disabled Sources:** Gemini and Grok are disabled due to low usage or quality.
