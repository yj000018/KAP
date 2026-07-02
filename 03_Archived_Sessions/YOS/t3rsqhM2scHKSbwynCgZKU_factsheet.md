---
uid: t3rsqhM2scHKSbwynCgZKU
session_url: https://manus.im/app/t3rsqhM2scHKSbwynCgZKU
session_title: "Tally MCP Connector — Test, Capability Brief & Notion Onboarding"
date: 2026-06-16
project: "Y-OS Tools Registry / Architecture Hub"
language: mixed
depth: moderate
length: short
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 13:12
referenced_sessions: []
referenced_artifacts: []
referenced_urls: ["https://app.notion.com/p/38635e218cf88126b435cc2a88b8a748", "https://app.notion.com/p/38635e218cf88162880fda0147acb164", "https://manus.im/app/t3rsqhM2scHKSbwynCgZKU"]
input_files: []
message_count: 19
---

# Tally MCP Connector — Test, Capability Brief & Notion Onboarding

> **Session:** [t3rsqhM2scHKSbwynCgZKU](https://manus.im/app/t3rsqhM2scHKSbwynCgZKU) | **Date:** 2026-06-16 | **Project:** Y-OS Tools Registry / Architecture Hub | **Language:** mixed

## 📋 SESSION CARD

### 🧭 Executive Summary
The session tested the Tally MCP connector end-to-end, including OAuth authentication and live data extraction from a real workspace. A full Factsheet and Tools Registry entry were produced and published to Notion following the standard Y-OS tool onboarding protocol. Tally is now officially registered as a Production-grade MCP connector in the Y-OS architecture.

### 🎯 Context & Intent
User wanted to validate the Tally MCP connector's functionality, explore its capabilities with live data, and permanently document it in the Y-OS tooling infrastructure (Notion Factsheet + Tools Registry) — consistent with how all other tools are tracked.

### ✅ What Was Done
1. Triggered Tally MCP OAuth flow and awaited user authorization (completed June 21 after initial June 16 attempt)
2. Listed available Tally MCP tools post-authentication
3. Queried the user's live Tally account and retrieved workspace (`mDAR7E`) and form data (`9qrP95` — "Test form", empty)
4. Compiled a capability brief covering form block creation, ledger management, conditional logic, CSS injection, and brand extraction
5. Read `tools-registry` skill to determine correct Notion archiving structure
6. Created a Tally Factsheet page in the Y-OS Architecture Hub on Notion
7. Created a Tally entry in the Y-OS Tools Registry v2 with all standard metadata fields

### 💡 Key Insights
- Tally MCP requires OAuth, which introduced a multi-day delay between session start and productive work — OAuth friction is a recurring onboarding cost for MCP connectors
- Live workspace had one form ("Test form") with zero submissions — connector is functional but no meaningful form data was available to demo
- The session confirmed the tool onboarding protocol works: test → capability brief → Factsheet → Registry entry
- Tally is categorized as **Automation / Workflows**, type **MCP Connector**, auth **OAuth MCP**, pricing **Freemium**
- Factsheet follows the 6-section standard: Synthèse, Executive Summary, Capacités, Limites/Bugs, Pricing, Intégrations Y-OS

### 📦 Outputs Produced
- **[doc]** `Tally Factsheet — Notion`: https://app.notion.com/p/38635e218cf88126b435cc2a88b8a748 — Full 6-section capability factsheet with live test findings and workarounds
- **[doc]** `Y-OS Tools Registry v2 — Tally entry`: https://app.notion.com/p/38635e218cf88162880fda0147acb164 — Standardized registry row with status, category, auth type, pricing, and factsheet link
- **[data]** `Live Tally workspace snapshot`: Workspace `mDAR7E`, Form `9qrP95` ("Test form"), 0 submissions

### ⚠️ Open Items & Blockers
- No real form data exists yet — Tally capabilities around submission retrieval and analysis are untested against real submissions
- [INCERTAIN] CSS injection and brand extraction features were documented but not live-tested during this session
- OAuth token persistence across sessions has not been verified — re-auth may be required in future sessions

### 🔁 Next Steps
1. Create a real test form with submissions in Tally to validate submission retrieval, filtering, and export capabilities
2. Live-test the brand extraction feature by pointing it at a real website
3. Live-test conditional logic block creation by building a non-trivial form via MCP
4. Verify OAuth token longevity — confirm whether re-auth is needed per session or persists
5. Apply same onboarding protocol to the next untested MCP connector in the Y-OS stack

### 🔗 Links & References
- 🌐 https://app.notion.com/p/38635e218cf88126b435cc2a88b8a748 — Tally Factsheet (Architecture Hub)
- 🌐 https://app.notion.com/p/38635e218cf88162880fda0147acb164 — Tools Registry entry (Y-OS Tools Registry v2)
- 🔗 session:t3rsqhM2scHKSbwynCgZKU — This session

### 🧠 Resume Hint
Tally MCP connector is authenticated and registered in Notion (Factsheet + Registry); next step is testing with real form submissions and live-validating untested capabilities (brand extraction, conditional logic).

### 🏷️ Tags
`tally` `mcp-connector` `tools-registry` `tool-onboarding` `notion-architecture` `oauth`

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 19 messages — 2026-06-16

**[2026-06-16 09:07] USER:** Help me test the Tally connector and show me how to use its feature (e.g. show any data you fetched with it). Give me a brief about its capabilities.

**[2026-06-16 09:07] MANUS:** Sur it — je lis le skill yos-optimizer d'abord, puis j'explore le connecteur Tally via MCP.

**[2026-06-16 09:11] MANUS:** Le connecteur Tally nécessite une **autorisation OAuth** pour s'authentifier. Un flux d'auth a été déclenché.

**Action requise :** Ouvre l'URL d'autorisation qui a été générée (elle devrait apparaître dans ton navigateur ou dans une notification Manus) et connecte-toi avec ton compte Tally.

Une fois l'auth complétée, dis-moi et je reprends immédiatement les tests.

**[2026-06-16 18:47] USER:** Continue

**[2026-06-16 18:47] MANUS:** Relance du tool list Tally MCP...

**[2026-06-21 11:26] USER:** Auth ok

**[2026-06-21 11:26] MANUS:** Auth confirmée — je liste les outils Tally et tire les données live.

**[2026-06-21 11:28] MANUS:** L'authentification OAuth est passée et le connecteur Tally est 100% opérationnel. 

J'ai interrogé ton compte et extrait les données en live : tu as un workspace (`mDAR7E`) contenant un formulaire nommé "Test form" (`9qrP95`), actuellement vide et sans soumission.

J'ai rédigé un brief complet sur les capacités du connecteur (création de blocs, gestion du ledger, logique conditionnelle, injection CSS, extraction de marque) et le détail des données live. 

Le document est en pièce jointe. Veux-tu que l'on teste une création de formulaire complète ou une extraction de design depuis un site web ?

**[2026-06-21 11:31] USER:** Bien
Garde en mémoire ces capabilities et use cases, comme pour tous les autres outils avec même structure type Fact Sheet, dans bon endroit dans notion

**[2026-06-21 11:31] MANUS:** Je lis le skill tools-registry avant d'agir.

**[2026-06-21 11:32] MANUS:** Tout est en place dans Notion. Voici le récap :

**Factsheet Tally** — Architecture Hub
→ https://app.notion.com/p/38635e218cf88126b435cc2a88b8a748

**Entrée Tools Registry** (🗂️ Y-OS Tools Registry v2)
→ https://app.notion.com/p/38635e218cf88162880fda0147acb164

**Ce qui a été archivé :**

| Champ | Valeur |
|---|---|
| Status | 🟢 Production |
| Category | Automation / Workflows |
| Tool Type | MCP Connector |
| Auth | OAuth MCP |
| Pricing | Freemium |
| Factsheet | Lien direct vers la page détaillée |

La Factsheet couvre les 6 sections standard (Synthèse, Executive Summary, Capacités, Limites/Bugs, Pricing, Intégrations Y-OS) avec les workarounds issus du test live du 21 Juin 2026.

Pour les prochains outils, même protocole : test → factsheet → Registry + page Notion.
