---
uid: xus3YBWJTs7gqiABvnuJuZ
session_url: https://manus.im/app/xus3YBWJTs7gqiABvnuJuZ
session_title: "Semrush MCP Connector — Test & Factsheet Y-OS"
date: 2026-06-16
project: "Y-OS Technologie & Infra"
language: mixed
depth: moderate
length: medium
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 13:10
referenced_sessions: []
referenced_artifacts: ["https://app.notion.com/p/38135e218cf881b38cb5fd75fcbc5142"]
referenced_urls: ["https://app.notion.com/p/38135e218cf881b38cb5fd75fcbc5142", "https://manus.im/app/xus3YBWJTs7gqiABvnuJuZ"]
input_files: []
message_count: 12
---

# Semrush MCP Connector — Test & Factsheet Y-OS

> **Session:** [xus3YBWJTs7gqiABvnuJuZ](https://manus.im/app/xus3YBWJTs7gqiABvnuJuZ) | **Date:** 2026-06-16 | **Project:** Y-OS Technologie & Infra | **Language:** mixed

## 📋 SESSION CARD

### 🧭 Executive Summary
Yannick a testé le connecteur Semrush MCP dans Manus, découvrant que l'accès aux données live est bloqué faute d'un plan Semrush compatible. Suite à ce test, une factsheet structurée a été produite et archivée dans Notion, suivant la convention existante des factsheets Y-OS (Apify, MailerLite comme templates). La factsheet cartographie les 13 outils MCP, les capacités business, les limites d'accès et la valeur pour Y-OS.

---

### 🎯 Context & Intent
Yannick souhaitait (1) valider le bon fonctionnement du connecteur Semrush MCP dans son environnement Manus, et (2) produire une factsheet outil standardisée pour documenter Semrush dans Y-OS — à la fois pour usage futur et pour constituer une référence de capabilities techniques et business (lecture/écriture, accès API, coût, limites).

---

### ✅ What Was Done
1. Détection et énumération des 13 outils exposés par le connecteur Semrush MCP
2. Tentative de fetch de données live sur 4 modules (domain overview, organic keywords, backlinks, keyword research) avec `semrush.com` comme domaine test
3. Identification du bloquant : plan Semrush actuel incompatible avec l'accès MCP
4. Récupération de la structure existante des factsheets Y-OS dans Notion (templates Apify + MailerLite)
5. Scraping de la documentation officielle Semrush MCP en ligne
6. Rédaction et publication de la factsheet complète dans Notion sous **⚙️ TECH — Technologie & Infra**

---

### 💡 Key Insights
- **Le connecteur est fonctionnel côté Manus** (13 outils détectés) mais l'accès aux données réelles nécessite un plan Semrush avec droits API/MCP — ce n'est pas un bug Manus
- **13 outils cartographiés** en 4 catégories : SERP & mots-clés, Domaines & concurrents, Netlinking, Système
- La factsheet couvre 5 sections : Synthèse télégraphique, Executive Summary, Capacités techniques, Limites/accès/coût, Lessons learned
- La convention Y-OS pour les factsheets outils est bien établie et reproductible (Apify + MailerLite comme références de format)
- **Business value identifiée** : décharge cognitive SEO, veille automatisée, validation data — même sans test live complet

---

### 📦 Outputs Produced
- **[doc]** `Notion: 🟠 Semrush MCP — Factsheet & Capability Assessment` : Factsheet complète archivée dans ⚙️ TECH — Technologie & Infra, 5 sections, 13 outils cartographiés
- **[data]** `Semrush MCP tool list` : Inventaire des 13 outils MCP avec catégorisation fonctionnelle
- **[skill]** `Semrush MCP capability brief` : Connaissance structurée des capabilities, limites, coût et valeur business du connecteur

---

### ⚠️ Open Items & Blockers
- 🔴 **Bloquant actif** : Plan Semrush actuel ne permet pas l'accès MCP — aucune donnée live n'a pu être récupérée
- [INCERTAIN] Le niveau de plan Semrush exact requis pour débloquer l'accès MCP n'est pas confirmé
- [INCERTAIN] Les 13 outils listés n'ont pas tous pu être testés en conditions réelles — leurs comportements edge-case restent inconnus
- La factsheet est basée partiellement sur documentation en ligne, pas sur test exhaustif live

---

### 🔁 Next Steps
1. Vérifier le plan Semrush actuel et identifier l'upgrade nécessaire pour activer l'accès MCP
2. Une fois l'accès débloqué, re-tester les 4 modules principaux avec un domaine réel (ex. domaine client ou domaine Yannick)
3. Mettre à jour la factsheet Notion avec les résultats de test live et les lessons learned réels
4. Décider si Semrush MCP est intégré dans les workflows Y-OS automatisés (veille, reporting SEO)

---

### 🔗 Links & References
- 🌐 `https://app.notion.com/p/38135e218cf881b38cb5fd75fcbc5142` — Factsheet Semrush MCP dans Notion
- 🌐 `https://manus.im/app/xus3YBWJTs7gqiABvnuJuZ` — Session Manus source
- 🔗 session:`xus3YBWJTs7gqiABvnuJuZ` — Session courante
- 📄 Templates de référence : Factsheets Apify + MailerLite dans Notion ⚙️ TECH

---

### 🧠 Resume Hint
Le connecteur Semrush MCP est installé et cartographié (13 outils) mais bloqué faute de plan compatible — la factsheet est dans Notion ; la prochaine action est de débloquer l'accès MCP côté Semrush et de faire un test live pour valider et enrichir la factsheet.

---

### 🏷️ Tags
`semrush` `mcp-connector` `factsheet` `seo-tools` `y-os-infra` `tool-onboarding`

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 12 messages — 2026-06-16

**[2026-06-16 09:56] USER:** Help me test the Semrush connector and show me how to use its feature (e.g. show any data you fetched with it). Give me a brief about its capabilities.

**[2026-06-16 09:56] MANUS:** On it — testing the Semrush MCP connector, exploring its tools, fetching live data, and compiling a capability brief.

**[2026-06-16 09:57] MANUS:** 13 tools confirmed. Now fetching live data across 4 modules: domain overview, organic keywords, backlinks, and keyword research for a well-known domain (semrush.com itself as test subject).

**[2026-06-16 09:58] MANUS:** ### 📊 Test du Connecteur Semrush MCP

L'exploration du connecteur Semrush a été effectuée. Cependant, **l'accès aux données réelles est bloqué car ton plan Semrush actuel n'inclut pas l'accès MCP.**

Voici le brief de capacité détaillé basé sur l'exploration des outils disponibles.

---

### 1️⃣ Capacités du Connecteur (Brief)

Le connecteur expose 13 outils spécialisés, couvrant l'ensemble du spectre SEO et d'analyse concurrentielle :

*   **`overview_research`** : Snapshot global (Authority Score, trafic estimé, tendances historiques).
*   **`organic_research`** : Analyse SEO & PPC (mots-clés organiques/payants, concurrents, ad copies, keyword gap).
*   **`keyword_research`** : Analyse détaillée de mots-clés (volume, KD, CPC, SERP features, questions liées).
*   **`backlink_research`** :

**[2026-06-16 13:25] USER:** C'est donc un nouvel outil disponible pour iOS. Il faut donc une factsheet et d'un outil avec ses capabilités, ses limites, les lessons learned, les éventuels accès, etc. Comme d'habitude, on fait cette factsheet pour cet outil. Là, on l'a vraiment testé avec tous les accès et tous les API, les entry points, etc. D'autres fois, on n'a pas eu le temps de tester et donc c'est ce que ça donne en général d'après la documentation que tu retrouves online. Mais je veux savoir que pour tel outil, on a telle possibilité et que ça offre. On est capable d'écrire, de lire, de faire, les possibilités techniques d'accès à l'outil et les possibilités en termes de capabilities, de features, donc business-wise. Qu'est-ce que ça m'importe d'avoir cette connexion-là ? Et puis, c'est gratuit, payant, etc. Don

**[2026-06-16 13:25] MANUS:** Compris. Je vais d'abord localiser la structure existante des factsheets dans Notion/yOS, puis scraper la doc Semrush MCP online, et produire une factsheet complète et enrichie.

**[2026-06-16 13:26] MANUS:** Structure factsheet récupérée (Apify + MailerLite comme templates). Je scrape maintenant la doc officielle Semrush MCP pour enrichir avec les données techniques réelles.

**[2026-06-16 13:32] MANUS:** ## 🟠 Factsheet Semrush MCP — Livrée

La factsheet est créée et archivée dans Notion sous **⚙️ TECH — Technologie & Infra**, en suivant exactement la structure des factsheets existantes (Apify, MailerLite).

**Notion :** [🟠 Semrush MCP — Factsheet & Capability Assessment](https://app.notion.com/p/38135e218cf881b38cb5fd75fcbc5142)

---

### Résumé de ce qui a été produit

La factsheet couvre 5 sections :

| Section | Contenu |
| :--- | :--- |
| **0. Synthèse Télégraphique** | Action principale, méthode, business value, coût, accès, place dans Y-OS — lisible en 30 secondes |
| **1. Executive Summary** | 3 axes de valeur : décharge cognitive, veille automatisée, validation data |
| **2. Capacités Techniques** | 13 outils MCP cartographiés en 4 catégories (SERP, Domaines, Netlinking, Système) a
