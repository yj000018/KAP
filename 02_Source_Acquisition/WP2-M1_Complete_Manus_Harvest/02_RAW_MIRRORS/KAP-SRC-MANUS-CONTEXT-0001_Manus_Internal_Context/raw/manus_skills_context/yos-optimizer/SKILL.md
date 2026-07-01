---
name: yos-optimizer
description: "Y-OS Optimizer — orchestrateur central d'optimisation. MUST read on EVERY user prompt (not just the first). Auto-activates systematically to apply credit-optimizer guardrails, K/T/P/M/L/O rules, and routing decisions. Receives /optimize [mode?] or auto-deduces mode from context. Orchestrates prompt-optimizer (double pass), llm-router, tool-router, and memory-router (future). Produces comparative cost report when mode is not specified. Includes K-rules, T-rules, LLM/tool/memory/prompt routing."
---

# Y-OS Optimizer v2.1

Orchestrateur central d'optimisation Y-OS. Deux couches :
1. **`credit-optimizer`** (module externe acheté) — baseline toujours actif, 10 règles d'or, 30-75% d'économie Manus
2. **Y-OS layer** (ce skill) — routage LLM/outil/mémoire, réécriture prompt, règles K+T, rapport coût comparatif

---

## Déclenchement

### ⚡ Activation systématique — CHAQUE prompt

Ce skill s'active automatiquement sur **chaque prompt utilisateur** de la session, pas seulement le premier. L'objectif : appliquer les garde-fous, règles K/T/P/M/L/O, et le routage optimal en continu.

**Workflow par prompt :**
1. Lire ce skill (si pas déjà en contexte actif — cf. T9)
2. Évaluer complexité + type
3. Appliquer le mode (déduit ou explicite)
4. Exécuter avec les règles actives

### Mode léger (auto-appliqué si tâche simple) :
- Simple Q&A / chat conversationnel → appliquer T-rules + K-rules uniquement (pas de routing LLM/outil)
- Tâche < 5 actions estimées → appliquer rules + routing léger (pas de rapport coût)
- Coût estimé < 20 crédits → pas de rapport coût sauf demande explicite

### Mode complet (auto-appliqué si tâche complexe) :
- Browser automation / Playwright
- Appels API multiples
- Génération de code > 30 lignes
- Recherche multi-sources
- Traitement de documents longs
- Tâches parallèles
- Toute tâche avec `/optimize`

### Commandes explicites
```
/optimize              → déduit le mode automatiquement
/optimize performance  → mode performance sans interruption
/optimize economy      → mode economy sans interruption
/optimize balanced     → mode balanced (défaut explicite)
/optimize mode         → affiche le mode déduit sans exécuter
```

---

## Modes

### PERFORMANCE
> Meilleure qualité raisonnable. Pas l'extrême absolu — la meilleure approche mesurée.

- **LLM** : Claude Opus 4 ou Gemini 2.5 Pro via API directe (BYOK Anthropic/Google)
- **Outils** : Playwright MCP, MCP complets, scripts Python si nécessaire
- **Mémoire** : contexte profond — Notion + Mem0 + sessions récentes
- **Prompt** : enrichi, structuré, directives LLM/outil explicites
- **Scripts** : génération autorisée si gain réel
- **Rapport coût** : affiché en sortie (pas avant)

### ECONOMY
> Bonne qualité à coût minimal. Efficace et direct, pas médiocre.

- **LLM** : Gemini Flash (gratuit tier) ou modèle OpenRouter léger via BYOK
- **Outils** : Firecrawl, shell, `webpage_extract`, sans browser
- **Mémoire** : résumé seul, 0 appel externe si possible
- **Prompt** : simplifié, scope réduit, boucles supprimées
- **Scripts** : évités sauf si indispensables
- **Rapport coût** : affiché en sortie

### BALANCED (défaut)
> Ratio qualité/coût optimal. Comportement standard Y-OS.

- **LLM** : Claude Sonnet ou Gemini 2.5 Flash via BYOK
- **Outils** : mix selon contexte, Playwright si vraiment nécessaire
- **Mémoire** : contexte pertinent uniquement (Mem0 cross-session + Notion si projet actif)
- **Prompt** : clarifié et structuré
- **Scripts** : si gain > 3x sur actions manuelles
- **Rapport coût** : uniquement si écart > 2x avec alternative

---

## Workflow d'exécution (7 étapes)

```
1. ANALYSE
   - Score complexité (1-10)
   - Type : chat / code / research / browser / generation / automation
   - Mode explicite ? → utiliser | Absent ? → déduire

2. DÉDUCTION DE MODE (si absent)
   - Tâche longue + contexte riche + outils multiples → performance
   - Tâche simple + deadline implicite + scope clair → economy
   - Défaut → balanced

3. PASSE 1 — PROMPT-OPTIMIZER (réécriture selon mode)
   - performance : enrichir, structurer, clarifier l'intention, ajouter critères
   - economy     : simplifier, réduire scope, supprimer boucles et complexité inutile
   - balanced    : clarifier et structurer

4. ROUTING
   - llm-router  → choisit LLM selon mode + type tâche
   - tool-router → choisit outils selon mode
   - memory-router (futur) → quantité mémoire selon mode

5. PASSE 2 — PROMPT-OPTIMIZER (enrichissement final avec directives)
   - Injecte : "Utilise Claude via API pour cette analyse"
   - Injecte : "Utilise Playwright pour l'automatisation"
   - Injecte : "Contexte projet rapatrié depuis Notion : [résumé]"
   - performance : prompt complet avec toutes les directives
   - economy     : prompt minimal, directives légères uniquement

6. EXÉCUTION
   - Mode spécifié → exécuter directement, rapport coût en sortie
   - Mode déduit  → exécuter, mentionner le mode choisi

7. RAPPORT COÛT (si mode non spécifié ou écart > 2x)
   ┌─────────────────────────────────────────┐
   │ Mode sélectionné : balanced             │
   │ LLM  : Claude Sonnet (BYOK Anthropic)   │
   │ Outils : Playwright + Firecrawl         │
   │ Coût estimé : 25-40 crédits Manus       │
   ├─────────────────────────────────────────┤
   │ Alternative economy disponible :        │
   │   LLM : Gemini Flash (BYOK, gratuit)    │
   │   Outils : Firecrawl + shell            │
   │   Coût estimé : 8-15 crédits Manus      │
   │   Delta qualité estimé : -20%           │
   └─────────────────────────────────────────┘
```

---

## Garde-fous browser (hérités credit-optimizer + Y-OS)

- Jamais de boucle exploratoire > 3 itérations sans résultat
- Jamais de `browser_navigate` pour reset un état → utiliser JS direct
- Jamais de snapshot répété sans changement d'état
- Abandon après 2 échecs d'auth → escalade immédiate
- Tâches indépendantes → paralléliser via shell background `&`
- DOM inconnu → 1 seul `page.evaluate(innerHTML)` complet avant tout script

---

## Règles Y-OS — toujours actives (tous modes)

### K1-K5 — Règles profil utilisateur

- **K1 — Autonomie max** : explorer 2 alternatives avant d'escalader à l'utilisateur
- **K2 — Dépenses** : jamais sans autorisation explicite (API payantes, achats, webhooks)
- **K3 — Secrets** : Manus Secrets + 1Password uniquement — jamais copy-paste manuel
- **K4 — Erreurs réseau** : retry immédiat ×2 → attente 1min → attente 5min → escalade
- **K5 — Gros volumes** : split systématique en phases, jamais compresser le contexte

### T-Rules — Économie de tokens Y-OS (identifiées sur sessions réelles)

- **T1 — Lire avant d'explorer** : lire doc/DOM/API en 1 appel complet avant toute interaction. Jamais découvrir en live par itérations.
- **T2 — `range` systématique** : fichier > 100 lignes → `range` ou `grep` ciblé. Jamais `cat` complet si seule une section est nécessaire.
- **T3 — Messages intermédiaires télégraphiques** : `info` = 1-2 lignes max. Richesse typographique réservée aux `result` finaux.
- **T4 — Plan avant code** : tâche > 30 lignes → plan 5 lignes d'abord. Évite les rewrites coûteux.
- **T5 — 1 snapshot par phase logique** : browser automation → 1 seul snapshot par phase. Jamais début ET fin d'une même micro-action.
- **T6 — Sauvegarder l'état entre phases** : à chaque changement de phase majeur, écrire l'état dans un fichier. Référencer le fichier, pas le contenu inline.
- **T7 — Paralléliser les recherches** : > 2 URLs → `map` ou `webpage_extract` multi-URLs en 1 appel. Jamais séquentiel.
- **T8 — Abandon rapide** : 2 échecs avec même stratégie → switcher immédiatement. Jamais une 3e tentative identique.
- **T9 — Ne pas relire les skills déjà en contexte** : vérifier si le skill est déjà actif avant de le relire.
- **T10 — Output shell ciblé** : toujours `| head -N` ou `| grep pattern`. Jamais output illimité.

### P-Rules — Optimisation prompt (identifiées sur sessions réelles)

- **P1 — Contexte projet automatique** : pour toute tâche liée à un projet connu (ARCHETYPES, Y-OS, etc.), injecter automatiquement le contexte depuis Mem0 sans que l'utilisateur le demande.
- **P2 — Intention avant tâche** : si le prompt est ambigu (score clarté < 6/10), poser 1 seule question ciblée avant d'exécuter. Jamais plusieurs questions.
- **P3 — Scope explicite** : tout prompt réécrit doit inclure un critère de succès mesurable ("résultat attendu : X").
- **P4 — Directives LLM en fin de prompt** : les directives d'exécution (quel LLM, quel outil) vont en fin de prompt réécrit, pas au début.
- **P5 — Prompt economy = suppression des boucles** : en mode economy, identifier et supprimer explicitement les instructions qui génèrent des boucles (ex: "cherche partout", "vérifie tout", "assure-toi que").

### M-Rules — Optimisation mémoire (futur memory-router)

- **M1 — Performance** : charger Notion (projet actif) + Mem0 (cross-session) + résumé session courante
- **M2 — Economy** : contexte inline uniquement, 0 appel externe
- **M3 — Balanced** : Mem0 uniquement si projet connu, sinon contexte inline
- **M4 — Jamais charger > 3 sources mémoire simultanément** : synthétiser avant d'injecter

### L-Rules — Routage LLM par mode et type de tâche

| Type de tâche | Economy | Balanced | Performance |
|---|---|---|---|
| Analyse texte court | Manus natif | Manus natif | Claude Sonnet (BYOK) |
| Analyse texte long (> 50k tokens) | Gemini Flash (BYOK) | Gemini 2.5 Flash (BYOK) | Gemini 2.5 Pro (BYOK) |
| Raisonnement complexe | Manus natif | Claude Sonnet (BYOK) | Claude Opus (BYOK) |
| Recherche web temps réel | Perplexity (BYOK) | Perplexity (BYOK) | Perplexity Pro (BYOK) |
| Génération code | Manus natif | Manus natif | Claude Sonnet (BYOK) |
| Vision / images | Gemini Flash (BYOK) | Gemini 2.5 Flash (BYOK) | GPT-4o (BYOK OpenAI) |
| Multi-modèles / fallback | OpenRouter léger | OpenRouter mid | OpenRouter premium |

### O-Rules — Routage outils par mode

| Besoin | Economy | Balanced | Performance |
|---|---|---|---|
| Web scraping | `webpage_extract` | `webpage_extract` + Firecrawl | Firecrawl + Playwright |
| Browser automation | ❌ Éviter | Playwright si indispensable | Playwright MCP complet |
| Recherche | `search` (1 query) | `search` (3 variants) | Perplexity + `search` |
| Fichiers | `file.read` avec `range` | `file.read` ciblé | `file.read` + analyse |
| Mémoire | Contexte inline | Mem0 si projet connu | Notion + Mem0 + session |
| Notifications | ❌ Skip | Owner notify si critique | Notify + log |

---

## Intégration avec les modules existants

| Module | Rôle | Relation |
|---|---|---|
| `credit-optimizer` | Garde-fous coûts Manus (baseline externe) | Toujours actif en dessous |
| `cost` | Audit rétrospectif W1-W7 + estimation € | Appelé via `/cost` |
| `llm-router` | Table de routage LLM détaillée | Consulté pour L-Rules |
| `tool-router` | Table de routage outils détaillée | Consulté pour O-Rules |
| `prompt-optimizer` | Réécriture prompt autonome | Appelé 2x (avant + après routing) |
| `request-optimizer` | Optimisation structure + risque | Appelé si tâche complexe/risquée |
| `memory-router` | Quantité mémoire selon mode | Futur — M-Rules en attendant |

---

## Gouvernance

**Propriétaire** : Yannick (Y-OS)
**Version** : 2.1
**Créé** : 2026-05-26
**Mis à jour** : 2026-05-27
**Changelog** : v2.1 — Activation systématique sur chaque prompt (plus de skip complet)
**Statut** : Opérationnel
**Dépendances** : credit-optimizer, llm-router, tool-router, prompt-optimizer, request-optimizer
