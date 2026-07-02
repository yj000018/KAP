---
uid: RSzecGh7nhKX7GRQLB24Ks
session_url: https://manus.im/app/RSzecGh7nhKX7GRQLB24Ks
session_title: "MailerLite MCP Connector — Live Test & Y-OS Factsheet Production"
date: 2026-06-16
project: "Y-OS / Wrios"
language: mixed
depth: substantial
length: medium
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 13:01
referenced_sessions: []
referenced_artifacts: ["MailerLite Connector Factsheet (Notion)", "Playbook Connecteurs Y-OS (Notion)"]
referenced_urls: ["https://manus.im/app/RSzecGh7nhKX7GRQLB24Ks"]
input_files: []
message_count: 15
---

# MailerLite MCP Connector — Live Test & Y-OS Factsheet Production

> **Session:** [RSzecGh7nhKX7GRQLB24Ks](https://manus.im/app/RSzecGh7nhKX7GRQLB24Ks) | **Date:** 2026-06-16 | **Project:** Y-OS / Wrios | **Language:** mixed

## 📋 SESSION CARD

### 🧭 Executive Summary
Live testing of the MailerLite MCP connector against a real account (ID 2220658) confirmed full operational status across 68 detected tools. Manus cross-referenced the official MailerLite API documentation to map capabilities, hard limits, and inter-tool dependencies. A structured Y-OS-format Factsheet was produced and pushed to Notion as a reusable reference artifact.

### 🎯 Context & Intent
Yannick wanted to validate the MailerLite connector as a newly available Y-OS tool, understand what it can and cannot do programmatically (vs. UI-only actions), and produce a standardized Factsheet following the Y-OS Playbook Connecteurs template — useful both technically and as a business-value reference for Wrios workflows.

### ✅ What Was Done
1. Read the `yos-optimizer` skill to align with Y-OS operational context
2. Executed parallel live API calls: auth, subscribers, campaigns, groups, segments, automations, forms, webhooks — all against real account
3. Retrieved and validated MailerLite official API documentation online
4. Located existing Y-OS connector factsheet template in Notion (Playbook Connecteurs Y-OS)
5. Mapped 68 MCP tools, their input dependencies, and inter-tool sequencing requirements
6. Identified hard API limits (rate limits, sender domain requirements, batch webhook restrictions)
7. Ran AI-validation tests on email subject (spam flag on "FREE") and body (missing CTA warning)
8. Created and published a complete Y-OS Factsheet in Notion

### 💡 Key Insights
- **68 tools confirmed active** — the MailerLite MCP connector is among the most feature-rich tested to date
- **Inter-tool dependencies matter**: e.g., `list_resources` must be called first to obtain a `group_id` before creating forms or segments — sequencing is non-trivial
- **Key hard limit**: Subscriber import is rate-limited at only **5 req/min** (vs. 120 req/min global) — critical for bulk operations
- **Segment creation via API is complex**: JSON rule format is unwieldy; best practice = create segment name via MCP, configure rules in UI
- **Sender domain verification is mandatory** to send campaigns — MCP cannot bypass this platform-level requirement
- **Webhooks are not batch-compatible** — must be called individually
- **AI content validation is built-in** to the connector, offering spam detection and CTA presence checks
- The session established a repeatable pattern: live test → doc validation → factsheet publication in Y-OS standard format

### 📦 Outputs Produced
- **[doc]** `MailerLite Connector Factsheet (Notion)`: Full Y-OS-format reference card covering capabilities, limits, inter-tool dependencies, lessons learned, rate limits, and business value for Wrios — published to Notion

### ⚠️ Open Items & Blockers
- Factsheet content was cut off mid-sentence in the transcript (business value / "Val..." section) — completeness of the Notion page is **[INCERTAIN]**
- No Notion URL for the created page was confirmed in the visible transcript — exact page location **[INCERTAIN]**
- Wrios-specific business use cases mentioned but not fully elaborated in the session
- Only 1 active subscriber in the test account — real-scale behavior (bulk imports, large segment queries) not validated

### 🔁 Next Steps
1. Verify and retrieve the Notion URL of the published MailerLite Factsheet to archive in Y-OS links registry
2. Complete the business value section of the Factsheet (Wrios use cases: list management, campaign automation, lead nurturing flows)
3. Design the first real automation using the connector (e.g., Welcome sequence triggered by Wrios signup)
4. Test subscriber import at scale to validate the 5 req/min rate limit behavior in practice
5. Document the `list_resources → group_id` dependency chain as a reusable snippet in the Y-OS Playbook
6. Replicate this test+factsheet pattern for any new connector onboarded into Y-OS

### 🔗 Links & References
- 🌐 `https://manus.im/app/RSzecGh7nhKX7GRQLB24Ks` — Session URL
- 📁 Notion: Playbook Connecteurs Y-OS (template source — exact path not confirmed)
- 📁 Notion: MailerLite Connector Factsheet (created this session — URL not captured)
- 🌐 MailerLite Official API Documentation (consulted live — exact URL not captured in transcript)

### 🧠 Resume Hint
The MailerLite Factsheet has been created in Notion following Y-OS Playbook Connecteurs format — next agent should retrieve its URL, verify the business value section is complete, and begin designing the first Wrios-integrated automation using the connector.

### 🏷️ Tags
`mailerlite` `connector-factsheet` `y-os-tooling` `mcp-testing` `wrios` `email-automation`

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 15 messages — 2026-06-16

**[2026-06-16 11:24] USER:** Help me test the MailerLite connector and show me how to use its feature (e.g. show any data you fetched with it). Give me a brief about its capabilities.

**[2026-06-16 11:24] MANUS:** Sur ça — je lis d'abord le skill yos-optimizer, puis j'explore le connecteur MailerLite en live.

**[2026-06-16 11:25] MANUS:** 68 outils détectés. Je lance maintenant les appels live en parallèle — auth, subscribers, campaigns, groups, segments, automations, forms, webhooks.

**[2026-06-16 11:26] MANUS:** Le connecteur MailerLite est pleinement opérationnel (68 outils détectés). 

J'ai exécuté les tests en parallèle sur ton compte :
* **Auth** : OK (ID 2220658, yannick.jolliet@gmail.com)
* **Abonnés** : 1 abonné actif détecté (toi).
* **Automations** : Découverte des templates "Welcome" (Simple, Advanced, Premium).
* **Validation IA** : Test des objets (alerte spam sur le mot "FREE") et du corps d'email (alerte sur l'absence de Call-to-Action).

Le brief détaillé avec les données réelles est en pièce jointe. Que veux-tu automatiser en premier ?

**[2026-06-16 13:18] USER:** N'hésite pas à augmenter, euh, la, la facti-- euh, de l'outil, à apporter des nouvelles métadonnées, euh, en particulier pour connecter les outils entre eux ou les interdépendances. Hum, n'hésite pas à aller voir la documentation en ligne pour, euh, valider si-- c'qu'on peut faire, c'qu'on ne peut pas faire, surtout highlighter les, les limites de, de l'outil, parce que des fois, en front-end, on peut faire plein de choses et pareil, via, on peut pas créer des documents, c'est juste pour lire les documents existants, etc. Et puis, évidemment, il me faut une synthèse pour que je puisse lire ça très rapidement. Cet outil permet de, d'un accès à, on peut créer, lire, faire ceci, ça. Euh, et puis, euh, et c'est très utile et d'un point de vue business, euh, pour ceci dans, dans Wrios, hein.

**[2026-06-16 13:18] MANUS:** Compris. Je vais chercher la doc officielle MailerLite API + MCP, cartographier les limites réelles (create vs read-only), les interdépendances entre outils, et produire une fiche de référence dense avec valeur business Y-OS.

**[2026-06-16 13:18] USER:** Ok, ça c'est un petit test et d'un connecteur. C'est donc un nouvel outil disponible pour iOS. Il faut donc une factsheet et d'un outil avec ses capabilités, ses limites, les lessons learned, les éventuels accès, etc. Comme d'habitude, on fait cette factsheet pour cet outil. Là, on l'a vraiment testé avec tous les accès et tous les API, les entry points, etc. D'autres fois, on n'a pas eu le temps de tester et donc c'est ce que ça donne en général d'après la documentation que tu retrouves online. Mais je veux savoir que pour tel outil, on a telle possibilité et que ça offre. On est capable d'écrire, de lire, de faire, les possibilités techniques d'accès à l'outil et les possibilités en termes de capabilities, de features, donc business-wise. Qu'est-ce que ça m'importe d'avoir cette connexio

**[2026-06-16 13:19] MANUS:** Parfait. Avant de créer quoi que ce soit, je vais d'abord retrouver la structure de factsheet existante dans Notion/Mem0 pour repartir du bon template. Je cherche.

**[2026-06-16 13:19] MANUS:** Je vois des pages de test de connecteurs existantes. Je vais en lire une pour récupérer la structure exacte utilisée, puis chercher s'il existe un template/factsheet standard.

**[2026-06-16 13:21] MANUS:** J'ai le Playbook Connecteurs Y-OS. Je vois la structure existante. Maintenant je vais chercher la doc MailerLite API en ligne pour les limites précises, puis rédiger la factsheet dans le format Y-OS et la pousser dans Notion.

**[2026-06-16 13:23] MANUS:** La Factsheet a été créée et structurée dans Notion avec succès ! 

**Ce qu'elle contient (et qui a été validé) :**
* **Capabilités & Interdépendances :** 68 outils cartographiés (ex: besoin de faire un `list_resources` pour obtenir un `group_id` avant de pouvoir créer un formulaire ou un segment).
* **Limites & Contraintes (issues de la doc officielle) :** 
    * Rate limits stricts (120 req/min global, mais seulement **5 req/min** pour l'import d'abonnés).
    * Obligation d'avoir un domaine expéditeur vérifié pour envoyer une campagne (le MCP ne peut pas bypasser ça).
    * Les webhooks ne sont pas supportés dans les requêtes "batch".
    * La création de segments par API demande un format JSON très complexe (il vaut mieux créer le nom via MCP et configurer les règles dans l'UI).
* **Val
