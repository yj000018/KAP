# KAP Core Backbone Specification

**Program:** KAP — Knowledge Assimilation Program
**Sprint:** WP0-ENG-1
**Status:** Canonical Reference

## 3.1 Purpose

KAP is the **acquisition, preservation, normalization, distillation, and memory-instillation layer** of yOS.
It is not a one-time extraction script. It is the durable, delta-ready engineering backbone that allows yOS to continuously assimilate knowledge from any source (APIs, UI, local files, logs, home automation) into a unified, version-controlled, and actively queryable memory structure (Mem0/Notion) without losing provenance or creating duplication.

## 3.2 Core Invariants

To guarantee absolute data integrity and process scalability, KAP enforces the following invariants:

1. **No synthesis before acquisition proof:** Source data must be verifiably captured and committed to Git before any summarization or structuring begins.
2. **No canonization before normalization:** Raw data must pass through standard schemas before being merged into the civilizational ontology.
3. **Git/KAP is the source of truth:** All raw and normalized data lives in the Git repository. Notion and Mem0 are projections of this truth.
4. **ZIPs are transport only:** ZIP files and manual exports are transport mechanisms, not durable storage formats. Their contents must be unpacked and tracked in Git.
5. **Every item must have provenance:** Source cards (`_SOURCE_CARD.md`), manifests, and checksums must accompany every acquired asset.
6. **Every output must pass a persistence gate:** Nothing is considered "done" until it is proven to be tracked, committed, and pushed to the remote repository.
7. **Source branches can advance independently:** Different sources (e.g., Manus vs. Notion) can be at different stages of the KAP pipeline without blocking each other.
8. **Deltas must compare against prior state:** Future acquisitions must only process the delta (new or changed data) compared to the last known state registry, avoiding full re-ingestion.
9. **Mem0 is active distilled memory, not raw corpus:** Mem0 stores highly concentrated, associative memory vectors, not the raw chat transcripts or full documents.
10. **Notion is hub/navigation/archive, not sole source of truth:** Notion provides the UI and relational database for human and AI navigation, but the underlying data is backed by Git.
11. **UI/manual fallbacks are valid but must be documented:** When APIs fail, manual UI extraction is permitted, provided the method is documented in a runbook and the data enters the same Git-backed pipeline.

## 3.3 System Layers

KAP is structured as a pipeline of independent, sequential layers. Data flows unidirectionally through these layers.

| Layer | Role | Examples / Outputs |
|---|---|---|
| **0. Source Layer** | The origin of the knowledge. | Manus, ChatGPT, Notion, GitHub, Obsidian, Local Files, Websites, Telemetry. |
| **1. Acquisition Layer** | Fetching raw data from sources via API or UI fallback. | `sessions.json`, `verbatim.md`, ZIP exports, `_SOURCE_CARD.md`, checksums. |
| **2. Preservation Layer** | Storing raw data immutably in Git with provenance. | `git commit`, `manifest.json`, `SHA256_manifest.md`. |
| **3. Normalization Layer** | Converting raw, heterogeneous data into standard yOS schemas. | `session_card.json`, `normalized_markdown.md`, deduplication logs. |
| **4. Distillation Layer** | Extracting high-value concepts, decisions, and context. | Executive summaries, theme extraction, entity recognition. |
| **5. Active Memory Layer** | Pushing distilled knowledge to queryable vector/relational stores. | Mem0 API calls, Notion Database sync scripts. |
| **6. Canonization Layer** | Merging validated knowledge into the Elysium Civilizational Ontology. | Updates to `Y-WORLD` Obsidian vault, ADRs, `concepts/`. |
| **7. Automation/yOS Loop** | Autonomous scheduling of the entire pipeline for future deltas. | Cron jobs, webhooks, n8n workflows, yOS telemetry triggers. |
