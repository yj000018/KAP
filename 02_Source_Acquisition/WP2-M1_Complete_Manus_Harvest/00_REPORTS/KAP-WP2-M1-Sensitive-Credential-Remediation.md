# KAP-WP2-M1-Sensitive-Credential-Remediation

## Sensitive remediation table

| sensitive_id | source | path | type | action | raw_value_exposed | redacted_copy | notes |
|---|---|---|---|---|---|---|---|
| SEN-001 | WP2-E2 | pipeline_scripts/collect_session.py | JWT Token | Quarantined | No | Yes | Hardcoded fallback token |
| SEN-002 | WP2-E2 | pipeline_scripts/run_pipeline.py | JWT Token | Quarantined | No | Yes | Hardcoded fallback token |
| SEN-003 | WP2-E1 | manus_skills/session-synthesis/collect_session.py | JWT Token | Quarantined | No | Yes | Hardcoded fallback token |