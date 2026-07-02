---
uid: ptzehrpxrHnXVu55XXLbuZ
session_url: https://manus.im/app/ptzehrpxrHnXVu55XXLbuZ
session_title: "Démonstration du skill tool-router Y-OS — matrice de routage par domaine"
date: 2026-05-02
project: "Y-OS"
language: fr
depth: moderate
length: short
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 15:25
referenced_sessions: []
referenced_artifacts: ["tool-router-demo"]
referenced_urls: ["https://manus.im/app/ptzehrpxrHnXVu55XXLbuZ"]
input_files: []
message_count: 5
---

# Démonstration du skill tool-router Y-OS — matrice de routage par domaine

> **Session:** [ptzehrpxrHnXVu55XXLbuZ](https://manus.im/app/ptzehrpxrHnXVu55XXLbuZ) | **Date:** 2026-05-02 | **Project:** Y-OS | **Language:** fr

## 📋 SESSION CARD

### 🧭 Executive Summary
Yannick a ajouté le skill `/tool-router` à Manus et a demandé une démonstration concrète. Manus a analysé la matrice de routage Y-OS et produit un document structuré illustrant la logique de décision outil-par-outil à travers 4 domaines fonctionnels. Le livrable établit une référence visuelle claire pour comprendre et justifier les choix d'outils dans Y-OS.

---

### 🎯 Context & Intent
Valider et illustrer le nouveau skill `/tool-router` fraîchement intégré à Y-OS. L'objectif était de démontrer que Manus peut correctement lire la matrice de routage et appliquer sa logique (Intention → Vérification des redondances → Outil optimal) avec des exemples réels et pertinents.

---

### ✅ What Was Done
1. Lecture et analyse du skill `tool-router` tel qu'ajouté par Yannick
2. Identification des 4 domaines couverts par la matrice de routage Y-OS
3. Construction d'un document de démonstration structuré avec tableaux de décision
4. Illustration de la logique de routage pour chaque domaine (Web, LLM, Code/DB, Design/Multimédia)
5. Justification architecturale des choix d'outils selon les règles du skill

---

### 💡 Key Insights
- Le skill `tool-router` fonctionne correctement : Manus peut le lire et l'appliquer sans intervention supplémentaire
- La logique tripartite **Intention → Redondances → Outil optimal** est opérationnelle comme principe de routage
- La matrice couvre 4 domaines distincts avec des outils à risque de chevauchement : Web (Bright Data / Playwright / Perplexity), LLM (Gemini / OpenRouter / Grok), Code (GitHub / Linear / Supabase), Design (Canva / HeyGen / Hume)
- Les tableaux comparatifs sont le format le plus adapté pour rendre la logique de routage lisible et auditable
- [INCERTAIN] Le contenu exact du document produit n'est pas entièrement visible dans le transcript — seule la structure est confirmée

---

### 📦 Outputs Produced
- **[doc]** `tool-router-demo`: Document structuré illustrant la logique de routage Y-OS avec tableaux de décision par domaine (Web, LLM, Code/DB, Design/Multimédia)

---

### ⚠️ Open Items & Blockers
- [INCERTAIN] Le document complet n'est pas reproduit dans le transcript — son contenu précis (exemples, cas limites) reste non archivé
- [INCERTAIN] Il n'est pas confirmé que tous les outils listés dans la matrice sont activement intégrés dans Y-OS au moment de la session
- Aucun test de routage en conditions réelles (vraie requête ambiguë → décision de routage) n'a été effectué dans cette session

---

### 🔁 Next Steps
1. Archiver le document de démonstration complet dans Y-OS (vault ou knowledge base)
2. Tester le skill `tool-router` sur des cas réels ambigus (ex. requête pouvant aller à Perplexity ou Playwright)
3. Itérer sur la matrice si des zones de chevauchement non couvertes émergent à l'usage
4. Envisager une version interactive du routeur (CLI ou prompt guidé) pour faciliter la décision en temps réel

---

### 🔗 Links & References
- 🔗 session:`ptzehrpxrHnXVu55XXLbuZ`
- 🌐 https://manus.im/app/ptzehrpxrHnXVu55XXLbuZ
- 📄 skill: `/tool-router` (Y-OS)

---

### 🧠 Resume Hint
Le skill `/tool-router` est actif dans Y-OS et a été validé par démonstration ; le prochain agent peut l'utiliser directement pour arbitrer entre outils redondants selon la logique Intention → Redondances → Outil optimal.

---

### 🏷️ Tags
`tool-router` `y-os-skills` `routing-logic` `tool-selection` `manus-demo`

---

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 5 messages — 2026-05-02

**[2026-05-02 00:20] USER:** I just added the /tool-router skill for Manus. Can you demo it with some great examples?

**[2026-05-02 00:20] MANUS:** Got it — reading the tool-router skill first, then I'll build a sharp demo with real examples.

**[2026-05-02 00:21] MANUS:** Voici la démonstration structurée du skill `tool-router`. 

J'ai analysé la matrice de routage Y-OS et construit un document qui illustre la logique de décision (Intention → Vérification des redondances → Outil optimal) à travers 4 grands domaines :
1. Recherche Web & Extraction (Bright Data vs Playwright vs Perplexity)
2. LLM & Traitement Cognitif (Gemini vs OpenRouter vs Grok)
3. Code, Projets & DB (GitHub vs Linear vs Supabase)
4. Design & Multimédia (Canva vs HeyGen vs Hume)

Le document utilise des tableaux clairs pour justifier chaque choix architectural selon tes règles.
