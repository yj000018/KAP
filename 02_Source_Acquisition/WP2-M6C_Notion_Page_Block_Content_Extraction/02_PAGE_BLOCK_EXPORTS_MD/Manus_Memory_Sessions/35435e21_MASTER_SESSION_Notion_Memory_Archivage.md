---
source_id: KAP-WP2-M6C-Manus_Memory_Sessions-35435e21
notion_page_id: 35435e21-8cf8-818a-b330-df4161d24eac
notion_database_id: 5e51ded4-0b46-4a68-acc2-4e90886a2499
title: "📚 MASTER SESSION — Notion Memory & Archivage"
database_name: Manus_Memory_Sessions
acquired_at: 2026-07-01T19:03:19Z
acquisition_method: Notion_Blocks_API_v1
canonical_status: not_canonical
limitations: block_content_only_no_media_downloads
---

# 📚 MASTER SESSION — Notion Memory & Archivage

**Page ID:** `35435e21-8cf8-818a-b330-df4161d24eac`  
**Database:** Manus_Memory_Sessions  
**Created:** 2026-05-02  
**Last Edited:** 2026-06-16  

## Properties

- **Language:** fr
- **Project:** yOS
- **Date:** 2026-05-02
- **Themes:** Notion, mémoire, archivage, accès, workflow
- **Depth:** substantial
- **Title:** 📚 MASTER SESSION — Notion Memory & Archivage

## Content


## Vision

Système de mémoire persistante dans Notion : archiver, retrouver et injecter le contexte des sessions Manus pour la continuité cognitive.


## État actuel (2026-05-02)

Base Sessions opérationnelle (200+ entrées). Workflow d'archivage défini. Accès MCP Notion configuré.


## Structure Notion

- Manus Memory Sessions : 5e51ded4-0b46-4a68-acc2-4e90886a2499
- Manus Memory Hub : 533401fa-1702-4d9d-a60e-5433cac72fe1
- yOS Memory Inbox : 938332ff-ed1d-4965-8...
- YOS Memory Project Registry : 32935e21-8cf8-8158-9b23-cb4e17486a1f

## Procédure d'accès

1. Utiliser notion MCP avec notion-search ou notion-fetch
1. Charger via /hydrater skill au démarrage de session
1. Archiver via /memoriser ou /session-synthesis

## Décisions clés

- Notion = SSOT unique pour la mémoire
- Pages publiques par défaut
- Accès MCP universel (pas de browser spécifique)

## Prochaines étapes

1. Automatiser l'archivage quotidien
1. Améliorer la recherche sémantique
1. Créer des vues filtrées par projet

## Sessions sources (8+)

How to Access Notion Page x8, Regrouper sessions disparates (actuelle).


## Protocole de continuation

Au démarrage : charger cette Master Session pour le workflow mémoire complet.

---

## Consolidation KM (2026-06-16)


### Workflows d'Export Session (fusionné)

- Archive simple : commande Archive cette conversation → entrée Notion Conversation Archive
- Archive + Fusion : workflow CLOSE + fusion en MASTER SESSION via fusion_engine.py
- Contrainte : renommage session UI Manus = manuel (API PUT non supportée)
- YOS Archives = fallback si Memory Hub indisponible
- Data Source ID actif : 94086d51-ac40-4027-b994-55c5681f72e5

### KM Hub — Règle de maintenance

- Viser < 10 entrées actives en permanence
- Archiver (Statut = Archive) toute entrée absorbée dans un MASTER
- Ne jamais supprimer définitivement

### Sessions sources archivées

- Export Session vers Notion v1, v2, v3 → Archivé
- MASTER SESSION Fusion x3 → Archivé
- Test Export → Archivé