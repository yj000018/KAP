---
uid: kPrbbK9RoZM9N2X1TfTjn9
session_url: https://manus.im/app/kPrbbK9RoZM9N2X1TfTjn9
session_title: "RevenueCat MCP — Test Live & Production Factsheet Y-OS"
date: 2026-06-16
project: "Y-OS Tech Stack / iOS Infrastructure"
language: fr
depth: moderate
length: short
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 13:16
referenced_sessions: []
referenced_artifacts: []
referenced_urls: ["https://app.notion.com/p/38135e218cf881e1b272d304a6a520ce", "https://manus.im/app/kPrbbK9RoZM9N2X1TfTjn9"]
input_files: []
message_count: 11
---

# RevenueCat MCP — Test Live & Production Factsheet Y-OS

> **Session:** [kPrbbK9RoZM9N2X1TfTjn9](https://manus.im/app/kPrbbK9RoZM9N2X1TfTjn9) | **Date:** 2026-06-16 | **Project:** Y-OS Tech Stack / iOS Infrastructure | **Language:** fr

## 📋 SESSION CARD

### 🧭 Executive Summary
Session de test et documentation du connecteur RevenueCat MCP, avec exploration live des 93 outils disponibles et extraction de données réelles depuis le compte RevenueCat de Yannick. Une factsheet structurée en 6 sections a été produite et publiée dans Notion (espace ⚙️ TECH). La valeur principale : avoir une référence permanente des capacités, limites et lessons learned de cet outil pour l'écosystème iOS Y-OS.

---

### 🎯 Context & Intent
Yannick dispose d'un connecteur RevenueCat MCP nouvellement activé et veut : (1) valider qu'il fonctionne réellement via un test live avec tous les endpoints/API, et (2) produire une factsheet standardisée Y-OS documentant capacités techniques, features business, limites, coûts et accès — dans le même format que les autres outils tech déjà archivés (ex. Apify).

---

### ✅ What Was Done
1. Lecture du skill `yos-optimizer` pour aligner le format de réponse
2. Connexion et exploration du connecteur RevenueCat via MCP
3. Détection et inventaire des 93 outils MCP disponibles (structurés par catégories)
4. Fetch de données réelles : projets, apps, métriques, entitlements, offerings (compte vide/nouveau)
5. Recherche du template de factsheet existant dans Notion/mémoire Y-OS
6. Production d'une factsheet RevenueCat en 6 sections (Synthèse, Executive Summary, Capacités Techniques, Limites & Lessons Learned, Coûts, et Accès)
7. Publication de la factsheet dans Notion (espace ⚙️ TECH — même niveau qu'Apify)

---

### 💡 Key Insights
- **93 outils MCP détectés**, structurés en 3 grandes catégories : Infrastructure, Clients, Analyse/AI
- **Compte testé réel mais vide** (projet fraîchement créé) — les données retournées sont structurellement valides mais sans historique métier
- **4 contraintes critiques identifiées en live** : rate limits, paywalls async, Apple gate (règles App Store), et scopes API à configurer
- **Valeur business core** : RevenueCat agit comme SSOT (Single Source of Truth) des revenus IAP + décharge la gestion technique des abonnements + permet des paywalls AI-natifs
- Le format de factsheet Y-OS est désormais confirmé comme standard réutilisable pour tout nouvel outil tech

---

### 📦 Outputs Produced
- **[doc]** `Notion — RevenueCat MCP Factsheet` : Factsheet 6 sections publiée dans Notion, espace ⚙️ TECH — https://app.notion.com/p/38135e218cf881e1b272d304a6a520ce
- **[doc]** `Markdown joint (session)` : Brief des 93 outils MCP structurés par catégories + audit log de connexion (produit en session, non archivé séparément)

---

### ⚠️ Open Items & Blockers
- Le compte RevenueCat testé était vide — aucune donnée métier réelle (revenus, subscribers actifs) n'a pu être validée [INCERTAIN : les outils de reporting/analytics fonctionnent-ils identiquement sur un compte avec données ?]
- La section finale de la factsheet (transcript tronqué à "4 contraintes testées") — vérifier que les sections 4, 5, 6 (Coûts, Accès, Next Steps) sont bien complètes dans Notion [INCERTAIN]
- Scopes API : configuration exacte des permissions nécessaires non entièrement documentée dans la session

---

### 🔁 Next Steps
1. Alimenter le compte RevenueCat avec des produits/abonnements réels (iOS) et re-tester les outils de reporting et analytics
2. Vérifier l'intégrité complète de la factsheet Notion (sections 4-6)
3. Connecter RevenueCat aux apps iOS Y-OS actives pour activer le flux de données réel
4. Documenter les scopes API exacts requis pour chaque catégorie d'outils (lecture vs écriture)
5. Planifier un test des fonctionnalités de Paywall AI natif (Async) une fois un produit live configuré

---

### 🔗 Links & References
- 🌐 https://app.notion.com/p/38135e218cf881e1b272d304a6a520ce — Factsheet RevenueCat MCP dans Notion
- 🔗 session:kPrbbK9RoZM9N2X1TfTjn9 — Session courante (test RevenueCat + production factsheet)

---

### 🧠 Resume Hint
La factsheet RevenueCat MCP a été créée et publiée dans Notion (⚙️ TECH) — le compte testé était vide ; la prochaine étape est de tester les outils analytics/reporting avec un compte ayant des données réelles, et de vérifier la complétude des sections 4-6 de la factsheet.

---

### 🏷️ Tags
`revenuecat` `mcp-connector` `ios-monetization` `factsheet` `yos-tech-stack` `iap`

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 11 messages — 2026-06-16

**[2026-06-16 08:47] USER:** Help me test the RevenueCat connector and show me how to use its feature (e.g. show any data you fetched with it). Give me a brief about its cap

**[2026-06-16 08:47] MANUS:** Sur ça — je lis le skill yos-optimizer d'abord, puis j'explore le connecteur RevenueCat via MCP.

**[2026-06-16 08:47] MANUS:** 93 outils détectés. Je fetch maintenant les données réelles — projets, apps, métriques, entitlements, offerings.

**[2026-06-16 08:49] MANUS:** Voici le brief des capacités du connecteur RevenueCat MCP et les données réelles extraites de ton compte (projet vide fraîchement créé). Tout est fonctionnel. 

Le fichier Markdown joint contient le détail des 93 outils structurés par catégories et l'audit log de ta connexion.

**[2026-06-16 13:27] USER:** C'est donc un nouvel outil disponible pour iOS. Il faut donc une factsheet et d'un outil avec ses capabilités, ses limites, les lessons learned, les éventuels accès, etc. Comme d'habitude, on fait cette factsheet pour cet outil. Là, on l'a vraiment testé avec tous les accès et tous les API, les entry points, etc. D'autres fois, on n'a pas eu le temps de tester et donc c'est ce que ça donne en général d'après la documentation que tu retrouves online. Mais je veux savoir que pour tel outil, on a telle possibilité et que ça offre. On est capable d'écrire, de lire, de faire, les possibilités techniques d'accès à l'outil et les possibilités en termes de capabilities, de features, donc business-wise. Qu'est-ce que ça m'importe d'avoir cette connexion-là ? Et puis, c'est gratuit, payant, etc. Don

**[2026-06-16 13:27] MANUS:** Je cherche d'abord la structure de factsheet existante dans Notion/mémoire Y-OS avant de construire celle de RevenueCat.

**[2026-06-16 13:31] MANUS:** Factsheet créée et publiée dans Notion. Voici le résumé de ce qui a été produit.

---

## 💳 RevenueCat MCP — Factsheet

**Notion :** [Ouvrir la page](https://app.notion.com/p/38135e218cf881e1b272d304a6a520ce) (dans ⚙️ TECH — Technologie & Infra, même niveau qu'Apify)

---

### Structure de la factsheet (6 sections)

| Section | Contenu |
|---|---|
| **0. Synthèse Télégraphique** | Action principale, méthode, business value, coût, place dans Y-OS — lisible en 30 secondes |
| **1. Executive Summary** | 3 angles : décharge technique IAP, Paywall AI natif, SSOT revenus |
| **2. Capacités Techniques** | 93 outils MCP, 3 catégories (Infrastructure, Clients, Analyse/AI) |
| **3. Limites & Lessons Learned** | 4 contraintes testées en live : rate limits, async paywall, Apple gate, scopes API |
| **
