---
name: llm-router
description: "Routage intelligent des requêtes vers le LLM optimal (auto ou semi-auto avec confirmation). Inclut la stratégie de pricing fournisseurs - OpenRouter pour les modèles à poids ouverts (Kimi K2.6, Llama, DeepSeek, Qwen), API directe pour les modèles fermés (GPT, Claude, Gemini). Use when routing LLM requests, choosing between OpenRouter and direct API, or configuring Kimi K2.6 access."
---

# Skill: LLM Router

## Description

Cette skill analyse les requêtes de l'utilisateur pour déterminer le Grand Modèle de Langage (LLM) le plus adapté à la tâche. Elle peut fonctionner en mode entièrement automatique ou en mode semi-automatique, qui demande une confirmation avant de router la requête vers un modèle spécifique.

## Objectif

Optimiser la qualité des réponses et l'efficacité des coûts en utilisant le LLM le plus pertinent pour chaque type de tâche, tout en offrant à l'utilisateur le contrôle sur le choix final du modèle.

## Architecture et Logique

Le processus de routage se déroule en plusieurs étapes clés :

1.  **Analyse de l'Intention** : La skill intercepte la requête de l'utilisateur et effectue une méta-analyse pour en classifier l'intention principale. Les catégories incluent, sans s'y limiter : la recherche web, la génération de code, l'analyse de données, la créativité, ou le raisonnement complexe.

2.  **Critères de Sélection** : Une matrice de décision est utilisée pour associer l'intention détectée au LLM le plus performant pour cette catégorie. Cette matrice prend en compte les forces et faiblesses connues de chaque modèle disponible via API.

    | Catégorie de Tâche | LLM Recommandé | Justification |
    | :--- | :--- | :--- |
    | Recherche temps réel, actualités | `Perplexity (sonar-pro)` | Spécialisé dans la recherche web avec citations. |
    | Génération/Analyse d'images, multimodal | `Google (gemini-2.5-flash)` | Capacités de vision avancées. |
    | Génération de code, logique complexe | `OpenAI (gpt-5)` | Leader pour le raisonnement et la programmation. |
    | Tâches créatives, longs documents | `Anthropic (claude-3-opus)` | Contexte étendu et finesse d'écriture. |
    | Requêtes non structurées, conversation | `Grok (grok-4)` | Approche conversationnelle et base de connaissances unique. |
    | Tâche par défaut, équilibrée | `Anthropic (claude-3.7-sonnet)` | Excellent rapport performance/coût. |

3.  **Modes de Fonctionnement** :
    *   **`semi-auto` (par défaut)** : Après avoir sélectionné un LLM, la skill formule une recommandation à l'utilisateur via l'outil `message`. Elle explique pourquoi un certain modèle a été choisi et attend une confirmation. L'utilisateur peut accepter, refuser (et rester sur le modèle par défaut), ou suggérer un autre modèle.
    *   **`auto`** : Si l'utilisateur a activé ce mode, la skill exécute directement la requête avec le LLM sélectionné, sans étape de confirmation. Ce mode privilégie la vitesse et l'autonomie.

4.  **Exécution** : Une fois le LLM finalisé (par confirmation ou en mode auto), la skill construit et exécute l'appel API correspondant, en passant la requête de l'utilisateur. La réponse est ensuite retournée à l'utilisateur.

## Provider Pricing Strategy

La stratégie de tarification et de routage des fournisseurs LLM obéit à une règle stricte d'optimisation des coûts :

> **Règle clé :** OpenRouter est moins cher **UNIQUEMENT** pour les modèles à poids ouverts (ex. Kimi K2.6, Llama, DeepSeek, Qwen) où plusieurs hébergeurs cloud sont en concurrence sur les prix. Pour les modèles fermés/propriétaires (GPT-5.5, Claude, Gemini), OpenRouter agit comme un revendeur transparent facturant le tarif du fournisseur PLUS des frais de plateforme de 5,5 % — ce qui le rend ~5,5 % PLUS cher qu'un accès API direct. Manus n'est PAS disponible sur OpenRouter car c'est un SaaS grand public basé sur des crédits, et non un modèle API.

| Type de Modèle | OpenRouter | API Directe | Recommandation |
| :--- | :--- | :--- | :--- |
| **Poids ouverts** (Kimi, Llama, DeepSeek) | Moins cher (concurrence des hébergeurs) | Plus cher | Utiliser OpenRouter pour optimiser les coûts |
| **Fermés** (GPT-5.5, Claude, Gemini) | Tarif fournisseur + frais de 5,5 % | Tarif de base | Utiliser l'API Directe pour éviter les frais |
| **Manus** | N/A | SaaS basé sur crédits uniquement | Utiliser Manus.im directement |

*Note : Pour une utilisation à haut volume de modèles à poids ouverts (ex. >10M tokens de sortie/mois), OpenRouter peut générer 30 à 50 % d'économies. Pour les modèles fermés, la prime de 5,5 % n'est justifiée que si une facturation unifiée, un routage de basculement (failover) ou des politiques de non-conservation des données (zero-data-retention) sont requis.*

## Implémentation

La logique de cette skill est implémentée dans le script Python `/home/ubuntu/skills/llm-router/router.py`. Ce script centralise les appels aux différentes APIs LLM et peut être invoqué directement par Manus ou via CLI pour tests.

## Usage

### Commandes utilisateur

*   `"Mode routeur auto"` ou `"Passe le routeur LLM en mode automatique"` → Active le mode automatique
*   `"Mode routeur semi-auto"` ou `"Active la confirmation pour le choix du LLM"` → Active le mode semi-automatique (défaut)
*   `"Utilise [GPT-5/Gemini/Grok/etc.] pour cette requête"` → Override ponctuel du modèle sélectionné
*   `"Pourquoi ce modèle ?"` → Affiche la justification du choix de routage

### Test CLI

```bash
# Routage automatique avec analyse
python3 /home/ubuntu/skills/llm-router/router.py "Quelle est l'actualité en IA ?"

# Override manuel du modèle
python3 /home/ubuntu/skills/llm-router/router.py "Écris un poème" grok
```

### Configuration

Le mode de fonctionnement est stocké dans `/home/ubuntu/skills/llm-router/config.json` :

```json
{
  "mode": "semi-auto"
}
```

Pour modifier :

```bash
# Passer en mode auto
echo '{"mode": "auto"}' > /home/ubuntu/skills/llm-router/config.json
```

## Dépendances

**Packages Python** (déjà installés) :
- `requests`
- `google-genai`
- `openai`
- `anthropic`
- `xai-sdk`

**Variables d'environnement** (déjà configurées) :
- `SONAR_API_KEY` (Perplexity)
- `GEMINI_API_KEY` (Google)
- `OPENAI_API_KEY` (OpenAI)
- `XAI_API_KEY` (Grok)
- `ANTHROPIC_API_KEY` (Claude)
- `OPENROUTER_API_KEY` (OpenRouter — poids ouverts : Kimi K2.6, Llama, DeepSeek, Qwen)

## Extension

Pour ajouter une nouvelle catégorie de tâche ou un nouveau LLM, consulter le fichier `/home/ubuntu/skills/llm-router/README.md` qui contient les instructions détaillées.

## Gouvernance

**Propriétaire** : Yannick (Y-OS)  
**Créé** : 2026-02-08  
**Mis à jour** : 2026-06-25  
**Version** : 1.1  
**Statut** : Opérationnel  
**Changelog** : v1.1 — Ajout OpenRouter comme fournisseur, routage Kimi K2.6 / Llama / DeepSeek / Qwen, section Provider Pricing Strategy
