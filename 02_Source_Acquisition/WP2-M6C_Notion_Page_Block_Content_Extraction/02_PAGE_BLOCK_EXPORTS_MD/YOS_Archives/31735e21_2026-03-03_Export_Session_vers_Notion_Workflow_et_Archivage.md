---
source_id: KAP-WP2-M6C-YOS_Archives-31735e21
notion_page_id: 31735e21-8cf8-8124-8a83-c9eab01819e5
notion_database_id: 31235e21-8cf8-8126-9212-f5a0eebadce0
title: "📝 [2026-03-03] Export Session vers Notion — Workflow et Archivage"
database_name: YOS_Archives
acquired_at: 2026-07-01T19:03:19Z
acquisition_method: Notion_Blocks_API_v1
canonical_status: not_canonical
limitations: block_content_only_no_media_downloads
---

# 📝 [2026-03-03] Export Session vers Notion — Workflow et Archivage

**Page ID:** `31735e21-8cf8-8124-8a83-c9eab01819e5`  
**Database:** YOS_Archives  
**Created:** 2026-03-02  
**Last Edited:** 2026-03-02  

## Properties

- **Tags:** yOS, architecture
- **Action:** archive
- **Keywords:** export, session, Notion, archivage, memory-manager, workflow, Archive simple, Archive + Fusion
- **Summary:** Session de documentation du workflow d'export de sessions Manus vers Notion. Yannick a demandé comment exporter une session, a reçu une explication structurée des deux modes disponibles (Archive simple et Archive + Fusion), puis a déclenché l'archivage de la session courante. La session illustre le fonctionnement complet du skill memory-manager en conditions réelles.
- **Source:** Manus
- **Title:** 📝 [2026-03-03] Export Session vers Notion — Workflow et Archivage

## Content


# Résumé Exécutif

Session de documentation du workflow d'export de sessions Manus vers Notion. Yannick a demandé comment exporter une session, a reçu une explication structurée des deux modes disponibles (Archive simple et Archive + Fusion), puis a déclenché l'archivage de la session courante. La session illustre le fonctionnement complet du skill memory-manager en conditions réelles.


# Table des Matières

1. Question initiale : comment exporter une session vers Notion
1. Réponse : deux workflows disponibles gf(Archive simple / Archive + Fusion)
1. Déclenchement de l'archivage de la session courante

# Points Clés


## Question initiale

- Yannick demande la procédure d'export d'une session vers Notion
- Manus consulte les skills session-navigator et memory-manager pour répondre avec précision

## Deux workflows disponibles

- Option 1 — Archive simple : commande "Archive cette conversation", crée une page Notion 📝 Conversation Archive avec résumé, ToC, points clés, décisions, actions, transcript
- Option 2 — Archive + Fusion : pour plusieurs sessions liées, workflow CLOSE + fusion en MASTER SESSION via fusion_engine.py, export Notion avec cross-références
- Contrainte identifiée : renommage de session dans l'UI Manus est manuel (API PUT non supportée), l'export Notion est entièrement automatisé
- Destination Notion : base 🧠 Manus Memory Hub (à créer) ou YOS Archives (existant)

## Archivage de la session courante

- Yannick déclenche "Archive cette session"
- Manus exécute le workflow complet : lecture des constantes, analyse de la session, construction du JSON, appel au script archive_conversation.py
- Diagnostic : base Memory Hub absente du workspace actuel (IDs obsolètes)
- Résolution : archivage dans YOS Archives, base native du workspace yONE

# Décisions Prises

- Utiliser YOS Archives comme destination d'archivage (Memory Hub absent du workspace)
- Mettre à jour les constantes du skill memory-manager avec les IDs corrects
- Tagger la session avec yOS et architecture

# Transcription Complète


## Échange 1 — Question initiale

Yannick : How to export a session to Notion

Manus : [Consultation des skills session-navigator et memory-manager]

Réponse structurée avec deux workflows : Archive simple (commande "Archive cette conversation") et Archive + Fusion (plusieurs sessions liées). Tableau comparatif fourni. Contrainte API PUT identifiée.


## Échange 2 — Déclenchement de l'archivage

Yannick : Archive cette session

Manus : [Exécution du workflow d'archivage]

1. Lecture des constantes memory-manager → IDs Notion obsolètes (404)
1. Recherche de la base Memory Hub dans le workspace → introuvable
1. Identification de YOS Archives comme alternative viable
1. Construction du JSON d'archive adapté au schéma YOS Archives
1. Création de l'entrée dans YOS Archives