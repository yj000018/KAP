# KAP-ARCH-1: Roadmap Reset & Gates

**Program:** KAP
**Sprint:** KAP-ARCH-1
**Date:** 2026-07-02

## Overview
This document resets the KAP roadmap based on the consolidated architecture and defines the strict gates that must be passed before advancing to subsequent phases.

## 1. Roadmap Reset

The roadmap is divided into 4 sequential phases. No phase can begin until the previous phase's Completion Gate is passed.

### Phase 1: System Knowledge Consolidation (Current)
**Goal:** Acquire and structure all existing knowledge about yOS, KAP, and active projects.
- WP1: Source Inventory & Reconciliation (Complete)
- WP2-MANUS: Archive all Manus sessions (In Progress)
- WP2-NOTION: Migrate legacy Notion corpus to Git
- WP2-GITHUB: Map existing GitHub repositories
- WP3: Obsidian Vault Indexing (Navigation layer)

### Phase 2: Active Memory Integration
**Goal:** Connect the distilled system knowledge to Mem0 for agent autonomy.
- WP4: Knowledge Distillation (run existing 9-layer pipeline on Git corpus)
- WP5: Mem0 Injection (push distilled candidates to Mem0)
- WP6: Agent Retrieval Tests

### Phase 3: YOUniverse (Personal Data)
**Goal:** Expand KAP to acquire personal data and feed the YOUniverse visualization layer.
- Activate Readwise, YouTube, Emails, Calendar connectors.
- Implement 2-Phase Funnel for personal data.
- Map outputs to 7-Domain Model.

### Phase 4: Telemetry & Autonomy
**Goal:** Continuous ingestion of sensor data and fully autonomous execution loops.
- Activate Home Assistant and sensor pipelines.
- Implement WP8 (Autonomous Loop).

## 2. Gates

### Gate 1: Phase 1 Readiness (ACTIVE)
- [x] KAP Core Engine Backbone Defined
- [x] Source State Registry Created
- [x] Protocol Registry Consolidated
- [ ] Manus Session Archive Complete (Blocked by My Browser Mac collection)
- [ ] Notion Migration Complete

### Gate 2: WP3 Entry Gate (PENDING)
WP3 (Normalization/Obsidian Indexing) cannot begin until:
- All WP2 acquisition tasks for System Knowledge (Manus, Notion, GitHub) are complete.
- No raw, uncommitted data exists in temp folders.

### Gate 3: Mem0 Injection Gate (PENDING)
WP5 (Mem0 Injection) cannot begin until:
- WP4 distillation has produced valid Memory Candidate JSONs.
- Manual review of the first batch of candidates is complete to ensure the "Semantic-Only Rule" is respected.
