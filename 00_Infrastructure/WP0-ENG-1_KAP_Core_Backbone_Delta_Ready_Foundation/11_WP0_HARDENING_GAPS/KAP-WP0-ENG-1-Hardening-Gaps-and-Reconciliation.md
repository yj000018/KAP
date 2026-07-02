# KAP WP0 Hardening Gaps & WP1/WP2 Reconciliation

**Program:** KAP — Knowledge Assimilation Program
**Sprint:** WP0-ENG-1
**Status:** Canonical Reference

## 1. Objective

To identify the gaps between the current state of KAP and the hardened WP0 Backbone defined in this sprint, and to specify the requirements for reconciling the existing WP1 (Inventory) and WP2 (Acquisition) work with this new backbone.

## 2. WP0 Hardening Gaps

The following elements are required by the new backbone but do not yet exist or are incomplete:

1. **Centralized Source State Registry:** Currently, scripts rely on local file checks (`if exists`) rather than a central JSON ledger tracking the high-water mark for each source.
2. **Standardized Normalization Schema (WP3):** We have `_card.json` generation scripts, but no canonical schema definition document that dictates exactly what fields must exist for all source families.
3. **Automated Persistence Gate Validation:** The Git-Proof step is often a manual script run at the end of a sprint. It needs to be a callable Python function that blocks pipeline advancement if it fails.
4. **Universal Connector Authentication:** The Mem0 and Notion connectors are frequently disabled in the sandbox environment, blocking downstream instillation. A permanent auth strategy (e.g., ENV variables injected by the orchestrator) is required.

## 3. WP1 Reconciliation Requirements

The existing WP1 (Global Source Inventory) must be updated to align with the new Source Family Model.

- **Action Required:** Re-map all entries in `/home/ubuntu/KAP/01_Source_Inventory/KAP-Source-Registry-WP1-S1.md` to the new SF-01 through SF-07 family IDs.
- **Action Required:** Initialize the `KAP-Source-State-Registry.json` with the current state of all sources acquired during the historical WP2 sprints.

## 4. WP2 Branching Requirements

Future WP2 acquisitions must strictly follow the branch architecture defined in the WP Architecture document.

- **Action Required:** Restructure future sprint folders to clearly indicate the branch (e.g., `WP2-MANUS-01`, `WP2-NOTION-02`) rather than generic labels.
- **Action Required:** Update all WP2 scripts to implement the Delta-Ready Process (Read State -> Fetch Delta -> Local Check -> Acquire -> Update State).

## 5. Runbooks

To ensure operability during the transition to full autonomy, the following runbooks must be created in `/home/ubuntu/KAP/00_Infrastructure/WP0-ENG-1.../14_RUNBOOKS/`:

1. **Runbook-01-Manual-API-Fallback:** How to extract data via UI when an API rate limit is hit (based on WP2-M8 findings).
2. **Runbook-02-State-Registry-Reset:** How to manually reset the high-water mark in the Source State Registry if a sync fails or data corruption occurs.
3. **Runbook-03-Git-Disaster-Recovery:** How to recover from a corrupted Git index without losing the raw acquired files.
