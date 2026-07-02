---
uid: v5e19qsh5tydAeTSzGAyF6
session_url: https://manus.im/app/v5e19qsh5tydAeTSzGAyF6
session_title: "Wolfram MCP Connector — Test Live & Factsheet Y-OS"
date: 2026-06-16
project: "Y-OS Registre Connecteurs Manus"
language: fr
depth: moderate
length: medium
llm_used: unknown
card_generated_by: claude-sonnet-4-6 via KAP pipeline v3
card_generated_at: 2026-07-02 13:14
referenced_sessions: []
referenced_artifacts: ["\ud83e\uddee Wolfram MCP \u2014 Factsheet & Capabilities"]
referenced_urls: ["https://app.notion.com/p/38135e218cf881cd9bcefd9772a59bc5", "https://manus.im/app/v5e19qsh5tydAeTSzGAyF6"]
input_files: []
message_count: 11
---

# Wolfram MCP Connector — Test Live & Factsheet Y-OS

> **Session:** [v5e19qsh5tydAeTSzGAyF6](https://manus.im/app/v5e19qsh5tydAeTSzGAyF6) | **Date:** 2026-06-16 | **Project:** Y-OS Registre Connecteurs Manus | **Language:** fr

## 📋 SESSION CARD

### 🧭 Executive Summary
Session de test live du connecteur Wolfram MCP dans Manus, couvrant les 3 outils disponibles (WolframAlpha, WolframLanguageEvaluator, WolframContext) avec 5 requêtes de démonstration réelles. Une factsheet standardisée Y-OS a été produite et poussée dans Notion, alignée sur le format du registre des connecteurs. Le connecteur est validé pour la data dure et le calcul formel, avec des réserves sur le module sémantique.

---

### 🎯 Context & Intent
Yannick dispose d'un nouveau connecteur Wolfram dans Manus et souhaite (1) valider techniquement son fonctionnement via des tests live, et (2) documenter l'outil selon le standard Y-OS de factsheet connecteur — incluant capabilities, limites, pricing, lessons learned et valeur business — pour alimenter le registre des connecteurs Manus dans Notion.

---

### ✅ What Was Done
1. Inventaire des 3 outils MCP Wolfram disponibles dans Manus
2. Exécution de 5 requêtes de démonstration en parallèle couvrant : data socio-économique (France), astronomie temps réel (Mars), chimie, calcul symbolique, finance
3. Collecte et synthèse des résultats live (données réelles retournées par l'API)
4. Rédaction d'une factsheet complète au format standard Y-OS (9 sections)
5. Push de la factsheet dans Notion, dans la base "🔌 Y-OS — Registre Connecteurs Manus"

---

### 💡 Key Insights
- **WolframAlpha & WolframLanguageEvaluator** : fiables, précis, excellents pour la data factuelle dure et le calcul symbolique — zéro hallucination
- **WolframContext** (module sémantique) : instable, sujets aux timeouts — à utiliser avec précaution
- **Stateless by design** : le noyau Wolfram ne retient pas les variables entre deux requêtes séparées ; toute session doit être auto-contenue
- **Format de sortie raster** pour les visualisations : pas d'output vectoriel natif, ce qui peut limiter l'intégration dans certains flows
- La syntaxe Wolfram Language est stricte — les requêtes mal formées échouent silencieusement
- **Pricing** : Free tier 2 000 calls/mois, Pro $9.99/mois, serveur MCP gratuit → faible coût d'entrée pour Y-OS
- La factsheet suit le gabarit standard du registre Y-OS (même structure que les autres connecteurs documentés)

---

### 📦 Outputs Produced
- **[doc]** `🧮 Wolfram MCP — Factsheet & Capabilities` : Factsheet complète au format Y-OS (9 sections : synthèse télégraphique, executive summary, capacités techniques, limites, pricing, intégration, lessons learned, use cases, verdict), avec données live issues des tests
- **[data]** `Résultats tests live Wolfram` : Données réelles récupérées via les 5 requêtes de démonstration (socio-éco France, Mars, chimie, calcul symbolique, finance) — incluses dans le document joint à la session

---

### ⚠️ Open Items & Blockers
- WolframContext fait des timeouts récurrents — cause non identifiée (rate limit ? endpoint instable ?) `[INCERTAIN]`
- La factsheet mentionne "Intégration" comme section 5 mais le transcript est tronqué — contenu complet de cette section non vérifiable `[INCERTAIN]`
- Aucune confirmation que la page Notion est visible/accessible à d'autres membres de l'espace Y-OS (permissions non vérifiées)
- Pas de test effectué sur des volumes élevés (near-limit du free tier) — comportement à la limite des 2 000 calls/mois inconnu

---

### 🔁 Next Steps
1. Vérifier la stabilité de WolframContext en relançant des tests ciblés sur ce seul module
2. Documenter un exemple de requête Wolfram Language correctement formée dans la factsheet (guide syntaxe)
3. Tester un workflow stateful workaround (passer les variables dans chaque appel explicitement) et documenter le pattern
4. Ajouter la factsheet Wolfram au dashboard récapitulatif des connecteurs Y-OS si celui-ci existe
5. Définir 2-3 use cases Y-OS concrets qui exploiteront le connecteur Wolfram en production (ex : rapports financiers, calculs scientifiques, data viz)

---

### 🔗 Links & References
- 🌐 `https://app.notion.com/p/38135e218cf881cd9bcefd9772a59bc5` — Page Notion : 🧮 Wolfram MCP — Factsheet & Capabilities
- 🌐 `https://manus.im/app/v5e19qsh5tydAeTSzGAyF6` — Session Manus source
- 🔗 session:`v5e19qsh5tydAeTSzGAyF6` — Session courante (test + factsheet Wolfram)

---

### 🧠 Resume Hint
La factsheet Wolfram MCP est créée et dans Notion ; le connecteur est validé pour WolframAlpha et WolframLanguageEvaluator, mais WolframContext reste instable (timeouts) et le noyau est stateless — prochaine action : stabiliser le module Context et définir les use cases Y-OS production.

---

### 🏷️ Tags
`wolfram-mcp` `connector-factsheet` `y-os-registry` `tool-testing` `notion-push` `manus-connector`

---

---

## 📜 VERBATIM ARCHIVE

> Raw transcript — 11 messages — 2026-06-16

**[2026-06-16 08:58] USER:** Help me test the Wolfram connector and show me how to use its feature (e.g. show any data you fetched with it). Give me a brief about its capabi

**[2026-06-16 08:58] MANUS:** Sur ça. Je liste les outils Wolfram disponibles, exécute quelques requêtes de démonstration, et te produis un brief complet des capacités.

**[2026-06-16 08:59] MANUS:** 3 outils confirmés. Je lance maintenant 5 requêtes de démonstration en parallèle : WolframAlpha (factuel + science), WolframLanguageEvaluator (calcul symbolique + data viz), et WolframContext (sémantique).

**[2026-06-16 09:07] MANUS:** Tests terminés. J'ai sollicité le connecteur Wolfram sur de la data socio-éco (France), de l'astronomie temps réel (Mars), de la chimie, du calcul symbolique et de la finance.

Le brief détaillé avec les données live est dans le document joint.

⭐ **Conclusion rapide :** Excellent pour la data dure et le calcul formel (WolframAlpha / Evaluator). Attention au module sémantique (Context) qui fait des timeouts, et au noyau qui est stateless (ne retient pas les variables entre deux requêtes).

**[2026-06-16 13:25] USER:** C'est donc un nouvel outil disponible pour iOS. Il faut donc une factsheet et d'un outil avec ses capabilités, ses limites, les lessons learned, les éventuels accès, etc. Comme d'habitude, on fait cette factsheet pour cet outil. Là, on l'a vraiment testé avec tous les accès et tous les API, les entry points, etc. D'autres fois, on n'a pas eu le temps de tester et donc c'est ce que ça donne en général d'après la documentation que tu retrouves online. Mais je veux savoir que pour tel outil, on a telle possibilité et que ça offre. On est capable d'écrire, de lire, de faire, les possibilités techniques d'accès à l'outil et les possibilités en termes de capabilities, de features, donc business-wise. Qu'est-ce que ça m'importe d'avoir cette connexion-là ? Et puis, c'est gratuit, payant, etc. Don

**[2026-06-16 13:25] MANUS:** Compris. Je cherche d'abord la structure de factsheet existante dans Notion/yOS, puis je complète avec la doc Wolfram online, les tests live qu'on vient de faire, et je produis la factsheet complète.

**[2026-06-16 13:28] MANUS:** Factsheet créée et poussée dans Notion. ✅

**Page Notion :** [🧮 Wolfram MCP — Factsheet & Capabilities](https://app.notion.com/p/38135e218cf881cd9bcefd9772a59bc5)
**Emplacement :** 🔌 Y-OS — Registre Connecteurs Manus

---

**Structure de la factsheet (identique aux autres connecteurs yOS) :**

| Section | Contenu |
|---|---|
| **0. Synthèse Télégraphique** | Action principale, méthode, business value, coût, place dans Y-OS |
| **1. Executive Summary** | Valeur business détaillée (zéro hallucination, hard data, viz native) |
| **2. Capacités Techniques** | 3 outils MCP + données live récupérées lors des tests |
| **3. Limites & Constraints** | Stateless, timeouts, format raster, syntaxe stricte |
| **4. Pricing** | Free 2k calls/mois, Pro $9.99/mois, MCP server gratuit |
| **5. Intégration 
