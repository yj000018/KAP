# Source Activation Policy

> KAP Source Inventory — Rules for Activating and Orchestrating Sources

## 1. Purpose

Not all sources should feed KAP continuously. Some require manual triggering, others run on cron jobs, and some are paused to prevent noise. This policy governs the state and frequency of source acquisition.

**Scope rule**: Only `yOS Core` and `yOS Peripheral` sources are activated in KAP. `YOUniverse` sources (GDrive, Calendar, Email, YouTube, Browsing history) are explicitly excluded and reserved for a future YOUniverse pipeline.

---

## 2. Activation States

| State | Description | Action |
|---|---|---|
| **ON** | Source is actively acquired | Connector runs according to Schedule |
| **PAUSED** | Acquisition temporarily stopped | Connector disabled, historical data preserved |
| **OFF** | Source disabled or deprecated | No acquisition, historical data preserved |
| **TESTING** | Source running in isolated sandbox | Output routed to `04_Execution/Dry_Runs/` |
| **ACQUIRED** | One-time bulk acquisition complete | Historical data in KAP, no ongoing acquisition needed |

---

## 3. Orchestration Modes

| Mode | Trigger | Best For | Example |
|---|---|---|---|
| **AUTO_CRON** | Time-based (e.g., daily at 2AM) | Continuous passive sources | GitHub commits |
| **AUTO_HOOK** | Event-based (e.g., on save) | Real-time active sources | Obsidian save, Notion edit |
| **SEMI_AUTO** | Human approval of batch | High-noise sources | Other LLM exports |
| **MANUAL** | Explicit CLI/Agent command | Bulk historical imports | ChatGPT JSON export |
| **PROMPT_EXTRACTION** | Deliberate prompt to LLM | LLM internal memory | "Synthesize what you know about X" |

---

## 4. Current Source Matrix

| Source ID | Source | Scope | State | Mode | Notes |
|---|---|---|---|---|---|
| SRC-001 | Manus Sessions | yOS Core | ON | MANUAL | 194 factsheets done; ongoing for new sessions |
| SRC-002 | Notion | yOS Core | TESTING | MANUAL | Census in progress |
| SRC-003 | Obsidian | yOS Core | OFF | AUTO_HOOK | Gate pending |
| SRC-004 | GitHub | yOS Core | OFF | AUTO_CRON | Acquisition gate pending |
| SRC-005 | ChatGPT | yOS Core | OFF | MANUAL | Needs export file |
| SRC-006 | LLM Internal Memory | yOS Core | OFF | PROMPT_EXTRACTION | Gate to be defined |
| SRC-007 | Mem0 | yOS Peripheral | **ACQUIRED** | — | All entries captured, no ongoing acquisition |
| SRC-008 | Other LLMs | yOS Peripheral | OFF | MANUAL | Export per platform |

---

## 5. Noise Prevention Rule

```text
If a source generates >20% noise (fragments rejected during synthesis),
it MUST be downgraded from AUTO to SEMI_AUTO or PAUSED
until the connector filtering is improved.
```

---

## 6. YOUniverse Exclusion Rule

```text
GDrive, Calendar, Email, YouTube, Web Bookmarks, Browsing History, Voice Memos
are EXPLICITLY OUT OF SCOPE for KAP.
They contain no yOS architecture knowledge.
They are reserved for the future YOUniverse pipeline.
Never activate these sources in KAP without an explicit architect decision.
```
