# Source Catalog

> KAP Source Registry — Master List of All Knowledge Sources

## Scope Classification

Each source is tagged with one or more scope labels. The same engine processes all sources — scope tags determine routing, not pipeline branching.

| Scope | Tag | Destination |
|---|---|---|
| Y-OS architecture, decisions, tools, projects | `scope:yos` | KAP synthesis → yOS Obsidian graph |
| Personal facts, behaviors, life events, external world | `scope:youniverse` | YOUniverse synthesis → YOUniverse graph |
| Both | `scope:both` | Both destinations |

---

## 1. Active Sources (Currently Acquiring)

| Source ID | Origin | Scope | Format | Status | Connector | Notes |
|---|---|---|---|---|---|---|
| SRC-001 | Manus Sessions | `scope:yos` | Markdown | **ACTIVE** | `kap_session_archive` | 194 factsheets acquired |
| SRC-002 | Notion (Y-world) | `scope:yos` | Markdown | **IN_PROGRESS** | `notion_full_census` | Census in progress, 1300+ pages |

---

## 2. Planned Sources (Connectors to Build)

| Source ID | Origin | Scope | Format | Status | Notes |
|---|---|---|---|---|---|
| SRC-003 | Obsidian (9 vaults) | `scope:yos` | Markdown | **DISCOVERED** | ~4400+ notes, gate pending |
| SRC-004 | GitHub (yj000018) | `scope:yos` | Git/MD | **CATALOGUED** | 36 repos, acquisition gate pending |
| SRC-005 | ChatGPT | `scope:both` | JSON | **PLANNED** | Needs `conversations.json` export |
| SRC-006 | Mem0 | `scope:yos` | JSON | **ACQUIRED** | All entries captured — routing aid, not primary source |
| SRC-007 | LLM Internal Memory | `scope:both` | Prompted Text | **DEFERRED** | Batch PROMPT_EXTRACTION after THOUGHT-LINE-SEEDING-GATE |
| SRC-008 | Other LLMs (Claude, Gemini, Grok…) | `scope:both` | JSON/Text | **PLANNED** | Open-ended list — new LLMs added as history accumulates |

---

## 3. Future yOS Sources

| Source ID | Origin | Scope | Format | Status | Notes |
|---|---|---|---|---|---|
| SRC-F01 | Excalidraw / Figma / Spline | `scope:yos` | SVG/JSON/MD | **IDEA** | Architecture schemas, visual thought lines |
| SRC-F02 | Specialized AI Tool Outputs | `scope:yos` | JSON/MD | **IDEA** | Outputs from research agents, graph generators |

---

## 4. YOUniverse Sources (Catalogued — Connectors Not Yet Built)

> These sources are catalogued now. Connectors will be built when Phase 2 (YOUniverse) is formally opened.
> Note: some fragments from these sources may also carry `scope:yos` (e.g., a calendar event about an architecture decision). The classifier handles this at extraction time.

| Source ID | Origin | Scope | Format | Status | YOUniverse Value |
|---|---|---|---|---|---|
| SRC-Y01 | Google Drive | `scope:youniverse` | Docs/PDF | **CATALOGUED** | Personal docs, EYA/Roberta files |
| SRC-Y02 | Google Calendar | `scope:youniverse` | JSON | **CATALOGUED** | Life timeline, recurring patterns |
| SRC-Y03 | Email | `scope:youniverse` | Text/JSON | **CATALOGUED** | Relationships, decisions, history |
| SRC-Y04 | YouTube (Watched) | `scope:youniverse` | Transcript/MD | **CATALOGUED** | Interests, intellectual diet |
| SRC-Y05 | Web Bookmarks | `scope:youniverse` | URL/MD | **CATALOGUED** | External curation |
| SRC-Y06 | Browsing History | `scope:youniverse` | JSON | **CATALOGUED** | Passive interest tracking |
| SRC-Y07 | Voice Memos | `scope:youniverse` | Transcript/MD | **CATALOGUED** | Spontaneous thoughts |
| SRC-Y08 | App Usage Logs | `scope:youniverse` | JSON | **CATALOGUED** | Tool preferences, workflow patterns |

---

## 5. Mem0 — Status Note

> **ACQUIRED** — All entries captured in previous sessions.
> Mem0 is a compressed derivative (routing aid), not a primary source.
> Verify no delta sync needed at start of THOUGHT-LINE-SEEDING-GATE.

---

## 6. LLM Internal Memory — Deferred Extraction

> **DEFERRED** — Execute after THOUGHT-LINE-SEEDING-GATE (full taxonomy known).
> Single batch session per LLM with full project/theme/tag list.
> Scope: `scope:both` — fragments may contain yOS architecture AND personal context.
> Target LLMs: Claude, ChatGPT, Gemini, Grok + any future LLM with persistent context (open list).

---

## 7. Source Registration Protocol

To add a new source:
1. Add entry here with scope tag(s).
2. Define state/mode in `SOURCE-ACTIVATION-POLICY.md`.
3. Build Connector in `02_Source_Acquisition/Connectors/`.
4. Run Pilot Gate.
5. Activate.
