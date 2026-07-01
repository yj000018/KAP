---
name: prompt-optimizer
description: "Autonomous prompt rewriter for Y-OS. Rewrites user prompts according to a mode (performance/balanced/economy). Can be called independently via /prompt-optimize or by yos-optimizer for double-pass optimization. Performance mode enriches and adds LLM/tool directives. Economy mode simplifies and removes costly loops. Balanced mode clarifies and structures."
---

# Prompt Optimizer

Réécriture intelligente de prompts selon le mode d'optimisation Y-OS. Autonome et appelable indépendamment ou via `yos-optimizer`.

---

## Déclenchement

### Indépendant
```
/prompt-optimize [mode?]   → réécriture du dernier prompt
/prompt-optimize performance "mon prompt"
/prompt-optimize economy "mon prompt"
/prompt-optimize balanced "mon prompt"
```

### Appelé par yos-optimizer
- **Passe 1** : avant routing — réécriture selon mode
- **Passe 2** : après routing — enrichissement avec directives LLM/outil/mémoire

---

## Règles de réécriture par mode

### PERFORMANCE
**Objectif :** Maximiser la qualité de la réponse. Prompt enrichi, structuré, avec toutes les directives nécessaires.

**Transformations :**
- Ajouter contexte manquant depuis la conversation
- Structurer en étapes numérotées si tâche complexe
- Préciser les critères de succès
- Ajouter directive LLM si tâche spécialisée :
  - Analyse longue / document > 50 pages → "Utilise Gemini 2.5 Pro via API (longue context window)"
  - Raisonnement complexe / code → "Utilise Claude Opus via API"
  - Recherche web temps réel → "Utilise Perplexity via API"
  - Génération image → "Utilise FLUX via API Replicate"
- Ajouter directive outil si automatisation :
  - Browser → "Utilise Playwright MCP"
  - Extraction web → "Utilise Firecrawl MCP"
  - Données → "Génère un script Python si nécessaire"
- Autoriser les boucles et itérations si elles apportent de la qualité

**Exemple :**
```
Avant  : "Analyse ce document et fais un résumé"
Après  : "Utilise Gemini 2.5 Pro via API pour analyser ce document de 80 pages.
          Produis :
          1. Résumé exécutif (300 mots)
          2. Points clés structurés par thème
          3. Citations importantes avec numéros de page
          4. Recommandations actionnables
          Critère de succès : résumé utilisable sans lire le document original."
```

### ECONOMY
**Objectif :** Résultat suffisant au coût minimal. Prompt simplifié, scope réduit, pas de boucles coûteuses.

**Transformations :**
- Réduire le scope à l'essentiel
- Supprimer les étapes non critiques
- Remplacer browser par extraction directe si possible
- Remplacer scripts par commandes shell si possible
- Ajouter directive LLM léger si applicable :
  - "Utilise Gemini Flash via API (rapide, gratuit tier)"
  - "Utilise OpenRouter avec modèle Llama-3 (coût minimal)"
- Supprimer les demandes de validation intermédiaire
- Limiter la profondeur de recherche

**Exemple :**
```
Avant  : "Recherche les 50 meilleures startups IA en Europe, analyse leurs produits,
          compare leurs modèles business, fais un rapport complet avec visualisations"
Après  : "Liste les 10 startups IA européennes les plus citées en 2025.
          Pour chacune : nom, produit principal, modèle business (1 ligne).
          Format : tableau markdown. Utilise Perplexity via API.
          Pas de visualisations, pas d'analyse approfondie."
```

### BALANCED (défaut)
**Objectif :** Clarté maximale, structure propre, coût raisonnable.

**Transformations :**
- Clarifier les pronoms vagues ("ça", "ici", "le truc")
- Préciser les objectifs si manquants
- Structurer si > 2 étapes
- Ajouter contexte pertinent depuis la conversation
- Pas de directive LLM sauf si évidente
- Conserver le scope original

**Exemple :**
```
Avant  : "Améliore ça et mets à jour le site"
Après  : "Améliore le composant Dashboard (client/src/pages/Dashboard.tsx) :
          1. Réduire le temps de chargement via lazy loading
          2. Ajouter l'export CSV des données
          Puis mettre à jour le site en production via checkpoint + publish."
```

---

## Passe 2 — Enrichissement post-routing

Appelée par `yos-optimizer` après que LLM, outils et mémoire ont été choisis.

**Ajoute au prompt réécrit (Passe 1) :**

```
[Directives d'exécution]
LLM      : {LLM choisi} via API — appeler directement avec ANTHROPIC_API_KEY / GEMINI_API_KEY / etc.
Outils   : {outils choisis} — utiliser en priorité
Mémoire  : {contexte rapatrié} — voici le contexte projet pertinent : [résumé]
Mode     : {mode} — {rappel des contraintes du mode}
```

**Règle :** La Passe 2 ne réécrit pas — elle ajoute une section `[Directives d'exécution]` à la fin du prompt de Passe 1.

---

## Seuil de déclenchement

**Ne pas réécrire si :**
- Prompt < 10 mots ET intention claire
- Question factuelle simple
- Commande directe sans ambiguïté ("liste les fichiers", "affiche le statut")

**Toujours réécrire si :**
- Prompt contient "améliore", "optimise", "fais mieux", "ça", "le truc"
- Tâche multi-étapes sans structure
- Tâche coûteuse sans scope défini

---

## Format de sortie

```
📝 PROMPT OPTIMISÉ [{mode}]
─────────────────────────────
{prompt réécrit}
─────────────────────────────
Modifications : {liste courte des changements apportés}
```

Si Passe 2 :
```
📝 PROMPT FINAL [{mode}] — avec directives d'exécution
─────────────────────────────
{prompt Passe 1}

[Directives d'exécution]
LLM    : {LLM} via API
Outils : {outils}
Mode   : {mode}
─────────────────────────────
```

---

## Gouvernance

**Propriétaire** : Yannick (Y-OS)
**Version** : 1.0
**Créé** : 2026-05-26
**Statut** : Opérationnel
**Appelé par** : yos-optimizer (Passe 1 + Passe 2), utilisateur direct (/prompt-optimize)
