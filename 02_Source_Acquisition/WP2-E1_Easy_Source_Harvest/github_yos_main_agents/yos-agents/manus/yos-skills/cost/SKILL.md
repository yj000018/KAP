---
name: cost
description: Audit credit consumption of the current Manus session AND optimize upcoming tasks in real-time. Use when the user asks "combien de crédits", "cost estimate", "économies possibles", "optimize credits", "/cost", or wants a session cost breakdown with actionable reduction suggestions and projected savings.
---

# Cost — Session Auditor & Real-Time Optimizer

Two modes in one skill:

- **Mode AUDIT** (`/cost`) — analyse la session passée, identifie les gaspillages, produit un rapport structuré
- **Mode OPTIMIZE** (avant une tâche) — évalue le coût estimé d'une tâche à venir et propose le plan le moins cher sans perte de qualité

---

## Mode AUDIT — Rapport de session

### Step 1 — Compter les actions par catégorie

| Catégorie | Exemples | Poids crédit |
|---|---|---|
| Browser navigate | `browser_navigate`, `browser_view` | Moyen |
| Browser eval/run | `browser_evaluate`, `browser_run_code_unsafe` | Moyen |
| Shell exec | commandes shell | Faible |
| File read/write | `file read`, `file write` | Faible |
| Search / extract | `search`, `webpage_extract` | Moyen |
| MCP tool call | `manus-mcp-cli tool call` | Moyen-Élevé |
| LLM inference | chaque tour de réponse agent | Élevé |
| Map parallel | outil `map` × N sous-tâches | Élevé × N |

### Step 2 — Identifier les patterns de gaspillage (W1-W7)

**W1 — Boucles d'exploration** : Plusieurs itérations browser/shell pour découvrir une structure DOM ou API qui aurait pu être lue en 1 action.

**W2 — Retries échoués** : Même action répétée 3+ fois avec variations mineures → changer de stratégie après le 2e échec.

**W3 — Navigation redondante** : `browser_navigate` vers la même URL plusieurs fois dans la même phase.

**W4 — Contexte surdimensionné** : Lecture de fichiers/pages entiers quand seule une section était nécessaire (utiliser `range` ou `grep`).

**W5 — Séquentiel au lieu de parallèle** : N tâches indépendantes similaires faites une par une au lieu d'utiliser l'outil `map`.

**W6 — Modèle premium pour tâche simple** : Inférence LLM utilisée pour du formatage, copy-paste ou lookup.

**W7 — Snapshot sans extraction** : `browser_navigate` appelé juste pour "vérifier l'état" sans extraire de données ciblées.

### Step 3 — Rapport structuré

```
## Session Cost Audit

### Comptage actions
[tableau : catégorie | count | poids]

### Coût total estimé
[Minimal / Faible / Moyen / Élevé / Très élevé] — [N actions totales]
Équivalent crédit Manus estimé : [X-Y crédits] (fourchette relative)

### Gaspillages identifiés
[flags W1-W7 avec exemples concrets de la session]

### Suggestions d'optimisation
[liste numérotée : pattern → correction → économie estimée %]

### Estimation replay optimisé
Si la session était rejouée avec ces optimisations : [X% moins d'actions]
Gain crédit estimé : [X-Y crédits économisés]
```

---

## Mode OPTIMIZE — Évaluation avant exécution

Quand l'utilisateur soumet une tâche à venir, évaluer AVANT d'exécuter :

### Grille d'évaluation

| Dimension | Question | Impact |
|---|---|---|
| Clarté | La demande est-elle précise ? (score 1-10) | Score < 5 → clarifier d'abord |
| Scope | Peut-on découper en sous-tâches atomiques ? | Oui → découper + router chaque partie |
| Données | Faut-il des données temps réel ? | Oui → search d'abord, LLM ensuite |
| Parallélisme | Y a-t-il N tâches homogènes indépendantes ? | Oui → outil `map` |
| Modèle | La tâche nécessite-t-elle un raisonnement profond ? | Non → Standard, pas Premium |

### Output Mode OPTIMIZE

```
## Plan optimisé pour : [titre tâche]

### Coût estimé sans optimisation : [X crédits]
### Coût estimé avec optimisation : [Y crédits]
### Économie projetée : [Z%]

### Plan d'exécution optimisé
[étapes numérotées avec outil recommandé pour chaque étape]

### Risques identifiés
[ce qui pourrait faire déraper le plan + mitigation]
```

---

## Échelle de référence crédit Manus

| Profil session | Actions typiques | Niveau coût | Crédits estimés |
|---|---|---|---|
| Q&A / chat simple | < 10 | Minimal | 1-3 |
| Tâche outil unique | 10-30 | Faible | 3-8 |
| Workflow multi-étapes | 30-80 | Moyen | 8-20 |
| Automation complexe | 80-200 | Élevé | 20-50 |
| Boucle debug intensive | 200+ | Très élevé | 50+ |

> Les crédits Manus ne sont pas exposés directement — ces fourchettes sont des estimations relatives calibrées sur des sessions réelles.

---

## Règles d'exécution

- Ne jamais inventer de chiffres exacts — toujours des fourchettes relatives
- Prioriser les suggestions par impact décroissant
- Si le contexte est compressé/tronqué, le signaler comme limitation
- En Mode OPTIMIZE : produire le plan AVANT de demander confirmation d'exécution
