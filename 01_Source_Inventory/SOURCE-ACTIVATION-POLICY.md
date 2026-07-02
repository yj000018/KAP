# Source Activation Policy

> KAP Source Registry — Activation States, Modes, and Rules

## 1. Activation States

| State | Description |
|---|---|
| **ON** | Actively acquired — connector runs per schedule |
| **PAUSED** | Temporarily stopped — historical data preserved |
| **OFF** | Disabled — no acquisition, historical data preserved |
| **TESTING** | Isolated sandbox — output to `04_Execution/Dry_Runs/` |
| **ACQUIRED** | One-time bulk acquisition complete — no ongoing acquisition needed |
| **DEFERRED** | Planned but waiting for a prerequisite gate or condition |
| **CATALOGUED** | Registered, connector not yet built |

---

## 2. Orchestration Modes

| Mode | Trigger | Best For |
|---|---|---|
| **AUTO_CRON** | Time-based (e.g., daily 2AM) | Continuous passive sources (GitHub commits) |
| **AUTO_HOOK** | Event-based (on save, on edit) | Real-time sources (Obsidian, Notion) |
| **SEMI_AUTO** | Human approval of batch | High-noise sources (LLM exports) |
| **MANUAL** | Explicit CLI/Agent command | Bulk historical imports (ChatGPT JSON) |
| **PROMPT_EXTRACTION** | Deliberate batch prompt to LLM | LLM internal memory (after taxonomy complete) |

---

## 3. Current Source Matrix

| Source ID | Source | Scope | State | Mode | Prerequisite / Notes |
|---|---|---|---|---|---|
| SRC-001 | Manus Sessions | `scope:yos` | ON | MANUAL | 194 done; ongoing for new sessions |
| SRC-002 | Notion | `scope:yos` | TESTING | MANUAL | Census in progress |
| SRC-003 | Obsidian | `scope:yos` | OFF | AUTO_HOOK | Gate pending |
| SRC-004 | GitHub | `scope:yos` | OFF | AUTO_CRON | Acquisition gate pending |
| SRC-005 | ChatGPT | `scope:both` | OFF | MANUAL | Needs export file from user |
| SRC-006 | Mem0 | `scope:yos` | ACQUIRED | — | All entries captured |
| SRC-007 | LLM Internal Memory | `scope:both` | DEFERRED | PROMPT_EXTRACTION | After THOUGHT-LINE-SEEDING-GATE |
| SRC-008 | Other LLMs | `scope:both` | OFF | MANUAL | Open-ended list |
| SRC-F01 | Excalidraw / Figma | `scope:yos` | OFF | AUTO_HOOK | Connector TBD |
| SRC-F02 | Specialized AI Tools | `scope:yos` | OFF | SEMI_AUTO | Connector TBD |
| SRC-Y01–Y08 | YOUniverse sources | `scope:youniverse` | CATALOGUED | TBD | Connectors built when Phase 2 opens |

---

## 4. Noise Prevention Rule

```text
If a source generates >20% noise (fragments rejected during synthesis),
downgrade from AUTO to SEMI_AUTO or PAUSED until connector filtering improves.
```

---

## 5. Cross-Scope Fragments

```text
Some fragments belong to both scopes (e.g., "I decided to use Notion for yOS").
These are tagged scope:both and routed to both synthesis targets.
The classifier (manual, rule-based, or AI-assisted) handles this at extraction time.
No fragment is forced into a single scope if it genuinely spans both.
```
