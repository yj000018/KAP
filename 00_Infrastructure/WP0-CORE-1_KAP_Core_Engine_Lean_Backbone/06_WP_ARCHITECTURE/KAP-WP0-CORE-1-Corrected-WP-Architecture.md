# Corrected Work Package Architecture

**Sprint:** WP0-CORE-1
**Generated:** 2026-07-02

## 1. Canonical Structure

```text
WP0 — Infrastructure / Backbone / Protocols / Gates
WP1 — Source Inventory / Source Registry / Freeze Map
WP2 — Source Acquisition by Branch
  WP2-MANUS
  WP2-CHATGPT
  WP2-CLAUDE
  WP2-GEMINI
  WP2-GROK
  WP2-PERPLEXITY
  WP2-NOTION
  WP2-MEM0
  WP2-GITHUB
  WP2-OBSIDIAN
  WP2-LOCAL-FILES
  WP2-WEBSITES
  WP2-LOGS-TELEMETRY
  WP2-HOME-AUTOMATION
  WP2-OTHER
WP3 — Normalization / Structuring / Deduplication
WP4 — Knowledge Distillation / Memory Candidates
WP5 — KAP-to-Mem0 Instillation
WP6 — Retrieval Tests / yOS Memory Validation
WP7 — Canonization / Ontology / KOSMOS-yOS Integration
WP8 — Autonomous yOS Knowledge Consolidation Loop
```

## 2. Operational Rules

- WP2 is branch-based, not monolithic. A failure in `WP2-NOTION` does not block `WP2-MANUS`.
- Each source branch can be in one of these states: baseline-captured, frozen, deferred, or delta-ready.
- WP3 starts **only** after selected source branches are closed or explicitly frozen.
- New sources can be added later without redesigning the architecture.
