---
uid: 73hnoBd0jBJzcAsbUJGuVW
session_url: https://manus.im/app/73hnoBd0jBJzcAsbUJGuVW
session_title: "Instagram MCP Connector — Live Test & Capability Brief"
date: 2026-05-04
project: "Y-OS Tool Infrastructure"
language: en
depth: quick
length: short
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 15:19
referenced_sessions: []
referenced_artifacts: []
referenced_urls: ["https://manus.im/app/73hnoBd0jBJzcAsbUJGuVW"]
input_files: []
message_count: 6
---

# Instagram MCP Connector — Live Test & Capability Brief

> **Session:** [73hnoBd0jBJzcAsbUJGuVW](https://manus.im/app/73hnoBd0jBJzcAsbUJGuVW) | **Date:** 2026-05-04 | **Project:** Y-OS Tool Infrastructure | **Language:** en

## 📋 SESSION CARD

### 🧭 Executive Summary
Manus tested the Instagram MCP connector live against the `@yannick_jolliet` Business account, confirming all 4 tools operational and fetching real account data, post list, and post insights. The session produced a structured capability brief with live data including 7 posts, follower counts, and per-post engagement metrics. This validates the connector as ready for use in future automation or analytics workflows.

---

### 🎯 Context & Intent
The user wanted to verify that the Instagram MCP connector was functional, understand its full capabilities, and see proof of live data retrieval — essentially a smoke test and capability onboarding in one session.

---

### ✅ What Was Done
1. Read the tool-router skill to identify available Instagram tools
2. Confirmed 4 tools operational within the connector
3. Fetched live account info for `@yannick_jolliet` (followers, following, post count)
4. Fetched full post list (7 posts) with type, engagement, and date metadata
5. Fetched post-level insights for 2 posts
6. Compiled and delivered a structured Instagram MCP Connector Test Report

---

### 💡 Key Insights
- **Connector is live and fully operational** — all 4 tools confirmed working
- **Account is a Business account**, which enables access to insights (not available on personal accounts)
- **Engagement is low on recent posts** — the 2 most recent posts (2026-02-17 and 2026-01-01) have 0 and 2 likes respectively; older posts perform better
- **Post history spans 13 years** (2013–2026), suggesting the account predates conversion to Business
- **4 tools available** — likely: get_account_info, get_posts, get_post_insights, and one additional (possibly publish or comment — not explicitly named in the transcript excerpt)
- The connector is suitable for analytics, reporting, and potentially publishing automation workflows

---

### 📦 Outputs Produced
- **[data]** `instagram-connector-test-report`: Live test report with account info, 7-post list, and insights — delivered inline in session

---

### ⚠️ Open Items & Blockers
- The full transcript was cut off before the post insights data was shown — insights content for the 2 fetched posts is **not visible** in this archive [INCERTAIN]
- The 4th tool's identity is not explicitly named in the available transcript [INCERTAIN]
- No information on rate limits, token expiry, or authentication method for the connector

---

### 🔁 Next Steps
1. Document the 4 tool names and their full parameter schemas for the Y-OS skill registry
2. Review post insights data (reach, impressions, saves) once full transcript is confirmed
3. Consider building an Instagram analytics dashboard or periodic reporting skill using this connector
4. Test publish/schedule capabilities if the 4th tool supports content creation
5. Set up recurring account snapshot to track follower growth over time

---

### 🔗 Links & References
- 🌐 https://manus.im/app/73hnoBd0jBJzcAsbUJGuVW
- 📄 Instagram Business Account: `@yannick_jolliet`

---

### 🧠 Resume Hint
The Instagram MCP connector is live with 4 tools against `@yannick_jolliet` Business account; next agent should document full tool schemas and explore the 4th tool's capabilities (possibly publish), then build an analytics or automation skill on top.

---

### 🏷️ Tags
`instagram` `mcp-connector` `social-media` `tool-testing` `analytics`

---

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 6 messages — 2026-05-04

**[2026-05-04 12:21] USER:** Help me test the Instagram connector and show me how to use its feature (e.g. show any data you fetched with it). Give me a brief about its capabilities.

**[2026-05-04 12:21] MANUS:** On it — I'll read the tool-router skill first, then explore the Instagram MCP connector, fetch live data, and give you a full capability brief.

**[2026-05-04 12:21] MANUS:** 4 tools confirmed. Fetching account info, post list, and post insights now.

**[2026-05-04 12:22] MANUS:** ## Instagram MCP Connector — Test Report

---

### 1. Connector Status

**Live. All 4 tools operational.** Connected to the Business account `@yannick_jolliet`.

---

### 2. Account Info (live fetch)

| Field | Value |
|---|---|
| Username | @yannick_jolliet |
| Display Name | Yannick Jolliet (Yogeshwar) |
| Followers | 319 |
| Following | 113 |
| Total Posts | 7 |

---

### 3. Post List (live fetch — 7 posts total)

| # | Type | Likes | Comments | Date |
|---|---|---|---|---|
| 1 | IMAGE | 0 | 0 | 2026-02-17 |
| 2 | VIDEO (Reel) | 2 | 0 | 2026-01-01 |
| 3 | VIDEO (Reel) | 9 | 0 | 2024-08-09 |
| 4 | CAROUSEL | 15 | 2 | 2024-05-06 |
| 5 | VIDEO | 22 | 2 | 2019-02-11 |
| 6 | CAROUSEL | 17 | 0 | 2018-08-19 |
| 7 | IMAGE | 27 | 0 | 2013-12-16 |

---

### 4. Post Insights (live fetch — 2 posts)
