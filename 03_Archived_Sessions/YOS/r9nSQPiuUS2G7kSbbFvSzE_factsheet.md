---
uid: r9nSQPiuUS2G7kSbbFvSzE
session_url: https://manus.im/app/r9nSQPiuUS2G7kSbbFvSzE
session_title: "Granola Connector Test & Factsheet Creation – Y-OS Tool Hub"
date: 2026-06-16
project: "Y-OS Multi-Agent Architecture"
language: mixed
depth: substantial
length: medium
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 13:16
referenced_sessions: []
referenced_artifacts: ["Granola Connector Test Report", "Granola Factsheet \u2013 Notion"]
referenced_urls: ["https://manus.im/app/r9nSQPiuUS2G7kSbbFvSzE"]
input_files: []
message_count: 15
---

# Granola Connector Test & Factsheet Creation – Y-OS Tool Hub

> **Session:** [r9nSQPiuUS2G7kSbbFvSzE](https://manus.im/app/r9nSQPiuUS2G7kSbbFvSzE) | **Date:** 2026-06-16 | **Project:** Y-OS Multi-Agent Architecture | **Language:** mixed

## 📋 SESSION CARD

### 🧭 Executive Summary
The session tested the Granola MCP connector end-to-end, successfully extracting meeting data (medical appointments, personal calls) from Yannick's Granola account. A structured factsheet was then produced and pushed to the Y-OS Multi-Agent Architecture Hub in Notion, following the established tool-documentation template (à la MailerLite). The session closed with an open discussion on enriching the factsheet to better surface the iOS-app dimension and MCP/API distinction.

---

### 🎯 Context & Intent
Granola became available as a new iOS/MCP connector in Y-OS. Yannick wanted to (1) validate that the connector actually works by running live tests against real data, and (2) produce a standardized factsheet — covering technical access points, capabilities, limits, pricing, and business value — to be archived in the Y-OS tool knowledge base alongside other connector fiches.

---

### ✅ What Was Done
1. Probed all available Granola connector endpoints to inventory tools and entry points.
2. Ran live queries using `query_granola_meetings` and `get_meetings`, confirming which endpoints return data on the free tier.
3. Extracted real meeting data: index of 4 meetings (late March – April 2026), medical RDV details (neurology/neuropsychology), and a personal call summary (Robi).
4. Produced a full test report with extracted data.
5. Located the existing factsheet template in Notion (Y-OS Multi-Agent Architecture Hub).
6. Created and pushed the Granola factsheet to Notion, structured with: Executive Summary, Tool Mapping (6 read-only endpoints), Limits, Business Value, Pricing, and Lessons Learned.
7. Identified a delta between the delivered fiche and Yannick's fuller vision (iOS-app framing, frontend vs. MCP distinction, inter-tool dependencies, TL;DR block).

---

### 💡 Key Insights
- **`query_granola_meetings` is the power tool**: acts as an autonomous RAG agent over all meeting notes/summaries; it bypasses the free-tier limitations that block `get_meetings` direct ID lookups.
- **Connector is 100% read-only** on the current tier: 6 endpoints, no write/create access.
- **Free tier hard limits**: no raw transcript access, no folder listing, `get_meetings` returns empty arrays — semantic query is the only reliable path.
- **Factsheet template is established**: the MailerLite structure is the canonical model for all tool fiches in Y-OS.
- **Gap identified**: the fiche needs a clearer iOS-app vs. MCP-connector distinction, a TL;DR header block, and inter-tool dependency mapping (e.g. Granola → Notion, Granola → Linear).
- **Privacy note**: the connector has access to sensitive personal data (medical details), which implies data-handling considerations for agent use.

---

### 📦 Outputs Produced
- **[doc]** `Granola Factsheet – Notion (Y-OS Hub)`: Structured tool factsheet covering endpoints, capabilities, limits, pricing, business value, and lessons learned — pushed to the Multi-Agent Architecture Hub in Notion.
- **[data]** `Granola Meeting Index`: Live-extracted index of 4 meetings (late March – April 2026) with metadata.
- **[data]** `Granola Meeting Details`: Extracted content from neurology/neuropsychology RDVs and personal call (Robi) — included in test report.
- **[doc]** `Granola Connector Test Report`: Full report of connector test with real data samples (attached in session).

---

### ⚠️ Open Items & Blockers
- The factsheet **delta is unresolved**: the iOS-app framing, frontend vs. MCP block, TL;DR header, and inter-tool dependency section were identified but not yet added to the Notion fiche.
- [INCERTAIN] It's unclear whether Yannick's second duplicate message was intentional (requesting a revision) or an accidental resend — Manus flagged it but no explicit confirmation was received.
- **No write access**: Granola connector cannot create or update meetings/notes — any enrichment workflow must go through another tool.
- [INCERTAIN] Whether the Granola paid tier unlocks raw transcripts and folder access has not been fully verified against live paid-tier documentation.
- The broader question of **which other iOS connectors need factsheets** was raised but not scoped.

---

### 🔁 Next Steps
1. **Update the Granola Notion fiche** to add: TL;DR block, explicit iOS app vs. MCP connector section, inter-tool dependency map (Granola → Notion, Granola → Linear), and a privacy/data-sensitivity flag.
2. **Confirm paid-tier capabilities**: check Granola API/MCP documentation for what unlocks at higher tiers (raw transcripts, folder access, write endpoints).
3. **Apply the factsheet workflow to next iOS connectors** — establish a queue/backlog of tools pending documentation.
4. **Consider a privacy policy note** in the factsheet given the medical data accessible via the connector.
5. **Validate the fiche structure** with Yannick: is the MailerLite template still the canonical model, or does the iOS-app dimension require a new template variant?

---

### 🔗 Links & References
- 🌐 `https://manus.im/app/r9nSQPiuUS2G7kSbbFvSzE` — Current session
- 📁 Notion: Y-OS Multi-Agent Architecture Hub → Granola Factsheet (pushed during session)
- 📄 Granola Connector Test Report (session artifact, attached)
- 🔗 Reference tool: MailerLite factsheet (canonical template model, same Notion hub)

---

### 🧠 Resume Hint
The Granola connector is tested and documented in Notion, but the factsheet needs a second pass to add a TL;DR block, iOS-app vs. MCP distinction, inter-tool dependencies, and a privacy flag — pick up by opening the Granola fiche in the Y-OS Multi-Agent Architecture Hub and applying the delta items listed above.

---

### 🏷️ Tags
`granola` `connector-factsheet` `mcp-testing` `y-os-architecture` `ios-tools` `knowledge-base`

---

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 15 messages — 2026-06-16

**[2026-06-16 08:48] USER:** Help me test the Granola connector and show me how to use its feature (e.g. show any data you fetched with it). Give me a brief about its capabilities.

**[2026-06-16 08:48] MANUS:** Sur ça — je lis les outils disponibles du connecteur Granola, teste ses capacités, et te présente un rapport complet avec données réelles.

**[2026-06-16 09:02] MANUS:** Test du connecteur Granola terminé.

Le connecteur est fonctionnel, bien qu'il présente des limitations liées au tier gratuit (pas d'accès direct aux transcripts bruts ni aux dossiers). Cependant, l'outil de requête sémantique (`query_granola_meetings`) est extrêmement puissant et permet d'extraire tout le contenu des notes et résumés.

J'ai pu extraire :
1. L'index de tes 4 réunions (fin mars - avril 2026).
2. Les détails médicaux précis de tes rendez-vous Neurolog/Neuropsy (symptômes, traitement anticoagulant, plan de réhab à Crans-Montana).
3. Le résumé de ton appel personnel avec Robi.

Le rapport complet avec les données extraites est en pièce jointe.

**[2026-06-16 13:26] USER:** C'est donc un nouvel outil disponible pour iOS. Il faut donc une factsheet et d'un outil avec ses capabilités, ses limites, les lessons learned, les éventuels accès, etc. Comme d'habitude, on fait cette factsheet pour cet outil. Là, on l'a vraiment testé avec tous les accès et tous les API, les entry points, etc. D'autres fois, on n'a pas eu le temps de tester et donc c'est ce que ça donne en général d'après la documentation que tu retrouves online. Mais je veux savoir que pour tel outil, on a telle possibilité et que ça offre. On est capable d'écrire, de lire, de faire, les possibilités techniques d'accès à l'outil et les possibilités en termes de capabilities, de features, donc business-wise. Qu'est-ce que ça m'importe d'avoir cette connexion-là ? Et puis, c'est gratuit, payant, etc. Don

**[2026-06-16 13:26] MANUS:** Je cherche d'abord la structure de factsheet existante dans Notion/yOS avant de construire celle de Granola.

**[2026-06-16 13:28] MANUS:** C'est fait ! La factsheet pour le connecteur Granola a été créée et ajoutée dans ton Hub d'Architecture Multi-Agents Y-OS (aux côtés des autres fiches comme MailerLite, Notion, etc.).

Voici ce que j'ai structuré dans la fiche :

1️⃣ **Synthèse et Capabilities** : L'outil offre 6 endpoints exclusivement en lecture (Read-Only). Sa grande force réside dans `query_granola_meetings` qui agit comme un agent RAG autonome sur tes réunions.
2️⃣ **Limites (très importantes)** : Le tier gratuit bloque l'accès aux transcripts bruts et à la liste des dossiers. De plus, les requêtes directes par ID (`get_meetings`) renvoient souvent des tableaux vides sur ce tier. Il faut donc **toujours** utiliser l'outil de requête sémantique (`query_granola_meetings`) qui, lui, arrive à contourner cette limite pour 

**[2026-06-16 13:35] USER:** C'est donc un nouvel outil disponible pour iOS. Il faut donc une factsheet et d'un outil avec ses capabilités, ses limites, les lessons learned, les éventuels accès, etc. Comme d'habitude, on fait cette factsheet pour cet outil. Là, on l'a vraiment testé avec tous les accès et tous les API, les entry points, etc. D'autres fois, on n'a pas eu le temps de tester et donc c'est ce que ça donne en général d'après la documentation que tu retrouves online. Mais je veux savoir que pour tel outil, on a telle possibilité et que ça offre. On est capable d'écrire, de lire, de faire, les possibilités techniques d'accès à l'outil et les possibilités en termes de capabilities, de features, donc business-wise. Qu'est-ce que ça m'importe d'avoir cette connexion-là ? Et puis, c'est gratuit, payant, etc. Don

**[2026-06-16 13:35] MANUS:** Je vois que tu as renvoyé le même message que précédemment — la factsheet Granola vient d'être créée et poussée dans Notion. Est-ce que tu voulais parler d'un **autre outil iOS** spécifique, ou bien tu confirmes que le workflow de factsheet est validé et qu'on doit maintenant l'appliquer à d'autres connecteurs de ta liste ?

**[2026-06-16 13:35] MANUS:** Pour être précis sur ce qu'on a livré vs ce que tu décris :

**Ce qui est fait ✅**
La factsheet Granola est dans Notion, calquée sur la structure MailerLite (Executive Summary, Tool Mapping, Limites, Business Value, Pricing, Lessons Learned).

**Ce que je détecte dans ton message comme delta ⚠️**
Tu mentionnes que Granola est un **outil iOS** — ce que j'ai partiellement couvert (app iPhone disponible) mais pas mis en avant comme axe principal de la fiche.

Tu veux aussi que la fiche couvre explicitement :
- La distinction **frontend app** vs **accès MCP/API** (ce qu'on peut faire dans l'app vs via connecteur)
- Les **interdépendances entre outils** (ex : Granola → Notion, Granola → Linear)
- Un **bloc synthèse rapide** en tête de fiche (style "TL;DR — cet outil permet de : lire / écrire / 
