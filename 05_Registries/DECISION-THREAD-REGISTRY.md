# Decision Thread Registry

> KAP Evolutionary Knowledge Merge — Tracked Decisions, Reversals, and Rationale

## Purpose

Track all architectural and operational decisions made during KAP construction. Each decision preserves its rationale, alternatives rejected, and supersession chain.

## Registry

| Decision ID | Decision | Status | Domain | Supersedes | Superseded By | Evidence | Review Needed | Notes |
|---|---|---|---|---|---|---|---|---|
| DEC-001 | Git/Markdown-first persistence is mandatory | active | architecture | — | — | All gates enforce this | NO | Canonical since STRUCTURE-GATE |
| DEC-002 | ZIP is not primary corpus format | active | source_policy | — | — | KAP-ARCH-1-PATCH | NO | Explicit rejection |
| DEC-003 | Connector design before acquisition | active | gate_policy | — | — | CONNECTOR-DESIGN-GATE | NO | Architecture before extraction |
| DEC-004 | WP3 broad acquisition blocked until explicit gate | active | gate_policy | — | — | All gate reports | NO | No uncontrolled acquisition |
| DEC-005 | Manus tasks are not flat primary corpus | active | source_policy | — | — | KAP-ARCH-1-PATCH, No-Extraction-Policy | NO | Tasks = execution traces, not knowledge |
| DEC-006 | Notion canonical merge blocked until review | active | source_policy | — | — | PIPELINE-FEASIBILITY-GATE | YES | Awaiting NOTION-RECONCILIATION-GATE |
| DEC-007 | Obsidian real vault scan blocked until dry-run gate | active | source_policy | — | — | OBSIDIAN-PIPELINE-PATCH-GATE | NO | Fake vault validated first |
| DEC-008 | One Notion token for all Y-OS (KAP-Executor) | active | security | — | — | 1Password stored, API validated | NO | Universal access via single integration |
| DEC-009 | Manus API key stored in .env, never in git | active | security | DEC-old-hardcoded | — | Push rejection incident | NO | Learned from push failure |
| DEC-010 | 1Password as central secrets vault for Y-OS | active | security | — | — | op CLI installed, tokens stored | NO | Single source of truth for credentials |
| DEC-011 | Never auto-resolve contradictions | active | merge_policy | — | — | CONTRADICTION-AND-SUPERSESSION-POLICY.md | NO | Human review required |
| DEC-012 | Never delete historical variants during dedup | active | merge_policy | — | — | DEDUPLICATION-AND-MERGE-POLICY.md | NO | Preserve evolution |
| DEC-013 | Kim Jimenez = primary Notion account (not Yannick) | active | architecture | — | — | Architect decision 2026-07-03 | NO | Y-world workspace under Kim |
| DEC-014 | 5 ROOT pages in Notion for centralized access | active | architecture | — | — | Architect action 2026-07-03 | NO | KOSMOS, Y-OS, ELYSIUM, Y-WORLD, YANNICK |

## Decision Statuses

```text
proposed → accepted → active → superseded → rejected → deprecated → under_review
```

## Rules

1. Every decision must have a rationale
2. Superseded decisions are never deleted — they become negative knowledge
3. Reversals must document why the old decision was wrong
4. Implementation evidence outweighs conceptual proposals
