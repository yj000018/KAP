---
source_id: KAP-WP2-M6C-Manus_Memory_Sessions-33d35e21
notion_page_id: 33d35e21-8cf8-817e-bd1f-ce973273ce5e
notion_database_id: 5e51ded4-0b46-4a68-acc2-4e90886a2499
title: "Wrike MCP Connector OAuth Authentication Troubleshooting"
database_name: Manus_Memory_Sessions
acquired_at: 2026-07-01T19:03:19Z
acquisition_method: Notion_Blocks_API_v1
canonical_status: not_canonical
limitations: block_content_only_no_media_downloads
---

# Wrike MCP Connector OAuth Authentication Troubleshooting

**Page ID:** `33d35e21-8cf8-817e-bd1f-ce973273ce5e`  
**Database:** Manus_Memory_Sessions  
**Created:** 2026-04-09  
**Last Edited:** 2026-04-09  

## Properties

- **Length:** medium
- **Language:** en
- **Subthemes:** Wrike API, access tokens, redirect URLs, MCP configuration
- **Project:** UNKNOWN
- **UID:** FeZeM7gpLl0uYBklTXrV0n
- **Date:** 2026-01-06
- **Themes:** MCP connectors, OAuth authentication, API integration, troubleshooting
- **Archived:** True
- **Depth:** standard
- **Title:** Wrike MCP Connector OAuth Authentication Troubleshooting

## Content


## Executive Summary

User attempted to test the Wrike MCP connector by providing API credentials, but encountered persistent OAuth authentication failures. Assistant identified the root cause as incomplete OAuth flow configuration and provided troubleshooting guidance. The session revealed that MCP connectors require proper OAuth setup at the server level rather than direct API credential input.


## Context & Intent

User wanted to test and explore the capabilities of a Wrike MCP connector, expecting to see data fetching and feature demonstrations.


## What Was Done

Attempted to connect to Wrike MCP server, diagnosed OAuth authentication issues, analyzed provided API credentials and configuration screenshots, provided troubleshooting steps for OAuth setup.


## Outputs Produced

- [diagnosis] OAuth Authentication Analysis — Identified that MCP connector requires OAuth flow completion at server level
- [troubleshooting_guide] OAuth Configuration Steps — Provided specific steps for resolving authentication issues including redirect URL configuration

## Key Decisions & Validations

- Identified OAuth authentication as the blocking issue rather than attempting alternative approaches
- Recommended contacting Manus support for proper OAuth configuration

## Lessons Learned

Worked well:

- Clear error diagnosis from 401 responses
- Systematic troubleshooting approach
Failed / suboptimal:

- Could not complete the primary objective of testing connector features
- OAuth flow not properly configured
Discoveries:

- MCP connectors require OAuth configuration at server level
- Direct API credentials cannot bypass OAuth requirements in MCP system

## Challenges & Blockers

- Incomplete OAuth authentication setup
- Redirect URL configuration mismatch
- Unable to access Wrike connector functionality

## Open Questions

- What is the correct redirect URL for Wrike MCP connector?
- How to properly configure OAuth in MCP settings?
- Can permanent access tokens be used as alternative to OAuth flow?

## Next Steps

- Configure proper redirect URL in Wrike app settings
- Complete OAuth authorization flow through MCP interface
- Contact Manus support for connector configuration guidance
- Retry connector testing once authentication is resolved
---
UID: FeZeM7gpLl0uYBklTXrV0n | Model: claude-sonnet-4-20250514 | Cost: $0.0148
