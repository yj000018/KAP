# Runbook: Existing Source Delta

| step | action | output | gate |
|---|---|---|---|
| 1 | Read State Registry | `last_seen_item_count` / hash | - |
| 2 | Fetch only new/changed items | Raw files | Gate 5 |
| 3 | Generate delta manifest | `delta_manifest.schema.json` | Gate 2 |
| 4 | Commit to Git | Git hash | Gate 3 |
| 5 | Update registry | New high-water mark | - |
