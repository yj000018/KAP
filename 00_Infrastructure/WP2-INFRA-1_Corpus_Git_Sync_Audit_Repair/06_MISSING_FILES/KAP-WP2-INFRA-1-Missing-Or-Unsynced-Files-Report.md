# KAP-WP2-INFRA-1-Missing-Or-Unsynced-Files-Report

| missing_or_unsynced_item | expected_source | current_status | reason | recovery_action | priority |
|---|---|---|---|---|---|
| Git remote / push | KAP Git repo | ❌ NOT PUSHED | GitHub connector not enabled | Enable GitHub connector → `git remote add origin` → `git push` | HIGH |
| M6C block extraction | WP2-M6C | ⚠️ IN PROGRESS (236/363 pages) | Still running | Wait for completion | HIGH |
| M6C in Git | WP2-M6C | ⚠️ NOT YET COMMITTED | M6C still running during INFRA-1 | Run second commit after M6C completes | MEDIUM |
| Manus Task full details | WP2-M4 | ⚠️ DEFERRED | 10,000+ tasks — too large | Filtered subset extraction in WP2-M8 | LOW |
| KOR Knowledge Object Repository | Notion | ❌ EMPTY | DB has 0 entries | Nothing to extract | LOW |
| Verbatim Pages DB | Notion | ❌ NOT FOUND | No dedicated Verbatim DB | Content embedded in session pages | LOW |
| ChatGPT OAuth on Y-world | Notion | ❌ NOT CONFIGURED | User action required | Settings > Connected Apps > Notion | MEDIUM |
