# KAP WP2-M2 — User Input Request Pack
**To:** Yannick  
**Generated:** 2026-07-01  
**Priority:** Execute in order — #1 unlocks the most value

---

## Request Table

| request_id | screen_to_open | action | preferred_format | exact_steps | why_needed | after_user_provides |
|---|---|---|---|---|---|---|
| UIR-001 | Notion → any page in Manus Memory workspace | Share Manus Memory with YOS Comet-Light integration | Click action | 1. Open Notion. 2. Navigate to "Manus Memory" parent page. 3. Click `...` top-right → Connections. 4. Search "YOS Comet-Light". 5. Click Connect. 6. Confirm. | Unlocks 325+ session cards + project clusters via API | I run WP2-M6 immediately — acquire all session cards automatically |
| UIR-002 | manus.im/app → Knowledge tab (left sidebar) | Screenshot full Knowledge list | Screenshot | 1. Open manus.im. 2. Click Knowledge in left sidebar. 3. Scroll to bottom to load all entries. 4. Screenshot full list. | 42+ entries not rendered in prior DOM extraction — need full count | I extract all entry titles and create acquisition queue |
| UIR-003 | manus.im/app → Knowledge → each entry | Copy-paste full content of each Knowledge entry | Copy-paste text | 1. Click each Knowledge entry. 2. Select all text (Cmd+A). 3. Copy. 4. Paste into a text file per entry. 5. Send as ZIP or paste block. | No API endpoint for Knowledge content — only accessible via UI | I create one raw markdown file per entry and add to capsule |
| UIR-004 | manus.im/app → Websites/Library tab | Screenshot all website cards showing URLs | Screenshot | 1. Open manus.im. 2. Click Library or Websites in sidebar. 3. For each card, click to open settings/details. 4. Screenshot the URL field. 5. Or copy-paste URL list. | 30 of 33 website URLs are missing — cannot capture content without URL | I probe all URLs, capture HTML/text, add to WP2-M5 capsule |
| UIR-005 | manus.im/app → any P0 task (KAP, yOS, memory) | Download task output files | File download | 1. Open a KAP or yOS task. 2. Click Files/Outputs section. 3. Download all files. 4. Send as ZIP. | API has no /files endpoint — files only accessible via UI | I add all files to task outputs capsule with checksums |
| UIR-006 | manus.im/app → task list | Screenshot full task list with project filters | Screenshot | 1. Open manus.im task list. 2. Filter by project (Y-OS, KAP, ELYSIUM). 3. Screenshot each filtered view. | Verify our 2392 task count and project assignments | I cross-validate API metadata with UI display |

---

## Priority Order

1. **UIR-001** (Notion share) — 30 seconds, unlocks 325+ session cards
2. **UIR-004** (Website URLs) — 5 minutes, unlocks 30 website captures
3. **UIR-002** (Knowledge list screenshot) — 2 minutes, unlocks hidden entries
4. **UIR-005** (Task file downloads) — 10 minutes, unlocks P0 task outputs
5. **UIR-003** (Knowledge copy-paste) — 15-30 minutes, unlocks full Knowledge content
6. **UIR-006** (Task list screenshot) — 5 minutes, validates task count

---

## What Manus Can Do Without User Input Right Now

- Complete all 2392 task metadata via API (WP2-M4)
- Classify tasks by project domain
- Acquire full Mem0 400 entries
- Acquire GitHub remaining content
- Search local filesystem for build artifacts
- Generate source cards and checksums for already-acquired material
