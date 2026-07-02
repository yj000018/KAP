---
uid: aWTQQSpS80yDbbrX05H7gb
session_url: https://manus.im/app/aWTQQSpS80yDbbrX05H7gb
session_title: "Sentry MCP Connector — Capability Test & Live Org Validation"
date: 2026-05-04
project: "Y-OS Infrastructure / Connectors"
language: mixed
depth: moderate
length: short
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 15:20
referenced_sessions: []
referenced_artifacts: ["Sentry Connector Capability Brief"]
referenced_urls: ["https://manus.im/app/aWTQQSpS80yDbbrX05H7gb"]
input_files: []
message_count: 5
---

# Sentry MCP Connector — Capability Test & Live Org Validation

> **Session:** [aWTQQSpS80yDbbrX05H7gb](https://manus.im/app/aWTQQSpS80yDbbrX05H7gb) | **Date:** 2026-05-04 | **Project:** Y-OS Infrastructure / Connectors | **Language:** mixed

## 📋 SESSION CARD

### 🧭 Executive Summary
Yannick tested the Sentry MCP connector within the Y-OS environment, triggering a live exploration of its tools and data. Manus successfully connected to the `yos-00` Sentry organization, enumerated 14 available tools, and produced a structured capability brief. The organization is properly wired but currently empty (no projects or events), making this a validation/discovery session rather than an operational one.

### 🎯 Context & Intent
The user wanted to validate that the Sentry MCP connector was functional, understand its full range of capabilities, and see concrete evidence of live data retrieval — essentially a "does it work and what can it do?" audit.

### ✅ What Was Done
1. Connected to the Sentry MCP connector and authenticated against the `yos-00` organization
2. Enumerated all 14 available tools exposed by the connector
3. Fetched live organizational data from Sentry to confirm connectivity
4. Verified the absence of projects and events in the current org state
5. Produced a structured capability brief document summarizing findings

### 💡 Key Insights
- The Sentry connector exposes **14 tools**, ranging from basic project/issue search to AI-powered root cause analysis (Sentry Seer)
- The `yos-00` organization is **successfully connected** and authenticated
- The org is currently **empty** (no projects, no events) — the connector is ready but has no data to act on yet
- The most advanced capability noted is **Seer (AI root cause analysis)**, which is a high-value tool once real projects/events exist
- This session establishes a baseline: the plumbing works, the next step is populating the org

### 📦 Outputs Produced
- **[doc]** `Sentry Connector Capability Brief`: Structured summary of 14 tools, live org status, and usage guidance for the `yos-00` organization

### ⚠️ Open Items & Blockers
- The `yos-00` organization has **no projects or events** — most connector tools cannot be meaningfully demonstrated until data exists
- [INCERTAIN] It is unclear whether projects need to be created manually in Sentry or if they will be auto-provisioned by Y-OS workflows
- [INCERTAIN] The full capability brief document was described but not reproduced in the transcript — content details may be incomplete

### 🔁 Next Steps
1. Create at least one Sentry project within the `yos-00` organization to enable real tool testing
2. Generate or ingest a test error event to validate issue retrieval, grouping, and Seer analysis tools
3. Re-run a capability demo session once data is present to document all 14 tools with live examples
4. Consider integrating Sentry connector triggers into Y-OS error-monitoring workflows

### 🔗 Links & References
- 🌐 https://manus.im/app/aWTQQSpS80yDbbrX05H7gb
- 📄 Sentry Connector Capability Brief (produced in-session, attached to Manus output)

### 🧠 Resume Hint
The Sentry MCP connector is confirmed working and connected to org `yos-00`, but the org is empty — the next agent should focus on creating a project and seeding an error event to test the connector's 14 tools in a live data context.

### 🏷️ Tags
`sentry` `mcp-connector` `integration-testing` `y-os-infra` `error-monitoring`

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 5 messages — 2026-05-04

**[2026-05-04 12:20] USER:** Help me test the Sentry connector and show me how to use its feature (e.g. show any data you fetched with it). Give me a brief about its capabilities.

**[2026-05-04 12:21] MANUS:** On it — I'll explore the Sentry MCP connector, fetch live data, and give you a structured capability brief.

**[2026-05-04 12:23] MANUS:** Voici le document de synthèse des capacités du connecteur Sentry, basé sur les données live récupérées de ton organisation. Le connecteur offre 14 outils puissants allant de la recherche de base à l'analyse de cause racine par IA (Seer). L'organisation `yos-00` est bien connectée, bien qu'elle ne contienne pas de projets ou d'événements pour le moment.

Tu trouveras tous les détails dans le document joint.
