# KAP-ARCH-1: Protocol Registry

**Program:** KAP
**Sprint:** KAP-ARCH-1
**Date:** 2026-07-02

## Overview
This registry captures all durable rules and methods that must guide future KAP work. These are not pipelines (which are operational sequences) but canonical principles and methods that apply across all work packages.

## Protocol Registry

| protocol_id | protocol_name | origin | description | applies_to_wp | canon_status | required_adaptation | owner |
|---|---|---|---|---|---|---|---|
| P-01 | Persistence Gate | WP0-CORE-1 | No knowledge object is considered acquired until it is committed to Git with checksum. Raw data in memory or temp files does not count. | All WPs | CANON_NOW | None | KAP |
| P-02 | Source Cards / Manifests / Checksums | WP2-M8 | Every acquired source must have a source card (MD), an acquisition manifest (JSON), and a checksum. | WP2, WP3 | CANON_NOW | None | KAP |
| P-03 | Git/Markdown as Source of Truth | WP0-CORE-1 | Git is the only durable knowledge repository. Every output must be committed. Obsidian reads from Git. Mem0 receives from Git-derived distillation only. | All WPs | CANON_NOW | None | KAP |
| P-04 | Obsidian as Consultation Layer | KAP-ARCH-1 | Obsidian is not a database. It is the navigation and reading layer over the Git/MD repository. No writes to Obsidian that are not backed by Git. | All WPs | CANON_NOW | None | KAP |
| P-05 | Notion Frozen Legacy / Decommission Rule | KAP-ARCH-1 | Notion is no longer an active repository. It is a frozen legacy source. All new knowledge goes to Git/MD. Notion must be migrated and decommissioned. | WP2-NOTION | CANON_NOW | None | KAP |
| P-06 | Mem0 Semantic-Only Rule | WP0-CORE-1 | Mem0 receives only validated, distilled, semantic memory candidates. Never raw logs, credentials, conversations, or personal datasets. Mem0 injection = WP5 or explicit sprint. | WP5 | CANON_NOW | None | KAP |
| P-07 | Canonical Key Strategy for Deduplication | WP2-M8 | Every source object must have a stable canonical key (uid, checksum, or composite key) to prevent duplicate acquisition and processing. | WP2, WP3 | CANON_NOW | None | KAP |
| P-08 | 9-Layer LLM Knowledge Distillation | WP2-M6 | Raw → Clean → Chunk → Embed → Classify → Extract → Synthesize → Score → Distill. Battle-tested pipeline for knowledge distillation. | WP4 | CANON_NOW | Map to WP4/WP5 | KAP |
| P-09 | LMP v2 Session/Project Card Separation | WP2-M6 | Collection, session cards, project cards, and clustering are separate phases. Never collapse them. Multi-LLM routing per phase. | WP4, WP5 | CANON_NOW | Map to WP4/WP5 | KAP |
| P-10 | Two-Phase Funnel for Personal Data | WP2-M6 | Heuristic filter first (fast, cheap), AI second (precise, expensive). Never apply AI to unfiltered personal data at scale. | WP2-personal | CANON_NOW | Apply to all personal sources | KAP |
| P-11 | Read-Only Unidirectional Sync for Downstream UI | WP2-M6 | YOUniverse UI and any downstream visualization layer is read-only. Sync is unidirectional from Git/MD. No writes from UI back to corpus. | WP6+ | CANON_NOW | None | KAP |
| P-12 | Two-Level Research Protocol | WP2-E2 | Meta-monitoring (what exists, what quality) before extraction. Never extract blindly. | WP2 | CANON_NOW | None | KAP |
| P-13 | Task vs Session Separation | WP2-M8 | Manus tasks ≠ Manus sessions. Wide Research Subtasks are noise. Only human-initiated sessions are corpus. Filter by title pattern. | WP2-MANUS | CANON_NOW | None | KAP |
| P-14 | ZIP = Transport Only | WP2-M8 | ZIP files are transport containers, not knowledge objects. Always extract and commit contents. Never treat ZIP as final storage. | WP2 | CANON_NOW | None | KAP |
| P-15 | Source Lifecycle Management | WP1-R | Every source has a lifecycle: PLANNED → ACTIVE → FROZEN → MIGRATED → DECOMMISSIONED. Managed via Source State Registry. | WP1, WP2 | CANON_NOW | None | KAP |
| P-16 | Project Fact Sheet / Project Delta | KAP-ARCH-1 | Every project must have a living Fact Sheet (MD) capturing state, decisions, blockers, next actions. Delta = what changed since last update. | WP5 | FUTURE_CANON | Define schema first | KAP |
| P-17 | Restricted Secret Surface Rule | WP2-M8 | Secrets, tokens, credentials, API keys are never committed to Git. Never in corpus. Stored in Manus Secrets or 1Password only. | All WPs | CANON_NOW | None | KAP |
| P-18 | No WP3 Before Gates Rule | WP0-CORE-1 | WP3 (normalization) cannot start until WP1 (source inventory), WP2 (acquisition), and architecture gates are all PASS. | WP3 | CANON_NOW | None | KAP |
| P-19 | My Browser Mac-Only Rule | KAP-ARCH-1 | My Browser connector requires Chrome on Mac with active Manus session. iOS and sandbox VM lose session. Playwright cannot control My Browser (no CDP port). | WP2-MANUS | CANON_NOW | Add to Runbook | KAP |
| P-20 | Reuse Before Rebuild | KAP-ARCH-1 | Every existing protocol or pipeline must be classified (ADOPT/ADAPT/REFERENCE/SUPERSEDED/DEPRECATED) before any new build. | All WPs | CANON_NOW | None | KAP |
