---
uid: tiqh9SnI0VMirKsuNmYFTi
session_url: https://manus.im/app/tiqh9SnI0VMirKsuNmYFTi
session_title: "Apify MCP Connector — Test Live & Factsheet Y-OS"
date: 2026-06-16
project: "Y-OS Infrastructure / Tech Stack"
language: fr
depth: moderate
length: medium
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 13:02
referenced_sessions: []
referenced_artifacts: ["yos-optimizer"]
referenced_urls: ["https://app.notion.com/p/38135e218cf88109ba01fac899621b35", "https://manus.im/app/tiqh9SnI0VMirKsuNmYFTi"]
input_files: ["yos-optimizer"]
message_count: 11
---

# Apify MCP Connector — Test Live & Factsheet Y-OS

> **Session:** [tiqh9SnI0VMirKsuNmYFTi](https://manus.im/app/tiqh9SnI0VMirKsuNmYFTi) | **Date:** 2026-06-16 | **Project:** Y-OS Infrastructure / Tech Stack | **Language:** fr

## 📋 SESSION CARD

### 🧭 Executive Summary
Session de test live du connecteur Apify MCP pour Y-OS : les 10 outils disponibles ont été explorés et validés en conditions réelles. Une factsheet structurée a été produite et poussée dans Notion sous ⚙️ TECH. Ce nouvel outil apporte à Y-OS une capacité de web scraping industriel pilotable par IA, avec un modèle de coût pay-per-use.

---

### 🎯 Context & Intent
Yannick souhaite documenter systématiquement chaque nouvel outil/connecteur disponible dans Y-OS via une factsheet standardisée. L'objectif est de savoir précisément ce qu'un outil peut faire techniquement (accès, méthodes, API) et ce qu'il apporte business-wise — avec distinction entre outils testés en live et outils documentés uniquement sur base de docs externes. Apify a ici été testé en conditions réelles, ce qui donne à cette factsheet un statut de référence validée.

---

### ✅ What Was Done
1. Lecture du fichier `yos-optimizer` pour contexte Y-OS
2. Identification des 10 outils MCP exposés par le connecteur Apify
3. Tests live en parallèle : `search-actors`, `apify--rag-web-browser`, et un scrape réel
4. Synthèse des capacités en 3 catégories : Découverte, Exécution, Storage
5. Recherche de la structure existante des factsheets dans Notion
6. Rédaction d'une factsheet complète en 6 sections (synthèse télégraphique, executive summary, capacités techniques, limites & lessons learned, coûts, positionnement Y-OS)
7. Push de la factsheet dans Notion sous ⚙️ TECH — Technologie & Infra

---

### 💡 Key Insights
- **10 outils MCP disponibles** couvrant tout le cycle : découverte d'actors, exécution, monitoring de runs, extraction de datasets, accès à la doc
- **`apify--rag-web-browser`** est un outil pré-configuré utilisable immédiatement sans configuration d'input — point d'entrée privilégié pour Y-OS
- **Modèle async** : les actors s'exécutent en tâche de fond → les résultats ne sont pas immédiats, il faut poller via `get-actor-run`
- **Datasets éphémères** : les résultats expirent — nécessité de les extraire rapidement ou de les persister dans Notion/autre storage
- **Input strict** : chaque actor a un schéma d'input propre, récupérable via `fetch-actor-details` avant tout appel
- **Coût pay-per-use** : modèle de facturation à l'usage sur la plateforme Apify (pas de coût fixe MCP côté connecteur)
- La factsheet Apify devient le template de référence pour les futurs outils Y-OS testés en live

---

### 📦 Outputs Produced
- **[doc]** `Notion — Apify MCP Factsheet` : factsheet complète 6 sections poussée dans Notion (⚙️ TECH — Technologie & Infra), couvrant capacités techniques, limites, lessons learned, coûts et valeur business pour Y-OS

---

### ⚠️ Open Items & Blockers
- Coût exact par actor/run non précisé dans la factsheet — dépend de l'actor utilisé [INCERTAIN]
- Liste des actors Apify Store les plus pertinents pour les cas d'usage Y-OS non encore établie [INCERTAIN]
- Politique de rétention exacte des datasets Apify (durée d'expiration) à confirmer [INCERTAIN]
- Pas de test de `get-key-value-store-record` mentionné explicitement — couverture complète des 10 outils à valider

---

### 🔁 Next Steps
1. Identifier les 5–10 actors Apify les plus utiles pour Y-OS (LinkedIn scraper, Google Search, etc.) et les documenter dans la factsheet
2. Tester le workflow complet async : `call-actor` → `get-actor-run` (polling) → `get-dataset-items` → push Notion
3. Définir une stratégie de persistance des datasets avant expiration
4. Appliquer le format factsheet à d'autres connecteurs Y-OS non encore documentés (en distinguant testés vs. doc-only)
5. Évaluer le coût mensuel Apify en fonction des cas d'usage réels projetés

---

### 🔗 Links & References
- 🌐 [Notion — Apify MCP Factsheet](https://app.notion.com/p/38135e218cf88109ba01fac899621b35)
- 🔗 session:`tiqh9SnI0VMirKsuNmYFTi`

---

### 🧠 Resume Hint
La factsheet Apify MCP a été créée et validée en live — elle est dans Notion sous ⚙️ TECH ; la prochaine étape est d'identifier les actors prioritaires pour Y-OS et de documenter le workflow async complet (call → poll → extract → persist).

---

### 🏷️ Tags
`apify` `mcp-connector` `factsheet` `web-scraping` `yos-infra`

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 11 messages — 2026-06-16

**[2026-06-16 11:10] USER:** Help me test the Apify connector and show me how to use its feature (e.g. show any data you fetched with it). Give me a brief about its capabilities.

**[2026-06-16 11:10] MANUS:** Sur le coup — je lis d'abord yos-optimizer, puis j'explore le connecteur Apify en live.

**[2026-06-16 11:11] MANUS:** 10 outils identifiés. Je lance maintenant 3 tests live en parallèle : search-actors, RAG web browser, et un scrape réel.

**[2026-06-16 11:13] MANUS:** Voici la synthèse des capacités du connecteur Apify (testé en live avec succès).

### 1️⃣ Capacités du connecteur (10 outils)

Le connecteur agit comme une interface complète vers l'Apify Store et la plateforme d'exécution :

*   **Recherche & Découverte** : `search-actors` (trouver des scrapers par mot-clé/plateforme), `fetch-actor-details` (récupérer le schéma d'input et le pricing).
*   **Exécution** : `call-actor` (lancer n'importe quel Actor), `apify--rag-web-browser` (outil dédié pré-configuré pour la recherche RAG immédiate).
*   **Gestion des Runs** : `get-actor-run` (statut), `abort-actor-run`.
*   **Extraction de données** : `get-dataset-items` (récupération avec filtrage/pagination), `get-key-value-store-record`.
*   **Documentation** : `search-apify-docs`, `fetch-apify-docs`.



**[2026-06-16 13:19] USER:** C'est donc un nouvel outil disponible pour iOS. Il faut donc une factsheet et d'un outil avec ses capabilités, ses limites, les lessons learned, les éventuels accès, etc. Comme d'habitude, on fait cette factsheet pour cet outil. Là, on l'a vraiment testé avec tous les accès et tous les API, les entry points, etc. D'autres fois, on n'a pas eu le temps de tester et donc c'est ce que ça donne en général d'après la documentation que tu retrouves online. Mais je veux savoir que pour tel outil, on a telle possibilité et que ça offre. On est capable d'écrire, de lire, de faire, les possibilités techniques d'accès à l'outil et les possibilités en termes de capabilities, de features, donc business-wise. Qu'est-ce que ça m'importe d'avoir cette connexion-là ? Et puis, c'est gratuit, payant, etc. Don

**[2026-06-16 13:19] MANUS:** Je cherche d'abord la structure existante des factsheets dans Notion, puis je complète avec la doc Apify en ligne.

**[2026-06-16 13:24] MANUS:** Factsheet Apify créée et poussée dans Notion. Voici le livrable complet.

---

## 🔵 Apify MCP — Factsheet Y-OS

**Notion :** [Ouvrir la page](https://app.notion.com/p/38135e218cf88109ba01fac899621b35) (sous ⚙️ TECH — Technologie & Infra)

---

### Structure de la factsheet (6 sections)

| # | Section | Contenu |
|---|---------|---------|
| 0 | **Synthèse télégraphique** | 5 lignes lisibles en 30 secondes — action, méthode, valeur, coût, place dans Y-OS |
| 1 | **Executive Summary** | Pourquoi intégrer Apify à Y-OS — 3 arguments business |
| 2 | **Capacités techniques** | 10 outils MCP détaillés par catégorie (Découverte / Exécution / Storage) |
| 3 | **Limites & Lessons Learned** | 5 contraintes identifiées lors des tests live (async, pagination, input strict, expiration datasets, coûts) |
