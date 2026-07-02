# Source Activation Policy

> KAP Source Inventory — Rules for Activating and Orchestrating Sources

## 1. Purpose

Not all sources should feed KAP continuously. This policy governs the state, frequency, and phase scope of source acquisition.

---

## 2. Activation States

| State | Description | Action |
|---|---|---|
| **ON** | Actively acquired | Connector runs per schedule |
| **PAUSED** | Temporarily stopped | Connector disabled, historical data preserved |
| **OFF** | Disabled / deprecated | No acquisition, historical data preserved |
| **TESTING** | Running in isolated sandbox | Output routed to `04_Execution/Dry_Runs/` |
| **ACQUIRED** | One-time bulk acquisition complete | No ongoing acquisition needed |
| **DEFERRED** | Planned but waiting for a prerequisite | Blocked until gate or condition is met |
| **PHASE_2** | Out of scope for Phase 1 | Will be activated in YOUniverse phase |

---

## 3. Orchestration Modes

| Mode | Trigger | Best For | Example |
|---|---|---|---|
| **AUTO_CRON** | Time-based (e.g., daily at 2AM) | Continuous passive sources | GitHub commits |
| **AUTO_HOOK** | Event-based (e.g., on save) | Real-time active sources | Obsidian save, Notion edit |
| **SEMI_AUTO** | Human approval of batch | High-noise sources | Other LLM exports |
| **MANUAL** | Explicit CLI/Agent command | Bulk historical imports | ChatGPT JSON export |
| **PROMPT_EXTRACTION** | Deliberate batch prompt to LLM | LLM internal memory | Batch synthesis after taxonomy complete |

---

## 4. Current Source Matrix

| Source ID | Source | Phase | State | Mode | Prerequisite / Notes |
|---|---|---|---|---|---|
| SRC-001 | Manus Sessions | 1 | ON | MANUAL | 194 done; ongoing for new sessions |
| SRC-002 | Notion | 1 | TESTING | MANUAL | Census in progress |
| SRC-003 | Obsidian | 1 | OFF | AUTO_HOOK | Gate pending |
| SRC-004 | GitHub | 1 | OFF | AUTO_CRON | Acquisition gate pending |
| SRC-005 | ChatGPT | 1 | OFF | MANUAL | Needs export file from user |
| SRC-006 | Mem0 | 1 | ACQUIRED | — | All entries captured |
| SRC-007 | LLM Internal Memory | 1 | **DEFERRED** | PROMPT_EXTRACTION | **Wait for THOUGHT-LINE-SEEDING-GATE** — batch extraction after full taxonomy |
| SRC-008 | Other LLMs | 1 | OFF | MANUAL | Export per platform; new LLMs added over time |
| SRC-F01 | Excalidraw / Figma | 1 | OFF | AUTO_HOOK | Connector TBD |
| SRC-F02 | Specialized AI Tools | 1 | OFF | SEMI_AUTO | Connector TBD |
| SRC-Y01–Y08 | YOUniverse sources | **2** | **PHASE_2** | TBD | Out of scope for Phase 1 |

---

## 5. LLM Internal Memory — Deferred Execution Protocol

```text
TRIGGER: After THOUGHT-LINE-SEEDING-GATE (full taxonomy known)
MODE: PROMPT_EXTRACTION
APPROACH: Single batch session per LLM
PROMPT: "For each of the following projects and themes, synthesize everything
         you know: [full taxonomy list]. Format: structured Markdown per topic."
TARGETS: Claude, ChatGPT, Gemini, Grok + any future LLM with persistent context
GATE: LLM-INTERNAL-MEMORY-EXTRACTION-GATE
```

---

## 6. Noise Prevention Rule

```text
If a source generates >20% noise (fragments rejected during synthesis),
it MUST be downgraded from AUTO to SEMI_AUTO or PAUSED
until the connector filtering is improved.
```

---

## 7. Phase Boundary Rule

```text
Phase 1 (KAP): Only yOS Core and yOS Peripheral sources.
Phase 2 (YOUniverse): All sources including personal/behavioral.

YOUniverse sources (GDrive, Calendar, Email, YouTube, Bookmarks, History, Voice, App logs)
are PHASE_2 only. They are catalogued now for future activation.
They must NOT be activated in Phase 1 without an explicit architect decision.

YOUniverse goal: 360° mega-profile — all data about Yannick, dynamic, continuously updated.
```
