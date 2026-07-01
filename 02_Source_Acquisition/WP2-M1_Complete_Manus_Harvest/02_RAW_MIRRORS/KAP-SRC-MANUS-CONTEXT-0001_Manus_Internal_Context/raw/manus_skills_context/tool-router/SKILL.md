---
name: tool-router
description: "Routing intelligent des outils Y-OS — MCP, API, connecteurs. MUST read before choosing any tool, connector, API or MCP in a Y-OS session. Covers search/web, LLM, memory, code, automation, project management, design, CRM. Prevents redundant tool use and ensures optimal routing decisions."
---

# Tool Router — Y-OS

Avant tout choix d'outil, connecteur, MCP ou API dans une session Y-OS : lire ce skill.

**Playbook complet (source de vérité) :** https://app.notion.com/p/35435e218cf88145ac11c5c082b4290b

---

## RÈGLE FONDAMENTALE

> Avant d'utiliser un outil, vérifier : existe-t-il déjà un connecteur actif qui couvre ce besoin à 80% ? Si oui, utiliser le connecteur existant. Si non, choisir selon la matrice ci-dessous.

---

## MATRICE DE ROUTAGE RAPIDE

### Recherche web
| Intention | Outil |
|-----------|-------|
| Question factuelle récente | **Perplexity** |
| Extraire contenu d'une URL | **Firecrawl** |
| Site bloqué / JS dynamique | **Playwright** → Bright Data* |
| Scraping industriel >1k pages | **Bright Data*** |

### LLM
| Intention | Outil |
|-----------|-------|
| Tâche principale | **Anthropic** (natif Manus) |
| Analyse image/vision | **OpenAI GPT-4o** |
| Document >200 pages | **Gemini 2.5** (2M context) |
| Veille Twitter/X | **Grok** |
| Batch >100 req / coût optimisé | **OpenRouter** |

### Mémoire & Connaissance
| Intention | Outil |
|-----------|-------|
| Stocker décision structurée | **Notion** (KMM) |
| Mémoriser contexte auto cross-sessions | **Mem0** |
| Docs techniques live versionnées | **Context7** (via UPSTASH) |

### Code & Dev
| Intention | Outil |
|-----------|-------|
| Repos, issues, PRs, CI/CD | **GitHub MCP (PAT)** |
| DB Postgres, schema, RLS | **Supabase** |

### Automation
| Intention | Outil |
|-----------|-------|
| Workflow complexe / logique conditionnelle | **n8n** (self-hosted) |
| Intégration rapide 2 apps cloud | **Zapier** |
| Workflow LLM natif | **Dify** |

### Projet & Tâches
| Intention | Outil |
|-----------|-------|
| Issue dev / bug / sprint | **Linear** |
| Tâche personnelle | **Todoist** |

### Design & Création
| Intention | Outil |
|-----------|-------|
| Design visuel, templates | **Canva** |
| Vidéo avatar IA | **HeyGen** |
| TTS expressif | **Hume** |
| Génération multimodale | **MiniMax** |

### CRM & Data
| Intention | Outil |
|-----------|-------|
| CRM contacts, deals | **HubSpot** |
| Base de données flexible | **Airtable** |
| Formulaires | **Jotform** |

---

## CUSTOM MCP À CONFIGURER (non natifs Manus)

Ces outils nécessitent une configuration via Settings > Connectors > Add Custom MCP :

| Outil | Commande npx | Prérequis |
|-------|-------------|----------|
| Sequential Thinking | `npx -y @modelcontextprotocol/server-sequential-thinking` | Aucun |
| Task Master | `npx -y task-master-ai` | Clé API LLM |
| Figma Context | `npx -y figma-developer-mcp` | Token API Figma |
| Bright Data | `npx -y @brightdata/mcp` | Clé API Bright Data |
| Tableau | `npx -y @tableau/tableau-mcp` | Licence Tableau |

---

## CONNECTEURS EN MODE BACKUP

> **Règle** : Ne jamais désactiver définitivement un connecteur redondant. Le reclasser en BACKUP ou CAS SPÉCIFIQUE — il peut être utile dans des situations précises non couvertes par le connecteur principal.

| Connecteur | Connecteur principal | Cas BACKUP / usage spécifique |
|------------|---------------------|-------------------------------|
| My Browser | Playwright | Login manuel, CAPTCHA, interaction humaine requise |
| ClickUp | Linear + Notion | Client ou équipe externe déjà sur ClickUp |
| Asana | Linear + Notion | Intégration avec écosystème Asana existant |
| monday.com | Linear + Notion | Reporting visuel pour parties prenantes non-tech |
| Wix | Webflow | Sites clients déjà hébergés sur Wix |
| Make | n8n + Zapier | Scénarios visuels à partager avec non-développeurs |

---

## PROTOCOLE D'AJOUT D'UN NOUVEAU CONNECTEUR

1. **Vérifier** : ce besoin est-il déjà couvert à 80% par un connecteur actif ?
2. **Classifier** : MCP natif Manus / Custom MCP / API directe / Browser Extension / Agent spécialisé ?
3. **Si absent du catalogue natif** → configurer via Custom MCP
4. **Analyser les redondances** : quel connecteur existant se chevauche ?
5. **Reclasser** les connecteurs redondants en BACKUP avec leur cas d'usage spécifique — ne jamais désactiver définitivement
6. **Mettre à jour** ce skill + le Playbook Notion (source de vérité)

---

## RÈGLE INTER-LLM

Ce Playbook est la référence universelle Y-OS. Tout LLM opérant dans Y-OS (Manus, Claude, GPT, Gemini, Grok) doit consulter le Playbook Notion avant de choisir un outil. Mis à jour bimensuellement avec le RADAR-MCP.
