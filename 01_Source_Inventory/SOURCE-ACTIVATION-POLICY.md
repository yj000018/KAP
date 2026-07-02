# Source Activation Policy

> KAP Source Inventory — Rules for Activating and Orchestrating Sources

## 1. Purpose

Not all sources should feed KAP continuously. Some require manual triggering, others run on cron jobs, and some are paused to prevent noise. This policy governs the state and frequency of source acquisition.

## 2. Activation States

| State | Description | Action |
|---|---|---|
| **ON** | Source is actively acquired | Connector runs according to Schedule |
| **PAUSED** | Acquisition temporarily stopped | Connector disabled, historical data preserved |
| **OFF** | Source disabled or deprecated | No acquisition, historical data preserved |
| **TESTING** | Source running in isolated sandbox | Output routed to `04_Execution/Dry_Runs/` |

## 3. Orchestration Modes

| Mode | Trigger | Best For | Example |
|---|---|---|---|
| **AUTO_CRON** | Time-based (e.g., daily at 2AM) | Continuous passive sources | Browsing history, GitHub commits |
| **AUTO_HOOK** | Event-based (e.g., on save) | Real-time active sources | Obsidian save, Notion page edit |
| **SEMI_AUTO** | Human approval of batch | High-noise sources | Web bookmarks, YouTube history |
| **MANUAL** | Explicit CLI/Agent command | Bulk historical imports | ChatGPT export JSON |

## 4. Current Source Matrix

| Source ID | Source | State | Mode | Frequency | Filters/Conditions |
|---|---|---|---|---|---|
| SRC-001 | Manus Sessions | ON | MANUAL | On demand | Exclude pure code-execution tasks |
| SRC-002 | Notion | TESTING | MANUAL | On demand | Target specific ROOTs only |
| SRC-003 | Obsidian | OFF | AUTO_HOOK | TBD | Only folders outside `_drafts` |
| SRC-004 | GitHub | OFF | AUTO_CRON | Daily | Exclude `noise` domain repos |

## 5. Future Source Guidelines

When adding a future source (e.g., YouTube, Excalidraw):
1. **Start in MANUAL mode** to assess noise ratio.
2. **Move to SEMI_AUTO** to train the filtering logic.
3. **Graduate to AUTO_CRON/HOOK** only when confidence is >95% that the connector extracts pure knowledge without garbage.

## 6. Noise Prevention Rule

```text
If a source generates >20% noise (fragments rejected during synthesis), it MUST be downgraded from AUTO to SEMI_AUTO or PAUSED until the connector filtering is improved.
```
