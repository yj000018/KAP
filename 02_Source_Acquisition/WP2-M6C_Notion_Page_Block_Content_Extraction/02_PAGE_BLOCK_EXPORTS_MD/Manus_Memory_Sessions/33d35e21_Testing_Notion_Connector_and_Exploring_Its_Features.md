---
source_id: KAP-WP2-M6C-Manus_Memory_Sessions-33d35e21
notion_page_id: 33d35e21-8cf8-8117-a522-fee02ef312bd
notion_database_id: 5e51ded4-0b46-4a68-acc2-4e90886a2499
title: "Testing Notion Connector and Exploring Its Features"
database_name: Manus_Memory_Sessions
acquired_at: 2026-07-01T19:03:19Z
acquisition_method: Notion_Blocks_API_v1
canonical_status: not_canonical
limitations: block_content_only_no_media_downloads
---

# Testing Notion Connector and Exploring Its Features

**Page ID:** `33d35e21-8cf8-8117-a522-fee02ef312bd`  
**Database:** Manus_Memory_Sessions  
**Created:** 2026-04-09  
**Last Edited:** 2026-04-09  

## Properties

- **Length:** short
- **Language:** en
- **Subthemes:** MCP Connector, Authentication, API Capabilities, Live Data Testing
- **Project:** yOS
- **UID:** xmv6ovvuh6HA2fwYJAptfv
- **Date:** 2026-02-27
- **Themes:** API Integration, Tool Testing, Notion Connector
- **Archived:** True
- **Depth:** standard
- **Title:** Testing Notion Connector and Exploring Its Features

## Content


## Executive Summary

Yannick requested testing and exploration of the Notion MCP connector features. Manus discovered 12 available tools but encountered authentication issues initially. After OAuth token refresh, successful connection was established and comprehensive testing performed, producing a detailed capability brief with live data demonstrations.


## Context & Intent

User wanted to understand the capabilities of the integrated Notion connector and see it working with real data from their workspace.


## What Was Done

Probed Notion MCP connector, identified 12 available tools, diagnosed authentication failure (401 Unauthorized), guided user through token refresh process, successfully reconnected, performed live read/write operations, and compiled comprehensive capability documentation.


## Outputs Produced

- [document] Notion Connector Capability Brief — Detailed documentation of all 12 Notion MCP tools with live data demonstrations and test results

## Key Decisions & Validations

- Proceeded with comprehensive testing after authentication resolution
- Created test page for live demonstration purposes

## Lessons Learned

Worked well:

- MCP connector discovery and diagnosis
- Clear authentication troubleshooting guidance
- Comprehensive capability documentation
Failed / suboptimal:

- Initial authentication token was expired/invalid
Discoveries:

- Notion MCP connector has 12 available tools
- OAuth token refresh resolves authentication issues
- Live read/write operations work as expected

## Challenges & Blockers

- Initial 401 Unauthorized error due to invalid/expired API token

## Open Questions

- Should the test page created during testing be deleted?

## Next Steps

- User to confirm if test page should be removed from workspace
---
UID: xmv6ovvuh6HA2fwYJAptfv | Model: claude-sonnet-4-20250514 | Cost: $0.0107
