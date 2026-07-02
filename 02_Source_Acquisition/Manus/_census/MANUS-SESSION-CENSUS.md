# Manus Session Census

**Date:** 2026-07-02  
**Method:** API Extraction (Metadata only)  

## Census Purpose
To perform a controlled metadata-only inventory of Manus sessions to prepare for future connector implementation and cleanup strategy, without triggering broad corpus ingestion.

## Scope & Method
- Extracted via `GET https://api.manus.im/v2/task.list` using cursor pagination.
- Only metadata fields were requested; no task bodies were downloaded.

## Findings
- **Total visible sessions/tasks:** 200 (API limit reached / account limit).
- **Pagination behavior:** Cursor-based (`last_id`), max 100 per page.
- **Metadata fields available:** `task_id`, `title`, `created_at`, `updated_at`, `status`, `project`, `tags`, `url`, `attachments`.
- **Date/time range:** 2026-06-27 to 2026-07-01.

## High-Level Category Counts
- **Total:** 200
- **Archived (`[✓]`):** 22
- **Subtasks (Noise):** 178
- **Durable Candidates:** 2
- **KAP-Relevant:** 2

## Access Limitations
The API currently returns a maximum of 200 recent tasks, heavily skewed by "Wide Research Subtasks". A deeper pagination or filtering strategy will be required for the full connector implementation.

## Compliance
**No-acquisition confirmation:** No task bodies or full conversation payloads were ingested. This is strictly a metadata census.
