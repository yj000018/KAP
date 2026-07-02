# Source Catalog

> KAP Source Inventory — Master List of All Knowledge Sources

## Pipeline Scope Model

KAP operates in two distinct phases with different source scopes:

| Phase | Name | Purpose | Sources In Scope |
|---|---|---|---|
| **Phase 1 — KAP** | yOS Knowledge Consolidation | Consolidate all Y-OS architecture, decisions, projects, intellectual threads | yOS Core + yOS Peripheral |
| **Phase 2 — YOUniverse** | 360° Personal Profile | Mega-profile: all data about Yannick — facts, behaviors, preferences, life events | All sources including personal/behavioral |

> **Current phase: Phase 1 — KAP**. YOUniverse sources are catalogued here for future activation but are NOT acquired in this phase.

---

## 1. yOS Core Sources (Phase 1 — Active)

| Source ID | Origin | Type | Format | Status | Connector | Notes |
|---|---|---|---|---|---|---|
| SRC-001 | Manus Sessions | AI Execution | Markdown | **ACTIVE** | `kap_session_archive` | 194 factsheets acquired |
| SRC-002 | Notion (Y-world) | Structured KB | Markdown | **IN_PROGRESS** | `notion_full_census` | Census in progress, 1300+ pages |
| SRC-003 | Obsidian (9 vaults) | Markdown KB | Markdown | **DISCOVERED** | TBD | ~4400+ notes, gate pending |
| SRC-004 | GitHub (yj000018) | Code/Docs | Git/MD | **CATALOGUED** | TBD | 36 repos, acquisition gate pending |
| SRC-005 | ChatGPT | AI Dialogue | JSON | **PLANNED** | TBD | Needs `conversations.json` export |

---

## 2. yOS Peripheral Sources (Phase 1 — Partial)

| Source ID | Origin | Type | Format | Status | Connector | Notes |
|---|---|---|---|---|---|---|
| SRC-006 | Mem0 | Cross-Session Memory | JSON | **ACQUIRED** | Mem0 API | See note §4 — all entries captured |
| SRC-007 | LLM Internal Memory | AI Introspection | Prompted Text | **DEFERRED** | PROMPT_EXTRACTION | See note §5 — execute at end of Phase 1 |
| SRC-008 | Other LLMs (Claude, Gemini, Grok…) | AI Dialogue | JSON/Text | **PLANNED** | Export per platform | New LLMs added as they accumulate history |

---

## 3. Future yOS Sources (Activatable when ready)

| Source ID | Origin | Type | Format | Status | Notes |
|---|---|---|---|---|---|
| SRC-F01 | Excalidraw / Figma / Spline | Visual | SVG/JSON/MD | **IDEA** | Architecture schemas, visual thought lines — high yOS signal |
| SRC-F02 | Specialized AI Tool Outputs | AI Output | JSON/MD | **IDEA** | Outputs from specific research agents, graph generators |

---

## 4. YOUniverse Sources (Phase 2 — Out of Scope for Phase 1)

> These sources contain personal life, behavioral, and external world data.
> They are **out of scope for Phase 1 (KAP)** but are **explicitly planned for Phase 2 (YOUniverse)**.
> YOUniverse goal: 360° mega-profile — all data about Yannick, dynamic, continuously updated.

| Source ID | Origin | Type | Phase 2 Value |
|---|---|---|---|
| SRC-Y01 | Google Drive | Documents | Personal docs, EYA/Roberta files |
| SRC-Y02 | Google Calendar | Events | Life timeline, recurring patterns |
| SRC-Y03 | Email | Communications | Relationships, decisions, history |
| SRC-Y04 | YouTube (Watched) | Video | Interests, intellectual diet |
| SRC-Y05 | Web Bookmarks | Curation | External references, intellectual curation |
| SRC-Y06 | Browsing History | Behavioral | Passive interest tracking |
| SRC-Y07 | Voice Memos | Audio | Spontaneous thoughts |
| SRC-Y08 | App Usage Logs | Behavioral | Tool preferences, workflow patterns |

---

## 5. Mem0 — Acquisition Status Note

> **Status: ACQUIRED** — All Mem0 entries have been captured in previous sessions.

Mem0 is a **compressed derivative** of session memory, not a primary source. It serves as:
- A routing aid for cross-session context
- A fast-recall index for agent queries

It does NOT replace primary sources (Manus factsheets, Notion, Obsidian). Its entries are already reflected in the KAP corpus. No ongoing acquisition needed.

**Open question**: Confirm whether all entries are indeed captured or if a delta sync is needed. → To verify at start of THOUGHT-LINE-SEEDING-GATE.

---

## 6. LLM Internal Memory — Extraction Strategy

> **Status: DEFERRED** — Execute at end of Phase 1, once all projects/themes/tags are identified and merged.

LLM internal memory (custom instructions, trained context, memory features) is **partially exportable** via structured prompts. The extraction is most effective when the full KAP taxonomy (projects, themes, tags) is known — allowing batch extraction across all known topics in a single session.

**Extraction approach:**
```text
Batch prompt template (run once per LLM, after taxonomy is complete):
"I will give you a list of projects and themes. For each one, synthesize everything
you know: current state, key decisions, rejected approaches, open questions,
evolution over time. Format: structured Markdown per topic.

Topics: [PROJECT-A], [PROJECT-B], [THEME-X], [THEME-Y], [TAG-Z]..."
```

**Target LLMs** (non-exhaustive — new LLMs added as they accumulate relevant history):
- Claude (Anthropic) — custom instructions + project context
- ChatGPT (OpenAI) — custom instructions + memory feature
- Gemini — workspace context
- Grok — X/web context
- *(future: any LLM with persistent context or memory)*

**Gate required:** `LLM-INTERNAL-MEMORY-EXTRACTION-GATE` — to be executed **after** `THOUGHT-LINE-SEEDING-GATE` (when taxonomy is complete).

---

## 7. Source Registration Protocol

To add a new source to KAP:
1. Add entry to this Catalog with phase classification (`Phase 1 yOS Core`, `Phase 1 Peripheral`, `Phase 2 YOUniverse`).
2. Define acquisition method in `SOURCE-ACTIVATION-POLICY.md`.
3. Build Connector in `02_Source_Acquisition/Connectors/`.
4. Run Pilot Gate.
5. Activate source.
