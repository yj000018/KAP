---
uid: apQRfj3wEA8jGKH4CEkkJX
session_url: https://manus.im/app/apQRfj3wEA8jGKH4CEkkJX
session_title: "Plaud MCP Connector — Test & Factsheet v1 (Registre Connecteurs)"
date: 2026-06-16
project: "Y-OS Registre Connecteurs"
language: fr
depth: moderate
length: medium
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 13:14
referenced_sessions: []
referenced_artifacts: ["https://app.notion.com/p/38135e218cf881fcb929c244df5167a0"]
referenced_urls: ["https://app.notion.com/p/38135e218cf881fcb929c244df5167a0", "https://manus.im/app/apQRfj3wEA8jGKH4CEkkJX"]
input_files: []
message_count: 15
---

# Plaud MCP Connector — Test & Factsheet v1 (Registre Connecteurs)

> **Session:** [apQRfj3wEA8jGKH4CEkkJX](https://manus.im/app/apQRfj3wEA8jGKH4CEkkJX) | **Date:** 2026-06-16 | **Project:** Y-OS Registre Connecteurs | **Language:** fr

## 📋 SESSION CARD

### 🧭 Executive Summary
The session tested the Plaud MCP connector end-to-end, validating authentication, all 5 API tools, and live data retrieval against Yannick's real account. A structured factsheet was then produced and pushed to the Y-OS Registre Connecteurs in Notion, aligned with the existing Miro/Shopify/MailerLite standard. This connector gives Y-OS read access to Plaud voice recordings, transcripts, and AI-generated notes.

---

### 🎯 Context & Intent
Yannick wanted to formally onboard the Plaud MCP connector into the Y-OS connector registry. The goal was twofold: (1) validate the connector works live with real credentials and API calls, and (2) produce a canonical factsheet documenting technical capabilities, business value, limits, pricing, and lessons learned — consistent with the factsheet format used for other connectors.

---

### ✅ What Was Done
1. Authenticated to Plaud MCP and confirmed connection (user identity retrieved: yannick.jolliet@gmail.com)
2. Enumerated and tested all 5 available MCP tools (`get_current_user`, `list_files`, `get_file`, `get_note`, `get_transcript`)
3. Retrieved live data samples from Plaud account to validate each tool's outputs
4. Located existing factsheet structure in Notion (Registre Connecteurs) and read reference models (Miro, Shopify, MailerLite)
5. Adopted the enriched factsheet format (Miro v1 standard) with all required sections
6. Authored the full Plaud factsheet covering: Identity, Overview, Technical Capabilities, Business Value, Limits, Access/Pricing, Live Data, Lessons Learned
7. Pushed the factsheet to Notion (after one timeout retry), successfully creating the page in the Registre Connecteurs

---

### 💡 Key Insights
- **Plaud MCP is read-only** — no write, create, or delete operations are available via the current API; this is a significant constraint for automation ambitions
- **5 tools confirmed operational** with real data; `get_transcript` returns timestamped, speaker-attributed transcriptions
- **S3 signed audio URLs are ephemeral** (24h validity), limiting asynchronous pipeline use cases
- **Standard factsheet format (Miro v1)** is now the established template — richer than the older MailerLite/Shopify versions; future connectors should follow this structure
- **Notion push experienced one timeout** before succeeding — a known fragility in the connector workflow
- Business value is concentrated in **voice-to-text pipeline automation**: feeding Plaud transcripts into Y-OS synthesis, action item extraction, and knowledge capture workflows

---

### 📦 Outputs Produced
- **[doc]** `🎙️ Plaud MCP Connector — Factsheet v1` — https://app.notion.com/p/38135e218cf881fcb929c244df5167a0 : Full connector factsheet in Notion (Registre Connecteurs), aligned with Miro v1 standard; covers 5 tools, business value, limits, live test data, lessons learned

---

### ⚠️ Open Items & Blockers
- **Notion push timed out once** before succeeding — page creation reliability is inconsistent [INCERTAIN: whether the final push fully captured all sections or was truncated]
- **Read-only API limitation** — no way to write back to Plaud (e.g., tag recordings, create notes) via MCP; blocks bidirectional automation
- **Search capability scope** [INCERTAIN: exact filtering options for `list_files` (date ranges, query syntax) not fully documented in the factsheet]
- **Pricing/tier details** for Plaud API access may need updating as the product evolves [INCERTAIN]

---

### 🔁 Next Steps
1. Verify the Notion factsheet page is complete and not truncated (open and review all sections)
2. Link the Plaud factsheet from the main Registre Connecteurs index/dashboard in Notion
3. Design a practical Y-OS workflow using Plaud — e.g., auto-pull latest recordings → extract transcript → feed into KAP or weekly synthesis
4. Monitor Plaud API for write capability releases (currently read-only)
5. Apply the Miro v1 factsheet format retroactively to any older connector factsheets that predate this standard

---

### 🔗 Links & References
- 🌐 https://app.notion.com/p/38135e218cf881fcb929c244df5167a0 — Plaud MCP Connector Factsheet v1 (Notion)
- 🌐 https://manus.im/app/apQRfj3wEA8jGKH4CEkkJX — Session URL

---

### 🧠 Resume Hint
Plaud MCP connector is live, tested, and documented in Notion (Registre Connecteurs) as a read-only voice recording accessor with 5 tools; the next step is verifying the Notion page completeness and wiring Plaud into a concrete Y-OS voice pipeline workflow.

---

### 🏷️ Tags
`plaud` `mcp-connector` `factsheet` `voice-recording` `yos-registry` `connector-onboarding`

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 15 messages — 2026-06-16

**[2026-06-16 08:57] USER:** Help me test the Plaud connector and show me how to use its feature (e.g. show any data you fetched with it). Give me a brief about its capabilities.

**[2026-06-16 08:57] MANUS:** Sur le coup — je lis le skill yos-optimizer puis j'explore le connecteur Plaud via MCP.

**[2026-06-16 08:59] MANUS:** ## Plaud MCP — Test & Capabilities Brief

**Connecteur opérationnel.** Auth validée, 5 outils disponibles, données réelles récupérées.

---

### Identité connectée

| Champ | Valeur |
|---|---|
| Email | yannick.jolliet@gmail.com |
| Nickname | yannick.jolliet |
| ID | `30f90f51...` |

---

### 5 outils disponibles

| Outil | Description | Paramètres clés |
|---|---|---|
| `get_current_user` | Profil de l'utilisateur connecté | — |
| `list_files` | Liste paginée des enregistrements | `query`, `date_from`, `date_to`, `page`, `page_size` |
| `get_file` | Détails complets d'un enregistrement + URL audio S3 signée (24h) | `file_id` |
| `get_note` | Notes IA générées : résumé compact, action items, topics | `file_id` |
| `get_transcript` | Transcription complète horodatée avec attribution speak

**[2026-06-16 13:27] USER:** C'est donc un nouvel outil disponible pour iOS. Il faut donc une factsheet et d'un outil avec ses capabilités, ses limites, les lessons learned, les éventuels accès, etc. Comme d'habitude, on fait cette factsheet pour cet outil. Là, on l'a vraiment testé avec tous les accès et tous les API, les entry points, etc. D'autres fois, on n'a pas eu le temps de tester et donc c'est ce que ça donne en général d'après la documentation que tu retrouves online. Mais je veux savoir que pour tel outil, on a telle possibilité et que ça offre. On est capable d'écrire, de lire, de faire, les possibilités techniques d'accès à l'outil et les possibilités en termes de capabilities, de features, donc business-wise. Qu'est-ce que ça m'importe d'avoir cette connexion-là ? Et puis, c'est gratuit, payant, etc. Don

**[2026-06-16 13:27] MANUS:** Compris. Je cherche d'abord la structure de factsheet existante dans Notion/yOS, puis je complète avec la doc Plaud en ligne + les données testées en live.

**[2026-06-16 13:28] MANUS:** Structure trouvée — Registre Connecteurs + 2 modèles de référence (MailerLite + Shopify). Je scrape maintenant la doc officielle Plaud pour enrichir la factsheet.

**[2026-06-16 13:35] USER:** C'est donc un nouvel outil disponible pour iOS. Il faut donc une factsheet et d'un outil avec ses capabilités, ses limites, les lessons learned, les éventuels accès, etc. Comme d'habitude, on fait cette factsheet pour cet outil. Là, on l'a vraiment testé avec tous les accès et tous les API, les entry points, etc. D'autres fois, on n'a pas eu le temps de tester et donc c'est ce que ça donne en général d'après la documentation que tu retrouves online. Mais je veux savoir que pour tel outil, on a telle possibilité et que ça offre. On est capable d'écrire, de lire, de faire, les possibilités techniques d'accès à l'outil et les possibilités en termes de capabilities, de features, donc business-wise. Qu'est-ce que ça m'importe d'avoir cette connexion-là ? Et puis, c'est gratuit, payant, etc. Don

**[2026-06-16 13:35] MANUS:** Compris — je reprends là où on en était. La factsheet est rédigée, je finalise le push Notion (le process précédent a timeout) puis je livre.

**[2026-06-16 13:35] MANUS:** Page non créée (timeout). Je vois qu'il existe déjà une structure de factsheets enrichie avec de nouvelles métadonnées (Miro, Fireflies, Twilio...). Je lis un de ces modèles récents avant de pousser la factsheet Plaud.

**[2026-06-16 13:35] MANUS:** Nouvelle structure trouvée (Miro v1). Beaucoup plus riche : Identité, Overview, Capacités par catégorie, Business Value, Limites, Accès/Pricing, Données Live, Lessons Learned. Je réécris la factsheet Plaud dans ce format et je la pousse.

**[2026-06-16 13:37] MANUS:** ## 🎙️ Plaud MCP — Factsheet v1 créée dans Notion

**Page Notion :** [🎙️ Plaud MCP Connector — Factsheet v1](https://app.notion.com/p/38135e218cf881fcb929c244df5167a0)
**Emplacement :** 🔌 Y-OS — Registre Connecteurs Manus

---

### Ce que contient la factsheet (structure alignée sur le standard Miro/Shopify/MailerLite)

| Section | Contenu |
|---|---|
| **Identité** | Type, catégorie, statut, auth, nb outils, appareils, plateformes, URLs doc |
| **Overview** | Positionnement de l'outil dans Y-OS en 1 paragraphe dense |
| **Capacités Techniques** | 5 outils mappés par catégorie (Auth, Recherche, Extraction) avec paramètres et outputs |
| **Business Value** | 5 cas d'usage concrets avec outils Y-OS impliqués |
| **Limites & Contraintes** | 6 contraintes avec niveau d'impact (Read-Only, search
