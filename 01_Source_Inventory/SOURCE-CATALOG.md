# Source Catalog

> KAP Source Inventory — Master List of All Knowledge Sources

## Source Taxonomy

KAP sources are classified into three scopes:

| Scope | Description | Examples |
|---|---|---|
| **yOS Core** | Contains Y-OS architecture, decisions, projects, intellectual threads | Manus, Notion, Obsidian, GitHub, ChatGPT, LLM Internal |
| **yOS Peripheral** | Contains partial yOS signal mixed with personal/project data | Mem0, Other LLMs |
| **YOUniverse** | Personal life, behavioral, external world — NOT yOS | GDrive, Calendar, Email, YouTube, Browsing history |

> **Rule**: Only `yOS Core` and `yOS Peripheral` sources feed KAP synthesis. `YOUniverse` sources are reserved for a future YOUniverse pipeline and are explicitly out of scope for KAP.

---

## 1. yOS Core Sources

| Source ID | Origin | Type | Format | Status | Connector | Notes |
|---|---|---|---|---|---|---|
| SRC-001 | Manus Sessions | AI Execution | Markdown | **ACTIVE** | `kap_session_archive` | 194 factsheets acquired |
| SRC-002 | Notion (Y-world) | Structured KB | Markdown | **IN_PROGRESS** | `notion_full_census` | Census in progress, 1300+ pages |
| SRC-003 | Obsidian (9 vaults) | Markdown KB | Markdown | **DISCOVERED** | TBD | ~4400+ notes, gate pending |
| SRC-004 | GitHub (yj000018) | Code/Docs | Git/MD | **CATALOGUED** | TBD | 36 repos, acquisition gate pending |
| SRC-005 | ChatGPT | AI Dialogue | JSON | **PLANNED** | TBD | Needs `conversations.json` export |
| SRC-006 | LLM Internal Memory | AI Introspection | Prompted Text | **PLANNED** | Prompt-based extraction | See extraction strategy below |

---

## 2. yOS Peripheral Sources

| Source ID | Origin | Type | Format | Status | Connector | Notes |
|---|---|---|---|---|---|---|
| SRC-007 | Mem0 | Cross-Session Memory | JSON | **ACQUIRED** | Mem0 API | All entries captured — see note below |
| SRC-008 | Other LLMs (Claude, Gemini, Grok) | AI Dialogue | JSON/Text | **PLANNED** | Export per platform | Partial signal — filter for yOS content |

---

## 3. YOUniverse Sources (Out of Scope for KAP)

These sources contain personal life, behavioral, and external world data. They are explicitly excluded from KAP synthesis and reserved for the future YOUniverse pipeline.

| Source ID | Origin | Type | Future Pipeline |
|---|---|---|---|
| SRC-Y01 | Google Drive | Documents | YOUniverse |
| SRC-Y02 | Google Calendar | Events | YOUniverse |
| SRC-Y03 | Email | Communications | YOUniverse |
| SRC-Y04 | YouTube (Watched) | Video | YOUniverse |
| SRC-Y05 | Web Bookmarks | Curation | YOUniverse |
| SRC-Y06 | Browsing History | Behavioral | YOUniverse |
| SRC-Y07 | Voice Memos | Audio | YOUniverse |

---

## 4. Future yOS Sources (Activatable)

Sources that may contain yOS-relevant knowledge and can be activated when ready.

| Source ID | Origin | Type | Format | Status | Notes |
|---|---|---|---|---|---|
| SRC-F01 | Excalidraw / Figma / Spline | Visual | SVG/JSON/MD | **IDEA** | Architecture schemas, visual thought lines — high yOS signal |
| SRC-F02 | Specialized AI Tool Outputs | AI Output | JSON/MD | **IDEA** | Outputs from specific research agents, graph generators |

---

## 5. Mem0 — Acquisition Status

> **Status: ACQUIRED** — All Mem0 entries have been captured in previous sessions.

Mem0 is a compressed derivative of session memory — it is not a primary source. It serves as:
- A routing aid for cross-session context
- A fast-recall index for agent queries
- A secondary validation layer for synthesis

It does NOT replace primary sources (Manus factsheets, Notion, Obsidian). Its entries are already reflected in the KAP corpus.

---

## 6. LLM Internal Memory — Extraction Strategy

> **Status: PLANNED** — Extractable via structured prompting.

LLM internal memory (custom instructions, system prompts, trained context) is partially exportable through deliberate extraction prompts:

```text
Extraction prompt template:
"Synthesize everything you know about [PROJECT / THEME / DECISION].
Include: current state, key decisions, rejected approaches, open questions, evolution over time.
Format: structured Markdown with sections."
```

**Target LLMs for extraction:**
- Claude (Anthropic) — custom instructions + project context
- ChatGPT (OpenAI) — custom instructions + memory feature
- Gemini — workspace context
- Grok — X/web context

**Gate required:** `LLM-INTERNAL-MEMORY-EXTRACTION-GATE`

---

## 7. Source Registration Protocol

To add a new source to KAP:
1. Add entry to this Catalog with scope classification (`yOS Core`, `yOS Peripheral`, or `YOUniverse`).
2. Define acquisition method in `SOURCE-ACTIVATION-POLICY.md`.
3. Build Connector in `02_Source_Acquisition/Connectors/`.
4. Run Pilot Gate.
5. Activate source.
