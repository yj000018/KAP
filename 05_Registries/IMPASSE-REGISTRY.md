# Impasse Registry

> KAP Evolutionary Knowledge Merge — Dead Ends, Traps, and Rejected Approaches

## Purpose

Preserve dead ends, bad approaches, traps, and rejected models so they are never repeated. Each impasse is negative knowledge — as valuable as positive knowledge for preventing wasted effort.

## Registry

| Impasse ID | Impasse | Why It Fails | Replaced By | Status | Evidence | Risk If Repeated |
|---|---|---|---|---|---|---|
| IMP-001 | Using ZIP as primary corpus | Loses provenance, not git-friendly, not Obsidian-compatible, not searchable | Git/Markdown-first persistence | confirmed | KAP-ARCH-1-PATCH | HIGH — would require re-extraction |
| IMP-002 | Treating Manus tasks as flat primary corpus | Tasks are execution traces, not knowledge — noise ratio too high (178/200 = subtasks) | Factsheet extraction + durable output detection | confirmed | Pipeline census, MANUS-SESSION-CENSUS | MEDIUM — would pollute knowledge graph |
| IMP-003 | Importing everything before architecture | Creates unmanageable corpus, no structure to receive data, impossible to normalize later | Architecture-before-extraction (gate sequence) | confirmed | All gates enforce this | HIGH — would require restart |
| IMP-004 | Deduplicating without preserving chronology | Loses evolution history, destroys thought lines, erases why decisions changed | DEDUPLICATION-AND-MERGE-POLICY | confirmed | Architecture decision | HIGH — irreversible knowledge loss |
| IMP-005 | Normalizing before provenance | Loses source attribution, makes claims unverifiable, breaks trust chain | Source Fragment Layer (provenance-first) | confirmed | Architecture decision | HIGH — unrecoverable |
| IMP-006 | Merging Notion blindly | Workspace has 1300+ pages, many are noise/drafts/abandoned — blind merge = noise amplification | Controlled census → pilot → selective acquisition | confirmed | NOTION-PIPELINE-CONTROLLED-EXECUTION-GATE | MEDIUM — would require cleanup |
| IMP-007 | Treating memory (Mem0) as source of truth | Memory is a compressed derivative, not a primary source — it loses nuance and context | Memory as routing/recall aid, sources as truth | confirmed | Architecture decision | MEDIUM — would create false confidence |
| IMP-008 | Collapsing old and new approaches without supersession logic | Loses the "why" of evolution, makes decisions appear arbitrary | CONTRADICTION-AND-SUPERSESSION-POLICY | confirmed | Architecture decision | HIGH — destroys decision intelligence |
| IMP-009 | JS script for Manus UID extraction (DOM-based) | Manus is a React SPA — no `<a href>` in DOM, `querySelectorAll` returns undefined | API-based extraction with cursor pagination | confirmed | Multiple failed attempts, RUNBOOK v1.2 | LOW — documented in RUNBOOK |
| IMP-010 | Hardcoding API keys in committed files | GitHub push protection rejects, secrets exposed | .env + 1Password + .gitignore | confirmed | Push rejection incident 2026-07-03 | HIGH — security breach |
| IMP-011 | Using Notion session tokens (ntn_) with API | Session tokens are web-only, return 401 on API calls | Integration token via my-integrations page | confirmed | Multiple 401 failures | LOW — documented |
| IMP-012 | Activating 100 Manus connectors simultaneously | Credit overhead, routing conflicts, no benefit for unused connectors | Core 8-10 connectors profile | confirmed | Architect decision 2026-07-03 | MEDIUM — credit waste |

## Statuses

```text
confirmed — validated dead end, never repeat
suspected — likely dead end, needs more evidence
mitigated — was a problem, now has workaround
historical — was relevant in old context, no longer applicable
```

## Rules

1. An impasse is never deleted
2. New impasses are added whenever a failed approach is identified
3. Each impasse must explain WHY it fails, not just THAT it fails
4. "Replaced By" must point to the current working approach
5. Risk If Repeated guides future agents away from the trap
