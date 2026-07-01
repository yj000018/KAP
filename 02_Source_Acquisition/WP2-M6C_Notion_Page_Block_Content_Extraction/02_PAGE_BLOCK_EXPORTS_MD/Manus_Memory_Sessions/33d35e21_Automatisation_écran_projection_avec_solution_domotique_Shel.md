---
source_id: KAP-WP2-M6C-Manus_Memory_Sessions-33d35e21
notion_page_id: 33d35e21-8cf8-8135-8877-d9c7a20a41c6
notion_database_id: 5e51ded4-0b46-4a68-acc2-4e90886a2499
title: "Automatisation écran projection avec solution domotique Shelly"
database_name: Manus_Memory_Sessions
acquired_at: 2026-07-01T19:03:19Z
acquisition_method: Notion_Blocks_API_v1
canonical_status: not_canonical
limitations: block_content_only_no_media_downloads
---

# Automatisation écran projection avec solution domotique Shelly

**Page ID:** `33d35e21-8cf8-8135-8877-d9c7a20a41c6`  
**Database:** Manus_Memory_Sessions  
**Created:** 2026-04-09  
**Last Edited:** 2026-04-09  

## Properties

- **Length:** xl
- **Language:** fr
- **Subthemes:** screen automation, Shelly devices, Home Assistant, iCloud integration, 1Password access, Swiss e-commerce
- **Project:** DOMUS
- **UID:** x9f3nFJxfM1dKkiqRYoyGi
- **Date:** 2026-02-15
- **Themes:** home automation, smart home integration, hardware configuration, system access
- **Archived:** True
- **Depth:** substantial
- **Title:** Automatisation écran projection avec solution domotique Shelly

## Content


## Executive Summary

Session focused on automating a manual projection screen using Shelly Plus 2PM smart switch integrated with Home Assistant. Delivered complete technical solution with architecture documents, BOM (~30€), and implementation plan. Encountered access challenges with iCloud contacts and 1Password CLI during procurement phase, requiring manual credential sharing. Successfully identified best price (22.70 CHF) but purchasing blocked by authentication requirements.


## Context & Intent

User wanted to replace manual remote control for projection screen with smart home automation solution integrated into broader domotique system.


## What Was Done

Designed complete automation architecture with Shelly Plus 2PM recommendation over Gen 1 version. Created 6 technical documents including hardware analysis, Home Assistant integration, and governance protocols. Attempted multiple access methods for iCloud contacts and 1Password credentials. Found best pricing on Swiss e-commerce site Galaxus.


## Outputs Produced

- [architecture] Complete Domotique Solution — 6 documents + diagram covering hardware, software, integration, and governance
- [recommendation] Shelly Plus 2PM Selection — Comparative analysis recommending Gen 2+ over Gen 1 for better future-proofing
- [pricing] Swiss Market Research — Best price identification at 22.70 CHF on Galaxus platform

## Key Decisions & Validations

- Selected Shelly Plus 2PM over standard 2PM for ESP32 architecture and scripting capabilities
- Chose Home Assistant as integration platform
- Identified Galaxus as best price vendor in Swiss market
- Deferred iCloud access configuration as P1 task
- Attempted 1Password CLI integration for credential management

## Lessons Learned

Worked well:

- Comprehensive technical documentation delivery
- Hardware comparison methodology
- Swiss e-commerce price research
Failed / suboptimal:

- iCloud API access from Linux sandbox limitations
- 1Password Service Account token configuration issues
- Swiss website CAPTCHA blocking automated browsers
- Authentication dependencies blocking purchase completion
Discoveries:

- Swiss e-commerce sites use aggressive anti-bot protection
- Service Account tokens require specific permissions configuration
- Browser automation needs human intervention for CAPTCHA resolution

## Challenges & Blockers

- No iCloud API access available in current Manus architecture
- 1Password CLI authentication failing with Service Account token
- Swiss e-commerce CAPTCHA preventing automated checkout
- Missing user credentials for Galaxus account login

## Open Questions

- How to properly configure 1Password Service Account permissions?
- What's the best method for persistent credential access in Manus?
- Should we implement alternative authentication flows for Swiss sites?
- How to balance automation vs. security for credential management?

## Next Steps

- Configure iCloud API access as P1 priority task
- Resolve 1Password Service Account token configuration
- Complete Shelly Plus 2PM purchase via manual login
- Implement hardware installation following provided documentation
- Test Home Assistant integration and automation scenarios
---
UID: x9f3nFJxfM1dKkiqRYoyGi | Model: claude-sonnet-4-20250514 | Cost: $0.0334
