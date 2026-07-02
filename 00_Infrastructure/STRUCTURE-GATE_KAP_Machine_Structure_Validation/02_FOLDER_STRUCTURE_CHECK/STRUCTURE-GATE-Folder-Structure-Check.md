# STRUCTURE-GATE — Folder Structure Check

**Purpose:** Validate that KAP has a coherent Git/Markdown folder structure for future phases. Inspection only — no files moved, no folders reorganized.

| target_folder | purpose | exists_now | current_path_if_exists | status | required_action |
|---|---|---|---|---|---|
| `00_Infrastructure/` | Architecture, protocols, registries, gates, Team OS | YES | `/home/ubuntu/KAP/00_Infrastructure/` | EXISTS_AND_USABLE | Add README/index |
| `01_Source_Inventory/` | Source registry, freeze map, WP1-R | YES | `/home/ubuntu/KAP/01_Source_Inventory/` | EXISTS_AND_USABLE | Add top-level README |
| `02_Source_Acquisition/` | Raw acquired content per source family | YES | `/home/ubuntu/KAP/02_Source_Acquisition/` | EXISTS_BUT_NEEDS_INDEX | Add per-source README |
| `03_Normalized_Knowledge/` | WP3 normalized output (future) | NO | — | MISSING_CREATE_LATER | Create when WP3 starts |
| `04_Distillation/` | Distilled insights, Mem0 candidates (future) | NO | — | MISSING_CREATE_LATER | Create when distillation starts |
| `05_Project_Knowledge/` | Dynamic project self-knowledge (Phase 2) | NO | — | MISSING_CREATE_LATER | Create when Phase 2 starts |
| `06_Memory_Candidates/` | Pre-Mem0 distilled facts (future) | NO | — | MISSING_CREATE_LATER | Create when distillation starts |
| `07_Obsidian_Index/` | Obsidian vault entry point / index files | NO | — | MISSING_CREATE_LATER | Create when Obsidian vault is set up |
| `08_Protocols/` | Execution protocols (currently in 00_Infrastructure) | PARTIAL | `00_Infrastructure/KAP-ARCH-1_.../02_PROTOCOL_REGISTRY/` | SUPERSEDED_BY_EXISTING_STRUCTURE | Keep in 00_Infrastructure; add cross-link |
| `09_Resources/` | Shared assets, templates, schemas | PARTIAL | `00_Infrastructure/WP0-CORE-1_.../03_SCHEMAS/` | SUPERSEDED_BY_EXISTING_STRUCTURE | Keep in WP0; add cross-link |
| `10_Roadmaps/` | Roadmaps and gate decisions | PARTIAL | `00_Infrastructure/KAP-ARCH-1_.../10_ROADMAP_RESET/` | SUPERSEDED_BY_EXISTING_STRUCTURE | Keep in KAP-ARCH-1; add cross-link |
| `99_Archive/` | Archived sessions, legacy content | PARTIAL | `/home/ubuntu/KAP/03_Archived_Sessions/` | SUPERSEDED_BY_EXISTING_STRUCTURE | Keep as `03_Archived_Sessions/`; rename not required |

**Note:** The existing KAP root structure (`00_Infrastructure/`, `01_Source_Inventory/`, `02_Source_Acquisition/`, `03_Archived_Sessions/`) is coherent and usable. The target canonical folders that are missing (`03_Normalized_Knowledge/` through `07_Obsidian_Index/`) are future-phase folders and do not block the current gate.

**Folder Structure Gate: PASS_WITH_MINOR_GAPS — structure is usable; future folders to be created as phases open.**
