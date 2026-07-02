# Source Registry System

> KAP Source Inventory — Modular Architecture for Knowledge Acquisition

## 1. Purpose

The Source Registry System is the core module managing all present and future knowledge sources for KAP. It defines a plug-and-play architecture where new sources (e.g., YouTube transcripts, web bookmarks, Excalidraw schemas) can be added, configured, and activated without altering the core synthesis engine.

## 2. Source Lifecycle

Every source in KAP follows a strict lifecycle:

1. **Discovered** — Identified as a potential knowledge source.
2. **Catalogued** — Added to the `SOURCE-CATALOG.md` with its metadata.
3. **Connector Designed** — An acquisition connector is designed (e.g., API script, scraper).
4. **Configured** — Activation policy, frequency, and filters are defined.
5. **Active** — Source is actively feeding the KAP Source Fragment Layer.
6. **Paused** — Acquisition temporarily stopped.
7. **Deprecated** — Source is no longer acquired (historical fragments remain).

## 3. Modular Components

### 3.1 The Catalog (`SOURCE-CATALOG.md`)
The master list of all sources (active, planned, and future). Each entry defines:
- **Source Type** (e.g., text, video, graph)
- **Origin** (e.g., YouTube, Excalidraw, Notion)
- **Format** (e.g., Markdown, JSON, SVG)

### 3.2 The Connectors (`02_Source_Acquisition/Connectors/`)
Isolated scripts or APIs responsible for pulling data from a source and converting it into standard `source_fragment.schema.json` format. Connectors do not synthesize; they only acquire and format.

### 3.3 The Activation Policy (`SOURCE-ACTIVATION-POLICY.md`)
Defines *when* and *how* a source is acquired:
- **Mode**: Auto (cron/webhook), Semi-Auto (human trigger), Manual (one-off)
- **Status**: ON / OFF
- **Filters**: What to include/exclude (e.g., "only YouTube videos with #KAP tag")

## 4. Future-Proofing

The system is designed to absorb any future source type:
- **Visuals**: Excalidraw, Spline, Figma (converted to text descriptions + SVG fragments)
- **Audio/Video**: YouTube, local voice memos (converted via Whisper to text fragments)
- **Behavioral**: Browser history, app usage logs (converted to event fragments)
- **External AI**: Outputs from specific specialized LLMs or tools

## 5. Rules

1. **No direct injection**: A source cannot inject data directly into the synthesis layer. It must pass through a Connector and become a Source Fragment first.
2. **State independence**: Pausing a source does not delete its historical fragments.
3. **Traceability**: Every fragment must carry its Source ID and Connector Version.
