# Runbook 01: Manual API Fallback

If an API (e.g., Manus task.list) is rate-limited or broken by pagination artifacts:

1. Obtain the exact target URLs or IDs from the user or a secondary index (e.g., Notion).
2. Create a text file containing one URL/ID per line.
3. Use a targeted fetch script (like `01_collect_session.py`) that iterates over the list with a 2-second delay between requests to avoid triggering further rate limits.
4. Ensure the output files follow the standard naming convention (`{id}_verbatim.json`) and are placed in the correct `raw_json` directory.
5. Generate the `_SOURCE_CARD.md` manually or via script, noting the fallback method in the provenance section `acquisition_method: MANUAL_FALLBACK_LIST`.
