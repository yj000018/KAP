# KAP State Registries & Quality Gates

**Program:** KAP — Knowledge Assimilation Program
**Sprint:** WP0-ENG-1
**Status:** Canonical Reference

## 1. Objective

To define the ledgers that track KAP's progress and the quality gates that ensure data integrity at every stage of the pipeline.

## 2. State Registries

KAP relies on three core registries to maintain state and prevent duplicate work:

### 2.1 Global Source Inventory (WP1)
The static map of all known sources.
- **Location:** `/home/ubuntu/KAP/01_Source_Inventory/KAP-Global-Source-Inventory.json`
- **Purpose:** Lists every source family, specific targets (e.g., specific Notion databases, specific Git repos), access methods, and credentials required.

### 2.2 Source State Registry (WP1/WP2)
The dynamic ledger of acquisition progress.
- **Location:** `/home/ubuntu/KAP/01_Source_Inventory/KAP-Source-State-Registry.json`
- **Purpose:** Tracks the high-water mark (last synced ID or timestamp) for every source defined in the Global Source Inventory. Updated *only* after a successful WP2 acquisition.

### 2.3 Asset Tracking Registry (WP3+)
The ledger of normalized assets.
- **Location:** `/home/ubuntu/KAP/00_Infrastructure/KAP-Asset-Tracking-Registry.json`
- **Purpose:** Maps the raw acquired asset (e.g., `raw_json/123.json`) to its normalized form (`normalized/123_card.md`) and tracks its instillation status in Mem0/Notion.

## 3. Quality Gates

No asset can move to the next Work Package without passing the appropriate gate.

### Gate 1: Acquisition Proof Gate (WP2 → WP3)
Before normalization can begin, the raw data must pass this gate.
- **Check 1:** Raw file exists on disk.
- **Check 2:** `_SOURCE_CARD.md` exists and contains valid metadata.
- **Check 3:** `manifest.json` exists and checksums match the raw files.
- **Check 4 (Persistence):** Files are tracked, committed, and pushed to the KAP GitHub repository.

### Gate 2: Normalization Quality Gate (WP3 → WP4)
Before distillation, the normalized data must be verified.
- **Check 1:** The output strictly adheres to the yOS JSON/Markdown schema (e.g., no missing required fields like `title` or `date`).
- **Check 2:** Deduplication check passed (the normalized content is not a 100% semantic match to an existing asset).

### Gate 3: Instillation Verification Gate (WP5 → WP6)
Before the pipeline completes, active memory injection must be verified.
- **Check 1:** API response from Mem0/Notion confirms successful insertion.
- **Check 2:** The Asset Tracking Registry is updated with the remote IDs (e.g., Notion Page ID, Mem0 Vector ID).
