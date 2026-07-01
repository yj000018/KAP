# KAP WP2-M8 — Manus Session Coverage Audit

| source | observed_session_count | has_titles | has_metadata | has_verbatim | coverage_scope | limitations |
|---|---:|---|---|---|---|---|
| Manus Tasks API (v1/v2) | 10000 | True | True | False | All tasks, including background operational noise | Verbatim content not exposed by list API |
| Notion Manus Memory Sessions DB | 363 | True | True | True | Explicitly archived sessions | Requires manual or explicit trigger to archive |
| Mem0 | 316 | False | True | False | Extracted key facts across sessions | Not a verbatim session archive |