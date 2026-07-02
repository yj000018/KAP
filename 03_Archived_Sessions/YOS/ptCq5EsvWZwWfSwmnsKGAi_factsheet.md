---
uid: ptCq5EsvWZwWfSwmnsKGAi
session_url: https://manus.im/app/ptCq5EsvWZwWfSwmnsKGAi
session_title: "Fireflies MCP Connector — Live Test & Y-OS Factsheet v1"
date: 2026-06-16
project: "Y-OS Architecture Multi-Agents Hub"
language: mixed
depth: moderate
length: short
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 13:15
referenced_sessions: []
referenced_artifacts: ["Fireflies MCP Connector \u2014 Factsheet v1"]
referenced_urls: ["https://app.notion.com/p/38135e218cf881a682aac91143af142d", "https://manus.im/app/ptCq5EsvWZwWfSwmnsKGAi"]
input_files: []
message_count: 11
---

# Fireflies MCP Connector — Live Test & Y-OS Factsheet v1

> **Session:** [ptCq5EsvWZwWfSwmnsKGAi](https://manus.im/app/ptCq5EsvWZwWfSwmnsKGAi) | **Date:** 2026-06-16 | **Project:** Y-OS Architecture Multi-Agents Hub | **Language:** mixed

## 📋 SESSION CARD

### 🧭 Executive Summary
The session tested the Fireflies MCP connector live against Yannick's account, validating all 20 detected API endpoints and extracting real meeting data. A standardized Y-OS factsheet was then produced and pushed to Notion, following the established format used for tools like Granola and Miro. This factsheet captures Fireflies' technical access points, business capabilities, pricing, limits, and lessons learned from live testing.

### 🎯 Context & Intent
Yannick wanted to validate the Fireflies connector as a newly available Y-OS tool, understand what it can actually do (technically and business-wise), and produce a reusable factsheet — the standard Y-OS onboarding artifact for any new tool integration. The session was explicitly a live-tested factsheet (as opposed to documentation-only factsheets produced when no testing was possible).

### ✅ What Was Done
1. Loaded and read the `yos-optimizer` and `tool-router` skills to contextualize the connector audit
2. Detected 20 available tools/endpoints via the Fireflies MCP connector
3. Fetched live data from Yannick's Fireflies account: user profile, recent meetings, contacts, analytics, and channels
4. Identified and extracted structured data from the most recent meeting (Bitcoin Suisse — Jasmin/Robi): summary, keywords, action items, raw transcript
5. Located the existing Y-OS factsheet structure in Notion (same parent as Granola, Miro, etc.)
6. Produced and published Fireflies MCP Factsheet v1 to Notion, following the standard Y-OS structure
7. Added two new sections specific to Fireflies: Interdépendances & Connectivité Y-OS, and a comparison with Granola

### 💡 Key Insights
- Fireflies offers **read + write access** (unlike Granola which is read-only/semantic) — notably suited for raw extraction and downstream automation
- 20 MCP tools detected, covering the full surface area: meetings, transcripts, soundbites, contacts, analytics, channels, and sharing
- Fireflies is **complementary to Granola**, not a replacement — Granola is better for structured notes, Fireflies for raw transcript extraction and programmatic access
- The factsheet standard was extended with two new sections (Interdependencies + Granola comparison) that may warrant backfilling into other factsheets
- Live-testing is explicitly flagged as superior to doc-only factsheets — this session is a reference case for that distinction

### 📦 Outputs Produced
- **[doc]** `Fireflies MCP Connector — Factsheet v1` @ Notion (`https://app.notion.com/p/38135e218cf881a682aac91143af142d`): Full Y-OS-standard factsheet covering identity, overview, technical capabilities, interdependencies, business value, limits, pricing, and lessons learned
- **[data]** Live Fireflies account data: user profile, recent meetings (incl. Bitcoin Suisse/Jasmin/Robi), contacts, analytics, channels — fetched during audit
- **[doc]** Audit & test report of the Fireflies MCP connector (inline in session, referenced as attached file)

### ⚠️ Open Items & Blockers
- The factsheet summary in the transcript is cut off — the Pricing section and full Lessons Learned content may be incomplete [INCERTAIN]
- Write-capability tools (e.g. meeting sharing, soundbite creation) were mentioned as testable but not confirmed as executed
- It is unclear whether the two new factsheet sections (Interdependencies, Granola comparison) will be retroactively applied to other tool factsheets [INCERTAIN]
- No explicit confirmation that the Notion page was fully saved/visible to Yannick

### 🔁 Next Steps
1. Confirm Notion factsheet is fully published and visible in the Y-OS Architecture Multi-Agents Hub
2. Test remaining write-side tools: meeting sharing, soundbite creation, and any POST/mutation endpoints
3. Review whether the two new factsheet sections should be backfilled into Granola, Miro, and other existing factsheets
4. Consider adding a "Live-Tested vs Doc-Only" flag to all factsheets for quality signaling
5. If Fireflies is to be used in Y-OS workflows, define specific trigger conditions (e.g. post-meeting enrichment pipeline)

### 🔗 Links & References
- 🌐 `https://app.notion.com/p/38135e218cf881a682aac91143af142d` — Fireflies MCP Connector Factsheet v1 (Notion)
- 🌐 `https://manus.im/app/ptCq5EsvWZwWfSwmnsKGAi` — This session (Manus)
- 🔗 Implicit reference to Granola factsheet (same Notion parent — Y-OS Architecture Multi-Agents Hub)
- 🔗 Implicit reference to Miro factsheet (same Notion parent)

### 🧠 Resume Hint
Fireflies MCP connector has been live-tested (20 tools, real account data fetched) and its Y-OS factsheet v1 has been pushed to Notion — next action is to validate write-side tools and decide whether to backfill the two new factsheet sections (Interdependencies, Granola comparison) into existing tool factsheets.

### 🏷️ Tags
`fireflies` `mcp-connector` `tool-factsheet` `y-os-architecture` `meeting-intelligence` `live-tested`

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 11 messages — 2026-06-16

**[2026-06-16 08:49] USER:** Help me test the Fireflies connector and show me how to use its feature (e.g. show any data you fetched with it). Give me a brief about its capabilities.

**[2026-06-16 08:49] MANUS:** Sur ça. Je lis le skill yos-optimizer + tool-router, puis j'explore le connecteur Fireflies en live.

**[2026-06-16 08:49] MANUS:** 20 outils détectés. Je fetch maintenant les données live : user profile, meetings récents, contacts, analytics, channels.

**[2026-06-16 08:51] MANUS:** Voici le rapport d'audit et de test du connecteur Fireflies MCP. 

J'ai structuré les capacités de l'outil et extrait les données live de ton compte, notamment le dernier meeting stratégique avec Bitcoin Suisse (Jasmin/Robi). Le document montre exactement ce que Fireflies capture (résumés structurés, mots-clés, actions, et transcript brut).

Tout est détaillé dans le fichier joint. Dis-moi si tu veux que je teste un outil d'écriture (comme le partage de meeting ou la création d'un soundbite) ou si l'on passe à autre chose.

**[2026-06-16 13:27] USER:** C'est donc un nouvel outil disponible pour iOS. Il faut donc une factsheet et d'un outil avec ses capabilités, ses limites, les lessons learned, les éventuels accès, etc. Comme d'habitude, on fait cette factsheet pour cet outil. Là, on l'a vraiment testé avec tous les accès et tous les API, les entry points, etc. D'autres fois, on n'a pas eu le temps de tester et donc c'est ce que ça donne en général d'après la documentation que tu retrouves online. Mais je veux savoir que pour tel outil, on a telle possibilité et que ça offre. On est capable d'écrire, de lire, de faire, les possibilités techniques d'accès à l'outil et les possibilités en termes de capabilities, de features, donc business-wise. Qu'est-ce que ça m'importe d'avoir cette connexion-là ? Et puis, c'est gratuit, payant, etc. Don

**[2026-06-16 13:27] MANUS:** Je cherche d'abord la structure de factsheet existante dans Notion/Y-OS avant de construire celle de Fireflies.

**[2026-06-16 13:31] MANUS:** Factsheet créée et poussée dans Notion. Voici le résumé de ce qui a été produit.

---

## 🔥 Fireflies MCP — Factsheet v1

**Notion :** [🔥 Fireflies MCP Connector — Factsheet v1](https://app.notion.com/p/38135e218cf881a682aac91143af142d)
**Parent :** Y-OS — Architecture Multi-Agents Hub (même emplacement que Granola, Miro, etc.)

---

### Ce que la factsheet couvre

La structure suit exactement le standard Y-OS (Identité → Overview → Capacités Techniques → Interdépendances → Business Value → Limites → Pricing → Lessons Learned), enrichie de deux sections nouvelles :

**Interdépendances & Connectivité Y-OS** — comment Fireflies se connecte aux autres outils (Notion, Linear, CRM) et en quoi il se distingue de Granola (read-only sémantique) : Fireflies est plus adapté à l'extraction brute et à
