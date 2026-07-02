# Runbook: New Source Baseline

| step | action | output | gate |
|---|---|---|---|
| 1 | Define source in WP1 | `source_registry.schema.json` instance | Gate 1 |
| 2 | Fetch all historical data | Raw files | - |
| 3 | Generate source cards & checksums | `_SOURCE_CARD.md`, `manifest.json` | Gate 2 |
| 4 | Commit to Git | Git hash | Gate 3 |
| 5 | Update registry status | Status = `BASELINE_CAPTURED` | - |
