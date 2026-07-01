---
source_id: KAP-WP2-M6C-Manus_Memory_Hub-31b35e21
notion_page_id: 31b35e21-8cf8-8101-a581-cc7ab7495722
notion_database_id: 533401fa-1702-4d9d-a60e-5433cac72fe1
title: "K3 — Credential & Secret Management — Master Rule"
database_name: Manus_Memory_Hub
acquired_at: 2026-07-01T19:03:19Z
acquisition_method: Notion_Blocks_API_v1
canonical_status: not_canonical
limitations: block_content_only_no_media_downloads
---

# K3 — Credential & Secret Management — Master Rule

**Page ID:** `31b35e21-8cf8-8101-a581-cc7ab7495722`  
**Database:** Manus_Memory_Hub  
**Created:** 2026-03-06  
**Last Edited:** 2026-03-06  

## Properties

- **Priorite:** Haute
- **Statut:** Reference
- **Type:** Connaissance Explicite
- **Tags:** yOS, systems-thinking, Manus
- **Name:** K3 — Credential & Secret Management — Master Rule

## Content


## K3 — Credential & Secret Management — Master Rule

Status: Enabled

Storage Rule: Every secret (API key, token, password) must be stored in:

1. Manus Internal Secrets
1. 1Password (1P)
Retrieval: Always programmatic via 1P CLI — never manual copy-paste.

Protocol:

- If a login succeeds but does not match the stored 1P entry, update 1P immediately.
- If credentials are inaccessible, proceed with a workaround (simulated data, sandbox) rather than blocking.
Tool: Use 1P CLI with OP_SERVICE_ACCOUNT_TOKEN.
