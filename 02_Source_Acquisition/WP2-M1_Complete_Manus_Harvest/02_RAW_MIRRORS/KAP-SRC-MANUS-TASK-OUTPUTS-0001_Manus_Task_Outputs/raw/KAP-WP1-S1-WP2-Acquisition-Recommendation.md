# KAP WP1-S1: WP2 Acquisition Recommendation

The objective of WP2 is to acquire sources identified in WP1. To ensure a structured, low-risk ingestion process, acquisition must be phased. Do not acquire everything at once.

## Recommended Acquisition Order

### Batch 1: The Foundations (P0)
**Goal:** Establish the architectural baseline and current operational capabilities.
1. **GitHub: YOS (`master` branch)**
   - Target: `concepts/` (39 files)
   - Target: `context_packs/` (14 files)
   - Target: `yos-governance/Decisions/` (ADRs)
   - *Rationale:* Foundational relevance. High dependency value for later KRE refinement.
2. **Manus: Local Sandbox Skills**
   - Target: `/home/ubuntu/skills/` (specifically `yos-mmm`, `program-os-orchestrator`, `memory-manager`, `yos-optimizer`)
   - *Rationale:* Represents the living, executable architecture of the agent. Ease of access (already local).

### Batch 2: The Living Context (P1)
**Goal:** Acquire the active knowledge base and recent session history.
1. **GitHub: YOS (`main` branch)**
   - Target: `yos-vault/knowledge/Y-WORLD/` (Obsidian Vault, specifically `60_Y-OS/`)
   - *Rationale:* Represents the most current human-facing cognitive map.
2. **Notion: Manus Memory Hub**
   - Target: `📝 Conversation Archive` and `🎯 Projet / Thème` entries.
   - *Prerequisite:* Resolution of BLK-001 (Enable Notion connector).
   - *Rationale:* Critical for cross-session continuity and recovering recent context.

### Batch 3: The Orchestration Layer (P1.5)
**Goal:** Acquire advanced workflows and protocols.
1. **GitHub: YOS (`phase-iii/yos-continuity-core-consolidation`)**
   - Target: `core/orchestration/`
   - *Rationale:* Contains the latest Continuity Core documentation and LLM routing matrices.
2. **GitHub: elysium-civilizational-ontology (`yos/fcs-multi-llm-orchestration-protocol`)**
   - Target: `07_YOS_PATTERN_LIBRARY/`
   - *Rationale:* Contains the multi-LLM orchestration protocols (FCS) which may be applicable to yOS generally.

### Batch 4: The Archives & Periphery (P2/P3)
**Goal:** Ingest historical data and peripheral interfaces.
1. **GitHub: YOS (`master` branch)**
   - Target: `mission_*/` folders (Historical logs)
   - Target: `runtime/` (Python engines)
2. **Mem0: Associative Memory**
   - Target: Full sync verification.
   - *Prerequisite:* Resolution of BLK-002.
3. **GitHub: Agent UIs**
   - Target: `y-menu`, `youniverse`, `yos-scripts`
   - *Rationale:* Implementation details, lower priority for core architectural canonization.

## Execution Notes for WP2
- **Deduplication:** When acquiring Batch 1 and Batch 2, explicitly flag overlaps between `concepts/` (master) and `Y-WORLD/60_Y-OS/` (main).
- **Format Preservation:** Retain all original Markdown formatting, YAML frontmatter, and JSON structures during acquisition. Do not summarize during the acquisition phase.
