---
uid: mSr5bEwX4QDBNCRELE4Q8Y
session_url: https://manus.im/app/mSr5bEwX4QDBNCRELE4Q8Y
session_title: "Calendly MCP — Test Live & Factsheet Capability Assessment"
date: 2026-06-16
project: "Y-OS Architecture Multi-Agents"
language: fr
depth: moderate
length: short
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 13:11
referenced_sessions: []
referenced_artifacts: ["https://app.notion.com/p/38135e218cf88176af78c17cd497c2c0"]
referenced_urls: ["https://app.notion.com/p/38135e218cf88176af78c17cd497c2c0", "https://calendly.com/yannick-jolliet", "https://manus.im/app/mSr5bEwX4QDBNCRELE4Q8Y"]
input_files: []
message_count: 11
---

# Calendly MCP — Test Live & Factsheet Capability Assessment

> **Session:** [mSr5bEwX4QDBNCRELE4Q8Y](https://manus.im/app/mSr5bEwX4QDBNCRELE4Q8Y) | **Date:** 2026-06-16 | **Project:** Y-OS Architecture Multi-Agents | **Language:** fr

## 📋 SESSION CARD

### 🧭 Executive Summary
Yannick a testé en live le connecteur Calendly MCP sur son compte réel, confirmant la récupération de données utilisateur et d'event types. Dans un second temps, il a demandé la création d'une factsheet standardisée pour cet outil, suivant le modèle des fiches existantes (Apify, MailerLite). La fiche a été produite et poussée dans Notion sous l'arborescence Y-OS Architecture Multi-Agents Hub.

---

### 🎯 Context & Intent
Valider opérationnellement le connecteur Calendly MCP nouvellement disponible dans Y-OS, puis documenter ses capacités techniques et business dans une factsheet réutilisable — permettant à tout agent ou collaborateur de savoir en un coup d'œil ce que cet outil apporte, comment y accéder, et à quel coût.

---

### ✅ What Was Done
1. Lecture du skill `yos-optimizer` pour calibrer le contexte
2. Connexion live au compte Calendly de Yannick via le MCP (34 outils disponibles)
3. Récupération de données réelles : profil utilisateur + 4 event types configurés
4. Consultation de la structure existante des factsheets dans Notion (templates Apify + MailerLite)
5. Scraping de la documentation officielle Calendly API pour compléter les données
6. Rédaction et push de la factsheet complète dans Notion, sous `⚙️ TECH → 🏛️ Y-OS Architecture Multi-Agents Hub`

---

### 💡 Key Insights
- Le connecteur Calendly MCP expose **34 outils** couvrant lecture, écriture et suppression — périmètre plus large que la majorité des autres connecteurs Y-OS documentés à ce jour
- Compte Yannick : Owner depuis Feb 2016, timezone Europe/Berlin, 4 event types dont 2 inactifs (30 min, 60 min)
- La factsheet suit un format normalisé en 4+ sections (Synthèse télégraphique, Executive Summary, Capacités techniques, Limites & Lessons Learned) — ce format doit être maintenu pour cohérence inter-fiches
- La session illustre deux niveaux de documentation : test live (données réelles) vs documentation par doc en ligne (cas où le test n'a pas eu lieu) — distinction utile à conserver dans la factsheet elle-même
- Les cas d'usage business identifiés : EA autonome, gestion post-réunion, no-show management

---

### 📦 Outputs Produced
- **[doc]** `🔵 Calendly MCP — Factsheet & Capability Assessment` → https://app.notion.com/p/38135e218cf88176af78c17cd497c2c0 : Factsheet complète structurée (synthèse, capacités, limites, coût, lessons learned), poussée dans Notion sous Y-OS Hub
- **[data]** *Profil utilisateur Calendly live* : nom, email, slug, URL booking, timezone, rôle org, date création
- **[data]** *Event Types live* : 4 types mappés (15 min actif, 30/60 min inactifs, + 1 autre)

---

### ⚠️ Open Items & Blockers
- Le transcript est tronqué — la section **Limites & Lessons Learned** de la factsheet n'est pas entièrement visible ; contenu exact [INCERTAIN]
- Le 4e event type n'est pas nommé dans le transcript visible [INCERTAIN]
- Coût exact du plan Calendly requis pour accès API non confirmé dans le transcript [INCERTAIN]
- Aucune mention de tests d'écriture (création/modification d'événement) — validé ou non [INCERTAIN]

---

### 🔁 Next Steps
1. Vérifier la factsheet Notion pour s'assurer que toutes les sections sont complètes et cohérentes avec le format Apify/MailerLite
2. Tester les outils d'écriture et suppression du MCP Calendly (pas seulement la lecture) pour compléter les lessons learned
3. Identifier un cas d'usage concret Y-OS à activer en priorité (ex. : routing EA → booking automatique)
4. Mettre à jour l'index des connecteurs Y-OS disponibles avec l'entrée Calendly
5. Si d'autres connecteurs sont testés, appliquer le même processus factsheet en distinguant "testé live" vs "documenté par API doc"

---

### 🔗 Links & References
- 🌐 https://app.notion.com/p/38135e218cf88176af78c17cd497c2c0 — Factsheet Calendly MCP dans Notion
- 🌐 https://calendly.com/yannick-jolliet — Page de booking Yannick
- 🌐 https://manus.im/app/mSr5bEwX4QDBNCRELE4Q8Y — Session source

---

### 🧠 Resume Hint
La factsheet Calendly MCP a été créée et pushée dans Notion (lien ci-dessus) ; pour continuer, vérifier la complétude des sections Limites/Lessons Learned et envisager les tests des outils d'écriture MCP encore non validés.

---

### 🏷️ Tags
`calendly` `mcp-connector` `factsheet` `y-os-infra` `tool-documentation` `integration-test`

---

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 11 messages — 2026-06-16

**[2026-06-16 09:17] USER:** Help me test the Calendly connector and show me how to use its feature (e.g. show any data you fetched with it). Give me a brief about its capabilities.

**[2026-06-16 09:17] MANUS:** Sur ce. Je lis le skill yos-optimizer puis je teste le connecteur Calendly en live — récupération de données réelles + brief des capacités.

**[2026-06-16 09:19] MANUS:** # Calendly MCP — Test & Brief

**Mode** : BALANCED | **Outil** : Calendly MCP (34 outils) | **Compte** : yannick.jolliet@gmail.com

---

## Données live récupérées

### Profil utilisateur
| Champ | Valeur |
|---|---|
| Nom | Yannick Jolliet |
| Slug | `yannick-jolliet` |
| Email | yannick.jolliet@gmail.com |
| URL de booking | https://calendly.com/yannick-jolliet |
| Timezone | Europe/Berlin |
| Compte créé | 11 Feb 2016 |
| Rôle org | **Owner** |

---

### Event Types (4 types configurés)
| Nom | Durée | Statut | URL |
|---|---|---|---|
| 15 Minute Meeting | 15 min | ✅ Actif | [/15min](https://calendly.com/yannick-jolliet/15min) |
| 30 Minute Meeting | 30 min | ❌ Inactif | [/30min](https://calendly.com/yannick-jolliet/30min) |
| 60 Minute Meeting | 60 min | ❌ Inactif | [/60min](https://ca

**[2026-06-16 13:25] USER:** C'est donc un nouvel outil disponible pour iOS. Il faut donc une factsheet et d'un outil avec ses capabilités, ses limites, les lessons learned, les éventuels accès, etc. Comme d'habitude, on fait cette factsheet pour cet outil. Là, on l'a vraiment testé avec tous les accès et tous les API, les entry points, etc. D'autres fois, on n'a pas eu le temps de tester et donc c'est ce que ça donne en général d'après la documentation que tu retrouves online. Mais je veux savoir que pour tel outil, on a telle possibilité et que ça offre. On est capable d'écrire, de lire, de faire, les possibilités techniques d'accès à l'outil et les possibilités en termes de capabilities, de features, donc business-wise. Qu'est-ce que ça m'importe d'avoir cette connexion-là ? Et puis, c'est gratuit, payant, etc. Don

**[2026-06-16 13:26] MANUS:** Compris. Je cherche d'abord la structure existante des factsheets dans Notion, puis je complète avec la doc Calendly en ligne avant de produire la fiche.

**[2026-06-16 13:27] MANUS:** Structure template capturée (Apify + MailerLite). Je scrape maintenant la doc officielle Calendly API avant de rédiger.

**[2026-06-16 13:30] MANUS:** ✅ Factsheet créée et poussée dans Notion.

**Emplacement :** [🔵 Calendly MCP — Factsheet & Capability Assessment](https://app.notion.com/p/38135e218cf88176af78c17cd497c2c0)
**Parent :** `⚙️ TECH — Technologie & Infra` → `🏛️ Y-OS — Architecture Multi-Agents Hub` (même arborescence que les autres factsheets Apify, MailerLite, etc.)

---

**Ce qui est couvert dans la fiche :**

| Section | Contenu |
|---|---|
| **0. Synthèse télégraphique** | Action principale, méthode, business value, coût, place dans Y-OS — lisible en 10 secondes |
| **1. Executive Summary** | Valeur métier détaillée (EA autonome, data post-réunion, no-show management) |
| **2. Capacités techniques** | 34 outils MCP mappés par domaine (Read/Write/Delete) avec rôle de chaque outil |
| **3. Limites & Lessons Learned** | Paywa
