# Source Registry System

> KAP — Modular Knowledge Acquisition Engine

## 1. Core Principle

**One engine. Multiple scopes. One destination per fragment.**

KAP is not a pipeline for yOS only. It is a universal knowledge acquisition engine that processes any source and routes each fragment to the correct destination based on its scope classification. The same engine logic — acquire → fragment → classify → route → synthesize — applies regardless of whether the source is a Manus session, a YouTube transcript, or a Google Calendar event.

```
Source → Connector → Source Fragment → Scope Classifier → Destination
                                              │
                              ┌───────────────┼───────────────┐
                              ▼               ▼               ▼
                           yOS KB        YOUniverse      Both (cross-scope)
                        (architecture)   (360° profile)  (e.g., "I decided to
                                                          use Notion for yOS")
```

> **Key insight**: A fragment about "how Yannick thinks about AI" belongs to **both** yOS KB (cognitive architecture) and YOUniverse (personal profile). The engine does not force a binary choice — it tags fragments with one or more scope labels.

---

## 2. Scope Model

| Scope | ID | Description | Destination | Current Phase |
|---|---|---|---|---|
| **yOS** | `scope:yos` | Y-OS architecture, decisions, tools, projects, intellectual threads | KAP synthesis → Obsidian yOS graph | **ACTIVE** |
| **YOUniverse** | `scope:youniverse` | Personal facts, behaviors, preferences, life events, external world | YOUniverse synthesis → Obsidian YOUniverse graph | **FUTURE** |
| **Cross-scope** | `scope:both` | Fragments that contain signal for both scopes | Both destinations | Classified at extraction time |

Scopes are **tags on fragments**, not separate pipelines. The engine is identical.

---

## 3. Source Lifecycle

Every source follows the same lifecycle regardless of scope:

```
discovered → catalogued → connector_designed → configured → testing → active → paused → deprecated
```

---

## 4. Modular Components

### 4.1 Source Catalog (`SOURCE-CATALOG.md`)
Master list of all sources — active, planned, future — with scope classification.

### 4.2 Connectors (`02_Source_Acquisition/Connectors/`)
Isolated scripts that pull from a source and output standard `source_fragment.schema.json`. Connectors do not synthesize — they only acquire and format.

### 4.3 Activation Policy (`SOURCE-ACTIVATION-POLICY.md`)
Defines state (ON/OFF/DEFERRED…), mode (AUTO/MANUAL/PROMPT_EXTRACTION…), and filters per source.

### 4.4 Scope Classifier
A lightweight classification step applied to each fragment at acquisition time. Rules:
- If fragment contains yOS architecture, decisions, tools, or projects → `scope:yos`
- If fragment contains personal facts, behaviors, or life events → `scope:youniverse`
- If both → `scope:both`
- Classification can be manual (human tag), rule-based (keyword), or AI-assisted

---

## 5. Destination Routing

| Scope Tag | Synthesis Target | Obsidian Graph | Current Status |
|---|---|---|---|
| `scope:yos` | KAP Thought Lines, Decision Threads, CBK | yOS graph | ACTIVE |
| `scope:youniverse` | YOUniverse Profile, Life Timeline, Preferences | YOUniverse graph | FUTURE |
| `scope:both` | Both synthesis targets | Both graphs | FUTURE |

---

## 6. Rules

1. **One engine** — never fork the pipeline for different scopes. Add scope tags instead.
2. **No direct injection** — every source passes through a Connector before entering the fragment layer.
3. **State independence** — pausing a source does not delete its historical fragments.
4. **Traceability** — every fragment carries its Source ID, Connector Version, and Scope Tags.
5. **Noise control** — if >20% of fragments from a source are rejected, downgrade acquisition mode.
6. **Phase discipline** — YOUniverse sources are catalogued now but connectors are not built until Phase 2 is formally opened.
