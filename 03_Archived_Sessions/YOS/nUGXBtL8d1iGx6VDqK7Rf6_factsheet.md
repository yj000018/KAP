---
uid: nUGXBtL8d1iGx6VDqK7Rf6
session_url: https://manus.im/app/nUGXBtL8d1iGx6VDqK7Rf6
session_title: "Google Calendar MCP Connector — Test Live & Factsheet Y-OS"
date: 2026-06-16
project: "Y-OS Tools & Connectors"
language: mixed
depth: moderate
length: short
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 13:10
referenced_sessions: []
referenced_artifacts: ["skill: yos-optimizer", "factsheet-google-calendar-connector"]
referenced_urls: ["https://manus.im/app/nUGXBtL8d1iGx6VDqK7Rf6", "https://developers.google.com/calendar/api"]
input_files: []
message_count: 12
---

# Google Calendar MCP Connector — Test Live & Factsheet Y-OS

> **Session:** [nUGXBtL8d1iGx6VDqK7Rf6](https://manus.im/app/nUGXBtL8d1iGx6VDqK7Rf6) | **Date:** 2026-06-16 | **Project:** Y-OS Tools & Connectors | **Language:** mixed

## 📋 SESSION CARD

### 🧭 Executive Summary
Yannick a testé en live le connecteur Google Calendar via MCP pour explorer ses capacités techniques et ses API entry points. Suite au test, il a demandé la production d'une factsheet standardisée documentant les capabilities, limites, accès, et valeur business de cet outil. La factsheet Google Calendar s'inscrit dans un processus récurrent de documentation des outils disponibles dans Y-OS.

---

### 🎯 Context & Intent
Yannick découvre ou valide un nouveau connecteur Google Calendar disponible dans son environnement iOS/Y-OS. L'objectif est double : (1) tester concrètement les API et entry points disponibles, et (2) produire une factsheet standardisée pour documenter l'outil — comme cela se fait systématiquement pour chaque nouvel outil intégré à Y-OS, qu'il ait été testé en live ou non.

---

### ✅ What Was Done
1. Lecture du skill `yos-optimizer` pour contexte initial
2. Exploration du connecteur Google Calendar via MCP (accès live)
3. Fetch de données réelles depuis Google Calendar via les API disponibles
4. Analyse des entry points, permissions et capacités techniques du connecteur
5. Initialisation de la rédaction d'une factsheet structurée pour Google Calendar
6. Recherche de la structure de factsheet existante dans Notion/mémoire Y-OS
7. Croisement des données live testées avec la documentation officielle Google Calendar API

---

### 💡 Key Insights
- Le connecteur Google Calendar a été testé **en conditions réelles** (accès + API live) — ce qui le distingue des factsheets produites uniquement sur base documentaire
- Le format factsheet Y-OS couvre systématiquement : capabilities techniques, features business, limites, accès requis, coût (gratuit/payant), et lessons learned
- Il existe deux catégories de factsheets dans Y-OS : **tested live** vs **doc-based only** — distinction importante pour la fiabilité des informations
- Google Calendar API est un connecteur MCP disponible pour iOS dans l'écosystème Y-OS
- La valeur business d'un tel connecteur réside dans la lecture/écriture programmatique des événements, disponibilités, et métadonnées calendaires

---

### 📦 Outputs Produced
- **[doc]** `factsheet-google-calendar-connector` : Factsheet standardisée Y-OS documentant le connecteur Google Calendar — capabilities techniques, features business, limites, accès, pricing, lessons learned (en cours de production en fin de session)

---

### ⚠️ Open Items & Blockers
- **[INCERTAIN]** Statut final de la factsheet : la session se termine sur la promesse de production — il est possible que le document n'ait pas été finalisé/sauvegardé dans Notion
- **[INCERTAIN]** Emplacement de stockage exact de la factsheet dans Notion (path non confirmé dans le transcript)
- **[INCERTAIN]** Périmètre exact des scopes OAuth testés (lecture seule vs lecture+écriture vs admin)
- **[INCERTAIN]** Compatibilité confirmée iOS vs desktop — la mention iOS est faite mais non détaillée
- Le transcript est tronqué (turn 3 coupé) — des instructions complémentaires de Yannick peuvent être manquantes

---

### 🔁 Next Steps
1. Confirmer que la factsheet Google Calendar a bien été sauvegardée dans Notion (vérifier path Y-OS Tools)
2. Compléter la factsheet avec les scopes OAuth précis testés et leur niveau d'accès
3. Valider la section "lessons learned" avec les observations du test live
4. Appliquer le même processus factsheet aux autres connecteurs MCP disponibles dans Y-OS
5. Créer un index/registre des connecteurs documentés (tested vs doc-only) dans Notion

---

### 🔗 Links & References
- 🌐 `https://manus.im/app/nUGXBtL8d1iGx6VDqK7Rf6` — Session Manus source
- 🌐 `https://developers.google.com/calendar/api` — Google Calendar API documentation officielle (référencée implicitement)
- 📁 `skill: yos-optimizer` — Skill lu en début de session pour contexte
- 🔗 `session:nUGXBtL8d1iGx6VDqK7Rf6` — Session courante

---

### 🧠 Resume Hint
La factsheet standardisée du connecteur Google Calendar (testé en live via MCP) était en cours de rédaction — reprendre à partir de la structure factsheet Y-OS existante dans Notion, en intégrant les données du test live (API entry points, scopes, read/write capabilities) et la doc officielle Google Calendar API.

---

### 🏷️ Tags
`google-calendar` `mcp-connector` `factsheet` `yos-tools` `api-testing` `ios`

---

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 12 messages — 2026-06-16

**[2026-06-16 09:39] USER:** Help me test the Google Calendar connector and show me how to use its feature (e.g. show any data you fetched with it). Give me a brief about its capabilities.

**[2026-06-16 09:39] MANUS:** Sur ça — je lis d'abord le skill yos-optimizer, puis j'explore le connecteur Google Calendar via MCP.

**[2026-06-16 13:25] USER:** C'est donc un nouvel outil disponible pour iOS. Il faut donc une factsheet et d'un outil avec ses capabilités, ses limites, les lessons learned, les éventuels accès, etc. Comme d'habitude, on fait cette factsheet pour cet outil. Là, on l'a vraiment testé avec tous les accès et tous les API, les entry points, etc. D'autres fois, on n'a pas eu le temps de tester et donc c'est ce que ça donne en général d'après la documentation que tu retrouves online. Mais je veux savoir que pour tel outil, on a telle possibilité et que ça offre. On est capable d'écrire, de lire, de faire, les possibilités techniques d'accès à l'outil et les possibilités en termes de capabilities, de features, donc business-wise. Qu'est-ce que ça m'importe d'avoir cette connexion-là ? Et puis, c'est gratuit, payant, etc. Don

**[2026-06-16 13:25] MANUS:** Compris. Je cherche d'abord la structure de factsheet existante dans Notion/mémoire, puis je complète avec les données live qu'on vient de tester + doc officielle Google Calendar API.
