# Runbook: Manual UI Fallback

| step | action | output | gate |
|---|---|---|---|
| 1 | Extract data via UI/browser | Raw text/JSON | - |
| 2 | Format as standard raw file | `{id}_verbatim.json` | - |
| 3 | Create manual source card | `_SOURCE_CARD.md` (flagged manual) | Gate 2 |
| 4 | Commit to Git | Git hash | Gate 3 |
