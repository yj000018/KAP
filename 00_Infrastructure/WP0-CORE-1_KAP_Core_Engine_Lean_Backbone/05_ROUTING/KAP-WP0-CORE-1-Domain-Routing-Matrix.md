# Domain Routing Matrix

**Sprint:** WP0-CORE-1
**Generated:** 2026-07-02

## 1. Axioms
- **KAP Core Engine** = Pipeline.
- **YOUniverse** = Personal domain.
- **Mem0** = Active distilled memory.
- **Git/KAP** = Source of truth.

## 2. Routing Matrix

| content_kind | destination | example | mem0_candidate | notes |
|---|---|---|---|---|
| yOS process rules | `yos_core` | Core Engine Backbone, Gate definitions | YES | Must be distilled before Mem0. |
| yOS bugs/failures | `yos_core` | Pagination bug docs, API rate limit reports | YES | Useful for agent context. |
| Agent/skill docs | `yos_core` | session-navigator skill code | YES | Essential for yOS autonomy. |
| Project knowledge | `project_knowledge` | ELYSIUM ontology, KOSMOS specs | YES | Core intellectual property. |
| Personal data | `youniverse` | Life logs, environment data | YES (restricted) | Highly sensitive, requires explicit tag. |
| Home automation | `telemetry` | Temperature logs, light state | NO | Too noisy, time-series data. |
| Monitoring streams | `telemetry` | Server uptime logs | NO | Operational noise. |
| LLM conversations | `archive` | Raw Manus JSON transcript | NO | Must be distilled via WP4 first. |
| Raw task metadata | `archive` | Task IDs, timestamps | NO | Operational noise. |
| Secrets/tokens | `archive_only` | API keys, passwords | NO | Must be redacted or excluded entirely. |
| Duplicated noise | `archive_only` | "Wide Research Subtask" | NO | Ignored by downstream processes. |
