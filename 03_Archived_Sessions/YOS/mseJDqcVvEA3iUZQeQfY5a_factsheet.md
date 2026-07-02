---
uid: mseJDqcVvEA3iUZQeQfY5a
session_url: https://manus.im/app/mseJDqcVvEA3iUZQeQfY5a
session_title: "Meta Ads Audit (No Data) + Meta Marketing MCP Factsheet Creation"
date: 2026-06-16
project: "yOS — Tech Infra / Tool Documentation"
language: mixed
depth: moderate
length: medium
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 13:17
referenced_sessions: []
referenced_artifacts: ["https://app.notion.com/p/38135e218cf88103b70eefe72e1305d3"]
referenced_urls: ["https://app.notion.com/p/38135e218cf88103b70eefe72e1305d3", "https://manus.im/app/mseJDqcVvEA3iUZQeQfY5a"]
input_files: []
message_count: 16
---

# Meta Ads Audit (No Data) + Meta Marketing MCP Factsheet Creation

> **Session:** [mseJDqcVvEA3iUZQeQfY5a](https://manus.im/app/mseJDqcVvEA3iUZQeQfY5a) | **Date:** 2026-06-16 | **Project:** yOS — Tech Infra / Tool Documentation | **Language:** mixed

## 📋 SESSION CARD

### 🧭 Executive Summary
Yannick a demandé un audit Meta Ads sur 30 jours, qui a révélé zéro dépense et zéro campagne active sur les deux comptes connectés, rendant l'analyse de performance impossible. La session a pivoté vers la documentation systématique du connecteur MCP Meta Marketing. Une factsheet complète a été produite et versée dans Notion (section TECH), couvrant les 9 outils read-only disponibles, les limites write, et les implications business.

### 🎯 Context & Intent
Yannick voulait initialement un diagnostic de performance publicitaire actionnable (ce qui fonctionne, ce qui gaspille du budget, prochaines étapes). Face à l'absence de données, la session a été réorientée vers la capitalisation systématique : créer une factsheet standardisée du connecteur Meta Marketing MCP, conforme au format yOS déjà utilisé pour Apify et MailerLite, documentant capabilities réelles (testées + doc officielle), limites techniques, accès, et valeur business.

### ✅ What Was Done
1. Chargement des skills `meta-ads-analyzer` et `tool-router`
2. Pull complet des données Meta Ads via MCP sur les deux comptes connectés (`act_157086230` / `act_498904971225575`)
3. Diagnostic des causes d'absence de données (3 hypothèses formulées)
4. Récupération du template factsheet existant depuis Notion (références Apify + MailerLite)
5. Extraction de la documentation officielle Meta Marketing API en ligne
6. Rédaction et push de la factsheet Meta Marketing MCP dans Notion (section TECH)

### 💡 Key Insights
- **Aucune donnée publicitaire disponible** : les deux comptes affichent `amount_spent: 0.00` — soit inactivité réelle, soit problème de connexion/permissions
- **1 campagne filtrée automatiquement** par le connecteur car classée Special Category (logement/emploi/finance) — limite structurelle du MCP
- **Le connecteur est 100% read-only** : pas d'écriture possible (création campagne, modification budget, pause) via MCP — nécessite l'API directe ou l'interface Meta pour toute action
- **9 outils MCP disponibles** couvrant campagnes, adsets, insights, ROAS, métriques granulaires — valeur réelle en mode audit/reporting
- **Valeur business confirmée** : le connecteur est utile pour l'extraction et l'audit automatisé, pas pour l'exécution

### 📦 Outputs Produced
- **[doc]** `https://app.notion.com/p/38135e218cf88103b70eefe72e1305d3` : Factsheet Meta Marketing MCP — Capability Assessment complet (9 outils, limites write, pricing, lessons learned, accès)

### ⚠️ Open Items & Blockers
- **[INCERTAIN]** Cause réelle de l'absence de données sur les comptes : inactivité vs. problème de token/permissions Meta à vérifier
- La campagne Special Category filtrée automatiquement reste non analysable via ce connecteur — contournement non documenté
- Les capacités write (création/modification campagnes) nécessitent une solution alternative non encore identifiée (API directe ? autre outil ?)
- **[INCERTAIN]** La factsheet est marquée comme documentée avec tests réels — certaines sections pourraient reposer partiellement sur doc officielle si les tests n'ont pas couvert tous les endpoints

### 🔁 Next Steps
1. Vérifier dans Meta Business Manager que les comptes `act_157086230` et `act_498904971225575` ont bien des campagnes actives avec dépenses récentes
2. Contrôler la validité et les permissions du token Meta connecté au MCP
3. Relancer l'audit Meta Ads une fois les données disponibles confirmées
4. Identifier une solution pour les actions write (pause/budget/création) : évaluer API Meta directe ou outil tiers
5. Documenter le cas Special Category dans la factsheet si un contournement est trouvé

### 🔗 Links & References
- 🌐 `https://app.notion.com/p/38135e218cf88103b70eefe72e1305d3` — Factsheet Meta Marketing MCP (Notion TECH)
- 🔗 `session:mseJDqcVvEA3iUZQeQfY5a` — Session courante
- 📄 Références templates : Factsheets Apify + MailerLite (Notion TECH, liens non capturés dans le transcript)

### 🧠 Resume Hint
Le connecteur Meta Marketing MCP est opérationnel mais read-only, les deux comptes publicitaires affichaient 0 dépense lors du test — relancer l'audit Meta Ads dès confirmation que des campagnes actives existent, et consulter la factsheet Notion pour les capacités exactes du connecteur.

### 🏷️ Tags
`meta-ads` `mcp-connector` `factsheet` `audit` `yos-infra` `tool-documentation`

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 16 messages — 2026-06-16

**[2026-06-16 08:44] USER:** Review my Meta Ads performance for the last 30 days. Identify what's working, what's wasting budget, and give me actionable next steps.

**[2026-06-16 08:44] MANUS:** Sur ça. Je lis d'abord les skills meta-ads-analyzer et tool-router avant de plonger dans les données.

**[2026-06-16 08:45] MANUS:** Skill chargé. Je pull maintenant les données Meta Ads — ad accounts, campagnes, ad sets, et métriques sur 30 jours.

**[2026-06-16 08:47] MANUS:** ## Meta Ads — Audit 30 jours : Résultat du diagnostic

### Constat : Aucune donnée de performance disponible

Après interrogation complète des deux comptes connectés via le MCP Meta Marketing, voici ce que j'ai trouvé :

| Compte | ID | Devise | Statut | Dépense totale | Campagnes actives |
|---|---|---|---|---|---|
| 157086230 | `act_157086230` | CHF | ACTIVE | CHF 0.00 | 0 (1 filtrée*) |
| Yannick Jolliet | `act_498904971225575` | EUR | ACTIVE | EUR 0.00 | 0 |

**\*** 1 campagne filtrée automatiquement car classée **Special Category** (logement, emploi, ou services financiers) — politique Meta stricte, non analysable via ce connecteur.

---

### Pourquoi aucune donnée ?

Trois causes possibles, à vérifier dans cet ordre :

**1. Comptes sans activité récente**
`amount_spent: "0.00"` sur l

**[2026-06-16 13:27] USER:** C'est donc un nouvel outil disponible pour iOS. Il faut donc une factsheet et d'un outil avec ses capabilités, ses limites, les lessons learned, les éventuels accès, etc. Comme d'habitude, on fait cette factsheet pour cet outil. Là, on l'a vraiment testé avec tous les accès et tous les API, les entry points, etc. D'autres fois, on n'a pas eu le temps de tester et donc c'est ce que ça donne en général d'après la documentation que tu retrouves online. Mais je veux savoir que pour tel outil, on a telle possibilité et que ça offre. On est capable d'écrire, de lire, de faire, les possibilités techniques d'accès à l'outil et les possibilités en termes de capabilities, de features, donc business-wise. Qu'est-ce que ça m'importe d'avoir cette connexion-là ? Et puis, c'est gratuit, payant, etc. Don

**[2026-06-16 13:27] MANUS:** Compris. Je cherche d'abord la structure de factsheet existante dans Notion/mémoire yOS, puis je documente le connecteur Meta Marketing en profondeur avec la doc officielle. Je reviens avec la factsheet complète.

**[2026-06-16 13:28] MANUS:** Template récupéré (Apify + MailerLite). Je recherche maintenant la doc officielle Meta Marketing API pour valider les capabilities réelles, les limites et le pricing.

**[2026-06-16 13:29] MANUS:** Doc extraite. Je compile maintenant les tests réels + doc officielle pour rédiger la factsheet complète.

**[2026-06-16 13:33] MANUS:** ## Factsheet Meta Marketing MCP générée et poussée

J'ai documenté en profondeur le connecteur Meta Marketing. La factsheet a été créée dans ta section **TECH — Technologie & Infra** (au même niveau que les factsheets Apify et MailerLite).

🔗 **Lien direct Notion :** [🔵 Meta Marketing MCP — Factsheet & Capability Assessment](https://app.notion.com/p/38135e218cf88103b70eefe72e1305d3)

### Synthèse Télégraphique des découvertes

1️⃣ **Capacités (Read-Only) :** 9 outils MCP disponibles. Excellent pour l'extraction de data granulaire (campagnes, adsets, insights, ROAS, metrics) et l'audit de performance.
2️⃣ **Limites critiques (Write) :** Le connecteur actuel **ne permet pas d'écrire**. Impossible de créer une campagne, de changer un budget ou de mettre une pub en pause via MCP. Pour ça, il f
