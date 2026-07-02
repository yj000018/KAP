# KAP-ARCH-1: Pipeline Registry

**Program:** KAP
**Sprint:** KAP-ARCH-1
**Date:** 2026-07-02

## Overview
This registry identifies all known existing or planned pipelines within the KAP/yOS ecosystem. It establishes the current status and reuse decisions for each pipeline before any new ingestion begins.

## Pipeline Registry

| pipeline_id | pipeline_name | purpose | source_types | output_target | tested_status | current_status | reuse_decision | required_adaptation | next_action |
|---|---|---|---|---|---|---|---|---|---|
| PL-01 | KAP Core Engine 5-Block | Central acquisition and routing backbone | All Sources | Git/MD | DESIGNED_NOT_TESTED | ACTIVE_CANON | ADOPT_AS_CANON | None | Implement in WP2 |
| PL-02 | 9-Layer LLM Knowledge Distillation | Deep distillation of raw text to semantic knowledge | Raw Text, MD | Distilled MD | BATTLE_TESTED | ACTIVE_CANON | ADOPT_AS_CANON | Map to WP4/WP5 | Use for WP4 |
| PL-03 | LMP v2 (Multi-LLM) | Generate session/project cards and cluster themes | Sessions, Projects | Fact Sheets | BATTLE_TESTED | ACTIVE_CANON | ADOPT_AS_CANON | Map to WP4/WP5 | Use for WP5 |
| PL-04 | yOS Memory Bridge | iOS/Shortcut capture to Mem0 via Webhook | Voice, Text | Mem0 | BATTLE_TESTED | ACTIVE_CANON | ADOPT_AS_CANON | Enforce semantic-only | Maintain |
| PL-05 | Mem0 Sync Pipeline | Push distilled memory candidates to Mem0 | Memory Candidates | Mem0 | BATTLE_TESTED | ACTIVE_CANON | ADOPT_AS_CANON | None | Run in WP5 |
| PL-06 | ChatGPT2Notion | Legacy sync of ChatGPT conversations to Notion | ChatGPT | Notion | LEGACY_ONLY | DEPRECATED | DEPRECATED | Replace with Git/MD | Do not use |
| PL-07 | Notion-to-Git Migration | Migrate frozen legacy Notion corpus to Git | Notion | Git/MD | DESIGNED_NOT_TESTED | FUTURE_PIPELINE | ADOPT_AS_CANON | None | Schedule WP2-NOTION |
| PL-08 | Manus Session Archive Pipeline | Extract, distill, and commit Manus sessions | Manus Sessions | Git/MD | TESTED_ON_REAL_DATA | ACTIVE_CANON | ADOPT_AS_CANON | Use My Browser Mac | Run bulk archive |
| PL-09 | GitHub Repo Acquisition | Clone and map GitHub repositories | GitHub Repos | Git/MD | TESTED_PARTIALLY | ACTIVE_CANON | ADOPT_AS_CANON | None | Schedule WP2-GITHUB |
| PL-10 | Obsidian Vault Indexing | Build navigation and backlinks over Git/MD | Git/MD | Obsidian | DESIGNED_NOT_TESTED | FUTURE_PIPELINE | ADOPT_AS_CANON | None | Schedule WP3 |
| PL-11 | Project Fact Sheet Pipeline | Generate living state cards for projects | Sessions, Artifacts | Git/MD | DESIGNED_NOT_TESTED | FUTURE_PIPELINE | ADOPT_AS_CANON | Define schema | Schedule WP5 |
| PL-12 | YOUniverse MVP1 Sync | Unidirectional sync to visualization layer | Git/MD | Web UI | BATTLE_TESTED | ACTIVE_CANON | ADOPT_AS_CANON | Move to Phase 3 | Defer to Phase 3 |
| PL-13 | Gmail 2-Phase Funnel | Heuristic filter then AI extraction for emails | Emails | Git/MD | BATTLE_TESTED | ACTIVE_CANON | ADOPT_AS_CANON | Apply to all personal | Defer to Phase 3 |
| PL-14 | Sensor Telemetry Pipeline | Ingest IoT/Home Assistant logs | Telemetry | Git/MD | DESIGNED_NOT_TESTED | FUTURE_PIPELINE | ADOPT_AS_CANON | None | Defer to Phase 4 |
| PL-15 | Two-Level Research Protocol | Meta-monitoring before extraction | Web, APIs | Git/MD | BATTLE_TESTED | ACTIVE_CANON | ADOPT_AS_CANON | None | Use in WP2 |
| PL-16 | Source Connector Lifecycle | Activate/deactivate connectors safely | Connectors | Registry | DESIGNED_NOT_TESTED | ACTIVE_CANON | ADOPT_AS_CANON | None | Use in WP1 |
