# STRUCTURE-GATE — Structure Gaps

**Purpose:** List gaps that must be fixed before future gates or acquisition.

| gap_id | gap | severity | blocks_CONNECTOR_DESIGN_GATE | blocks_PHASE1_SEED_PLAN | blocks_TARGETED_WP2 | blocks_WP3_N1 | recommended_fix |
|---|---|---|---|---|---|---|---|
| G01 | No README.md in KAP root or major subfolders | LOW | NO | NO | NO | NO | Create `README.md` in root + `00_Infrastructure/`, `01_Source_Inventory/`, `02_Source_Acquisition/`, `03_Archived_Sessions/` |
| G02 | Agent Role Registry not consolidated in `Team_OS/Agents/` | MEDIUM | NO | NO | NO | NO | Create `AGENT-ROLE-REGISTRY.md` in `Team_OS/Agents/` in CONNECTOR-DESIGN-GATE sprint |
| G03 | Connector Backlog not separated from Source Branch Mapping | LOW | NO | NO | NO | NO | Extract backlog into dedicated `CONNECTOR-BACKLOG.md` in WP1-R |
| G04 | No Obsidian `[[wikilinks]]` in existing Markdown files | LOW | NO | NO | NO | NO | Add wikilinks in future indexing sprint (not before vault activation) |
| G05 | `02_Source_Acquisition/` has no per-source README | LOW | NO | NO | NO | NO | Add README per source family folder when acquisition starts |
| G06 | Future phase folders (`03_Normalized_Knowledge/` through `07_Obsidian_Index/`) do not exist | INFO | NO | NO | NO | NO | Create on demand as phases open |
| G07 | Manus Executor role not formally documented in `Team_OS/Agents/` | MEDIUM | NO | NO | NO | NO | Create `MANUS-Executor.md` in CONNECTOR-DESIGN-GATE sprint |
| G08 | 11 sessions not found in API (beyond pagination limit) | MEDIUM | NO | NO | YES | NO | Retry after rate limit reset; or accept as unrecoverable |
| G09 | `scripts/` folder in `00_Infrastructure/` (not in root) — inconsistent location | LOW | NO | NO | NO | NO | Architect decision: move scripts to root or keep in infra |

**Total gaps: 9 | Blocking gaps: 0 | CONNECTOR-DESIGN-GATE blockers: 0**
