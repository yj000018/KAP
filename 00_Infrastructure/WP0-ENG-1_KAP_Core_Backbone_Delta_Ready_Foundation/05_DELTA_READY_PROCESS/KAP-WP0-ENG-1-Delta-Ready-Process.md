# KAP Delta-Ready Process

**Program:** KAP — Knowledge Assimilation Program
**Sprint:** WP0-ENG-1
**Status:** Canonical Reference

## 1. Objective

To define the exact workflow required to ensure KAP can run continuously and autonomously, processing only new or changed information (deltas) rather than re-ingesting the entire historical corpus every time.

## 2. The Delta Problem

Without a delta-ready process:
- API limits are exhausted quickly (e.g., Manus 2000-task pagination limit).
- LLM costs explode due to re-summarizing existing sessions.
- Duplicate entries pollute Notion and Mem0.
- Git repositories bloat with redundant commits.

## 3. The Delta Workflow

Every KAP acquisition script must follow this strict sequence:

### Step 1: Read State Registry
Before hitting any external API or file system, the script must read the `Source_State_Registry.json`.
*Example: What was the `last_task_id` or `last_sync_timestamp` for the Manus source?*

### Step 2: Fetch Delta Only
The script requests only data created or modified *after* the marker found in Step 1.
*Example: `GET /task.list?after_timestamp=1718293000` or `git diff HEAD..last_known_hash`.*

### Step 3: Local Deduplication Check (Safety Net)
Even if the API claims the data is new, the script must check the local Git filesystem to ensure the asset doesn't already exist.
*Example: `if os.path.exists(f"{uid}_card.json"): skip()`*

### Step 4: Acquire and Preserve
Download the raw delta, generate the `_SOURCE_CARD.md`, calculate checksums, and save to the local filesystem.

### Step 5: Update State Registry
Only after the new files are successfully written to disk (and ideally committed to Git), update the `Source_State_Registry.json` with the new high-water mark (the latest timestamp or ID just processed).

## 4. State Registry Schema

The `Source_State_Registry.json` must live in `/home/ubuntu/KAP/01_Source_Inventory/`.

```json
{
  "sources": {
    "manus_api": {
      "last_sync_date": "2026-07-01T22:00:00Z",
      "high_water_mark_id": "x9fcuVXGiPyNhmXqLHRr87",
      "high_water_mark_timestamp": 1719871200,
      "status": "HEALTHY"
    },
    "github_yos_master": {
      "last_sync_date": "2026-06-30T10:00:00Z",
      "last_commit_hash": "19643d2a7fa56504b9d47039ba9b44eda444a503",
      "status": "HEALTHY"
    }
  }
}
```

## 5. Handling Deletions and Modifications

- **Append-Only Sources (e.g., Chats):** Easy delta. Just fetch new IDs.
- **Mutable Sources (e.g., Notion, Obsidian):** Requires checking `last_edited_time` or file modification dates. If an item is modified, it must be re-acquired and overwrite the old raw file in Git. The normalization layer (WP3) must then be smart enough to update the existing Mem0/Notion entry rather than creating a duplicate.
- **Deletions:** If a source system supports webhooks for deletions, KAP should mark the local file as `[DELETED]` but preserve the history in Git. If not, periodic full-sync audits (WP1) are required to detect orphaned local files.
