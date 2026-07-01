# KAP WP2-INFRA-3 — ChatGPT Architect Notion OAuth Plan

**Generated:** 2026-07-01T21:00:47Z

## 1. Current Access Situation

| Actor | Access Method | Workspace | Status |
|---|---|---|---|
| Manus | Internal integration token (`ntn_14464158968...`) | Y-world | ✅ FULL ACCESS — 100+ DBs |
| ChatGPT | OAuth via ChatGPT Settings > Connected Apps | Y-world | ❌ NOT YET CONFIGURED |

## 2. What ChatGPT Can Access Directly Now

ChatGPT does **not** currently have direct Notion access. It receives data only via:
- Files transferred manually (ZIP, MD)
- Content copy-pasted into the conversation
- GitHub public repo (`https://github.com/yj000018/KAP`) — readable without auth

## 3. OAuth Connector Path

ChatGPT supports Notion OAuth natively via the **Notion connector** in ChatGPT Settings.

**OAuth flow:**
1. ChatGPT Settings → Connected Apps → Notion → Connect
2. Notion OAuth popup → Select workspace: **Y-world** (kjimene648)
3. Select access: **All pages** (not specific pages)
4. Authorize → ChatGPT receives read/write access token automatically

**This is a standard OAuth2 flow — no token copy-paste required.**

## 4. What Yannick Must Click

| step | actor | action | expected_result | fallback |
|---|---|---|---|---|
| 1 | Yannick | Open ChatGPT → Settings → Connected Apps | See list of connectors | — |
| 2 | Yannick | Click "Notion" → Connect | OAuth popup opens | Try browser refresh |
| 3 | Yannick | Select workspace: Y-world | Y-world workspace shown | Check Notion login |
| 4 | Yannick | Select "All pages" access | Full workspace access | Select manually |
| 5 | Yannick | Click Authorize | ChatGPT confirms connection | Re-try OAuth |
| 6 | ChatGPT | Test: "Search Notion for Manus Memory" | Returns results | Use GitHub fallback |

## 5. Pages/Databases to Share

With "All pages" selection in OAuth, all of Y-world is shared automatically.

Key databases ChatGPT needs:
- `5e51ded4` — Manus Memory Sessions (363 entries)
- `85f89b4e` — Y-OS Tools Registry v2
- `533401fa` — Manus Memory Hub
- `f2c0bc6c` — KOR Knowledge Object Repository

## 6. Access Level

**Recommended: Read-only** for ChatGPT Architect.

ChatGPT should read/search Notion but not write. Manus writes to Notion; ChatGPT reads.

## 7. Risks / Limitations

| risk | severity | mitigation |
|---|---|---|
| OAuth token expires | Low | ChatGPT auto-refreshes |
| ChatGPT writes unwanted content | Medium | Set read-only if option available |
| Y-world workspace not shown in OAuth | Low | Ensure logged into correct Notion account |
| ChatGPT Notion connector not available in your plan | Medium | Use GitHub fallback |

## 8. Fallback Path

If OAuth unavailable:
1. **GitHub** — All KAP sprint outputs are at `https://github.com/yj000018/KAP` (public)
2. **Manus-to-ChatGPT file transfer** — Manus exports MD/JSON, attaches to ChatGPT session
3. **Shared Notion page** — Yannick creates a public Notion page with key data

**Recommended fallback: GitHub** — zero manual effort, always up to date after each sprint push.
