---
source_id: KAP-WP2-M6C-Manus_Memory_Hub-31b35e21
notion_page_id: 31b35e21-8cf8-815e-82c5-d01cc0c1b08b
notion_database_id: 533401fa-1702-4d9d-a60e-5433cac72fe1
title: "K5 — Network Failure — Automatic Staggered Retry Policy"
database_name: Manus_Memory_Hub
acquired_at: 2026-07-01T19:03:19Z
acquisition_method: Notion_Blocks_API_v1
canonical_status: not_canonical
limitations: block_content_only_no_media_downloads
---

# K5 — Network Failure — Automatic Staggered Retry Policy

**Page ID:** `31b35e21-8cf8-815e-82c5-d01cc0c1b08b`  
**Database:** Manus_Memory_Hub  
**Created:** 2026-03-06  
**Last Edited:** 2026-03-06  

## Properties

- **Priorite:** Haute
- **Statut:** Reference
- **Type:** Connaissance Explicite
- **Tags:** yOS, systems-thinking, Manus
- **Name:** K5 — Network Failure — Automatic Staggered Retry Policy

## Content


## K5 — Network Failure — Automatic Staggered Retry Policy

Status: Enabled

Trigger: Network loss or network failure.

Retry Schedule:

1. 2x retry after a few seconds
1. 1x retry after 1 minute
1. 1x retry after 5 minutes
Constraint: Never interrupt the task to report a transient network issue.
