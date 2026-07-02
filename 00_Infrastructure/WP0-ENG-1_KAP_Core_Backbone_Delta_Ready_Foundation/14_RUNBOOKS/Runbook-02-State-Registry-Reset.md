# Runbook 02: State Registry Reset

If the `Source_State_Registry.json` becomes corrupted or a sync fails midway, leaving the registry out of sync with the actual files on disk:

1. Identify the affected source family (e.g., `manus_api`).
2. Scan the corresponding raw acquisition directory (e.g., `03_Archived_Sessions/raw_json/`).
3. Identify the most recent valid file based on the file modification timestamp or the timestamp embedded in the filename/content.
4. Open `/home/ubuntu/KAP/01_Source_Inventory/KAP-Source-State-Registry.json`.
5. Locate the entry for the affected source.
6. Manually update the `high_water_mark_id` and `high_water_mark_timestamp` to match the most recent valid file.
7. Change the `status` to `MANUAL_RESET`.
8. Run a dry-run sync to verify the delta process picks up correctly from the new mark.
