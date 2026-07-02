---
uid: 9hMGmkTUdqUyTG6HV3vMtp
session_url: https://manus.im/app/9hMGmkTUdqUyTG6HV3vMtp
session_title: "Flux MCP Connector — Test live, cartographie & factsheet Y-OS"
date: 2026-06-15
project: "Y-OS Tools Registry"
language: fr
depth: substantial
length: medium
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 13:19
referenced_sessions: []
referenced_artifacts: ["Flux MCP Connector \u2014 Factsheet & Capability Assessment", "Y-OS Tools Registry v2"]
referenced_urls: ["https://app.notion.com/p/38135e218cf881809409f18eb13d68d1", "https://app.notion.com/p/85f89b4e847d4cbea9310ffdf11b60f2", "https://manus.im/app/9hMGmkTUdqUyTG6HV3vMtp"]
input_files: []
message_count: 16
---

# Flux MCP Connector — Test live, cartographie & factsheet Y-OS

> **Session:** [9hMGmkTUdqUyTG6HV3vMtp](https://manus.im/app/9hMGmkTUdqUyTG6HV3vMtp) | **Date:** 2026-06-15 | **Project:** Y-OS Tools Registry | **Language:** fr

## 📋 SESSION CARD

### 🧭 Executive Summary
Cette session a servi à tester en live le connecteur MCP Flux (BFL) depuis Y-OS, en cartographiant ses 8 outils et en exécutant des démos réelles (T2I, variations, historique). Une factsheet structurée aux standards Y-OS a été produite et publiée dans Notion, puis enregistrée dans le Y-OS Tools Registry v2. Flux MCP est désormais documenté, testé et intégré à la base de connaissance outillage de Y-OS.

---

### 🎯 Context & Intent
Yannick souhaitait tester concrètement le connecteur Flux MCP (accès API Black Forest Labs), valider ses capacités réelles via des appels live, puis formaliser une factsheet outil selon le template Y-OS standard — couvrant capacités techniques, business value, limites, pricing et accès — et l'inscrire dans le registre centralisé des outils Y-OS sur Notion.

---

### ✅ What Was Done
1. Lecture et activation des skills `tool-router` et `yos-optimizer` pour cadrer l'exploration
2. Exploration et cartographie complète des 8 outils MCP exposés par le connecteur Flux
3. Exécution de 4 démos live : génération T2I (flux2_pro_preview, 1920×1080), variations, crédits, historique — consommant 5 crédits sur les 20 du free grant
4. Recherche de la structure de factsheet existante dans Notion (référence : fiche Cloudinary)
5. Rédaction et publication de la factsheet complète Flux MCP (7 sections, template Y-OS) dans Notion / System Architecture
6. Création d'une entrée structurée dans le Y-OS Tools Registry v2 avec tous les champs remplis (12 capacités, business value, dépendances, limites, pricing, auth, tags)

---

### 💡 Key Insights
- **8 outils MCP couverts** : `get_credits`, `generate_image`, `get_result`, `generate_variations`, `get_history`, `vto`, `refresh_image_url`, `request_upload_url`
- **`get_result` est requis** dans les environnements non-iframe comme Manus (polling manuel) — point d'attention pour l'intégration
- **Virtual Try-On (`vto`)** identifié comme use case business différenciant (personne + vêtement)
- **Pricing pay-as-you-go** avec un free grant one-time de 20 générations — modèle à surveiller pour la scalabilité
- **4 modèles FLUX.2** disponibles avec des profils coût/qualité distincts — tableau comparatif produit dans la factsheet
- **Dépendances identifiées** : Cloudinary, WebApp Factory, Miro — pertinent pour l'architecture de pipeline media
- La factsheet Cloudinary sert de **référence canonique** pour le template Y-OS Tools

---

### 📦 Outputs Produced
- **[doc]** `Flux MCP Connector — Factsheet & Capability Assessment` : Factsheet complète 7 sections (synthèse, executive summary, capacités techniques, modèles, limites, pricing, use cases) — publiée dans Notion / System Architecture
- **[data]** `Y-OS Tools Registry v2 — entrée Flux MCP` : Entrée structurée base de données Notion avec 12+ champs remplis (capabilities, business value, dépendances, limites connues, auth, tags)

---

### ⚠️ Open Items & Blockers
- **[INCERTAIN]** Solde exact des crédits restants après démos — 15 crédits annoncés mais non reconfirmés en fin de session
- **[INCERTAIN]** Les URLs signées des images générées en démo ont une durée de vie limitée — `refresh_image_url` nécessaire pour archivage long terme
- Les limites complètes (5 listées dans le Registry) sont tronquées dans le transcript — détail exact non visible
- Aucun test du tool `vto` réalisé en live — capacité cartographiée mais non validée empiriquement

---

### 🔁 Next Steps
1. Tester le tool `vto` (Virtual Try-On) avec un cas réel pour valider la capacité empiriquement
2. Archiver les images générées en démo via Cloudinary (pipeline `generate_image` → `refresh_image_url` → Cloudinary)
3. Vérifier que les URLs Notion des deux pages sont pérennes et accessibles depuis le dashboard Y-OS
4. Envisager un pipeline automatisé Flux → Cloudinary → Miro pour les use cases design/brand
5. Monitorer la consommation des crédits restants (15/20) et anticiper le passage en pay-as-you-go

---

### 🔗 Links & References
- 🌐 [Flux MCP Connector — Factsheet & Capability Assessment](https://app.notion.com/p/38135e218cf881809409f18eb13d68d1)
- 🌐 [Y-OS Tools Registry v2](https://app.notion.com/p/85f89b4e847d4cbea9310ffdf11b60f2)
- 🔗 session:`9hMGmkTUdqUyTG6HV3vMtp`

---

### 🧠 Resume Hint
Le connecteur Flux MCP est testé, documenté et enregistré dans Y-OS (factsheet + Registry) — prochaine action prioritaire : tester `vto` en live et connecter le pipeline Flux → Cloudinary pour l'archivage des générations.

---

### 🏷️ Tags
`flux-mcp` `image-generation` `tool-factsheet` `yos-tools-registry` `bfl-api` `media-ai`

---

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 16 messages — 2026-06-15

**[2026-06-15 09:08] USER:** Help me test the Flux connector and show me how to use its feature (e.g. sh

**[2026-06-15 09:08] MANUS:** Sur le coup — je lis le skill tool-router + yos-optimizer, puis j'explore le connecteur Flux MCP pour te montrer toutes ses capacités avec des exemples concrets.

**[2026-06-15 09:09] MANUS:** 8 outils cartographiés. Je lance maintenant les démos live — en commençant par les crédits disponibles, puis génération T2I, édition, variations, historique.

**[2026-06-15 09:14] MANUS:** ## Flux MCP — Test complet ✅

**Crédits** : 20 free generations (one-time grant) → 15 restantes après les démos.

---

### 8 outils cartographiés

| Outil | Rôle |
|---|---|
| `get_credits` | Solde crédits + free pool |
| `generate_image` | T2I, édition, outpainting, batch (1-8), multi-référence |
| `get_result` | Polling manuel (environnements non-iframe comme Manus) |
| `generate_variations` | N variations d'une gen existante (max 8) |
| `get_history` | Historique paginé avec thumbnails |
| `vto` | Virtual try-on — personne + vêtement |
| `refresh_image_url` | Renouveler URL signée expirée |
| `request_upload_url` | Upload image locale → bucket BFL |

---

### 4 démos live exécutées

**Démo 1 — T2I** (`flux2_pro_preview`, 1920×1080) : interface holographique Y-OS, palette bleu/or, éclair

**[2026-06-16 13:34] USER:** C'est donc un nouvel outil disponible pour iOS. Il faut donc une factsheet et d'un outil avec ses capabilités, ses limites, les lessons learned, les éventuels accès, etc. Comme d'habitude, on fait cette factsheet pour cet outil. Là, on l'a vraiment testé avec tous les accès et tous les API, les entry points, etc. D'autres fois, on n'a pas eu le temps de tester et donc c'est ce que ça donne en général d'après la documentation que tu retrouves online. Mais je veux savoir que pour tel outil, on a telle possibilité et que ça offre. On est capable d'écrire, de lire, de faire, les possibilités techniques d'accès à l'outil et les possibilités en termes de capabilities, de features, donc business-wise. Qu'est-ce que ça m'importe d'avoir cette connexion-là ? Et puis, c'est gratuit, payant, etc. Don

**[2026-06-16 13:35] MANUS:** Compris. Je cherche d'abord la structure de factsheet existante dans Notion/mémoire Y-OS, puis je consulte la doc BFL en ligne pour valider les limites réelles, et je produis la factsheet complète Flux MCP.

**[2026-06-16 13:40] MANUS:** ## Factsheet Flux MCP — Créée ✅

**Notion :** [🖼️ Flux MCP Connector — Factsheet & Capability Assessment](https://app.notion.com/p/38135e218cf881809409f18eb13d68d1)
Publiée sous **System Architecture** — même emplacement que Miro, Cloudinary, Wolfram, etc.

---

### Structure suivie (template Y-OS standard)

La factsheet reprend exactement la structure des fiches existantes (Cloudinary comme référence la plus récente) et l'enrichit avec 2 nouvelles sections :

| Section | Contenu |
|---|---|
| **0. Synthèse Télégraphique** | 5 lignes — lecture en 30 secondes |
| **1. Executive Summary** | Business value narrative (3 angles : photoréalisme, multi-ref, VTO) |
| **2. Capacités Techniques** | 8 outils MCP détaillés, groupés par catégorie |
| **3. Modèles FLUX.2** | Tableau comparatif des 4 mod

**[2026-06-21 11:33] USER:** Bien
Garde en mémoire ces capabilities et use cases, comme pour tous les autres outils avec même structure type Fact Sheet, dans yOS Tools  dans notion

**[2026-06-21 11:33] MANUS:** Je cherche la base Notion "yOS Tools" pour trouver la bonne structure et y insérer la fiche Flux MCP.

**[2026-06-21 11:34] MANUS:** ✅ Flux MCP enregistré dans les deux emplacements Notion :

**1. Factsheet complète** (page narrative, 7 sections)
→ [🖼️ Flux MCP Connector — Factsheet & Capability Assessment](https://app.notion.com/p/38135e218cf881809409f18eb13d68d1)

**2. Y-OS Tools Registry v2** (entrée structurée base de données)
→ [🗂️ Y-OS Tools Registry v2](https://app.notion.com/p/85f89b4e847d4cbea9310ffdf11b60f2)

Tous les champs du Registry sont remplis :

| Champ | Valeur |
|---|---|
| Tool Type | MCP Connector |
| Category | Image / Video / Voice AI |
| Status | Production |
| Pricing | Pay-as-you-go |
| Auth | OAuth MCP |
| Tags | media, design, vision |
| Capabilities | 12 capacités listées |
| Business Value | Synthèse narrative |
| Dependencies | Cloudinary / WebApp Factory / Miro |
| Known Limits | 5 contra
