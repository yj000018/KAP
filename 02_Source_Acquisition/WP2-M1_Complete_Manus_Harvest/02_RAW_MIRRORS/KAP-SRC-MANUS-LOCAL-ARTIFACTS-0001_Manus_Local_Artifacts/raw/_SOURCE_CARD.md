# Source Card — Memory Pipeline & Remote Knowledge

| Field | Value |
|-------|-------|
| source_id | KAP-ACQ-E2-001 |
| source_family | Manus |
| source_type | memory_pipeline_artifacts |
| title | LLM Memory Pipeline v2 — Scripts, Skills, State |
| acquisition_date | 2026-07-01 |
| total_files | 109 |
| total_size | 1.0 MB |
| checksum_file | _CHECKSUMS.txt (SHA-256 per file) |
| sensitive_content | MANUS_TOKEN embedded in collect_session.py (env var fallback — NOT hardcoded secret, JWT only) |
| fidelity | EXACT_COPY |
| relevance_to_kap | 5/5 |

## Pipeline State

| Item | Status |
|------|--------|
| `/home/ubuntu/manus_pipeline/` | NOT PRESENT — pipeline not initialized in this sandbox |
| Pipeline scripts (skills) | ACQUIRED — all 7 phase scripts available |
| State files (archived_uids.json, etc.) | NOT PRESENT — no prior run |
| Session cards | NOT PRESENT — no prior run |
| Project cards | NOT PRESENT — no prior run |
| Notion session archives (325 sessions) | BLOCKED — Notion connector disabled |
| Mem0 cross-session memory | BLOCKED — Mem0 connector disabled |

## Capsule Contents

| Subfolder | Source | Files | Key Content |
|-----------|--------|-------|-------------|
| pipeline_scripts/ | memory-pipeline skill | 5 | SKILL.md, run_pipeline.py, LLM_EXTRACTION_METHODS.md |
| session_synthesis_scripts/ | session-synthesis skill | 4 | collect_session.py, generate_card.py, archive_to_notion.py, SKILL.md |
| mem0_scripts/ | mem0-sync skill | 3 | sync_notion_to_mem0.py, sync_manus_to_mem0.py, SKILL.md |
| yos_scripts_memory/ | yos-scripts GitHub | 4 | push-mem0-core.js, YOS-MEMORY-BRIDGE-ARCHITECTURE.md, push-mem0-loader.js, push-mem0.user.js |
| session_navigator_data/ | session-navigator skill | 86 | Session tree examples, generation scripts |
| memory_manager_skill/ | memory-manager skill | 3 | SKILL.md, memory_system_constants.md, archive_conversation.py |
| yos_mmm_skill/ | yos-mmm skill | 1 | SKILL.md — Multi-session Multi-LLM Memory v2.0 |
| hydrater_skill/ | hydrater skill | 2 | SKILL.md, context_package.md template |

## Key Findings

- **Pipeline location**: `/home/ubuntu/manus_pipeline/` (not yet initialized in this sandbox)
- **Manus API token**: JWT embedded in collect_session.py (expires 2026-08-07 approx)
- **Notion DB**: `Manus Memory Hub` — DB ID `4ea5d9b7-1919-4ed6-974a-3e73049fe9bf`
- **Sessions DB**: `Manus Memory — Sessions` — DB ID `0720db9b-5e1d-41a2-bd0c-6721fe0dab94`
- **Reported state**: 325 sessions archived, 278 verbatim pages updated, 7 projects identified
- **LLM adapters**: Manus (✅), ChatGPT (✅ built), Gemini (✅ built), Grok (✅ built), Claude.ai (✅ built), Perplexity (✅ built)

## Blockers

| Blocker | Impact |
|---------|--------|
| Notion connector disabled | Cannot verify 325 session archives, cannot pull project cards |
| Mem0 connector disabled | Cannot verify cross-session memory state |
| manus_pipeline/ not initialized | No state files, no session exports, no cards |
| Pipeline not run in this sandbox | All state is in Notion/Mem0, not locally accessible |
