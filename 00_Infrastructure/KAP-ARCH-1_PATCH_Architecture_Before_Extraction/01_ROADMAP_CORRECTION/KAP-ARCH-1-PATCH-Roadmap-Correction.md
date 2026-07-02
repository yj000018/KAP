# KAP-ARCH-1-PATCH — Roadmap Correction

**Purpose:** Correct the roadmap after KAP-ARCH-1 to prioritize architecture before extraction.

## Corrections

| old_step_or_implication | problem | corrected_step | reason |
|---|---|---|---|
| WP2-MANUS-FINAL-BULK | Too extraction-oriented, bulk implies unvalidated ingestion | TARGETED-WP2-SOURCE-SPRINTS | Must validate machine structure and connectors first; extraction must be targeted, not bulk |
| WP2-NOTION migration | Notion is legacy and frozen, migration is low priority | Deferred | Decommissioning legacy takes resources away from building the core engine |
| WP3 opening | Premature, requires clean normalized Phase 1 corpus | Deferred behind Phase 1 Gate | WP3 dry run needs a validated, approved minimal seed corpus first |
| Full automatic extraction | Risky without validated gates and roles | No extraction policy | Machine must be built and validated before feeding it the full corpus |
| Bulk acquisition | Overloads the system before pipelines are tested | PHASE-1-SEED-PLAN | Acquisition must be planned, targeted, and approved |

## Corrected Roadmap

| order | step | purpose | acquisition_allowed | gate_required_before_next |
|---:|---|---|---|---|
| 1 | KAP-ARCH-1-PATCH | correct roadmap and harden anti-extraction policy | NO | Architect review |
| 2 | STRUCTURE-GATE | validate Git/MD/Obsidian structure, indexes, registries, folders | NO | structure pass |
| 3 | CONNECTOR-DESIGN-GATE | validate connector statuses and pipeline reuse decisions | NO | connector design pass |
| 4 | AGENT-ROLE-GATE | validate Team OS roles, Guardian Architect, Manus Executor, future agents | NO | role registry pass |
| 5 | PHASE-1-SEED-PLAN | decide minimal targeted Phase 1 acquisitions, not bulk | NO, planning only | Architect approval |
| 6 | TARGETED-WP2-SOURCE-SPRINTS | run approved minimal acquisitions only | YES, targeted only | source-specific gate |
| 7 | PHASE-1-GATE-REVIEW | decide if enough Phase 1 corpus exists for WP3 dry run | NO | all required Phase 1 gates |
| 8 | WP3-N1 DRY RUN | normalization dry run on limited approved corpus | YES, limited corpus only | Architect approval |
