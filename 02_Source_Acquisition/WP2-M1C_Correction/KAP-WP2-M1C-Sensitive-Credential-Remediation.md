# KAP-WP2-M1C-Sensitive-Credential-Remediation

| Path | Type | Action |
|---|---|---|
| WP2-E1.../session-synthesis/scripts/collect_session.py | JWT | Quarantined |
| WP2-E1.../memory-pipeline/scripts/run_pipeline.py | JWT | Quarantined |
| WP2-E1.../yos-agents/manus/yos-skills/memory-pipeline/scripts/run_pipeline.py | JWT | Quarantined |
| WP2-E1.../yos-agents/manus/yos-skills/session-synthesis/scripts/collect_session.py | JWT | Quarantined |
| WP2-E2.../pipeline_scripts/memory-pipeline/scripts/run_pipeline.py | JWT | Quarantined |
| WP2-E2.../session_synthesis_scripts/scripts/collect_session.py | JWT | Quarantined |
| WP2-E2_Addendum/_scripts/collect_tasks.py | JWT | Quarantined |
| WP2-E2_Addendum/_scripts/collect_tasks_v2.py | JWT | Quarantined |

**Conclusion:** 8 script copies contain the same hardcoded JWT fallback token. They are safely quarantined. No credentials exposed in normal files.
