---
uid: m7xXGwtz7C9VBNFzCAuN8e
session_url: https://manus.im/app/m7xXGwtz7C9VBNFzCAuN8e
session_title: "Fathom MCP Connector — Test Live & Factsheet Y-OS"
date: 2026-06-16
project: "Y-OS Tech Infrastructure / Connector Registry"
language: mixed
depth: moderate
length: short
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 13:13
referenced_sessions: []
referenced_artifacts: ["Fathom MCP \u2014 Factsheet & Capability Assessment"]
referenced_urls: ["https://app.notion.com/p/38135e218cf88149a6d6c8565503cd57"]
input_files: []
message_count: 11
---

# Fathom MCP Connector — Test Live & Factsheet Y-OS

> **Session:** [m7xXGwtz7C9VBNFzCAuN8e](https://manus.im/app/m7xXGwtz7C9VBNFzCAuN8e) | **Date:** 2026-06-16 | **Project:** Y-OS Tech Infrastructure / Connector Registry | **Language:** mixed

## 📋 SESSION CARD

### 🧭 Executive Summary
Session dédiée à l'exploration et à la documentation du connecteur Fathom MCP nouvellement disponible dans Y-OS. Le compte Fathom de Yannick a été testé en live (0 réunion enregistrée à ce jour), et une factsheet complète a été produite dans Notion suivant le template standardisé des outils tech Y-OS. Fathom est identifié comme la "mémoire orale" potentielle de Y-OS dès activation de l'enregistrement de calls.

---

### 🎯 Context & Intent
Yannick souhaite systématiquement documenter chaque nouvel outil intégré à Y-OS via une factsheet standardisée (capabilities techniques, limites, accès, pricing, lessons learned). Ce travail s'inscrit dans la constitution d'une bibliothèque de référence des connecteurs disponibles — distincts selon qu'ils ont été testés en live ou documentés depuis la documentation publique uniquement. Pour Fathom, le test live était possible et a été réalisé.

---

### ✅ What Was Done
1. Lecture du skill `yos-optimizer` et exploration initiale du connecteur Fathom MCP
2. Test de connexion live sur le compte `yannick.jolliet@gmail.com` — connecté, 0 donnée présente
3. Inventaire des 9 outils MCP exposés par Fathom (mode Read-Only)
4. Récupération du template de factsheet existant (référence : Apify, MailerLite)
5. Scraping de la documentation officielle Fathom (pricing, API, limites)
6. Rédaction et publication de la factsheet complète dans Notion, sous l'arborescence ⚙️ TECH — Technologie & Infra

---

### 💡 Key Insights
- **Fathom = Read-Only** : 9 outils MCP disponibles, aucune capacité d'écriture — pas de création de meeting ni de modification de données depuis Manus
- **Compte actif mais vide** : La connexion est validée, mais sans enregistrements, les capacités sont théoriques pour l'instant
- **Free tier généreux** : Enregistrement et transcription illimités gratuits ; le plan Premium ($16/mois) débloque les Action Items IA — upgrade à considérer dès usage régulier
- **Valeur stratégique différée** : Fathom devient un actif Y-OS dès la première réunion enregistrée (récupération auto des transcripts, résumés, décisions)
- **Standard de documentation** : La distinction "testé en live" vs "documenté depuis docs" est explicitement intégrée comme critère de qualité des factsheets

---

### 📦 Outputs Produced
- **[doc]** `Fathom MCP — Factsheet & Capability Assessment` — https://app.notion.com/p/38135e218cf88149a6d6c8565503cd57 : Factsheet complète publiée dans Notion (capabilities, limites, accès, pricing, lessons learned, recommandation d'upgrade)

---

### ⚠️ Open Items & Blockers
- Aucune donnée live testable : le compte Fathom est vide, les capacités de lecture (transcripts, résumés, action items) n'ont pas pu être validées en conditions réelles
- [INCERTAIN] Périmètre exact des 9 outils MCP : la liste complète et leurs paramètres n'est pas détaillée dans le transcript
- [INCERTAIN] Disponibilité d'une API Fathom officielle distincte du connecteur MCP (à vérifier pour intégrations futures hors Manus)
- Upgrade Premium non encore décidé — à réévaluer dès premier usage en réunion

---

### 🔁 Next Steps
1. Enregistrer un premier call avec Fathom pour valider les capacités live (transcript, résumé, action items)
2. Tester les 9 outils MCP en conditions réelles dès qu'une réunion est disponible et mettre à jour la factsheet avec les résultats
3. Évaluer l'upgrade vers Premium ($16/mois) si usage de calls > 2-3/semaine
4. Intégrer la factsheet Fathom dans le registre global des connecteurs Y-OS (vérifier si un index centralisé existe)
5. Définir un workflow type : "après chaque call Fathom → Manus pull transcript → extraction décisions/action items → sync Notion"

---

### 🔗 Links & References
- 🌐 https://app.notion.com/p/38135e218cf88149a6d6c8565503cd57 — Factsheet Fathom MCP publiée dans Notion
- 🔗 session:m7xXGwtz7C9VBNFzCAuN8e — Session courante
- 📄 Template de référence : Factsheets Apify & MailerLite (même arborescence Notion ⚙️ TECH)

---

### 🧠 Resume Hint
Le connecteur Fathom MCP est documenté (factsheet Notion publiée), connecté au compte yannick.jolliet@gmail.com, Read-Only, compte vide — la prochaine étape est de valider les capacités live après enregistrement d'un premier call.

---

### 🏷️ Tags
`fathom` `mcp-connector` `tool-factsheet` `meeting-intelligence` `yos-infra`

---

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 11 messages — 2026-06-16

**[2026-06-16 09:00] USER:** Help me test the Fathom connector and show me how to use its feature (e.g. show any data you fetched with it). Give me a brief about it

**[2026-06-16 09:00] MANUS:** Sur le coup — je lis le skill yos-optimizer puis j'explore le connecteur Fathom.

**[2026-06-16 09:01] MANUS:** Je t'ai préparé un brief sur le connecteur Fathom MCP suite à mes tests. 

*Note: Ton compte Fathom (yannick.jolliet@gmail.com) est bien connecté, mais il ne contient actuellement aucun meeting, transcript ou résumé. Je t'ai donc documenté les capacités complètes du connecteur.*

**[2026-06-16 13:27] USER:** C'est donc un nouvel outil disponible pour iOS. Il faut donc une factsheet et d'un outil avec ses capabilités, ses limites, les lessons learned, les éventuels accès, etc. Comme d'habitude, on fait cette factsheet pour cet outil. Là, on l'a vraiment testé avec tous les accès et tous les API, les entry points, etc. D'autres fois, on n'a pas eu le temps de tester et donc c'est ce que ça donne en général d'après la documentation que tu retrouves online. Mais je veux savoir que pour tel outil, on a telle possibilité et que ça offre. On est capable d'écrire, de lire, de faire, les possibilités techniques d'accès à l'outil et les possibilités en termes de capabilities, de features, donc business-wise. Qu'est-ce que ça m'importe d'avoir cette connexion-là ? Et puis, c'est gratuit, payant, etc. Don

**[2026-06-16 13:27] MANUS:** Compris. Je cherche d'abord la structure existante des factsheets d'outils dans Notion/mémoire, puis je scrape la doc Fathom, et je produis la factsheet complète.

**[2026-06-16 13:28] MANUS:** Structure trouvée — template Apify/MailerLite récupéré. Je scrape maintenant la doc officielle Fathom pour compléter les données (pricing, API, limites).

**[2026-06-16 13:30] MANUS:** ## 🟣 Fathom MCP — Factsheet publiée

**Notion :** [🟣 Fathom MCP — Factsheet & Capability Assessment](https://app.notion.com/p/38135e218cf88149a6d6c8565503cd57)
**Parent :** ⚙️ TECH — Technologie & Infra (même arborescence que Apify, MailerLite, etc.)

---

### Synthèse rapide

| Dimension | Résultat |
|---|---|
| **Type** | Meeting Intelligence / Transcription |
| **Accès testé** | ✅ Connecté — `yannick.jolliet@gmail.com` |
| **Données live** | ⚠️ 0 réunion enregistrée à ce jour |
| **Mode** | Read-Only (9 outils MCP, 0 écriture) |
| **Coût actuel** | Free (enregistrement/transcription illimités) |
| **Plan recommandé** | Premium ($16/mois) pour Action Items IA |

### Ce que Fathom peut faire pour Y-OS

**Fathom est la mémoire orale de Y-OS.** Dès que tu enregistres des calls, Manus peut :
