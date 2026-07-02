---
uid: hXBFBPDzVB5fXe8jAc92PR
session_url: https://manus.im/app/hXBFBPDzVB5fXe8jAc92PR
session_title: "Ahrefs MCP Connector — Test Live & Factsheet Y-OS"
date: 2026-06-16
project: "Y-OS Infrastructure / Tool Onboarding"
language: mixed
depth: moderate
length: medium
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 13:17
referenced_sessions: []
referenced_artifacts: ["Ahrefs MCP Factsheet Notion"]
referenced_urls: ["https://app.notion.com/p/38135e218cf88114b5abd77f1ae813ce", "https://manus.im/app/hXBFBPDzVB5fXe8jAc92PR"]
input_files: []
message_count: 11
---

# Ahrefs MCP Connector — Test Live & Factsheet Y-OS

> **Session:** [hXBFBPDzVB5fXe8jAc92PR](https://manus.im/app/hXBFBPDzVB5fXe8jAc92PR) | **Date:** 2026-06-16 | **Project:** Y-OS Infrastructure / Tool Onboarding | **Language:** mixed

## 📋 SESSION CARD

### 🧭 Executive Summary
Le connecteur Ahrefs MCP (129 outils) a été testé live dans Y-OS, révélant une limitation critique : le compte lié ne dispose pas de crédits API payants, bloquant la majorité des endpoints. Les seules données live extraites sont les Domain Ratings (OpenAI: 93, Anthropic: 92, Manus: 86). Une factsheet complète a été produite et poussée dans Notion, documentant capacités, limites et lessons learned pour référence permanente dans Y-OS.

---

### 🎯 Context & Intent
Yannick souhaitait (1) tester concrètement le connecteur Ahrefs disponible via MCP, et (2) produire une factsheet standardisée documentant ses capacités techniques et business, ses limites, ses accès et son coût — selon le format habituel Y-OS pour les nouveaux outils intégrés.

---

### ✅ What Was Done
1. Chargement des skills `tool-router` et `yos-optimizer` pour contextualiser l'exploration
2. Découverte et inventaire des 129 outils Ahrefs disponibles via MCP
3. Lancement de requêtes live : subscription info, Domain Rating, site metrics, keyword volume, SERP overview
4. Constat documenté : plan insuffisant (`Insufficient plan`) sur la majorité des endpoints payants
5. Extraction réussie des Domain Ratings via l'outil gratuit (OpenAI, Anthropic, Manus)
6. Recherche de la structure de factsheet existante dans Notion (Manus Memory)
7. Rédaction et push d'une factsheet 7-sections dans Notion

---

### 💡 Key Insights
- **129 outils MCP disponibles** couvrant Site Explorer, Keywords Explorer, SERP, Rank Tracker, Site Audit, Brand Radar LLM, Web Analytics, GSC, Batch Analysis
- **Paywall critique** : sans crédits API Ahrefs payants, seuls les outils gratuits (ex. Domain Rating) sont accessibles
- **Domain Rating est gratuit** et fonctionnel — seule donnée live extractible dans l'état actuel
- **Two-step process** identifié comme contrainte : certains outils nécessitent des appels asynchrones
- **Consommation API Units** à surveiller : chaque appel consomme des unités, la gestion budgétaire est un facteur clé
- **ToS MCP Ahrefs** : contraintes d'usage à respecter, documentées dans la factsheet
- Le format factsheet Y-OS est maintenant appliqué systématiquement aux nouveaux connecteurs, qu'ils soient testés live ou documentés via doc officielle

---

### 📦 Outputs Produced
- **[doc]** `https://app.notion.com/p/38135e218cf88114b5abd77f1ae813ce` : Factsheet Ahrefs MCP (7 sections) — Synthèse télégraphique, Executive Summary, Capacités Techniques, Limites & Lessons Learned, accès, coût, positionnement Y-OS
- **[data]** `domain_ratings_live` : Domain Ratings extraits live — OpenAI: 93, Anthropic: 92, Manus: 86

---

### ⚠️ Open Items & Blockers
- **🔴 BLOQUANT** : Compte Ahrefs sans crédits API payants → 90%+ des endpoints inaccessibles
- **[INCERTAIN]** Coût exact des API Units Ahrefs selon le plan nécessaire pour les cas d'usage Y-OS cibles
- **[INCERTAIN]** La factsheet est-elle poussée dans la bonne base Notion / sous le bon template final validé par Yannick ?
- Les sections 4–7 de la factsheet ne sont pas visibles dans le transcript — leur contenu exact est partiellement inconnu

---

### 🔁 Next Steps
1. **Décider** si l'on ajoute des crédits API Ahrefs (évaluer ROI vs cas d'usage : Content Strategy, Brand Radar IA, Audit automatisé)
2. **Valider** la factsheet Notion avec Yannick et confirmer qu'elle respecte le template standard Y-OS
3. **Tester les endpoints payants** une fois les crédits ajoutés : Keywords Explorer, SERP, Site Audit en priorité
4. **Documenter le coût réel** par requête type pour alimenter la section budget/pricing de la factsheet
5. **Intégrer la factsheet** dans l'index des outils Y-OS (si un index centralisé existe)

---

### 🔗 Links & References
- 🌐 `https://app.notion.com/p/38135e218cf88114b5abd77f1ae813ce` — Factsheet Ahrefs MCP dans Notion
- 🌐 `https://manus.im/app/hXBFBPDzVB5fXe8jAc92PR` — Session Manus source
- 🔗 `session:hXBFBPDzVB5fXe8jAc92PR` — Session courante

---

### 🧠 Resume Hint
Le connecteur Ahrefs MCP est installé et documenté (factsheet Notion), mais bloqué par l'absence de crédits API payants — la prochaine action est une décision go/no-go sur l'achat de crédits avant tout test approfondi.

---

### 🏷️ Tags
`ahrefs` `mcp-connector` `seo-tools` `factsheet` `tool-onboarding` `y-os-infrastructure`

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 11 messages — 2026-06-16

**[2026-06-16 08:44] USER:** Help me test the Ahrefs connector and show me how to use its feature (e.g. show any data you fetched with it). Give me a brief about its capabilities.

**[2026-06-16 08:44] MANUS:** Sur ça — je lis d'abord le skill tool-router + yos-optimizer, puis j'explore le connecteur Ahrefs via MCP. Je te reviens avec un brief complet + données réelles.

**[2026-06-16 08:44] MANUS:** 129 outils découverts. Je lance maintenant les requêtes live : subscription info (gratuit), domain rating, site metrics, keyword volume, SERP overview. Résultats dans 1-2 min.

**[2026-06-16 08:47] MANUS:** Voici le brief complet sur le connecteur Ahrefs.

### Points clés :
1️⃣ **129 outils disponibles** couvrant tout le scope SEO (Site Explorer, Rank Tracker, Brand Radar LLM).
2️⃣ **Limitation actuelle** : Le compte lié n'a pas de crédits API payants (`Insufficient plan` sur la majorité des endpoints).
3️⃣ **Données Live** : J'ai pu extraire les Domain Ratings (outil gratuit) d'un panel tech (OpenAI: 93, Anthropic: 92, Manus: 86).

Le fichier joint contient le détail complet. Si tu veux débloquer les autres endpoints, il faudra ajouter des crédits API au compte Ahrefs.

**[2026-06-16 13:27] USER:** C'est donc un nouvel outil disponible pour iOS. Il faut donc une factsheet et d'un outil avec ses capabilités, ses limites, les lessons learned, les éventuels accès, etc. Comme d'habitude, on fait cette factsheet pour cet outil. Là, on l'a vraiment testé avec tous les accès et tous les API, les entry points, etc. D'autres fois, on n'a pas eu le temps de tester et donc c'est ce que ça donne en général d'après la documentation que tu retrouves online. Mais je veux savoir que pour tel outil, on a telle possibilité et que ça offre. On est capable d'écrire, de lire, de faire, les possibilités techniques d'accès à l'outil et les possibilités en termes de capabilities, de features, donc business-wise. Qu'est-ce que ça m'importe d'avoir cette connexion-là ? Et puis, c'est gratuit, payant, etc. Don

**[2026-06-16 13:27] MANUS:** Compris. Je cherche d'abord la structure de factsheet existante dans Notion (Manus Memory), puis je complète avec la doc Ahrefs en ligne. Je reviens avec la factsheet complète.

**[2026-06-16 13:33] MANUS:** Factsheet créée et poussée dans Notion. Voici le lien direct :

**[🔍 Ahrefs MCP — Factsheet & Capability Assessment](https://app.notion.com/p/38135e218cf88114b5abd77f1ae813ce)**

---

### Ce qui a été documenté (7 sections) :

**0. Synthèse Télégraphique** — Lecture 30 secondes. Action, méthode, valeur, coût, place dans Y-OS.

**1. Executive Summary** — 3 cas d'usage business : Content Strategy, Brand Radar IA, Audit automatisé.

**2. Capacités Techniques** — 129 outils mappés par catégorie : Site Explorer, Keywords Explorer, SERP, Rank Tracker, Site Audit, Brand Radar, Web Analytics, GSC, Batch Analysis.

**3. Limites & Lessons Learned** — 5 contraintes critiques documentées depuis les tests live : paywall, two-step process, consommation API Units, asynchronisme, ToS MCP.

**4. Données Li
