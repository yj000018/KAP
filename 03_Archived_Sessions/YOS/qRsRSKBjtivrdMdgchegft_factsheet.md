---
uid: qRsRSKBjtivrdMdgchegft
session_url: https://manus.im/app/qRsRSKBjtivrdMdgchegft
session_title: "Otter.ai MCP Connector — Test Live & Factsheet Production"
date: 2026-06-16
project: "Y-OS Technologie & Infra"
language: fr
depth: moderate
length: medium
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 13:12
referenced_sessions: []
referenced_artifacts: ["Otter.ai MCP Factsheet"]
referenced_urls: ["https://app.notion.com/p/38135e218cf8817fb22ae6730d032577", "https://manus.im/app/qRsRSKBjtivrdMdgchegft"]
input_files: []
message_count: 11
---

# Otter.ai MCP Connector — Test Live & Factsheet Production

> **Session:** [qRsRSKBjtivrdMdgchegft](https://manus.im/app/qRsRSKBjtivrdMdgchegft) | **Date:** 2026-06-16 | **Project:** Y-OS Technologie & Infra | **Language:** fr

## 📋 SESSION CARD

### 🧭 Executive Summary
Session de test live du connecteur MCP Otter.ai, confirmant l'authentification réussie et l'accès en lecture seule à 3 outils. Une factsheet structurée a été produite et archivée dans Notion sous TECH — Technologie & Infra. Ce connecteur enrichit Y-OS d'une capacité de retrieval de transcriptions et métadonnées de réunions.

### 🎯 Context & Intent
Yannick souhaitait valider le fonctionnement du connecteur Otter.ai nouvellement disponible, en explorer les capacités réelles via tests live, puis produire une factsheet de référence standardisée (format Y-OS) documentant les accès techniques, les capabilities, les limites et la valeur business — pour servir de documentation pérenne dans la base de connaissance.

### ✅ What Was Done
1. Lecture du skill `yos-optimizer` pour récupérer le contexte et la structure de factsheet existante
2. Authentification et test live du connecteur Otter.ai (compte yannick.jolliet@gmail.com)
3. Exécution des 3 outils MCP disponibles : `get_user_info`, `search`, `fetch`
4. Recherche de réunions sur le compte (2020–2026) — aucun résultat retourné
5. Scraping de la documentation officielle Otter.ai (API, pricing, limites)
6. Rédaction de la factsheet complète au format Y-OS
7. Archivage de la factsheet dans Notion (TECH — Technologie & Infra)

### 💡 Key Insights
- Le connecteur Otter.ai MCP est **read-only** — aucune capacité d'écriture, de création ou de modification disponible via MCP
- Le compte testé ne contient aucune réunion enregistrée, ce qui limite la démonstration du `search` et `fetch` à des tests à vide
- L'API REST complète (webhooks, SSO, HIPAA) est réservée au plan **Enterprise** — le MCP couvre les plans Freemium et au-delà
- `get_user_info` doit être appelé en premier — il sert d'initialisation implicite du contexte de session
- La valeur business principale : automatiser la récupération de transcriptions et résumés de réunions dans les workflows Y-OS (briefings, actions items, mémoire organisationnelle)

### 📦 Outputs Produced
- **[doc]** `Notion: Otter.ai MCP Factsheet` — Factsheet complète archivée dans Notion (TECH — Technologie & Infra), couvrant capabilities, limites, accès techniques, pricing et lessons learned
- **[data]** `Live test results` — Résultats des appels live aux 3 outils MCP (profil authentifié, recherche vide, fetch testé)

### ⚠️ Open Items & Blockers
- Le compte Otter.ai ne contient aucune réunion enregistrée — impossible de tester `search` et `fetch` avec des données réelles [INCERTAIN : est-ce le bon compte ou y a-t-il un autre compte Otter actif ?]
- La factsheet a été tronquée dans le transcript — contenu complet non visible, à vérifier dans Notion [INCERTAIN]
- Capacités d'écriture (création de notes, upload d'audio) : non disponibles via MCP, statut via API REST Enterprise non testé [INCERTAIN]

### 🔁 Next Steps
1. Enregistrer une réunion test sur le compte Otter.ai pour valider `search` et `fetch` avec des données réelles
2. Vérifier la factsheet Notion pour s'assurer qu'elle est complète et non tronquée
3. Évaluer si le plan actuel suffit ou si une montée en plan est nécessaire pour les use cases Y-OS
4. Intégrer la factsheet Otter.ai dans le registre des connecteurs Y-OS (liste maître des outils MCP disponibles)
5. Définir les workflows Y-OS concrets utilisant Otter.ai (ex : briefing post-réunion automatique, extraction d'action items)

### 🔗 Links & References
- 🌐 `https://app.notion.com/p/38135e218cf8817fb22ae6730d032577` — Factsheet Otter.ai dans Notion
- 🌐 `https://manus.im/app/qRsRSKBjtivrdMdgchegft` — Session Manus source
- 🔗 `session:qRsRSKBjtivrdMdgchegft` — Session courante

### 🧠 Resume Hint
Le connecteur Otter.ai MCP est opérationnel (read-only, 3 outils), la factsheet est archivée dans Notion — la prochaine étape est de tester avec de vraies réunions enregistrées pour valider `search` et `fetch` en conditions réelles.

### 🏷️ Tags
`otter-ai` `mcp-connector` `factsheet` `meeting-intelligence` `knowledge-retrieval` `yos-infra`

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 11 messages — 2026-06-16

**[2026-06-16 09:00] USER:** Help me test the Otter.ai connector and show me how to use its feature (e.g. show any data you fetched with it). Give me a brief about its capabilities.

**[2026-06-16 09:00] MANUS:** Sur ça. Je lis le skill yos-optimizer d'abord, puis j'explore le connecteur Otter.ai.

**[2026-06-16 09:02] MANUS:** Test terminé. Le connecteur Otter.ai est actif et authentifié.

Voici ce que j'ai trouvé :
1️⃣ **Profil** : Connecté avec succès (Yannick Jolliet / yannick.jolliet@gmail.com).
2️⃣ **Recherche** : J'ai lancé plusieurs requêtes larges (sans filtre, de 2020 à 2026), mais aucune réunion n'a été trouvée sur ce compte pour l'instant.
3️⃣ **Capacités** : 3 outils (`get_user_info`, `search`, `fetch`). La recherche ramène les métadonnées (résumés, actions), et le fetch ramène la transcription complète via l'ID.

Le document joint contient la synthèse complète des capacités et les résultats live.

**[2026-06-16 13:26] USER:** C'est donc un nouvel outil disponible pour iOS. Il faut donc une factsheet et d'un outil avec ses capabilités, ses limites, les lessons learned, les éventuels accès, etc. Comme d'habitude, on fait cette factsheet pour cet outil. Là, on l'a vraiment testé avec tous les accès et tous les API, les entry points, etc. D'autres fois, on n'a pas eu le temps de tester et donc c'est ce que ça donne en général d'après la documentation que tu retrouves online. Mais je veux savoir que pour tel outil, on a telle possibilité et que ça offre. On est capable d'écrire, de lire, de faire, les possibilités techniques d'accès à l'outil et les possibilités en termes de capabilities, de features, donc business-wise. Qu'est-ce que ça m'importe d'avoir cette connexion-là ? Et puis, c'est gratuit, payant, etc. Don

**[2026-06-16 13:26] MANUS:** Compris. Je cherche d'abord la structure de factsheet existante dans Notion/mémoire, puis je scrape la doc Otter.ai officielle, et je produis la factsheet complète.

**[2026-06-16 13:27] MANUS:** Structure récupérée. Je scrape maintenant la doc officielle Otter.ai (API, pricing, limites) en parallèle.

**[2026-06-16 13:31] MANUS:** Factsheet créée et archivée dans Notion. Voici la synthèse complète :

---

## 🎙️ Otter.ai MCP — Factsheet

**Notion :** [Ouvrir la page](https://app.notion.com/p/38135e218cf8817fb22ae6730d032577) (sous TECH — Technologie & Infra)

---

### 0. Synthèse Télégraphique

| Dimension | Valeur |
|---|---|
| **Type** | Connecteur MCP — Knowledge Retrieval / Meeting Intelligence |
| **Statut** | Testé en live, authentifié, opérationnel |
| **Mode d'accès** | Lecture seule (Read-only) |
| **Outils MCP** | 3 (`get_user_info`, `search`, `fetch`) |
| **Coût** | Freemium — MCP inclus sur tous les plans |
| **API REST complète** | Enterprise uniquement (Webhooks, SSO, HIPAA) |

---

### 1. Ce que ça fait (capabilities)

**`get_user_info`** — Profil + date/heure courante. Obligatoire en premier appel pou
