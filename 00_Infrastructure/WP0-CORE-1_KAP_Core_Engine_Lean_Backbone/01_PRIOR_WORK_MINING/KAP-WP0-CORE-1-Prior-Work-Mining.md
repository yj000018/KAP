# KAP WP0-CORE-1 — Prior Work Mining

**Sprint:** WP0-CORE-1
**Generated:** 2026-07-02

## Inventory

| item | source_path | existing_principle | adopt_status | note |
|---|---|---|---|---|
| Source Manifests & Checksums | `WP2-M1/02_RAW_MIRRORS/*/manifest.json` | Every acquisition must produce a JSON manifest + SHA256 checksums. | ADOPT | Proven in WP2-M1, WP2-M6B. |
| Source Cards (`_SOURCE_CARD.md`) | `WP2-E1/local_artifacts/_SOURCE_CARD.md` | Each acquired asset must have a provenance metadata file. | ADOPT | Standard format already in use. |
| Persistence Gate | `WP2-M8D/07_PERSISTENCE_GATE/` | No sprint is complete until: file exists → in KAP → tracked → committed → pushed → visible on GitHub. | ADOPT | Canonical gate already defined. |
| Task vs Session Separation | `WP2-M8D/03_TASKS_VS_SESSIONS_PROOF/` | Manus API returns subtasks as noise. Human sessions are the real corpus. Pagination artifacts confirmed. | ADOPT | Critical for WP2-MANUS delta. |
| Manual UI Fallback Protocol | `WP2-M8/06_MANUAL_EXTRACTION_PROTOCOLS/` | When API fails, document the fallback method and inject result into same pipeline. | ADOPT_WITH_SIMPLIFICATION | Runbook already exists in WP0-ENG-1. |
| ZIP = Transport Only | `WP2-INFRA-4B/`, `WP2-INFRA-4C/` | ZIPs are not durable storage. Contents must be extracted and committed to Git. | ADOPT | Confirmed by INFRA-4C reconciliation. |
| Notion as Hub | `yOS skills: memory-manager` | Notion = structured navigation + archive. Not sole source of truth. | ADOPT | Downstream of Git. |
| Mem0 = Distilled Only | `yOS skills: mem0-sync, session-synthesis` | Mem0 receives only distilled, validated knowledge — never raw verbatim. | ADOPT | Confirmed by WP0-ENG-1 backbone. |
| Session Synthesis (card generation) | `scripts/kap_session_archive/02_generate_card.py` | Standardized JSON + MD card generation for archived sessions via LLM. | ADOPT | Working pipeline already deployed. |
| WP Architecture (WP0–WP8) | `WP0-ENG-1/03_WORK_PACKAGE_ARCHITECTURE/` | WP0–WP8 canonical structure with 15 WP2 branches. | ADOPT_WITH_SIMPLIFICATION | Lean version in this sprint. |
| Delta-Ready 5-step workflow | `WP0-ENG-1/05_DELTA_READY_PROCESS/` | Read State → Fetch Delta → Local Dedup → Acquire → Update State. | ADOPT | Already defined, not yet implemented. |
| Notion session corpus (363 sessions) | `WP2-M6B/01_MANIFESTS/sprint_manifest.md` | 363 sessions in Notion = authoritative corpus. Manus API pagination confirmed broken for historical sessions. | ADOPT | Source of truth for WP2-MANUS. |

## Answers to Mining Questions

**1. Existing KAP process elements already usable:**
Source cards, manifests, checksums, persistence gate, session synthesis pipeline, Notion/Mem0 positioning — all usable as-is.

**2. Source registry / source cards / manifests / checksums:**
Source cards (`_SOURCE_CARD.md`) and manifests (`manifest.json`, `SHA256_manifest.md`) are established patterns from WP2-M1 and WP2-M6B. No reinvention needed.

**3. Git persistence:**
The Persistence Gate (file → KAP → tracked → committed → pushed → GitHub) is canonical since WP2-M8D.

**4. Mem0 positioning:**
Mem0 = active distilled memory only. Raw verbatim never enters Mem0. Confirmed by `mem0-sync` skill and WP0-ENG-1 backbone.

**5. Future delta / yOS learning:**
Delta-ready 5-step workflow defined in WP0-ENG-1. Source State Registry schema defined. Not yet implemented as live scripts.

**6. What remains missing for WP0 to be solid:**
- Centralized `Source_State_Registry.json` (high-water marks per source)
- Canonical normalization schema (WP3 prerequisite)
- Routing matrix (this sprint)
- WP2-MANUS final coverage confirmation (M8C/M8D still pending full closure)
