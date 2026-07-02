# Scripts Location Decision

**Date:** 2026-07-02  
**Gate:** AGENT-ROLE-GATE  

## Options Evaluated
1. Root-level `scripts/`
2. `04_Execution/scripts/`
3. `02_Architecture/Connectors/scripts/`
4. Source-specific script folders under `02_Source_Acquisition/`
5. Hybrid model

## Recommended Canonical Location
**Hybrid Model:**
- **Global Utilities & Pipeline Orchestration:** Root-level `scripts/` (e.g., `scripts/kap_session_archive/`).
- **Connector Implementations:** Source-specific folders under `02_Source_Acquisition/[Source]/_scripts/` (e.g., `02_Source_Acquisition/Manus/_scripts/`).

## Rationale
Root-level `scripts/` is already established and functioning well for cross-cutting pipelines (like the current archive pipeline). However, as connectors scale, placing their specific extraction logic near their data (`02_Source_Acquisition/[Source]/_scripts/`) improves modularity and Obsidian navigation.

## Tradeoffs
- *Pros:* Separation of concerns; connector code lives with connector data.
- *Cons:* Two places to look for code. Mitigated by clear documentation.

## Migration Implications
Existing scripts in `scripts/` remain. Future connector implementations will use the `_scripts/` subfolders.

## Open Questions
None.
