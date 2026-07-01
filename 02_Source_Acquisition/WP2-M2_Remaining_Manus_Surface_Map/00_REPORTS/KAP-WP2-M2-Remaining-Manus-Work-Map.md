# KAP WP2-M2 — Remaining Manus Work Map
**Generated:** 2026-07-01

---

## Remaining Work

| priority | work_item | source_surface | current_state | target_state | estimated_effort | dependency | next_mpm |
|---|---|---|---|---|---|---|---|
| P0 | Complete Manus Tasks metadata (2340 missing) | S01 | 52/2392 acquired | 2392/2392 metadata | Low — API pagination already works | None | WP2-M4 |
| P0 | Classify all 2392 tasks by project/domain | S01, S04 | Unclassified | Classified by project (20 projects known) | Medium — script-based | S01 complete | WP2-M4 |
| P0 | Acquire Manus Knowledge full content | S05 | Metadata only (15 visible) | Full content for all entries | High — browser DOM or user copy-paste | None | WP2-M3 |
| P0 | Recover 30 missing website URLs | S06 | 3/33 URLs known | 33/33 URLs | Medium — task cross-reference + user input | None | WP2-M5 |
| P0 | Share Notion DBs with integration | S12, S13 | 0 DBs accessible | 325+ session cards accessible | Low — 1 user action in Notion | User action | WP2-M6 |
| P0 | Acquire 325+ Notion session cards | S12 | Blocked | All session cards acquired | High — API pagination after access granted | S12 unblocked | WP2-M6 |
| P1 | Acquire task full bodies (P0 tasks: KAP/yOS/memory) | S02 | Blocked (no API) | Full conversation content for P0 tasks | High — browser DOM extraction | None | WP2-M4 |
| P1 | Acquire task output files (P0 tasks) | S03 | 8 files found | All P0 task files downloaded | Medium — browser UI download | None | WP2-M4 |
| P1 | Capture website content for 30 unresolved sites | S07 | 3 captured | All reachable sites captured | Medium — HTTP probing after URL recovery | S06 unblocked | WP2-M5 |
| P1 | Acquire Mem0 full inventory (400 entries) | S14 | 400 entries acquired | Verified complete | Low — already done | None | WP2-M7 |
| P1 | Acquire Notion Projects DB | S13 | Blocked | Project cluster cards | Medium | S13 unblocked | WP2-M6 |
| P2 | Acquire task full bodies (P1 tasks: ELYSIUM/KOSMOS) | S02 | Blocked | Full content for P1 tasks | High | None | WP2-M4 |
| P2 | Acquire website source/build artifacts | S18 | Partial | All build folders captured | Medium | None | WP2-M5 |
| P2 | Acquire Manus session archives (in-app) | S17 | Blocked (DOM only) | Full conversation history | Very High | None | WP2-M4 |
| P3 | Acquire task full bodies (P2/P3 tasks) | S02 | Blocked | All remaining tasks | Very High | None | WP2-M4 |
| P3 | GitHub PAT for private repos | S15 | Public only | Private repos if any | Low — sudo verification | User action | WP2-E1 addendum |

---

## What Can Be Done NOW Without New Access

1. **Complete S01** — paginate all 2392 task metadata via API → WP2-M4
2. **Classify tasks by project** — cross-reference task IDs with 20 project names → WP2-M4
3. **Acquire Mem0 400 entries** — already done, save to capsule → WP2-M7
4. **Acquire GitHub remaining branches** — public API works → WP2-E1 addendum
5. **Search local filesystem for build artifacts** — scan /home/ubuntu for website source folders

## What Requires User Action (1 action each)

| # | Action | Time | Unlocks |
|---|---|---|---|
| 1 | Share Notion "Manus Memory" page with YOS Comet-Light integration | 30 sec | 325+ session cards (S12, S13) |
| 2 | Open Manus Knowledge tab → screenshot full list | 2 min | S05 hidden entries |
| 3 | Open each Knowledge entry → copy-paste content | 15-30 min | S05 full content |
| 4 | Open Manus Websites tab → screenshot all cards with URLs | 5 min | S06 30 missing URLs |
| 5 | Download task files for P0 tasks (KAP, yOS, memory) | 10 min | S03 P0 outputs |
