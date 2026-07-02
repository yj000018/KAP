# SESSION SCRATCHPAD — Règles Temporaires à Repositionner

**Sprint:** KAP-ARCH-1
**Date:** 2026-07-02
**Statut:** TEMPORAIRE — à repositionner dans les bons registres après validation

> Ce fichier capture les règles opérationnelles découvertes pendant ce sprint.
> Il doit être vidé et repositionné dans les registres canoniques (Tool Registry, Runbook, Protocol Registry) après revue Architecte.

---

## 🔧 My Browser — Règles Opérationnelles

| Règle | Détail | Destination finale |
|---|---|---|
| **Chrome uniquement** | My Browser ne fonctionne qu'avec Chrome sur Mac. Brave, Safari, Firefox = non supportés. | Tool Registry / Runbook Archive Pipeline |
| **Mac uniquement** | My Browser nécessite le navigateur Mac authentifié. iOS = session perdue. Sandbox VM = session perdue. | Runbook Archive Pipeline §CRITICAL |
| **Session Manus authentifiée** | La session Manus doit être active dans Chrome Mac avant d'utiliser My Browser. | Runbook Archive Pipeline |
| **Scroll manuel requis** | La sidebar Manus utilise du virtual scrolling. Pour charger toutes les sessions, l'utilisateur doit scroller manuellement jusqu'en bas dans Chrome Mac, puis dire "prêt". | Runbook Archive Pipeline §Mode C |
| **Extraction JS post-scroll** | Après scroll complet, lancer extraction JS via browser_view + console pour récupérer tous les UIDs et titres. | Runbook Archive Pipeline §Mode C |
| **Playwright sandbox = impossible** | Playwright Python dans le sandbox ne peut pas contrôler My Browser (pas de port CDP exposé). | Runbook Archive Pipeline §Blockers |

---

## 📋 Archive Pipeline — Règles Opérationnelles

| Règle | Détail | Destination finale |
|---|---|---|
| **Marqueur archivage** | `[✓] ` en préfixe du titre Manus = session archivée. Vérifier début ET fin du titre. | Runbook Archive Pipeline §Deduplication |
| **Titre Manus = jamais modifié** | Seul le préfixe `[✓] ` est ajouté. Le titre original est conservé intégralement. | Runbook Archive Pipeline §Title Rules |
| **Format fichier** | `{uid}_factsheet.md` — 3 couches : YAML metadata + Session Card + Verbatim Archive | Runbook Archive Pipeline §Output Format |
| **Déduplication** | Vérifier existence `{uid}_factsheet.md` ET présence `[✓]` dans le titre avant tout traitement. | run_pipeline_enhanced.py |
| **LLM** | Utiliser le proxy sandbox intégré (claude-sonnet-4-6). Ne pas utiliser de clés API externes. | run_pipeline_enhanced.py |
| **API Manus task.list** | Limite à ~200 tâches récentes. Ne peut pas remonter avant juin 2026 via pagination. | Runbook Archive Pipeline §API Limits |
| **API Manus listMessages** | Ne fonctionne que pour les sessions du même compte API. Les sessions anciennes retournent 404. | Runbook Archive Pipeline §API Limits |

---

## 🗂️ Registres Existants à Consulter

| Registre | Localisation | Statut |
|---|---|---|
| Tool Registry (yOS) | Notion DS: 76236561-0572-46bd-861b-636e61898921 | Actif — non chargé dans ce sprint |
| Source State Registry | WP1-R/02_SOURCE_REGISTRY/ | Actif — 15 branches |
| Connector Backlog | WP1-R/02_SOURCE_REGISTRY/KAP-WP1-R-Connector-Backlog.md | Actif |
| Archive Pipeline Runbook | scripts/kap_session_archive/RUNBOOK-KAP-Archive-Pipeline.md | Actif — à mettre à jour avec règles My Browser |
| CHATGPT Guardian Architect | 00_Infrastructure/Team_OS/Agents/CHATGPT-Guardian-Architect.md | Actif |

---

## ⚠️ À Faire Après Ce Sprint

1. Repositionner les règles My Browser dans le Runbook Archive Pipeline (§CRITICAL)
2. Ajouter règle "Chrome Mac uniquement" dans le Tool Registry yOS
3. Mettre à jour le Connector Backlog avec le statut réel de My Browser
4. Vider ce scratchpad après repositionnement
