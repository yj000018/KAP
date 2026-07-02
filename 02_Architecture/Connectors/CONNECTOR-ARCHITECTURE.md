# KAP Connector Architecture

**Version:** 1.0  
**Gate:** CONNECTOR-DESIGN-GATE  
**Status:** Canonical  

## Overall Connector Philosophy

KAP is an assimilation engine, not a scraping bot. Connectors exist to transform external entropy into canonical Git/Markdown structures. 
A connector is defined by its contract, not just its script. Acquisition is strictly gated and must never occur without explicit authorization per source.

## Source Categories

1. **Manus:** Execution/control-plane history. Not a primary corpus unless durable outputs are identified.
2. **ChatGPT / OpenAI:** Project conversations, generated artifacts, strategic context.
3. **Notion:** Structured pages, databases, legacy knowledge bases.
4. **Obsidian / Local Vaults:** Primary durable knowledge.
5. **Google Drive / Docs / Sheets:** Cloud documents and structured files.
6. **Mem0 / Memory Systems:** Compressed state, lower evidential confidence.
7. **Git / Repositories:** Canonical persistence layer.
8. **External URLs / Web:** Controlled reference ingestion, strictly whitelisted.

## Connector Lifecycle

1. **Discovery:** Source identified and added to Connector Backlog.
2. **Design:** Connector contract drafted and validated.
3. **Implementation Gate:** Script/API integration built and tested on sample data.
4. **Acquisition Gate:** Full extraction authorized.
5. **Normalization Gate:** Raw data converted to canonical Markdown.
6. **Distillation:** Normalized data processed into Mem0 candidates.

## Acquisition Boundary

Connectors must respect the acquisition boundary:
- Connectors extract data into `02_Source_Acquisition/`.
- Connectors DO NOT write directly to `03_Normalized_Knowledge/` or `04_Distillation/`.
- Connectors MUST preserve original metadata, timestamps, and source URLs.

## Validation Gates & Human Approval Points

- **CONNECTOR-DESIGN-GATE:** Validates the architecture and contracts (Current).
- **CONNECTOR-IMPLEMENTATION-GATE:** Validates the extraction code.
- **PHASE-1-SEED-PLAN:** Human Architect approves the exact scope of extraction.
- **TARGETED-WP2-SOURCE-SPRINTS:** Human Architect authorizes execution per source.

## Error Handling & Git Persistence

- Connectors must implement staggered retries (K5 policy).
- All durable outputs must be Markdown or JSON.
- No ZIP files as primary corpus.
- All extracted files must be committed to the KAP Git repository.
- Connectors must verify file placement in the KAP tree before reporting success.
