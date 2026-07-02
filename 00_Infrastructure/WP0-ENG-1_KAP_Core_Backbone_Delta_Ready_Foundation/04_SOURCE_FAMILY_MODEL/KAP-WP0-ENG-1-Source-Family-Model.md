# KAP Source Family Model

**Program:** KAP — Knowledge Assimilation Program
**Sprint:** WP0-ENG-1
**Status:** Canonical Reference

## 1. Objective

To define the categorization and handling protocols for all potential sources of knowledge entering the KAP pipeline.

## 2. Source Families

Knowledge sources are categorized into families based on their structure, access method, and update frequency.

| Family ID | Family Name | Characteristics | Acquisition Method | Examples |
|---|---|---|---|---|
| SF-01 | **Conversational AI** | Chronological dialogue, structured JSON/MD exports. | API pagination, bulk JSON export. | Manus, ChatGPT, Claude, Gemini. |
| SF-02 | **Structured Memory** | Relational databases, vector stores, tagged entries. | API sync, full DB dump. | Notion, Mem0, Airtable. |
| SF-03 | **Versioned Repositories** | Git-backed, folder structures, markdown/code. | `git clone`, `git pull`. | GitHub (YOS, Elysium), GitLab. |
| SF-04 | **Local File Systems** | Unstructured or semi-structured local files, vaults. | File system traversal, rsync. | Obsidian vaults, local PDF archives. |
| SF-05 | **Web & Ephemeral** | HTML/DOM structures, unversioned pages. | Web scraping, Playwright. | Websites, blogs, public wikis. |
| SF-06 | **Telemetry & Logs** | High-volume, time-series data, system events. | Log shipping, API streaming. | yOS telemetry, server logs. |
| SF-07 | **Physical & Ambient** | Sensor data, voice transcripts, home state. | Webhooks, IoT APIs. | Home automation (Home Assistant), voice memos. |

## 3. Handling Protocols per Family

### SF-01: Conversational AI
- **Pagination Risk:** Must implement strict deduplication and loop prevention (e.g., Manus `task.list` bugs).
- **Noise Filtering:** Must filter out internal subtasks (e.g., "Wide Research Subtask") and system prompts.
- **Delta Strategy:** Track by `last_id` or `last_timestamp`.

### SF-02: Structured Memory
- **Integrity Risk:** Must respect existing relationships and tags.
- **Delta Strategy:** Track by `last_edited_time` property in Notion/Mem0.

### SF-03: Versioned Repositories
- **Integrity Risk:** Must capture specific commit hashes in the source card.
- **Delta Strategy:** `git log` and `git diff` against the last acquired commit hash.

### SF-04: Local File Systems
- **Integrity Risk:** Files can be moved or renamed without tracking.
- **Delta Strategy:** Checksum comparison (SHA256) of all files to detect changes.

### SF-05: Web & Ephemeral
- **Integrity Risk:** Content changes silently; link rot.
- **Delta Strategy:** Periodic full snapshots or visual diffing. Must store raw HTML alongside extracted Markdown.

### SF-06 & SF-07: Telemetry & Physical
- **Volume Risk:** Data must be aggregated and summarized before entering KAP to avoid overwhelming the system.
- **Delta Strategy:** Time-windowed batch processing (e.g., daily summaries).
