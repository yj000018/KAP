# GitHub Inventory Findings — yj000018

## Summary
- **Account:** yj000018 (public_repos: 20, created 2013-10-13, last updated 2026-05-31)
- **Total public repos:** 20
- **Total branches across all repos:** ~60+
- **Largest repo:** YOS (main: 941 files, master: 1206 files, doctrine: 1203 files)

## Repos Inventory

| Repo | Updated | Branches | Files (main) | Description | Domain |
|------|---------|----------|--------------|-------------|--------|
| YOS | 2026-06-06 | 4 (main, master, phase-iii/yos-continuity-core-consolidation, y-os-doctrine) | 941 / 1206(master) | Core yOS monorepo | yOS Foundation |
| elysium-civilizational-ontology | 2026-06-28 | 39 | 237 (main) / 605 (fcs-multi-llm) | ELYSIUM ontology + FCS book production | ELYSIUM |
| elysium-book | 2026-06-28 | 1 (master) | 37 | FCS Book Repository | ELYSIUM |
| civilizational-awakening | 2026-06-06 | 1 | 267 | React+TS+Tailwind website | Civilizational Architecture |
| youniverse | 2026-06-04 | 1 | 103 | 3D Cognitive OS Interface (React+Three.js) | Private YOUniverse |
| one-galaxy | 2026-06-04 | 1 | 2 | 3D cognitive space visualization | Private YOUniverse |
| y-menu | 2026-06-04 | 1 | 41 | Cognitive Orchestration Interface | Agent Architecture |
| yos-scripts | 2026-06-04 | 2 (main, master) | 28 | Hub — Userscripts & automation | Manus Operations |
| yos-cockpit | 2026-06-04 | 2 (main, v2) | 16 | Brave Extension + TM Mobile | Manus Operations |
| y-llm-exporter | 2026-06-11 | 1 | 1 | Chrome extension to export LLM | Memory / Context |
| manus-enhancer | 2026-06-04 | 1 | 14 | Tampermonkey userscript | Manus Operations |
| yos-manus-client | 2026-06-04 | 1 | 2 | TamperMonkey client for manus.im | Manus Operations |
| yos-userscripts | 2026-06-04 | 1 | 4 | Auto-updatable userscripts | Manus Operations |
| daylog | 2026-06-04 | 1 | unknown | Day Log | Private YOUniverse |
| daylog-mvp | 2026-06-04 | 1 | unknown | MVP Day Log PWA | Private YOUniverse |
| relevance-ai-workforce | 2026-06-04 | 1 | unknown | AI workforce | Agent Architecture |
| UniversalChatThemeCanon | 2026-02-07 | 0 | unknown | Chat theme canon | Unknown |
| Y-Browser-Admin | 2025-10-16 | 1 | unknown | Browser admin | Manus Operations |
| YMap | 2025-10-22 | 1 | unknown | Map | Unknown |
| yannick | 2021-02-01 | 1 | unknown | Sample DatoCMS/Gatsby site | Legacy |

## Special Branch Located
- `yos/fcs-multi-llm-orchestration-protocol` → found in `elysium-civilizational-ontology` (605 files, sha: 30bd90aa)

## YOS Monorepo Structure (main branch)
- `archive/` (1 file)
- `plugins/yos-reader/` (19 files) — Obsidian plugin
- `yos-agents/manus/` (172 files) — Skills mirror, extensions
- `yos-agents/routing/` (1 file)
- `yos-apps/prototypes/` (145 files)
- `yos-apps/y-family/` (45 files)
- `yos-automations/scripts/` (68 files)
- `yos-governance/` (19 files) — ADRs, policies, project docs
- `yos-related/experiments/` (181 files)
- `yos-vault/knowledge/Y-WORLD/` (276 files) — Obsidian vault

## YOS Monorepo Structure (master branch — older/richer)
- 61 mission folders (mission_001 to mission_work_trace_001)
- `context_packs/` (14 files) — ARCH-001, BUILD-001, DOC-001, GOV-001, RES-001
- `concepts/` (39 files) — ART, CCR_Runtime, Canonical_Memory, Context_Pack, etc.
- `registry/` (13 files) — agent, capability, protocol, workflow entries
- `runtime/` (144 files) — Python runtime engines (CCR, event bus, KGC, etc.)
- `diagrams/` (16 files)
- `08_Visual_Maps/` (36 files)
- `09_Dashboards/` (9 files)
- `10_Live_Dashboards/` (18 files)
- `11_Timelines/` (4 files)

## YOS phase-iii branch
- `core/orchestration/continuity/` — Continuity Core docs (6 files)
- `core/orchestration/registries/` — LLM & Tool Routing Matrix
- `core/orchestration/reports/` — Consolidation & approval reports
- `BOOK/_fcs/registries/LLM_MATRIX.md`

## Elysium-civilizational-ontology (main)
- `00_PROGRAM_OFFICE/` (32 files)
- `02_ONTOLOGY_AND_KNOWLEDGE/` (42 files)
- `03_BOOK_AND_PUBLICATION/` (28 files)
- `04_DATASETS_AND_MATRICES/` (17 files)
- `05_RESEARCH_CORPUS/` (39 files)
- `06_ENGINEERING_AND_WORKFLOWS/` (26 files)
- `07_YOS_PATTERN_LIBRARY/` (28 files)
- `99_FINAL_REPORTS/` (12 files)
- `YOS_PROGRAM_OS/` (12 files)

## Elysium-civilizational-ontology (yos/fcs-multi-llm-orchestration-protocol)
- All above + `BOOK/` (365 files) + `PROGRAM_QUEUE/` (5 files) + `scripts/` (8 files)

## Key Observations
1. **main vs master divergence** in YOS repo — master has missions/runtime/concepts, main has vault/agents/apps structure
2. **39 branches** in elysium-civilizational-ontology — massive FCS book production history
3. **y-os-doctrine branch** nearly identical to master (1203 vs 1206 files)
4. **Context packs** exist in master branch (14 files)
5. **ADR series** from ADR-001 to ADR-0058+ across missions
6. **Runtime engines** in Python (CCR, KGC, event bus, etc.) — master only
7. **Y-WORLD Obsidian vault** (276 files) embedded in main branch
