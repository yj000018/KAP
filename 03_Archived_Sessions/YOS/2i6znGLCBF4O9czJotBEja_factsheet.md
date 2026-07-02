---
uid: 2i6znGLCBF4O9czJotBEja
session_url: https://manus.im/app/2i6znGLCBF4O9czJotBEja
session_title: "Architecture Y-OS : échec n8n Manus Cloud, pivot vers N100 Lambda + Capabilities Map"
date: 2026-06-16
project: "Y-OS Infrastructure"
language: fr
depth: moderate
length: medium
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 16:09
referenced_sessions: []
referenced_artifacts: ["Y-OS Capabilities Map (Excalidraw)"]
referenced_urls: ["https://manus.im/app#settings/my-computer/create", "https://manus.im/app#settings/my-computer/cloud-8cd489ill4h7i3u4ougzia68g/manage", "https://manus.im/desktop"]
input_files: []
message_count: 28
---

# Architecture Y-OS : échec n8n Manus Cloud, pivot vers N100 Lambda + Capabilities Map

> **Session:** [2i6znGLCBF4O9czJotBEja](https://manus.im/app/2i6znGLCBF4O9czJotBEja) | **Date:** 2026-06-16 | **Project:** Y-OS Infrastructure | **Language:** fr

## 📋 SESSION CARD

### 🧭 Executive Summary
Tentative d'installation de n8n sur le Manus Cloud Computer Basic (1GB RAM) qui a échoué par manque de mémoire. La décision stratégique a été prise de réserver le serveur Manus aux petits batchs légers, et de déployer n8n, Home Assistant et les apps lourdes sur le N100 physique (Lambda). Une carte complète des capabilities Y-OS (12 domaines, 80+ outils) a été produite en Excalidraw.

### 🎯 Context & Intent
Yannick souhaitait installer n8n en mode 24/7 sur son serveur Manus Cloud Computer pour centraliser ses automations. Il voulait aussi que Manus gère le serveur de façon autonome. La session a évolué vers une révision architecturale de l'écosystème Y-OS suite aux contraintes hardware révélées.

### ✅ What Was Done
1. Audit du Manus Cloud Computer (Basic 1GB RAM) — Docker v29.5.2 confirmé installé
2. Tentative de déploiement n8n via Docker (bloqué : Docker Hub CDN Cloudflare inaccessible depuis IP GCP)
3. Tentative d'installation n8n via npm + pm2 → crash OOM répété (RAM saturée à 955MB)
4. Diagnostic complet du crash : npm install n8n ~1GB dépendances incompatible avec plan Basic
5. Décision architecturale : N100 Lambda = serveur principal (n8n, Home Assistant, apps lourdes) ; Manus Cloud = batchs légers uniquement
6. Nettoyage du serveur Manus post-incident
7. Génération de la Y-OS Capabilities Map (Excalidraw) — 12 domaines, 80+ outils cartographiés
8. Vérification de la connectivité au N100 Lambda (session J+1) → non connecté, guidance fournie pour reconnexion via Manus Desktop Client

### 💡 Key Insights
- **Manus Cloud Basic (1GB RAM) est incompatible avec n8n** — npm install seul consomme ~900MB, provoquant des OOM crashes en boucle
- **Docker Hub CDN (Cloudflare) est bloqué depuis l'IP GCP** du Cloud Computer — pull d'images impossible sans workaround
- **Architecture Y-OS révisée** : N100 Lambda = serveur de production (n8n, Home Assistant, etc.) ; Manus Cloud = orchestration légère / batchs
- Le Manus Cloud Computer semble avoir été upgradé entre les deux jours (RAM affichée 3.8GB le 17/06 vs 955MB le 16/06)
- Le N100 n'est pas accessible depuis Manus sans que le Manus Desktop Client soit installé et actif sur la machine
- Le changement de WiFi ne bloque pas la reconnexion si le client Manus Desktop est en cours d'exécution

### 📦 Outputs Produced
- **[design]** `Y-OS Capabilities Map (Excalidraw)` : cartographie de l'écosystème Y-OS en 12 domaines (Memory & Knowledge, LLM/AI Models, Automation & Workflows, Communication, Media & Design, Data & Analytics, Web & Scraping, Meetings & Transcripts, E-Commerce & Finance, + autres) couvrant 80+ outils/services
- **[doc]** `Architecture Decision Record (informel)` : N100 Lambda = prod, Manus Cloud = batchs légers

### ⚠️ Open Items & Blockers
- Le N100 Lambda n'est pas connecté à Manus — Manus Desktop Client à installer/relancer sur la machine
- n8n n'est pas installé nulle part — installation sur N100 reste à faire
- Home Assistant à déployer sur N100 (mentionné mais non commencé)
- [INCERTAIN] Le changement de WiFi sur le réseau Lambda peut nécessiter une mise à jour de l'IP ou du tunnel si le client Manus utilise une IP fixe locale
- [INCERTAIN] L'upgrade RAM du Cloud Computer (955MB → 3.8GB) n'est pas confirmé volontaire — à clarifier dans les paramètres du compte

### 🔁 Next Steps
1. Installer le **Manus Desktop Client** sur le N100 Lambda → [manus.im/desktop](https://manus.im/desktop)
2. Attacher le N100 à une session Manus et vérifier la connectivité post-changement WiFi
3. Déployer **n8n via Docker** sur le N100 (Docker + docker-compose recommandés, resources suffisantes)
4. Déployer **Home Assistant** sur le N100 (Docker ou HAOS en VM)
5. Définir les batchs légers à héberger sur le Manus Cloud Computer (liste à établir)
6. Documenter l'architecture finale N100 + Manus Cloud dans la base de connaissance Y-OS (Notion/Mem0)
7. Valider la Y-OS Capabilities Map avec Yannick et la compléter si nécessaire

### 🔗 Links & References
- 🌐 https://manus.im/app#settings/my-computer/create — Provisionner un Cloud Computer Manus
- 🌐 https://manus.im/app#settings/my-computer/cloud-8cd489ill4h7i3u4ougzia68g/manage — Gérer / upgrader le Cloud Computer actuel
- 🌐 https://manus.im/desktop — Manus Desktop Client (à installer sur N100)
- 🔗 session:2i6znGLCBF4O9czJotBEja — Session courante

### 🧠 Resume Hint
Le N100 Lambda (Ubuntu, machine physique chez Yannick) est le serveur de production Y-OS désigné pour n8n, Home Assistant et les apps lourdes — il faut d'abord y installer Manus Desktop Client et le connecter à la session avant toute action ; le Manus Cloud Computer est réservé aux batchs légers uniquement.

### 🏷️ Tags
`n8n` `infrastructure` `yos-architecture` `n100-lambda` `manus-cloud` `capabilities-map`

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 28 messages — 2026-06-16

**[2026-06-16 11:19] USER:** sur mon serveur manus PC online, tu pourrais installer n8n proprement, ainsi toujours ON.... Je veux que tu manage 100% de ce servuer manus pour moi...

**[2026-06-16 11:19] MANUS:** Compris. Je lis d'abord les skills pertinents avant de planifier l'installation de n8n sur ton serveur persistant.

**[2026-06-16 11:20] MANUS:** Audit du serveur persistant en cours...

**[2026-06-16 11:20] MANUS:** Aucun "Cloud Computer" persistant n'est actuellement attaché à cette session Manus.

Pour que je puisse installer n8n en production (24/7, Docker, IP fixe) et manager le serveur de façon autonome, il faut d'abord provisionner un environnement persistant.

### 1️⃣ Option A : Manus Cloud Computer (Recommandé pour 24/7)
Machine virtuelle dédiée gérée par Manus, parfaite pour n8n.
* **Coût** : à partir de 10$/mois (Standard 30$/mois recommandé pour n8n + Docker).
* **Action** : Clique sur [Provisionner un Cloud Computer](https://manus.im/app#settings/my-computer/create). Une fois créé, attache-le à la conversation via l'icône ordinateur sous l'input de chat.

### 2️⃣ Option B : Ton propre MiniPC / Serveur local (Zéro coût cloud)
Si tu as déjà un MiniPC ou NAS sous Linux chez toi.
* **Action** 

**[2026-06-16 11:28] USER:** go

**[2026-06-16 11:28] MANUS:** Cloud Computer détecté. Audit en cours...

**[2026-06-16 11:28] MANUS:** Audit OK. Docker déjà installé (v29.5.2). Je déploie n8n maintenant.

**[2026-06-16 11:37] MANUS:** Pull Docker n8n en cours (image ~700MB). Je surveille en arrière-plan — pas d'action requise de ta part.

**[2026-06-16 11:53] MANUS:** pm2 installé. Lancement de l'installation n8n via npm (peut prendre 3-5 min)...

**[2026-06-16 12:15] MANUS:** Le Cloud Computer est temporairement déconnecté (probable OOM — npm install n8n consomme ~900MB sur 955MB de RAM). Le serveur redémarre automatiquement. J'attends la reconnexion...

**[2026-06-16 12:42] MANUS:** Le serveur reste déconnecté depuis ~30 min. Le processus npm install n8n (très lourd, ~1GB de dépendances) a saturé la RAM (955MB) et provoque des crashes répétés.

**Diagnostic** :
- RAM totale : 955MB (plan Basic 1GB) — insuffisante pour npm install n8n
- npm install n8n télécharge ~1500 packages, consomme ~900MB RAM pendant la compilation
- Docker Hub CDN (Cloudflare) bloqué depuis cette IP GCP → pull Docker impossible

**Solutions** :

1️⃣ **Upgrade vers Standard (4GB RAM)** — recommandé ⭐
   → [Upgrader le Cloud Computer](https://manus.im/app#settings/my-computer/cloud-8cd489ill4h7i3u4ougzia68g/manage)
   → 30$/mois, 4GB RAM, suffisant pour n8n + pm2 + futures apps
   → Après upgrade, je relance l'installation en 10 min

2️⃣ **Attendre que le serveur redémarre** (peut prendre encore 5

**[2026-06-16 13:12] USER:** OK, alors là, cette fois, je comprends que le serveur de, de Manus soit le-- très, très petit. On installera donc N8 et Home Assistant et tout le reste directement sur, euh, sur le N100, qui est la machine, euh, physique que j'ai à, à Lambda avec Ubuntu. Donc, on laisse tomber pour l'instant ça. Et on gardera simplement sur le serveur Manus des petits batchs et, euh, et voilà.

**[2026-06-16 13:13] MANUS:** Compris. Je nettoie le serveur Manus et je documente la nouvelle architecture.

**[2026-06-16 13:14] USER:** Trace Excalibur archi complète des app/saas accessibles via serveur mpc et access api depuis manus et déjà installé: donc notre écosystème yOS en terme de capabilities. Shema doit représenter ces capabklities par domaine/groupes de features

**[2026-06-16 13:14] MANUS:** Je lis le skill trace-excalidraw avant de générer.

**[2026-06-16 13:15] MANUS:** Mapping complet des capabilities Y-OS en cours — je construis le schéma Excalidraw par domaine.

**[2026-06-16 13:19] MANUS:** **Y-OS Capabilities Map** — livré en 2 formats.

**12 domaines / 80+ tools** cartographiés :

| Domaine | Outils clés |
|---|---|
| 🧠 Memory & Knowledge | Notion, Mem0, 1Password, Dropbox |
| 🤖 LLM / AI Models | Claude, GPT-5, Gemini, Grok, OpenRouter, Perplexity, Wolfram |
| ⚙️ Automation & Workflows | n8n (N100), Zapier, Make, Linear, ClickUp, Monday, Asana, Wrike |
| 💬 Communication | Gmail, Slack, Zoom, Twilio, ElevenLabs, Calendly |
| 🎨 Media & Design | FLUX, Replicate, MiniMax, HeyGen, Canva, Cloudinary, Hume |
| 📊 Data & Analytics | Airtable, Supabase, CoinGecko, SEMrush, Ahrefs, Similarweb |
| 🌐 Web & Scraping | Firecrawl, Apify, Anchor Browser, HARPA, Playwright, Context7 |
| 🎙️ Meetings & Transcripts | Granola, Fireflies, Fathom, Otter.ai, Read.ai, Plaud |
| 🛒 E-Commerce & Financ

**[2026-06-17 22:36] USER:** tu as acces à mon seerveur N100? on a change le wifi...

**[2026-06-17 22:37] MANUS:** Je vérifie quel device est connecté à cette session...

**[2026-06-17 22:37] MANUS:** **Ce n'est pas le N100.** Le device connecté est le **Manus Cloud Computer GCP** (Basic) :

| Paramètre | Valeur |
|---|---|
| Hostname | `3a4a919f71f1` |
| CPU | Intel Xeon @ 2.20GHz (2 vCPU) |
| RAM | **3.8 GB** (upgrade depuis la dernière fois ?) |
| Disque | 33 GB |
| IP | `169.254.0.21` (réseau interne GCP) |
| OS | Ubuntu 24.04.4 LTS |

Le **N100 Lambda** n'est pas connecté à cette session. Pour y accéder, il faut :

1. Installer le **Manus Desktop Client** sur le N100 → [manus.im/desktop](https://manus.im/desktop)
2. Se connecter avec ton compte Manus
3. Attacher le N100 à la conversation (icône ordinateur sous l'input)

Le changement de WiFi ne pose pas de problème — le client Manus se reconnecte automatiquement dès que le N100 est en ligne et que le client tourne. Tu veux qu'on pl
