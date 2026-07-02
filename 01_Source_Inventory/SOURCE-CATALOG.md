# Source Catalog

> KAP Source Inventory — Master List of All Knowledge Sources

## 1. Core Sources (Active/In Progress)

| Source ID | Origin | Type | Format | Status | Connector |
|---|---|---|---|---|---|
| SRC-001 | Manus Sessions | AI Execution | Markdown | ACTIVE | `kap_session_archive` |
| SRC-002 | Notion (Y-world) | Structured KB | Markdown | IN_PROGRESS | `notion_full_census` |
| SRC-003 | Obsidian (9 vaults) | Markdown KB | Markdown | DISCOVERED | TBD |
| SRC-004 | GitHub (yj000018) | Code/Docs | Git/MD | CATALOGUED | TBD |

## 2. Planned Sources (Short Term)

| Source ID | Origin | Type | Format | Status | Connector |
|---|---|---|---|---|---|
| SRC-005 | ChatGPT | AI Dialogue | JSON | PLANNED | TBD |
| SRC-006 | Mem0 | Cross-Session | JSON | PLANNED | TBD |
| SRC-007 | Google Drive | Documents | Docs/PDF | PLANNED | TBD |
| SRC-008 | Other LLMs | AI Dialogue | JSON/Text | PLANNED | TBD |

## 3. Future Sources (Mid/Long Term)

| Source ID | Origin | Type | Target Format | Status | Potential Use Case |
|---|---|---|---|---|---|
| SRC-009 | YouTube (Watched) | Video | Transcript/MD | IDEA | YOUniverse feeding, concept extraction |
| SRC-010 | Web Bookmarks | Curation | URL/MD | IDEA | External reference linking |
| SRC-011 | Browsing History | Behavioral | JSON/Events | IDEA | Passive interest tracking |
| SRC-012 | Excalidraw | Visual | SVG/JSON/MD | IDEA | Architecture schemas, visual thought lines |
| SRC-013 | Spline | 3D Visual | JSON/MD | IDEA | 3D interface state tracking |
| SRC-014 | Voice Memos | Audio | Transcript/MD | IDEA | Capturing spontaneous thoughts |
| SRC-015 | Figma / Design | Visual | SVG/MD | IDEA | UI/UX decision tracking |
| SRC-016 | Specialized LLM Tools | AI Output | JSON/MD | IDEA | E.g., specific research agent outputs |

## 4. Source Registration Protocol

To add a new source to KAP:
1. Add entry to this Catalog.
2. Define acquisition method in `SOURCE-ACTIVATION-POLICY.md`.
3. Build Connector in `02_Source_Acquisition/Connectors/`.
4. Run Pilot Gate.
5. Activate source.
