---
source_id: KAP-WP2-M6C-Manus_Memory_Hub-31735e21
notion_page_id: 31735e21-8cf8-8164-ac2d-ce7327279c37
notion_database_id: 533401fa-1702-4d9d-a60e-5433cac72fe1
title: "📝 [2026-03-03] Export Session vers Notion — Workflow et Archivage"
database_name: Manus_Memory_Hub
acquired_at: 2026-07-01T19:03:19Z
acquisition_method: Notion_Blocks_API_v1
canonical_status: not_canonical
limitations: block_content_only_no_media_downloads
---

# 📝 [2026-03-03] Export Session vers Notion — Workflow et Archivage

**Page ID:** `31735e21-8cf8-8164-ac2d-ce7327279c37`  
**Database:** Manus_Memory_Hub  
**Created:** 2026-03-02  
**Last Edited:** 2026-03-02  

## Properties

- **Priorite:** Moyenne
- **Statut:** Archive
- **Type:** Conversation Archive
- **Tags:** yOS, systems-thinking, Manus
- **Name:** 📝 [2026-03-03] Export Session vers Notion — Workflow et Archivage

## Content


# Résumé Exécutif

Session de documentation du workflow d'export de sessions Manus vers Notion. Yannick a demandé comment exporter une session, a reçu une explication structurée des deux modes disponibles (Archive simple et Archive + Fusion), puis a déclenché l'archivage de la session courante. La session illustre le fonctionnement complet du skill memory-manager en conditions réelles.


# Table des Matières

1. Question initiale : comment exporter une session vers Notion
1. Réponse : deux workflows disponibles (Archive simple / Archive + Fusion)
1. Déclenchement de l'archivage de la session courante
1. Diagnostic et création de la base 🧠 Manus Memory Hub

# Points Clés


## Question initiale

- Yannick demande la procédure d'export d'une session vers Notion
- Manus consulte les skills session-navigator et memory-manager pour répondre avec précision

## Deux workflows disponibles

- Option 1 — Archive simple : commande "Archive cette conversation", crée une entrée Notion Conversation Archive avec résumé, ToC, points clés, décisions, actions, transcript
- Option 2 — Archive + Fusion : pour plusieurs sessions liées, workflow CLOSE + fusion en MASTER SESSION via fusion_engine.py, export Notion avec cross-références
- Contrainte identifiée : renommage de session dans l'UI Manus est manuel (API PUT non supportée), l'export Notion est entièrement automatisé

## Archivage et création du Memory Hub

- Yannick déclenche "Archive cette session"
- Diagnostic : base Memory Hub absente du workspace (IDs obsolètes → 404)
- Archivage temporaire dans YOS Archives
- Yannick confirme la création de la base dédiée
- Création de 🧠 Manus Memory Hub dans yOS / yONE
- Migration de l'entrée vers la base dédiée
- Mise à jour des constantes du skill memory-manager

# Décisions Prises

- Créer la base 🧠 Manus Memory Hub dans le workspace yONE sous la page yOS
- Data Source ID actif : 94086d51-ac40-4027-b994-55c5681f72e5
- Mettre à jour les constantes du skill avec les IDs corrects
- YOS Archives conservé comme fallback

# Transcription Complète


## Échange 1 — Question initiale

Yannick : How to export a session to Notion

Manus : Réponse structurée avec deux workflows : Archive simple (commande "Archive cette conversation") et Archive + Fusion (plusieurs sessions liées). Tableau comparatif fourni. Contrainte API PUT identifiée.


## Échange 2 — Déclenchement de l'archivage

Yannick : Archive cette session

Manus : Exécution du workflow. Diagnostic : IDs Notion obsolètes (404). Archivage dans YOS Archives. Constantes mises à jour avec note d'obsolescence.


## Échange 3 — Création du Memory Hub

Yannick : Oui [confirme la création de la base dédiée]

Manus : Création de 🧠 Manus Memory Hub dans yONE/yOS. Schéma complet avec Type, Tags, Statut, Priorite. Migration de l'entrée. Mise à jour des constantes du skill.
