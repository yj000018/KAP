---
source_id: KAP-WP2-M6C-Manus_Memory_Hub-38135e21
notion_page_id: 38135e21-8cf8-81af-89eb-ea97a184dc2a
notion_database_id: 533401fa-1702-4d9d-a60e-5433cac72fe1
title: "📚 MASTER — Export Session vers Notion (Fusionné)"
database_name: Manus_Memory_Hub
acquired_at: 2026-07-01T19:03:19Z
acquisition_method: Notion_Blocks_API_v1
canonical_status: not_canonical
limitations: block_content_only_no_media_downloads
---

# 📚 MASTER — Export Session vers Notion (Fusionné)

**Page ID:** `38135e21-8cf8-81af-89eb-ea97a184dc2a`  
**Database:** Manus_Memory_Hub  
**Created:** 2026-06-16  
**Last Edited:** 2026-06-16  

## Properties

- **Priorite:** Moyenne
- **Statut:** Archive
- **Type:** Conversation Archive
- **Name:** 📚 MASTER — Export Session vers Notion (Fusionné)

## Content


# Résumé Exécutif

Session de documentation du workflow d'export de sessions Manus vers Notion. Deux modes disponibles (Archive simple et Archive + Fusion), diagnostic d'IDs obsolètes, et création de la base Manus Memory Hub.


# Points Clés

- Workflow 1 — Archive simple : commande Archive cette conversation, crée une entrée Notion Conversation Archive avec résumé, ToC, points clés, décisions, actions, transcript.
- Workflow 2 — Archive + Fusion : pour plusieurs sessions liées, workflow CLOSE + fusion en MASTER SESSION via fusion_engine.py, export Notion avec cross-références.
- Contrainte : renommage de session dans l'UI Manus est manuel, l'export Notion est entièrement automatisé.

# Décisions Prises

- Créer la base Manus Memory Hub dans le workspace yONE sous la page yOS.
- Data Source ID actif : 94086d51-ac40-4027-b994-55c5681f72e5
- YOS Archives conservé comme fallback.

# Sources Fusionnées

- [2026-03-03] Export Session vers Notion (v1 — YOS Archives) — Archivé
- [2026-03-03] Export Session vers Notion (v2 — Manus Memory Hub) — Archivé