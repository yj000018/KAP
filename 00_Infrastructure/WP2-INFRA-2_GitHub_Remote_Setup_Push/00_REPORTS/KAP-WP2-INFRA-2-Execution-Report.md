# KAP WP2-INFRA-2 — GitHub Remote Setup & Push
**Sprint ID:** WP2-INFRA-2  
**Date:** 2026-07-01  
**Status:** ✅ COMPLETE — CORPUS_PUSHED_TO_GITHUB

## Summary
| Field | Value |
|---|---|
| GitHub Repo | https://github.com/yj000018/KAP |
| Visibility | Private |
| Branch | main |
| Last Commit | 04e0d4651bebab81e204a0fcbf5f96b9298fd43c |
| Remote URL | https:***@github.com/yj000018/KAP.git |
| PAT Token | KAP-Corpus-Push-2026 (expires Jul 31, 2026) |
| PAT Scopes | repo |
| Push Status | ✅ SUCCESS |
| Large File Warning | all_tasks_raw.json (51.13 MB > 50 MB limit) |

## Token Audit (Page 1)
| Token Name | Scopes | Last Used | Expiry |
|---|---|---|---|
| KAP-Corpus-Push-2026 (NEW) | repo | Just now | Jul 31 2026 |
| Manus-yOS-full-access | repo | Last week | No expiry ⚠️ |
| manus-push | ALL | Last 2 weeks | Sep 19 2026 |
| manus-yos-voice-gateway | ALL | Never | No expiry ⚠️ |
| 12.6.2026 | ALL | Never | Sep 11 2026 |
| 12.6.2006 | ALL | Never | Sep 11 2026 |
| 6.6.2006 | ALL | Never | Sep 4 2026 |
| FULL PAT | ALL | Never | No expiry ⚠️ |
| GENERAL MANUS-yOS TOKEN | ALL | Last 2 months | No expiry ⚠️ |
| Manus-Full-Access (no expiry) | ALL | Last 4 weeks | No expiry ⚠️ |

## Cleanup Recommendation
**Tokens to delete immediately:** 12.6.2026, 12.6.2006, 6.6.2006 (never used, expired-ish)  
**Tokens to review:** FULL PAT, GENERAL MANUS-yOS TOKEN, manus-yos-voice-gateway (no expiry, broad scopes)  
**Keep:** manus-push (active, has expiry), Manus-yOS-full-access (active), KAP-Corpus-Push-2026 (new)

## Blockers
- all_tasks_raw.json (51.13 MB) exceeds GitHub 50 MB soft limit — consider git-lfs or exclude from tracking
- ChatGPT Notion OAuth still pending

## Next Sprint
**WP2-INFRA-3** — Token cleanup + git-lfs setup for large files + ChatGPT Notion OAuth
