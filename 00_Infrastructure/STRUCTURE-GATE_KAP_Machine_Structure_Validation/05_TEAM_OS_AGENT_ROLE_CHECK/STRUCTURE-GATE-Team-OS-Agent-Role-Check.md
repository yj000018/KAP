# STRUCTURE-GATE — Team OS / Agent Role Check

**Purpose:** Validate that Team OS / agent roles have a findable Git/MD structure and that the Guardian Architect role is properly stored.

| role_or_folder | expected_path | found | status | responsibility | future_merge |
|---|---|---|---|---|---|
| ChatGPT Guardian Architect / Architecte des gardiens | `00_Infrastructure/Team_OS/Agents/CHATGPT-Guardian-Architect.md` | YES | FOUND_CANONICAL | Strategic oversight, architecture validation, gate approval | NO — canonical location |
| Team_OS/Agents/ folder | `00_Infrastructure/Team_OS/Agents/` | YES | FOUND_CANONICAL | Container for all agent role definitions | NO |
| Manus Executor | `00_Infrastructure/Team_OS/Agents/MANUS-Executor.md` | NO | MISSING_CREATE_LATER | Execution, code generation, infrastructure building | YES — create in CONNECTOR-DESIGN-GATE sprint |
| Mem0 Memory Layer | `00_Infrastructure/Team_OS/Agents/MEM0-Memory-Layer.md` | NO | MISSING_CREATE_LATER | Semantic search, long-term distilled memory | YES — create when Mem0 integration starts |
| Obsidian Navigation Layer | `00_Infrastructure/Team_OS/Agents/OBSIDIAN-Navigation-Layer.md` | NO | MISSING_CREATE_LATER | Human consultation, graph visualization | YES — create when vault is activated |
| Future Connector Agents | `00_Infrastructure/Team_OS/Agents/` | NO | MISSING_CREATE_LATER | Specialized data extraction per source | YES — create per source sprint |
| Future Pipeline Agents | `00_Infrastructure/Team_OS/Agents/` | NO | MISSING_CREATE_LATER | Data normalization and routing | YES — create when WP3 opens |
| Future Gatekeeper / QA | `00_Infrastructure/Team_OS/Agents/` | NO | MISSING_CREATE_LATER | Quality control, gate validation | YES — create when QA layer is needed |
| Agent Role Registry (consolidated) | `00_Infrastructure/Team_OS/Agents/AGENT-ROLE-REGISTRY.md` | NO | MISSING_CREATE_LATER | Single index of all roles | YES — create in CONNECTOR-DESIGN-GATE sprint |

**Note:** Existing roles must not be overwritten. The PATCH sprint defined roles in `05_AGENT_ROLE_REGISTRY_PATCH/` — these must be merged into `Team_OS/Agents/` in a future sprint.

**Team OS / Agent Role Gate: PASS_WITH_MINOR_GAPS — Guardian Architect canonical; other roles to be created as sprints open.**
