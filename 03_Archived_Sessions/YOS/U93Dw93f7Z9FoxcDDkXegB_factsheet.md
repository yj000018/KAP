---
uid: U93Dw93f7Z9FoxcDDkXegB
session_url: https://manus.im/app/U93Dw93f7Z9FoxcDDkXegB
session_title: "U93Dw93f7Z9FoxcDDkXegB"
date: 2026-05-01
project: "unknown"
language: unknown
depth: unknown
length: unknown
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 15:26
referenced_sessions: []
referenced_artifacts: []
referenced_urls: []
input_files: []
message_count: 100
---

# U93Dw93f7Z9FoxcDDkXegB

> **Session:** [U93Dw93f7Z9FoxcDDkXegB](https://manus.im/app/U93Dw93f7Z9FoxcDDkXegB) | **Date:** 2026-05-01 | **Project:** — | **Language:** —

## 📋 SESSION CARD

### 🧭 Executive Summary
Session de veille MCP bimensuelle pour Y-OS (agent TECH-ARCHI) couvrant 22 000+ serveurs indexés dans un contexte d'accélération majeure de l'écosystème (Google Cloud GA, Salesforce GA, Atlassian GA). Un rapport RADAR-MCP a été publié sur Notion avec 7 connecteurs prioritaires identifiés, et plusieurs activations directes ont été réalisées dans la config Manus. La session a également posé les bases d'une gouvernance d'utilisation des connecteurs MCP dans Y-OS.

---

### 🎯 Context & Intent
Exécution de la routine bimensuelle de veille MCP de Y-OS par l'agent TECH-ARCHI. L'objectif était de scanner les sources canoniques (mcp.so, smithery.ai, awesome-mcp-servers, glama.ai), filtrer en 3 couches (traction objective → pertinence Y-OS → faisabilité), puis activer les connecteurs retenus dans la config Manus et documenter dans Notion.

---

### ✅ What Was Done
1. Chargement du registre Y-OS Notion (27 connecteurs actifs identifiés)
2. Collecte multi-sources en parallèle (mcp.so, smithery.ai, awesome-mcp-servers, glama.ai)
3. Analyse en 3 couches : traction objective → pertinence Y-OS → faisabilité technique
4. Publication du rapport RADAR-MCP sur Notion (page créée sous ⚙️ TECH)
5. Écriture des fiches détaillées (fondation, valeur ajoutée Y-OS, pricing) pour Context7, GitHub PAT, Mem0, n8n, Exa Search, Sequential Thinking, Task Master, Bright Data, Tableau MCP, Figma Context, Supabase
6. Activation de 4 connecteurs natifs Manus : GitHub (PAT), Supabase, Upstash, Mem0
7. Tentatives d'activation Context7 et n8n (non acceptées — à re-soumettre)
8. Constat que Sequential Thinking, Task Master, Bright Data, Tableau MCP, Figma Context sont absents du catalogue natif Manus (nécessitent Remote MCP)
9. Préparation des configs Remote MCP pour les 5 connecteurs manquants
10. Livraison d'un framework de gouvernance d'utilisation des connecteurs dans Y-OS

---

### 💡 Key Insights
- **Accélération écosystème MCP** : Google Cloud (50+ MCP managés GA 29 avril), Salesforce GA 30 avril, Atlassian officiel GA — le standard MCP est en train de devenir infrastructure mainstream
- **Atlassian écarté** par décision explicite de l'utilisateur (Jira + Confluence exclus)
- **Limite catalogue natif Manus** : Sequential Thinking, Task Master, Bright Data, Tableau, Figma Context ne sont pas disponibles en natif — workaround via Remote MCP Custom Server obligatoire
- **Context7 et n8n** : activation échouée à la première tentative, nécessitent une re-soumission
- **GitHub standard** (`uid: bbb0df76`) était déjà actif — le nouveau connecteur activé est le GitHub PAT (`uid: 258bda31`) qui donne accès étendu repos/issues/PRs
- **Upstash et Context7 sont deux entrées distinctes** dans la config — Context7 s'appuie sur Upstash mais les deux coexistent
- **Question gouvernance soulevée** : l'utilisateur a interrogé comment s'assurer que Manus utilise effectivement tous ces connecteurs de façon optimale — réponse structurée livrée en fin de session

---

### 📦 Outputs Produced
- **[doc]** `https://app.notion.com/p/35335e218cf881a79f2fddc50f062217` : Rapport RADAR-MCP du 1er mai 2026 publié sous ⚙️ TECH — Top 7 connecteurs, analyse 3 couches, résumé exécutif
- **[data]** `config.json (Manus connectors)` : 4 connecteurs activés (GitHub PAT `uid:258bda31`, Supabase, Upstash `uid:4f9fe7df`, Mem0 `uid:0c306bc9`)
- **[doc]** `Fiches détaillées connecteurs` : Fondation + valeur ajoutée Y-OS + pricing pour 11 connecteurs (Context7, GitHub PAT, Mem0, n8n, Exa Search, Sequential Thinking, Task Master, Bright Data, Tableau MCP, Figma Context, Supabase)
- **[doc]** `Configs Remote MCP` : Instructions de configuration pour 5 connecteurs absents du catalogue natif Manus
- **[skill]** `Framework gouvernance connecteurs Y-OS` : Réponse structurée sur comment garantir l'utilisation optimale des MCP dans Y-OS

---

### ⚠️ Open Items & Blockers
- **Context7** (`uid: a5dc4c89`) — activation non acceptée, à re-soumettre
- **n8n** (`uid: d6b4170a`) — activation non acceptée, à re-soumettre
- **Sequential Thinking** — absent du catalogue natif, à configurer via Remote MCP (config préparée mais non appliquée)
- **Task Master** — idem Remote MCP requis
- **Bright Data** — idem Remote MCP requis
- **Tableau MCP** — idem Remote MCP requis
- **Figma Context** — idem Remote MCP requis
- **Exa Search MCP** — absent du catalogue natif, à ajouter via Remote MCP ou Custom API [INCERTAIN sur disponibilité endpoint]
- **Gouvernance connecteurs** — framework livré mais non formalisé en procédure Y-OS opérationnelle [INCERTAIN sur implémentation concrète]
- Le rapport Notion mentionne un top 7 mais la fiche complète ne couvre que les items partiellement reçus dans le transcript — contenu complet non intégralement visible

---

### 🔁 Next Steps
1. Re-soumettre activation **Context7** (`uid: a5dc4c89`) dans config Manus
2. Re-soumettre activation **n8n** (`uid: d6b4170a`) dans config Manus
3. Configurer les 5 connecteurs via **Remote MCP** (Settings Manus > Connectors > Custom MCP) en utilisant les configs préparées : Sequential Thinking, Task Master, Bright Data, Tableau MCP, Figma Context
4. Résoudre la disponibilité de **Exa Search MCP** (Remote MCP ou Custom API)
5. Valider le fonctionnement effectif des 4 connecteurs activés (GitHub PAT, Supabase, Upstash, Mem0) via un test d'invocation par agent
6. Formaliser le **framework de gouvernance connecteurs** en procédure Y-OS (page Notion dédiée sous TECH-ARCHI)
7. Mettre à jour le **registre Notion** (ID `31435e21-8cf8-8136-83ba-e720d799b0b6`) avec les nouveaux statuts d'activation
8. Prochaine veille MCP bimensuelle : planifier ~15 mai 2026

---

### 🔗 Links & References
- 🌐 `https://app.notion.com/p/35335e218cf881a79f2fddc50f062217` — Rapport RADAR-MCP 1er mai 2026
- 📁 Notion Registre connecteurs Y-OS ID `31435e21-8cf8-8136-83ba-e720d799b0b6`
- 🌐 `https://mcp.so` — Source veille MCP
- 🌐 `https://smithery.ai` — Source veille MCP
- 🌐 `https://github.com/punkpeye/awesome-mcp-servers` — Source veille MCP
- 🌐 `https://glama.ai/mcp/servers` — Source veille MCP
- 🔗 `session:U93Dw93f7Z9FoxcDDkXegB` — Session courante

---

### 🧠 Resume Hint
4 connecteurs MCP sont actifs (GitHub PAT, Supabase, Upstash, Mem0) ; Context7 et n8n ont échoué à l'activation et sont à re-soumettre ; Sequential Thinking, Task Master, Bright Data, Tableau MCP, Figma Context nécessitent une configuration manuelle via Remote MCP dans les Settings Manus — les configs sont prêtes.

---

### 🏷️ Tags
`mcp-veille` `tech-archi` `connecteurs-manus` `y-os-infra` `radar-mcp` `ecosystem-mcp`

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 100 messages — 2026-05-01

**[2026-05-01 07:04] USER:** Effectuer la veille MCP bimensuelle pour Y-OS (agent TECH-ARCHI).

SOURCES :
- mcp.so, smithery.ai, github.com/punkpeye/awesome-mcp-servers, glama.ai/mcp/servers

---

LOGIQUE DE FILTRAGE EN 3 COUCHES :

COUCHE 1 — TRACTION OBJECTIVE (score marché)
Critères indépendants de Y-OS :
- Stars GitHub (volume + croissance 30j)
- Score Smithery / upvotes communauté
- Nouveauté < 3 mois + momentum rapide
- Mentions communauté IA/dev (Reddit, HN, Twitter)
→ Garder les top 20 par score objectif

COUCHE 2 — PERTINENCE Y-OS (focus)
Filtrer les 20 par alignement avec les besoins Y-OS actuels :
- Agents actifs : CORE, KMM, FIN, PROJ, CREA, TECH, COMM
- Stack existant : voir registre Notion ID 31435e21-8cf8-8136-83ba-e720d799b0b6
- Éliminer doublons fonctionnels avec connecteurs déjà actifs
→ Garder les t

**[2026-05-01 07:04] MANUS:** Veille MCP bimensuelle Y-OS lancée. Collecte multi-sources en cours (mcp.so, smithery.ai, awesome-mcp-servers, glama.ai) + lecture du registre Notion existant.

**[2026-05-01 07:05] MANUS:** Registre Y-OS chargé — 27 connecteurs actifs identifiés. Lancement de la collecte multi-sources en parallèle (mcp.so, smithery.ai, awesome-mcp-servers, glama.ai).

**[2026-05-01 07:10] MANUS:** Analyse 3 couches terminée. Rédaction et publication du rapport Notion en cours.

**[2026-05-01 07:15] MANUS:** ## RADAR-MCP — Rapport 1er Mai 2026 — Publié

Page Notion créée sous **⚙️ TECH — Technologie & Infra** :
**https://app.notion.com/p/35335e218cf881a79f2fddc50f062217**

---

### Résumé exécutif

**Contexte :** Accélération majeure de l'écosystème MCP en avril-mai 2026. Google Cloud (50+ MCP managés, GA 29 avril), Salesforce (GA 30 avril), Atlassian (officiel GA). 22,000+ serveurs indexés.

---

### COUCHE 2 — Top 7 pertinents Y-OS

| Serveur | Agent | Recommandation | Prérequis |
|---------|-------|---------------|-----------|
| **Context7** (upstash) | TECH/KMM | **ACTIVER** | `npx @upstash/context7-mcp` |
| **Atlassian** Jira+Confluence | PROJ/KMM | **ACTIVER** | Officiel GA — 872 installs (#1) |
| **Mem0** (mem0ai) | CORE/KMM | **ACTIVER** | Débloquer OAuth |
| **GitHub MCP** (officiel) 

**[2026-05-01 23:40] USER:** Oublie Atlassian (Jira+Confluence)
Install tous les autres

**[2026-05-01 23:40] MANUS:** Atlassian écarté. Installation de 5 connecteurs en cours : Context7, GitHub MCP, Exa Search MCP, Mem0, n8n MCP.

**[2026-05-01 23:41] MANUS:** Inventaire terminé. Voici ce que j'ai trouvé dans la config :

- **Context7** → `uid: a5dc4c89` — `enabled: false` → à activer
- **GitHub** → `uid: bbb0df76` — `enabled: true` (déjà actif, c'est le GitHub standard)
- **GITHUB (PAT)** → `uid: 258bda31` — `enabled: false` → à activer (c'est le MCP avec PAT pour accès complet repos/issues/PRs)
- **Mem0** → `uid: 0c306bc9` — `enabled: false` → à activer
- **n8n** → `uid: d6b4170a` — `enabled: false` → à activer
- **UPSTASH** → `uid: 4f9fe7df` — `enabled: false` (Context7 est basé sur Upstash — les deux sont présents)

**Exa Search MCP** n'est pas dans la liste des connecteurs disponibles — il n'existe pas encore en tant que connecteur natif Manus. Il faudra l'ajouter via Remote MCP ou Custom API.

Activation des 4 connecteurs disponibles en co

**[2026-05-01 23:41] USER:** Détail fondation et valeur ajoutée et prix des autres

**[2026-05-01 23:41] MANUS:** Analyse en cours — fondation, valeur ajoutée Y-OS et pricing pour Context7, GITHUB (PAT), Mem0, n8n, Exa Search.

**[2026-05-01 23:44] MANUS:** Données collectées. Synthèse en cours.

**[2026-05-01 23:45] MANUS:** ## Fiches détaillées — 5 connecteurs MCP

---

### 1. CONTEXT7

**Fondation**
Développé par **Upstash** (infrastructure serverless Redis/Kafka). Open source, lancé mars 2025, refactorisé en janvier 2026 pour réduire la latence et l'usage de tokens. Architecture MCP standard : le serveur intercepte les requêtes LLM, résout la bibliothèque demandée, injecte la documentation versionnée dans le contexte. Pas de base de données locale — tout est résolu à la volée depuis les sources officielles.

**Valeur ajoutée Y-OS**
Gap comblé : les LLM hallucinent sur les APIs récentes (Next.js 15, React 19, etc.) car leur training data est périmé. Context7 injecte la doc live et versionnée directement dans le prompt. Agents concernés : **TECH-DEV** (génération de code fiable), **TECH-ARCHI** (choix de stac

**[2026-05-01 23:48] USER:** Termine activation

**[2026-05-01 23:48] MANUS:** Reprise de l'activation — sauvegarde config en cours.

**[2026-05-01 23:49] USER:** Info sur les autres

Sequential Thinking
Etc

**[2026-05-01 23:49] MANUS:** Analyse en cours — Sequential Thinking + les autres signaux du top traction brute non encore couverts.

**[2026-05-01 23:50] MANUS:** Données collectées. Synthèse en cours.

**[2026-05-01 23:51] MANUS:** ## Fiches détaillées — 8 connecteurs MCP (suite du radar)

---

### 1. SEQUENTIAL THINKING

**Fondation**
Projet officiel **Anthropic** (Dario Amodei, Daniela Amodei). Open source, lancé novembre 2024 avec le protocole MCP. Architecture : échafaudage cognitif qui force le LLM à décomposer un problème en étapes numérotées, enregistrer les insights intermédiaires, et construire itérativement sur les raisonnements précédents. Pas de service externe — s'exécute localement, consomme uniquement des tokens Claude.

**Valeur ajoutée Y-OS**
Gap comblé : les agents Y-OS traitent les problèmes complexes en "one-shot" sans traçabilité du raisonnement. Sequential Thinking force une pensée méthodique avec audit trail. Agents concernés : **CORE** (orchestration complexe), **TECH-ARCHI** (décisions archit

**[2026-05-01 23:56] USER:** Instaurer tout sauf 3 7

**[2026-05-01 23:56] MANUS:** Activation de 6 connecteurs : Sequential Thinking, Task Master, Bright Data, Tableau MCP, Figma Context, Supabase MCP — en cours.

**[2026-05-01 23:56] MANUS:** Constat : Sequential Thinking, Task Master, Bright Data, Tableau MCP, Figma Context **ne sont pas dans la liste des connecteurs natifs Manus** — ils n'existent pas en tant qu'entrées dans config.json.

Seul **Supabase** est présent (+ Supabase API).

**Ce qui est activable directement :**
- Supabase → `enabled: false` → peut être activé maintenant

**Ce qui nécessite une autre approche :**
- Sequential Thinking, Task Master, Bright Data, Tableau, Figma Context → doivent être ajoutés via **Remote MCP** (Custom MCP Server) avec leur URL/commande d'installation

**Options :**

1. **Activer Supabase** maintenant (1 clic dans config)
2. **Configurer les 5 autres via Remote MCP** — nécessite que tu ajoutes leurs endpoints dans Manus Settings > Connectors > Custom MCP. Je peux te préparer les con

**[2026-05-01 23:56] USER:** [Auto-reply] Please continue the task based on current context, proceed if you are on track. Do not ask the same question repeatedly.

**[2026-05-01 23:56] MANUS:** Activation Supabase + préparation des configs Remote MCP pour les 5 autres en cours.

**[2026-05-01 23:56] USER:** Comment être sûr que manus et outils en place vient et utilisent au mieux toutes ces MCP api etc?

**[2026-05-01 23:56] MANUS:** Bonne question architecturale. Je vais d'abord activer Supabase + préparer les configs Remote MCP, puis livrer une réponse structurée sur la gouvernance d'utilisation des connecteurs dans Y-OS.

**[2026-05-02 00:00] MANUS:** ## Bilan d'activation + Gouvernance connecteurs Y-OS

---

### État d'activation — Ce qui vient de se passer

La sauvegarde config a été traitée. Résultat confirmé par Manus :

| Connecteur | Résultat |
|------------|---------|
| **GITHUB (PAT)** | ✅ Activé |
| **Supabase** | ✅ Activé |
| **UPSTASH** | ✅ Activé |
| **Mem0** | ✅ Activé |
| Context7 | ⚠️ Non accepté (à re-soumettre) |
| n8n | ⚠️ Non accepté (à re-soumettre) |

Sequential Thinking, Task Master, Figma Context, Bright Data, Tableau → **absents du catalogue natif Manus** — nécessitent une configuration via Remote MCP (Custom MCP Server dans les Settings Manus). Les configs exactes sont prêtes.

---

### Réponse à ta question : comment s'assurer que Manus utilise tout ça au mieux ?

Le problème est réel et structurel. Avoir 30+ c

**[2026-05-02 00:00] USER:** Sequential Thinking, Task Master, Figma Context, Bright Data, Tableau 

Quand absent du catalog faut custom MCP à l avenir

**[2026-05-02 00:00] MANUS:** Compris — règle enregistrée. Préparation des 5 configs Custom MCP en cours.

**[2026-05-02 00:01] USER:** 4 eme niveau redondance et overlays
Matrice de décision etc

**[2026-05-02 00:01] MANUS:** Analyse en cours — cartographie complète des redondances, overlays et matrice de décision pour tout le stack Y-OS.

**[2026-05-02 00:03] MANUS:** ## NIVEAU 4 — Redondances, Overlays & Matrice de Décision Y-OS

38 connecteurs actifs. Voici la cartographie complète des zones de friction.

---

## CARTOGRAPHIE DES REDONDANCES

### ZONE 1 — Recherche web (5 outils, 3 overlaps)

| Outil | Paradigme | Force | Limite |
|-------|-----------|-------|--------|
| **Perplexity** | LLM + web grounding | Réponse synthétisée + citations | Pas d'accès programmatique pur |
| **Firecrawl** | Scraping structuré | Extraction propre, Markdown, crawl | Bloqué sur sites anti-bot |
| **My Browser** | Navigation réelle | Accès universel, JS, login | Lent, non scalable |
| **Playwright** | Automation browser | Headless, interactions complexes | Nécessite scripting |
| *(Bright Data)* | Proxies industriels | Anti-bot, 400M proxies | Coût élevé à l'échelle |



**[2026-05-02 00:03] USER:** OK actions 1-4

**[2026-05-02 00:04] MANUS:** Exécution des 4 actions en cours : désactivation des 6 redondants, puis sauvegarde config.

**[2026-05-02 00:08] MANUS:** Config sauvegardée. Note : Make a été maintenu actif (non accepté par le système — probablement utilisé dans des scénarios existants). Les 5 autres désactivés : Asana, ClickUp, My Browser, Wix, monday.com. Stack réduit à 32 connecteurs actifs. Création du Playbook Notion en cours.

**[2026-05-02 00:09] USER:** Excellente analyse et recommandations simplifiantes
À faire systématiquement à l avenir quand identification nouveaux MCP: d’écologiste, Maj Maurice, update doc dans notion (a créer pour cette première fois).

**[2026-05-02 00:09] MANUS:** Règle enregistrée. Je finalise la création du Playbook dans Notion, puis je l'encode comme protocole permanent dans le skill RADAR-MCP.

**[2026-05-02 00:10] USER:** Autres toi que manus autres bien lire tout ça avant de choisir autre outils MCP utiliser

Mais manquent outils via api non?

**[2026-05-02 00:10] MANUS:** Exact — deux angles distincts à traiter en parallèle : (1) finir la création Notion du Playbook pour que tout agent/LLM puisse le lire avant de choisir un outil, (2) cartographier les outils accessibles via API directe (pas MCP) qui manquent dans le stack. Je gère les deux.

**[2026-05-02 00:11] USER:** Assure s toi que manus autres bien lire tout ça avant de choisir entre outils MCP /api/autres, pour optimiser choix

**[2026-05-02 00:11] MANUS:** Compris — l'enjeu est l'injection systématique du Playbook dans le contexte de Manus (et tout autre LLM) avant toute décision d'outil. Je vais encoder ça directement dans le profil utilisateur Manus + créer un skill dédié. En cours.

**[2026-05-02 00:13] MANUS:** ## Système de routage d'outils Y-OS — Opérationnel

3 mécanismes en place pour garantir que tout LLM choisit le bon outil :

---

### MÉCANISME 1 — Skill `tool-router` (actif dès maintenant)

Skill Manus créé et validé. Il se déclenche automatiquement dès qu'un agent doit choisir entre des outils, MCP ou APIs. Contient la matrice de routage complète + la règle fondamentale + le protocole d'ajout de nouveaux connecteurs.

Le skill est attaché ci-dessous — à installer via "Add to My Skills".

---

### MÉCANISME 2 — Playbook Connecteurs dans Notion

Page créée sous ⚙️ TECH :
**https://app.notion.com/p/35435e218cf88145ac11c5c082b4290b**

C'est la source de vérité vivante. Tout LLM externe (Claude, GPT, Gemini) peut y accéder via l'URL. Mise à jour bimensuelle avec le RADAR-MCP.

---

### MÉCAN

**[2026-05-02 00:16] USER:** On a un workflow en place pour outils
- monitoring
Notif
Choix ajout
Dedup
Docu (matrice etc manus, docu utilisateur) notion
Garantie manus utilisés bien routing matrix et fan back mechanism
Etc

Comment améliorer et arriver à top maturity autour de ces questions d extensions de possibilités de manus et de LLM?… improve et optimiser approche incluant éventuellement autres extensions (en plus de api MCP.

**[2026-05-02 00:16] MANUS:** Analyse architecturale en cours — modèle de maturité complet pour la gouvernance des extensions Y-OS.

**[2026-05-02 00:17] MANUS:** ## MODÈLE DE MATURITÉ — Gouvernance des Extensions Y-OS

---

## ÉTAT ACTUEL — Niveau 2 sur 5

Voici le diagnostic honnête de ce qui est en place aujourd'hui et ce qui manque pour atteindre le niveau 5.

| Dimension | Niveau actuel | Gap vers L5 |
|-----------|--------------|-------------|
| Veille (RADAR-MCP) | L3 — bimensuel, multi-sources, scoré | Automatisation complète, alertes temps réel |
| Documentation (Playbook Notion) | L2 — créé aujourd'hui, manuel | Vivant, auto-mis à jour, versionné |
| Routing (skill tool-router) | L2 — skill statique, déclaratif | Routing dynamique avec feedback loop |
| Déduplication | L2 — analyse manuelle par session | Détection automatique avant activation |
| Monitoring usage | L0 — inexistant | Télémétrie complète par outil |
| Notifications | L1 — al

**[2026-05-02 00:20] USER:** Pas désactiver directement connecter en cas de redundancy: parfois utile de je mettre en backup ou pour ça spécifique

Installer custom MCP manquant créer API auto du besoin

**[2026-05-02 00:20] MANUS:** Correction enregistrée — règle mise à jour : jamais désactiver un connecteur redondant, le reclasser en **BACKUP** ou **CAS SPÉCIFIQUE** dans le Playbook. Lancement de l'installation des 5 Custom MCP + setup Exa API en parallèle.

**[2026-05-02 00:24] MANUS:** ## Bilan — Extensions Y-OS

---

### CE QUI EST FAIT

**Règle BACKUP mise à jour** dans le skill tool-router : les connecteurs redondants ne sont plus "désactivés" — ils sont reclassés en BACKUP avec leur cas d'usage spécifique documenté (My Browser → login manuel/CAPTCHA, ClickUp → client externe déjà dessus, etc.).

**4 packages Custom MCP installés globalement** sur le sandbox :

| Package | Statut |
|---------|--------|
| `@modelcontextprotocol/server-sequential-thinking` | ✅ Installé |
| `task-master-ai` | ✅ Installé |
| `figma-developer-mcp` | ✅ Installé |
| `@brightdata/mcp` | ✅ Installé |
| `@tableau/tableau-mcp` | ⚠️ Non disponible sur npm — Tableau n'a pas encore de MCP officiel |

Les packages sont prêts. La configuration finale se fait via **Manus Settings > Connectors > Add Cu

**[2026-05-02 00:27] USER:** Peut pas ajouter ça au profile depuis iOS?? Si impossible taille moi d’eBay depuis laptop 

AVANT TOUT CHOIX D'OUTIL : lire le skill tool-router ou consulter
https://app.notion.com/p/35435e218cf88145ac11c5c082b4290b

**[2026-05-02 00:27] MANUS:** Je vérifie si c'est faisable depuis le browser Manus directement.

**[2026-05-02 00:31] MANUS:** La règle ROUTAGE OUTILS est bien présente dans les Custom Instructions (visible dans le contenu extrait de la page — 1153/3000 caractères). Le bouton Save résiste aux clics automatisés — l'UI Manus utilise probablement un React event handler qui ne répond pas aux clics JS simulés.

**Action manuelle requise — 30 secondes depuis laptop ou iOS :**

1. Ouvrir **manus.im > Settings > Personalization**
2. Le texte est déjà en place dans Custom Instructions (la règle ROUTAGE OUTILS est visible en bas)
3. Cliquer **Save**

C'est la seule étape qui ne peut pas être automatisée depuis le browser sandbox.

**[2026-05-02 00:33] USER:** Oui 
Routing dynamique avec feedback loop
Et

Registre unifié MCP + API + Plugins + Custo

Oui clef! À corriger et automatiser traitent au même niveau de chaque cat
OS traite les MCP comme la seule catégorie d’extension. Il en existe 6.

Ok until level 3 
Go

**[2026-05-02 00:33] MANUS:** Compris. 2 livrables en parallèle : (1) Registre unifié 6 catégories d'extensions, (2) Architecture du routing dynamique avec feedback loop. En cours.

**[2026-05-02 00:34] USER:** Fais springs pour atteindre L3

**[2026-05-02 00:34] MANUS:** Sprint L3 lancé — 4 livrables en séquence rapide.

**[2026-05-02 00:35] USER:** On pourrait ajouter aux 6 outils les skills et prompt librairies non? 2 outils moins fondamentaux mais utiles non

**[2026-05-02 00:35] MANUS:** Exact — 8 catégories, pas 6. Skills et Prompt Libraries sont des extensions cognitives de premier ordre dans Y-OS, pas des outils secondaires. Correction intégrée. Sprint 1 lancé avec la taxonomie complète.

**[2026-05-02 00:36] USER:** Fais pour moi I les 3 actions manuelles

**[2026-05-02 00:37] MANUS:** Les 3 actions manuelles identifiées jusqu'ici sont :

1. **Save Custom Instructions** — cliquer Save dans Settings > Personalization (la règle ROUTAGE OUTILS est déjà en place, il manque juste le clic de confirmation)
2. **Configurer les 4 Custom MCP** dans Settings > Connectors > Add Custom MCP (Sequential Thinking, Task Master, Figma Context, Bright Data)
3. **Ajouter EXA_API_KEY** dans Settings > Secrets

Pour les faire à ta place depuis le browser sandbox, j'ai besoin que tu prennes le contrôle du browser quelques secondes pour le Save (l'UI Manus bloque les clics automatisés). Pour les Custom MCP et la clé Exa, je peux tenter via Playwright headless si tu confirmes.

Veux-tu prendre le contrôle du browser pour le Save ?

**[2026-05-02 00:37] USER:** [Auto-reply] Please continue the task based on current context, proceed if you are on track. Do not ask the same question repeatedly.

**[2026-05-02 00:37] MANUS:** Sprint 1 en cours — construction du Registre Unifié 8 catégories pendant que je tente les 3 actions manuelles via Playwright.

**[2026-05-02 00:40] USER:** Save fait
Use play writer for next

**[2026-05-02 00:40] MANUS:** Save confirmé. Playwright pour les Custom MCP — en cours.

**[2026-05-02 00:43] USER:** On avait déjà travaillé les skills et gay inventaire non? Besoin retient ça et intègre bon management fond (dedup inventaire gaps recherche online super-skills etc
Et intégrer ça avec notre processus tools

 Idem for super-prompts

**[2026-05-02 00:43] MANUS:** Compris — 3 couches à unifier : Skills (inventaire + dedup + gaps + super-skills), Prompt Libraries (super-prompts), et le processus Tools. Tout ça doit être un seul système cohérent, pas 3 silos. Je construis l'architecture unifiée.

**[2026-05-02 00:44] USER:** Met à jour agent minitoring bi mensuel avec TOUUS les outils (8-9 cat) a monitorer etc
Améliore l agent au besoin

**[2026-05-02 00:44] MANUS:** Mise à jour de l'agent de veille bimensuelle pour couvrir les 8-9 catégories d'extensions — en cours.

**[2026-05-02 00:46] USER:** Instructions settings/customs peu rempli<50%
Pas grande valeur à le compléter à 80% au moins pour meilleur résultats de manus?
Avec quoi alors?

**[2026-05-02 00:46] MANUS:** Absolument — les Custom Instructions sont le levier le plus sous-exploité de Manus. À 50% tu laisses 1500 caractères de contexte permanent sur la table. Je vais analyser ce qui est déjà là et proposer un contenu optimal pour atteindre 80-90% (2400-2700/3000 caractères).

**[2026-05-02 00:46] MANUS:** ## Analyse — Custom Instructions Y-OS

**Contenu actuel (1153/3000) :**

Le texte actuel couvre bien le style, le format, l'interaction et le rythme. Il se termine par la règle ROUTAGE OUTILS ajoutée aujourd'hui.

**Ce qui manque à haute valeur (1247 caractères disponibles) :**

---

### PROPOSITION — Contenu à ajouter

Voici les 5 blocs à injecter, par ordre de valeur opérationnelle :

**Bloc 1 — Stack Y-OS actif** (~300 car.)
Dire à Manus quels sont les outils primaires par domaine, sans qu'il ait à lire le Playbook à chaque fois. Gain : routing plus rapide, moins de friction.

**Bloc 2 — Projets actifs** (~250 car.)
Lister les 4-5 projets Y-OS en cours (ODYSSEY, yOS-MMM, etc.) avec leur statut. Gain : Manus comprend le contexte projet sans hydratation manuelle.

**Bloc 3 — Règles d'exéc

**[2026-05-02 00:46] USER:** [Auto-reply] Please continue the task based on current context, proceed if you are on track. Do not ask the same question repeatedly.

**[2026-05-02 00:46] MANUS:** Rédaction et injection des 5 blocs en cours.
