---
uid: YP9AFcTGZY2X3NEnqMG4oS
session_url: https://manus.im/app/YP9AFcTGZY2X3NEnqMG4oS
session_title: "Veille MCP Bimensuelle Juin 2026 — Activation Context7, Mem0, Supabase, Perplexity"
date: 2026-06-15
project: "Y-OS"
language: fr
depth: moderate
length: medium
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 13:20
referenced_sessions: []
referenced_artifacts: ["https://app.notion.com/p/38035e218cf8817ca235cf5e684b94bf"]
referenced_urls: ["https://app.notion.com/p/38035e218cf8817ca235cf5e684b94bf", "https://mcp.so", "https://smithery.ai", "https://github.com/punkpeye/awesome-mcp-servers", "https://glama.ai/mcp/servers", "https://mem0.ai", "https://orgx.ai"]
input_files: []
message_count: 40
---

# Veille MCP Bimensuelle Juin 2026 — Activation Context7, Mem0, Supabase, Perplexity

> **Session:** [YP9AFcTGZY2X3NEnqMG4oS](https://manus.im/app/YP9AFcTGZY2X3NEnqMG4oS) | **Date:** 2026-06-15 | **Project:** Y-OS | **Language:** fr

## 📋 SESSION CARD

### 🧭 Executive Summary
Veille MCP bimensuelle exécutée par l'agent TECH-ARCHI sur 4 sources (~36k MCP indexés), produisant un rapport Notion avec 7 MCP pertinents scorés pour Y-OS. Les 4 connecteurs prioritaires (Context7, Mem0, Supabase, Perplexity) ont été activés manuellement par l'utilisateur après blocage des confirmations automatiques en session planifiée. Une seconde vague d'installation (Exa, Mesh/Clay, OrgX, WhisperGraph, DecisionNode) a été initiée via Custom MCP.

---

### 🎯 Context & Intent
Exécution de la veille MCP bimensuelle de Y-OS (cycle mi-juin 2026) via l'agent TECH-ARCHI. L'objectif était d'identifier les MCP à fort momentum marché, de les filtrer par pertinence Y-OS (7 agents actifs + stack existant), puis d'activer les connecteurs retenus dans l'environnement Manus.

---

### ✅ What Was Done
1. Scraping parallèle des 4 sources MCP : mcp.so, smithery.ai, awesome-mcp-servers (GitHub), glama.ai
2. Application du filtre 3 couches (traction objective → pertinence Y-OS → scoring final)
3. Sélection et scoring de 7 MCP pertinents + identification de 3 signaux émergents
4. Publication du rapport RADAR-MCP dans Notion (page sous TECH)
5. Tentatives d'activation automatique de Context7, Mem0, Supabase, Perplexity — bloquées par contrainte de sécurité Manus (session planifiée)
6. Activation manuelle confirmée par l'utilisateur des 4 connecteurs prioritaires
7. Fourniture des instructions d'installation Custom MCP pour Exa Search, Mesh (Clay), OrgX, WhisperGraph, DecisionNode

---

### 💡 Key Insights
- **Blocage sécurité Manus** : les sessions planifiées/autonomes ne peuvent pas auto-confirmer l'activation de connecteurs — `manus-config config save` soumet une suggestion qui requiert validation UI manuelle
- **Context7 + Mem0** : déjà en attente d'activation avant cette veille (pré-identifiés), priorité confirmée (57k et 58k stars respectivement)
- **Exa Search MCP** : clé `EXA_API_KEY` déjà présente dans les secrets Y-OS — installation immédiate possible
- **Perplexity** : clé SONAR déjà dans les secrets — idem
- **5 MCP de la vague 2** absents du catalogue natif Manus → nécessitent le workflow Custom MCP (npx ou Docker)
- **WhisperGraph et DecisionNode** semblent être des MCP émergents/expérimentaux (non trouvés dans catalogue natif)

---

### 📦 Outputs Produced
- **[doc]** `https://app.notion.com/p/38035e218cf8817ca235cf5e684b94bf` : Rapport RADAR-MCP 15 Juin 2026 — scoring 7 MCP pertinents Y-OS + 3 signaux émergents, publié sous TECH dans Notion

---

### ⚠️ Open Items & Blockers
- **Exa Search MCP** : installation Custom MCP à finaliser dans l'UI Manus (npx + `EXA_API_KEY`)
- **Mesh MCP (Clay)** : nécessite un compte Clay + clé API — à créer si non existant [INCERTAIN si compte Clay déjà actif]
- **OrgX MCP** : nécessite compte orgx.ai — statut compte inconnu [INCERTAIN]
- **WhisperGraph MCP** : installation Docker (self-hosted) — procédure détaillée non transmise dans le transcript [INCERTAIN sur disponibilité/stabilité]
- **DecisionNode MCP** : même catégorie que WhisperGraph — statut expérimental [INCERTAIN]
- **Registre Notion** (ID `31435e21-8cf8-8136-83ba-e720d799b0b6`) : mise à jour des statuts connecteurs à vérifier

---

### 🔁 Next Steps
1. Finaliser l'installation de **Exa Search MCP** via Custom MCP (npx `exa-mcp-server` + `EXA_API_KEY` depuis secrets)
2. Vérifier si un compte **Clay** est actif → installer Mesh MCP (`@clay-labs/mesh-mcp`)
3. Créer/vérifier compte **OrgX** (orgx.ai) → installer OrgX MCP
4. Décider de l'infrastructure pour **WhisperGraph** et **DecisionNode** (Docker self-hosted ou attendre version managée)
5. Mettre à jour le registre Notion (`31435e21-8cf8-8136-83ba-e720d799b0b6`) avec les nouveaux statuts d'activation
6. Planifier la prochaine veille MCP bimensuelle (~fin juin / début juillet 2026)

---

### 🔗 Links & References
- 🌐 `https://app.notion.com/p/38035e218cf8817ca235cf5e684b94bf` — Rapport RADAR-MCP 15 Juin 2026
- 📄 Registre stack Y-OS Notion ID : `31435e21-8cf8-8136-83ba-e720d799b0b6`
- 🌐 `https://mcp.so` — Source veille MCP
- 🌐 `https://smithery.ai` — Source veille MCP
- 🌐 `https://github.com/punkpeye/awesome-mcp-servers` — Source veille MCP
- 🌐 `https://glama.ai/mcp/servers` — Source veille MCP
- 🌐 `https://mem0.ai` — Création compte Mem0 (si clé API non encore générée)
- 🔗 session:`YP9AFcTGZY2X3NEnqMG4oS`

---

### 🧠 Resume Hint
Context7, Mem0, Supabase et Perplexity sont activés ; il reste à installer 5 MCP Custom (Exa, Mesh/Clay, OrgX, WhisperGraph, DecisionNode) via `Manus → Settings → Connectors → + Add → Custom MCP`, avec les clés Exa et Perplexity/Sonar déjà dans les secrets.

---

### 🏷️ Tags
`mcp-veille` `tech-archi` `connecteurs-manus` `y-os-stack` `custom-mcp` `radar-mcp`

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 40 messages — 2026-06-15

**[2026-06-15 07:04] USER:** Effectuer la veille MCP bimensuelle pour Y-OS (agent TECH-ARCHI).

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

**[2026-06-15 07:04] MANUS:** Veille MCP bimensuelle lancée. Lecture du skill yos-optimizer en cours avant exécution.

**[2026-06-15 07:04] MANUS:** Mode BALANCED activé. Scraping parallèle des 4 sources MCP en cours...

**[2026-06-15 07:12] MANUS:** Page Notion créée. Ajout du commentaire avec tag Manus en cours...

**[2026-06-15 07:13] MANUS:** ## RADAR-MCP — Rapport 15 Juin 2026 ✅

Page Notion publiée sous TECH : [🔌 RADAR-MCP — Rapport 15 Juin 2026](https://app.notion.com/p/38035e218cf8817ca235cf5e684b94bf)

---

### Couche 2 — Top 7 Pertinents Y-OS

| Rang | MCP | Agent | Reco |
|---|---|---|---|
| 1 | **Context7** (upstash) | TECH/DEV | ✅ ACTIVER — 57k stars, 6.4k uses, déjà en attente |
| 2 | **Mem0** (mem0ai) | KMM/CORE | ✅ ACTIVER — 58k stars, mémoire cross-session, déjà en attente |
| 3 | **Figma-Context-MCP** | CREA/TECH | ✅ ACTIVER — 15k stars, pont design-to-code, déjà en attente |
| 4 | **Supabase MCP** | TECH/DATA | ✅ ACTIVER — DB relationnelle + Edge Functions, nouveau |
| 5 | **Exa Search MCP** | TECH/KMM | ✅ ACTIVER — 32k uses Smithery, clé déjà dans secrets |
| 6 | **Perplexity MCP** | KMM/TECH | 👁️ SURVEILLER — d

**[2026-06-15 07:29] USER:** Active mem0 et context7

**[2026-06-15 07:29] MANUS:** Activation Mem0 + Context7 en cours — lecture config Manus.

**[2026-06-15 07:30] USER:** Active Supabase et perplexity

**[2026-06-15 07:30] MANUS:** Activation Supabase + Perplexity en cours...

**[2026-06-15 07:30] MANUS:** Les deux connecteurs ont été soumis pour activation mais la confirmation a été refusée automatiquement (probablement une restriction de la session planifiée).

**Supabase** et **Perplexity** nécessitent une confirmation manuelle de ta part dans l'interface Manus.

Pour les activer :
1️⃣ Va dans **Manus → Settings → Connectors**
2️⃣ Recherche "Supabase" → activer
3️⃣ Recherche "Perplexity" → activer

Note : Supabase nécessitera ton `SUPABASE_ACCESS_TOKEN` (déjà dans les secrets selon le registre). Perplexity nécessitera ta clé SONAR.

Veux-tu que je tente une autre approche, ou tu confirmes manuellement ?

**[2026-06-15 07:30] USER:** [Auto-reply] Please continue the task based on current context, proceed if you are on track. Do not ask the same question repeatedly.

**[2026-06-15 07:30] MANUS:** Session planifiée — confirmation manuelle requise pour Supabase + Perplexity. Mise à jour du registre Notion en cours.

**[2026-06-15 07:31] MANUS:** Le mécanisme `manus-config config save` soumet les changements pour **confirmation utilisateur** — c'est une contrainte de sécurité Manus, non contournable depuis une session planifiée ou autonome.

**État actuel :**

| Connecteur | Statut | Action requise |
|---|---|---|
| Context7 | Désactivé | Confirmation manuelle |
| Mem0 | Désactivé | Confirmation manuelle |
| Supabase | Désactivé | Confirmation manuelle |
| Perplexity | Désactivé | Confirmation manuelle |

**Pour activer les 4 en une fois :**
→ Va dans **Manus → Settings → Connectors**
→ Recherche et active : `Context7`, `mem0`, `Supabase`, `Perplexity`

Ou dans une session interactive (non planifiée), dis-moi "active Context7, Mem0, Supabase, Perplexity" — je soumets la suggestion et tu confirmes en 1 clic.

Le registre Notion a ét

**[2026-06-16 13:36] USER:** Erudite état nouveau installations

**[2026-06-16 13:36] USER:** Vérifie nouveaux status installations MCP

**[2026-06-16 13:36] MANUS:** Vérification statuts MCP en cours...

**[2026-06-16 13:36] MANUS:** ## Statut MCP — 16 Juin 2026

La config lue ici est la **config de session planifiée** (snapshot isolé), pas la config live de ton compte Manus. C'est pourquoi seul "My Browser" apparaît actif dans ce contexte.

**Statut réel des 4 connecteurs ciblés :**

| Connecteur | Statut config session | Action requise |
|---|---|---|
| **Context7** | `false` (non confirmé) | Activer manuellement |
| **Mem0** | `false` (non confirmé) | Activer manuellement |
| **Supabase** | `false` (non confirmé) | Activer manuellement |
| **Perplexity** | `false` (non confirmé) | Activer manuellement |

**Cause** : `manus-config config save` soumet une *suggestion* — elle requiert ta confirmation dans l'UI Manus. Les sessions planifiées ne peuvent pas auto-confirmer (sécurité by design).

**Action directe** → Dans 

**[2026-06-16 15:27] USER:** Ok

**[2026-06-16 15:27] MANUS:** Noté. Résumé de la session planifiée :

**Accompli ✅**
- Veille MCP 3 couches exécutée (4 sources, ~36k MCP indexés)
- Rapport publié dans Notion TECH : [🔌 RADAR-MCP — Rapport 15 Juin 2026](https://app.notion.com/p/38035e218cf8817ca235cf5e684b94bf)
- 7 MCP pertinents scorés + 3 signaux émergents identifiés

**Pending — action manuelle requise**
Dans ta prochaine session interactive, dis : *"Active Context7, Mem0, Supabase et Perplexity"* → confirmation en 1 clic.

**[2026-06-16 15:27] USER:** Active Context7, Mem0, Supabase et Perplexit

**[2026-06-16 15:27] MANUS:** Activation des 4 connecteurs en cours...

**[2026-06-16 15:28] MANUS:** La suggestion a encore été refusée automatiquement. Le log indique **"not accepted"** pour les 4 — ce n'est pas un bug de ma part, c'est le système de confirmation Manus qui rejette les activations dans ce contexte.

**Ce que tu dois faire directement dans l'UI Manus :**

1. Ouvre **Manus → Settings → Connectors** (icône engrenage)
2. Recherche et active un par un :
   - `Context7`
   - `mem0`
   - `Supabase`
   - `Perplexity`

Chaque activation peut demander une clé API :
- **Context7** → pas de clé requise (gratuit)
- **mem0** → clé API Mem0 (créer compte sur mem0.ai)
- **Supabase** → `SUPABASE_ACCESS_TOKEN` (déjà dans tes secrets selon le registre)
- **Perplexity** → clé SONAR API (déjà dans tes secrets)

Je ne peux pas contourner la confirmation UI — c'est une protection Manus intentio

**[2026-06-16 18:51] USER:** 4 activation ok
comment faire pour Exa Search MCP, Mesh MCP (Clay), OrgX MCP,WhisperGraph MCP, DecisionNode MCP

**[2026-06-16 18:51] MANUS:** Recherche des 5 MCP dans la config Manus...

**[2026-06-16 18:52] MANUS:** ## Exa, Mesh (Clay), OrgX, WhisperGraph, DecisionNode — Mode d'installation

Ces 5 MCP **ne sont pas dans le catalogue natif Manus** (contrairement à Context7, Mem0, Supabase, Perplexity qui y étaient). Il faut les installer comme **Custom MCP**.

---

### Méthode : Custom MCP dans Manus

**Manus → Settings → Connectors → + Add → Custom MCP**

---

| MCP | Type | Commande d'installation | Clé requise |
|---|---|---|---|
| **Exa Search MCP** | Custom MCP (npx) | `npx -y exa-mcp-server` | `EXA_API_KEY` (déjà dans tes secrets) |
| **Mesh MCP (Clay)** | Custom MCP (npx) | `npx -y @clay-labs/mesh-mcp` | Compte Clay + API key |
| **OrgX MCP** | Custom MCP (npx) | `npx -y @orgx/mcp-server` | Compte OrgX (orgx.ai) |
| **WhisperGraph MCP** | Custom MCP (Docker) | Self-hosted — voir ci-dessous | Auc
