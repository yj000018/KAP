---
uid: pBdfajxqriZVvwCbixj9Zj
session_url: https://manus.im/app/pBdfajxqriZVvwCbixj9Zj
session_title: "AllTrails Connector — Live Test & Y-OS Factsheet Publication"
date: 2026-06-16
project: "Y-OS Connector Registry"
language: mixed
depth: moderate
length: short
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 13:13
referenced_sessions: []
referenced_artifacts: []
referenced_urls: ["https://manus.im/app/pBdfajxqriZVvwCbixj9Zj", "https://app.notion.com/p/38135e"]
input_files: []
message_count: 10
---

# AllTrails Connector — Live Test & Y-OS Factsheet Publication

> **Session:** [pBdfajxqriZVvwCbixj9Zj](https://manus.im/app/pBdfajxqriZVvwCbixj9Zj) | **Date:** 2026-06-16 | **Project:** Y-OS Connector Registry | **Language:** mixed

## 📋 SESSION CARD

### 🧭 Executive Summary
The session tested the AllTrails MCP connector live, fetching real trail data, weather forecasts, and geographic search results. A structured Y-OS factsheet was then produced and published to the Notion Connector Registry, documenting capabilities, limits, and business value. This connector is now formally catalogued as read-only within the Y-OS ecosystem.

### 🎯 Context & Intent
Yannick wanted to validate the AllTrails connector end-to-end (live API calls, all entry points), then produce the standard Y-OS factsheet format for new tools — covering technical access modes, capabilities, limits, cost model, and business value — consistent with how other connectors are documented in the registry.

### ✅ What Was Done
1. Tested the AllTrails connector live: searched trails, retrieved details for "Mont Blanc via Bellevue," fetched 7-day weather forecast for that trail
2. Performed a bounding box geographic search for trails around Paris
3. Documented all available tools and API entry points discovered during testing
4. Retrieved the existing Y-OS factsheet structure from Notion/memory
5. Enriched the factsheet with online AllTrails documentation and live test results
6. Published the completed AllTrails factsheet to the Notion Connector Registry

### 💡 Key Insights
- **Read-only only**: The connector has zero write capability — no interaction with user accounts, no bookmarks, no activity logging
- **Bounding Box search** is a powerful entry point for finding trails in areas not easily indexed by name
- **Integrated weather** removes the need for a separate weather connector in trail-planning workflows — a meaningful simplification
- **Native `locale` parameter** translates metadata (difficulty labels, trail types) at the source, reducing downstream processing
- This session established or reinforced the standard Y-OS practice: test live when possible, otherwise document from official docs, always produce a factsheet for new connectors

### 📦 Outputs Produced
- **[doc]** `Factsheet AllTrails — Notion`: Full Y-OS connector factsheet published to the Notion Connector Registry, covering tools, capabilities, limits, access model, cost, and business value
- **[data]** `Live trail data — Mont Blanc via Bellevue`: Real search results, trail details, and 7-day weather forecast fetched during testing
- **[data]** `Bounding Box search results — Paris area`: Geographic trail search output used to validate that entry point

### ⚠️ Open Items & Blockers
- No write/auth capability confirmed — any future use case requiring user-specific data (saved trails, user history) is **not possible** with this connector [INCERTAIN: whether a user-authenticated API tier exists]
- [INCERTAIN] Whether the AllTrails API is officially public or accessed via a third-party/unofficial wrapper — cost and stability implications unclear
- The Notion page URL (`https://app.notion.com/p/38135e`) appears truncated — full canonical URL not confirmed

### 🔁 Next Steps
1. Verify the Notion factsheet URL is complete and accessible (truncated link in transcript)
2. Clarify whether the AllTrails API access is official/paid or unofficial — document tier and pricing in the factsheet if not already done
3. Identify concrete Y-OS workflows where AllTrails connector adds value (e.g., trip planning agents, weekend activity suggestions)
4. Cross-reference with other connectors (weather, maps) to design a trail/outdoor planning workflow template
5. Apply the same factsheet process to any other recently added iOS connectors not yet catalogued

### 🔗 Links & References
- 🌐 `https://manus.im/app/pBdfajxqriZVvwCbixj9Zj` — This session
- 🌐 `https://app.notion.com/p/38135e` — AllTrails Factsheet in Notion Connector Registry (URL may be truncated)

### 🧠 Resume Hint
The AllTrails connector has been tested live and its factsheet published to Notion; the next agent should verify the Notion URL completeness, confirm the API access model (official vs. unofficial), and explore concrete Y-OS workflow integrations for outdoor/trail planning.

### 🏷️ Tags
`alltrails` `connector-registry` `factsheet` `ios-tools` `read-only` `trail-planning`

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 10 messages — 2026-06-16

**[2026-06-16 08:59] USER:** Help me test the AllTrails connector and show me how to use its feature (e.g. show any data you fetched with it). Give me a brief about its capabilities.

**[2026-06-16 08:59] MANUS:** On it — testing the AllTrails connector now, fetching live data, and building a capability brief.

**[2026-06-16 09:00] MANUS:** J'ai testé le connecteur AllTrails et extrait des données en direct. 

Le brief de capacité est prêt dans le document joint. Il contient :
1️⃣ La liste des outils disponibles.
2️⃣ Un test de recherche et de détails sur le "Mont Blanc via Bellevue".
3️⃣ Les prévisions météo sur 7 jours pour ce même sentier.
4️⃣ Un test de recherche par zone (Bounding Box) autour de Paris.

Consulte le fichier Markdown pour voir les données réelles récupérées et structurées.

**[2026-06-16 13:27] USER:** C'est donc un nouvel outil disponible pour iOS. Il faut donc une factsheet et d'un outil avec ses capabilités, ses limites, les lessons learned, les éventuels accès, etc. Comme d'habitude, on fait cette factsheet pour cet outil. Là, on l'a vraiment testé avec tous les accès et tous les API, les entry points, etc. D'autres fois, on n'a pas eu le temps de tester et donc c'est ce que ça donne en général d'après la documentation que tu retrouves online. Mais je veux savoir que pour tel outil, on a telle possibilité et que ça offre. On est capable d'écrire, de lire, de faire, les possibilités techniques d'accès à l'outil et les possibilités en termes de capabilities, de features, donc business-wise. Qu'est-ce que ça m'importe d'avoir cette connexion-là ? Et puis, c'est gratuit, payant, etc. Don

**[2026-06-16 13:27] MANUS:** Compris. Je vais d'abord récupérer la structure de factsheet existante dans Notion/mémoire yOS, puis enrichir avec la doc AllTrails en ligne, les tests live qu'on vient de faire, et produire la factsheet complète.

**[2026-06-16 13:31] MANUS:** La Factsheet Y-OS pour le connecteur AllTrails a été créée et publiée avec succès dans Notion, au sein du Registre des Connecteurs.

**Points clés de l'intégration :**
1️⃣ **Read-Only exclusif** : Accès complet aux données (recherche, détails, météo), mais aucune capacité d'écriture ou d'interaction avec un compte utilisateur.
2️⃣ **Précision géographique** : Utilisation redoutable des Bounding Boxes pour trouver des sentiers dans des zones non indexées.
3️⃣ **Météo intégrée** : Évite de devoir utiliser un connecteur météo tiers, simplifiant les workflows de planification.
4️⃣ **Traduction native** : Le paramètre `locale` traduit les métadonnées (difficulté, type de parcours) directement à la source.

Tu peux consulter la factsheet complète dans Notion ici : https://app.notion.com/p/38135e
