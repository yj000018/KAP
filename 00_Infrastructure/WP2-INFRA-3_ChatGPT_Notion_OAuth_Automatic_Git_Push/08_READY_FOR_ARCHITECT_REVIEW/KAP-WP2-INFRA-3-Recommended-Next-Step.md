# KAP WP2-INFRA-3 — Recommended Next Sprint

**Generated:** 2026-07-01T21:00:47Z

## WP2-INFRA-4 — ChatGPT OAuth Confirmation + Credential Consolidation

**Priority:** HIGH  
**Estimated duration:** 20 min

### Objectives

1. **Confirm ChatGPT OAuth** — verify Yannick completed Notion OAuth in ChatGPT Settings
2. **Test ChatGPT Notion access** — ask ChatGPT to search "Manus Memory Sessions" and confirm results
3. **Consolidate Mem0 keys** — identify canonical key, store in Manus project file
4. **Store Notion token** in Manus project file for persistence across sessions
5. **PAT renewal plan** — create reminder for Jul 31 2026 PAT expiry
6. **GitHub Actions first run** — verify `kap-corpus-validate.yml` ran successfully after INFRA-3 push

### Canonical Credentials to Consolidate

| service | key | status |
|---|---|---|
| Notion | `<NOTION_TOKEN_IN_MANUS_SECRETS>` | ✅ Valid |
| GitHub PAT | `<GITHUB_PAT_IN_MANUS_SECRETS>` | ✅ Valid (exp Jul 31) |
| Mem0 | `m0-AaySh4Tbbwf2DA5TpXzqcBJSiDnFRIlFrF695fJE` | ✅ Valid (to confirm) |
| ChatGPT OAuth | pending | ❌ Requires user action |
