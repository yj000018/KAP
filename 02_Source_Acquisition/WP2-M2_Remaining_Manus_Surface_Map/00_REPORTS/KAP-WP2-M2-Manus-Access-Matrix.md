# KAP WP2-M2 — Manus Access Matrix
**Generated:** 2026-07-01  
**Sprint:** WP2-M2 — Remaining Manus Surface Map  
**Gate after WP2-M1C:** MANUS_INCOMPLETE_ACCESS_REQUIRED

---

## Access Matrix

| surface_id | surface_name | expected_content | current_access_method | accessible_now | acquired_already | missing_content | blocker | best_next_method | user_input_needed |
|---|---|---|---|---|---|---|---|---|---|
| S01 | Manus Tasks (metadata) | 2392 task titles, dates, status, model, credits | Manus API v1 GET /v1/tasks | ACCESSIBLE_NOW | PARTIAL (52 of 2392) | 2340 task metadata entries | None | API full pagination | No |
| S02 | Manus Task full bodies | Conversation content, final answers, reasoning | API /v1/tasks/{id}/messages | BLOCKED_API | No | Full task content | No messages/files endpoint in API v1 | USER_COPYPASTE_REQUIRED or browser DOM | Yes |
| S03 | Manus Task outputs/files | Generated files, ZIPs, PDFs, code, reports | API /v1/tasks/{id}/files | BLOCKED_API | PARTIAL (8 files) | All task-generated files | No files endpoint in API v1 | Browser UI download | Yes |
| S04 | Manus Projects | 20 project names and IDs | Manus API v1 GET /v1/projects | ACCESSIBLE_NOW | No | Project task assignments | /projects/{id}/tasks returns 404 | API acquired | No |
| S05 | Manus Knowledge | Full knowledge entry content | API /v1/knowledge | BLOCKED_API | METADATA_ONLY (15 visible) | 42+ hidden entries + full content | No /v1/knowledge endpoint | Browser DOM + user copy-paste | Yes |
| S06 | Manus Websites | URLs, deployment metadata, content | Browser DOM + probing | METADATA_ONLY | PARTIAL (3 of 33 URLs) | 30 website URLs + content | No API endpoint for websites | Browser UI + user screenshots | Yes |
| S07 | Manus Website content | HTML, text, screenshots for each site | HTTP probing | PARTIAL | 3 sites captured | 30 sites unresolved | No URL available | Recover URLs first | Yes |
| S08 | Manus Config | Connectors, project instructions, settings | manus-config CLI | ACCESSIBLE_NOW | YES (redacted) | None critical | None | Already acquired | No |
| S09 | Manus Skills (local) | 60 skills SKILL.md + scripts | Local filesystem | ACCESSIBLE_NOW | YES (59 skills) | None | None | Already acquired | No |
| S10 | Manus Memory / Internal context | Project instructions, knowledge base | manus-config CLI | ACCESSIBLE_NOW | YES | None | None | Already acquired | No |
| S11 | Manus Remote Files / Downloads | Files generated in prior tasks | Local /home/ubuntu + Downloads | ACCESSIBLE_NOW | PARTIAL | Many task outputs not in sandbox | Files may be in task UI only | Browser UI + user download | Yes |
| S12 | Notion Memory Hub — Sessions DB | 325+ archived Manus session cards | Notion API | BLOCKED_CONNECTOR | No | All 325+ session cards | Bot not shared with DBs | Share Notion DBs with integration | Yes |
| S13 | Notion Memory Hub — Projects DB | Project cluster cards | Notion API | BLOCKED_CONNECTOR | No | All project cards | Bot not shared with DBs | Share Notion DBs with integration | Yes |
| S14 | Mem0 memories | Cross-session memory entries | Mem0 API v1 | ACCESSIBLE_NOW | PARTIAL (400 entries) | Unknown if complete | None | API full pagination done | No |
| S15 | GitHub repos (public) | 20 repos, all branches | GitHub public API | ACCESSIBLE_NOW | PARTIAL (key branches) | Private repos if any; full file content | No PAT for private | Public API + sparse checkout | No |
| S16 | Local KAP artifacts | All prior sprint outputs | Local filesystem | ACCESSIBLE_NOW | YES (3627 files) | None | None | Already acquired | No |
| S17 | Manus session archives (in-app) | Full conversation history per task | Browser DOM | BLOCKED_DOM | No | All conversation history | No API endpoint; UI-only | Browser scroll + DOM extraction | Yes |
| S18 | Website build/source folders | React/Next.js source for deployed sites | Local filesystem search | PARTIAL | PARTIAL | Most build folders absent | Sites deployed to manus.space CDN | Local search + task output files | No |

---

## Summary

| Status | Count | Surfaces |
|---|---|---|
| ACCESSIBLE_NOW | 7 | S01, S04, S08, S09, S10, S14, S16 |
| METADATA_ONLY | 2 | S05, S06 |
| PARTIAL | 3 | S07, S11, S15 |
| BLOCKED_API | 3 | S02, S03, S05 |
| BLOCKED_CONNECTOR | 2 | S12, S13 |
| BLOCKED_DOM | 1 | S17 |

**User input required:** S02, S03, S05, S06, S07, S11, S12, S13, S17

---

## Critical Discovery

**Manus Tasks: 2392 total** (not 52 as previously estimated)
- Prior sprint only captured 52 via DOM scraping
- API returns full 2392 task metadata entries
- Task bodies/content NOT accessible via API (no /messages or /files endpoint)

**Manus Projects: 20 projects** — full list acquired:
Y-OS, MDMA-ONENESS JOURNEY PROGRAM, mac-root, Y Life, --- eia ---, VISUAL REALITY, MEDIA & CREA, --- ELYSIUM ---, LUDIVINE, FULL MAC ACCESS, (archives), Y-ONE, LightWay editions, KAP, MAGIC AI, Odyssey, GEN5, Y-World, HOME AUTOMATION, PRECIPITATION

**Mem0: 400 memories** acquired (2 pages × 200, page 3 = 404 = complete)

**Notion: 0 DBs accessible** — bot connected to workspace "Yannick" but no databases shared with integration YOS Comet-Light
