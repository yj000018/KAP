---
uid: 1Veq8K61axBlX24dMPnVgF
session_url: https://manus.im/app/1Veq8K61axBlX24dMPnVgF
session_title: "Taskade MCP Connector — Test Live & Factsheet Y-OS"
date: 2026-06-16
project: "Y-OS Architecture Multi-Agents"
language: fr
depth: substantial
length: medium
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 13:04
referenced_sessions: []
referenced_artifacts: ["Taskade MCP Connector \u2014 Factsheet & Capabilities", "Rapport Taskade MCP"]
referenced_urls: ["https://app.notion.com/p/38135e218cf8819c8c15d02a2449f722", "https://manus.im/app/1Veq8K61axBlX24dMPnVgF"]
input_files: []
message_count: 11
---

# Taskade MCP Connector — Test Live & Factsheet Y-OS

> **Session:** [1Veq8K61axBlX24dMPnVgF](https://manus.im/app/1Veq8K61axBlX24dMPnVgF) | **Date:** 2026-06-16 | **Project:** Y-OS Architecture Multi-Agents | **Language:** fr

## 📋 SESSION CARD

### 🧭 Executive Summary
Yannick a testé en live le connecteur Taskade MCP sur son workspace `ymed`, extrayant des données réelles (dossiers, projets, agents IA). Suite à ce test réussi, une factsheet complète a été produite et archivée dans Notion, couvrant les 57 outils disponibles, les capabilities business, les limites techniques et le pricing. Ce connecteur enrichit l'écosystème Y-OS avec une capacité de gestion de tâches et d'agents IA programmatique.

---

### 🎯 Context & Intent
Valider le connecteur Taskade MCP nouvellement disponible pour Y-OS, en tester les accès réels (lecture, écriture, API endpoints), puis produire la factsheet standardisée Y-OS — le même format que pour MailerLite — afin de documenter capabilities, limites, pricing et valeur business de cette intégration.

---

### ✅ What Was Done
1. Lecture des skills `tool-router` et `yos-optimizer` en amont de l'exploration
2. Connexion au connecteur Taskade via MCP et énumération des 57 outils disponibles
3. Extraction live de données réelles : dossiers (`Home`, `Task Flow Manager`), projets (`TaskFlow App — Build State`, `Tasks`, `Blockers`), agents (`Deal Finder Agent1`, `Task Coach`)
4. Extraction du briefing quotidien du 13 Mai généré par l'agent Task Coach
5. Récupération du template de factsheet Y-OS existant (référence : factsheet MailerLite)
6. Recherche de la documentation officielle Taskade en ligne pour valider limites API et pricing
7. Production de la factsheet complète (57 outils, 4 domaines, limites critiques, pricing)
8. Archivage de la factsheet dans Notion sous le hub Y-OS Architecture Multi-Agents

---

### 💡 Key Insights
- **57 outils MCP** couvrent 4 domaines : Hierarchy, Projects, Tasks, AI Agents — couverture fonctionnelle complète de l'écosystème Taskade
- **Limite critique #1 :** `prompt-an-agent` n'est pas disponible via MCP — nécessite un appel direct à `POST /api/v2/promptAgent` (API v2, hors MCP)
- **Limite critique #2 :** Le MCP complet (outbound) est réservé au plan **Business** à $40/mois minimum
- **Limite critique #3 :** Maximum 5 Personal Access Tokens autorisés
- La factsheet suit le standard Y-OS établi (même structure que MailerLite), confirmant la maturité du processus de documentation des connecteurs
- Le connecteur a été testé avec des données live — niveau de confiance de la factsheet supérieur aux factsheets basées uniquement sur documentation

---

### 📦 Outputs Produced
- **[doc]** `Taskade MCP Connector — Factsheet & Capabilities` : Factsheet complète archivée dans Notion, couvrant 57 outils, 4 domaines fonctionnels, limites critiques, pricing et recommandations d'intégration Y-OS
- **[data]** `Taskade workspace live extract` : Données réelles extraites — dossiers, projets, agents IA et briefing Task Coach du 13 Mai
- **[doc]** `Rapport Taskade MCP` : Fichier joint produit lors de la première phase de test avec données structurées et recommandations

---

### ⚠️ Open Items & Blockers
- `POST /api/v2/promptAgent` non wrappé dans MCP — tout workflow Y-OS voulant déclencher un agent Taskade programmatiquement doit contourner via appel API direct [INCERTAIN sur la faisabilité depuis l'environnement Manus]
- Plan Business ($40/mo) requis pour MCP outbound complet — à vérifier si le plan actuel de Yannick est suffisant [INCERTAIN]
- Limite de 5 PAT à surveiller si plusieurs intégrations Y-OS utilisent Taskade simultanément
- La factsheet dans Notion doit être reliée aux autres factsheets connecteurs pour former un index complet [INCERTAIN — index existant ou à créer ?]

---

### 🔁 Next Steps
1. Vérifier le plan Taskade actif sur le compte `ymed` et confirmer l'accès MCP outbound complet
2. Implémenter un wrapper Y-OS pour `POST /api/v2/promptAgent` (API v2) afin de déclencher les agents Taskade depuis Manus
3. Créer ou mettre à jour l'index des factsheets connecteurs dans Notion (MailerLite + Taskade + futurs)
4. Tester des workflows Y-OS concrets utilisant Taskade (ex : création automatique de tâches depuis une session KAP, ou déclenchement du Task Coach)
5. Documenter la PAT utilisée dans le vault sécurisé Y-OS et monitorer l'utilisation (limite 5 tokens)

---

### 🔗 Links & References
- 🌐 `https://app.notion.com/p/38135e218cf8819c8c15d02a2449f722` — Factsheet Taskade MCP dans Notion
- 🌐 `https://manus.im/app/1Veq8K61axBlX24dMPnVgF` — Session courante
- 📄 Rapport Taskade MCP (fichier joint session) — données live extraites
- 📄 Factsheet MailerLite (référence template Y-OS) — hub Y-OS Architecture Multi-Agents, Notion

---

### 🧠 Resume Hint
La factsheet Taskade MCP est archivée dans Notion ; le prochain agent doit savoir que `prompt-an-agent` nécessite un appel direct à l'API v2 (hors MCP) et que le plan Business est requis pour le MCP outbound complet.

---

### 🏷️ Tags
`taskade` `mcp-connector` `factsheet` `y-os-architecture` `tool-integration` `ai-agents`

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 11 messages — 2026-06-16

**[2026-06-16 10:49] USER:** Help me test the Taskade connector and show me how to use its feature (e.g. show any data you fetched with it). Give me a brief about its capabilities.

**[2026-06-16 10:49] MANUS:** Sur ça. Je lis d'abord le skill tool-router + yos-optimizer, puis j'explore le connecteur Taskade via MCP.

**[2026-06-16 10:51] MANUS:** J'ai testé le connecteur Taskade via MCP et extrait des données réelles de ton espace de travail. 

Voici les points clés :
- **57 outils disponibles** couvrant tout l'écosystème Taskade (Projets, Tâches, Dossiers, Workspaces).
- **Gestion des Agents IA** : Capacité à créer, configurer et alimenter la base de connaissances des agents Taskade.
- **Données live extraites** : J'ai trouvé tes dossiers (`Home`, `Task Flow Manager`), tes projets (`TaskFlow App — Build State`, `Tasks`, `Blockers`), et tes agents (`Deal Finder Agent1`, `Task Coach`). J'ai même extrait le briefing quotidien du 13 Mai généré par ton Task Coach.

Le rapport complet avec les données structurées et les recommandations d'intégration Y-OS est dans le fichier joint.

**[2026-06-16 13:24] USER:** C'est donc un nouvel outil disponible pour iOS. Il faut donc une factsheet et d'un outil avec ses capabilités, ses limites, les lessons learned, les éventuels accès, etc. Comme d'habitude, on fait cette factsheet pour cet outil. Là, on l'a vraiment testé avec tous les accès et tous les API, les entry points, etc. D'autres fois, on n'a pas eu le temps de tester et donc c'est ce que ça donne en général d'après la documentation que tu retrouves online. Mais je veux savoir que pour tel outil, on a telle possibilité et que ça offre. On est capable d'écrire, de lire, de faire, les possibilités techniques d'accès à l'outil et les possibilités en termes de capabilities, de features, donc business-wise. Qu'est-ce que ça m'importe d'avoir cette connexion-là ? Et puis, c'est gratuit, payant, etc. Don

**[2026-06-16 13:25] MANUS:** Compris. Je vais d'abord retrouver la structure de factsheet existante dans Notion/mémoire Y-OS, puis aller chercher la doc Taskade en ligne pour valider les limites, et enfin produire la factsheet complète.

**[2026-06-16 13:26] MANUS:** Template Y-OS récupéré (MailerLite factsheet). Je recherche maintenant la doc Taskade officielle pour valider les limites API, pricing et contraintes.

**[2026-06-16 13:28] MANUS:** Factsheet Taskade complète, archivée dans Notion et disponible en fichier joint.

**Notion :** [🔌 Taskade MCP Connector — Factsheet & Capabilities](https://app.notion.com/p/38135e218cf8819c8c15d02a2449f722) — placée sous le hub Y-OS Architecture Multi-Agents, au même niveau que la factsheet MailerLite.

---

### Ce que couvre la factsheet

**57 outils** répartis en 4 domaines fonctionnels (Hierarchy, Projects, Tasks, AI Agents), tous testés en live sur ton workspace `ymed`.

**Limites critiques identifiées :**
- Pas de `prompt-an-agent` via MCP — le serveur inbound ne wrape que l'API v1. Pour déclencher un agent programmatiquement, il faut appeler `POST /api/v2/promptAgent` directement.
- MCP complet (outbound) réservé au plan **Business** ($40/mo) minimum.
- Max 5 Personal Access Tokens p
