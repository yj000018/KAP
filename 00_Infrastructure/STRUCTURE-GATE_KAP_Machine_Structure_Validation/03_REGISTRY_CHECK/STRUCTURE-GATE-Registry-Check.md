# STRUCTURE-GATE — Registry Check

**Purpose:** Validate that core registries exist, are findable, and are usable as future control surfaces.

| registry | expected_file_or_folder | found | status | issue | required_fix |
|---|---|---|---|---|---|
| Source State Registry | `01_Source_Inventory/WP1-R_.../02_SOURCE_REGISTRY/` | YES | FOUND_USABLE | — | — |
| Freeze Map | `01_Source_Inventory/WP1-R_.../03_FREEZE_MAP/` | YES | FOUND_USABLE | — | — |
| Connector Backlog | `01_Source_Inventory/WP1-R_.../04_SOURCE_BRANCH_MAPPING/` | YES | FOUND_NEEDS_PATCH | Backlog mixed with branch mapping | Separate backlog into dedicated file |
| Current Acquisition Scope | `KAP-ARCH-1-PATCH.../04_PHASE1_SEED_PLAN/` | YES | FOUND_USABLE | Scope is planning-only, no active acquisition | — |
| Protocol Registry | `00_Infrastructure/KAP-ARCH-1_.../02_PROTOCOL_REGISTRY/KAP-ARCH-1-Protocol-Registry.md` | YES | FOUND_USABLE | — | — |
| Pipeline Registry | `00_Infrastructure/KAP-ARCH-1_.../03_PIPELINE_REGISTRY/KAP-ARCH-1-Pipeline-Registry.md` | YES | FOUND_USABLE | — | — |
| Connector Readiness Matrix | `00_Infrastructure/KAP-ARCH-1_.../04_CONNECTOR_READINESS/KAP-ARCH-1-Connector-Pipeline-Readiness-Matrix.md` | YES | FOUND_USABLE | — | — |
| Agent Role Registry / Team OS agent folder | `00_Infrastructure/Team_OS/Agents/CHATGPT-Guardian-Architect.md` | YES | FOUND_NEEDS_PATCH | Only Guardian Architect defined; other roles are in PATCH file only | Create full Agent Role Registry MD |
| Roadmap Reset | `00_Infrastructure/KAP-ARCH-1_.../10_ROADMAP_RESET/` | YES | FOUND_USABLE | — | — |
| No Extraction Policy | `KAP-ARCH-1-PATCH.../06_NO_EXTRACTION_POLICY/KAP-ARCH-1-PATCH-No-Extraction-Policy.md` | YES | FOUND_USABLE | — | — |
| Notion Decommission Plan | `00_Infrastructure/KAP-ARCH-1_.../06_NOTION_DECOMMISSION_PLAN/KAP-ARCH-1-Notion-Decommission-Plan.md` | YES | FOUND_USABLE | — | — |
| Mem0 Positioning | `00_Infrastructure/KAP-ARCH-1_.../07_MEM0_POSITIONING/KAP-ARCH-1-Mem0-Positioning.md` | YES | FOUND_USABLE | — | — |
| Project Knowledge Layer | `00_Infrastructure/KAP-ARCH-1_.../08_PROJECT_KNOWLEDGE_LAYER/` | YES | FOUND_USABLE | — | — |
| YOUniverse Positioning | `00_Infrastructure/KAP-ARCH-1_.../09_YOUNIVERSE_POSITIONING/` | YES | FOUND_USABLE | — | — |
| Git Proof convention | `00_Infrastructure/KAP-ARCH-1-PATCH.../08_GIT_PROOF/KAP-ARCH-1-PATCH-Git-Proof.md` | YES | FOUND_USABLE | Convention established in PATCH sprint | — |

**Registry Gate: PASS_WITH_MINOR_GAPS — 13/15 FOUND_USABLE, 2 FOUND_NEEDS_PATCH (non-blocking).**
