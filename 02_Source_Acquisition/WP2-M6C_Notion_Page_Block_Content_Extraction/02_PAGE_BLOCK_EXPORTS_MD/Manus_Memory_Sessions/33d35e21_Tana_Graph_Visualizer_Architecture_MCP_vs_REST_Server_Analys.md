---
source_id: KAP-WP2-M6C-Manus_Memory_Sessions-33d35e21
notion_page_id: 33d35e21-8cf8-8146-8af1-c263edd0a167
notion_database_id: 5e51ded4-0b46-4a68-acc2-4e90886a2499
title: "Tana Graph Visualizer Architecture: MCP vs REST Server Analysis"
database_name: Manus_Memory_Sessions
acquired_at: 2026-07-01T19:03:19Z
acquisition_method: Notion_Blocks_API_v1
canonical_status: not_canonical
limitations: block_content_only_no_media_downloads
---

# Tana Graph Visualizer Architecture: MCP vs REST Server Analysis

**Page ID:** `33d35e21-8cf8-8146-8af1-c263edd0a167`  
**Database:** Manus_Memory_Sessions  
**Created:** 2026-04-09  
**Last Edited:** 2026-04-09  

## Properties

- **Length:** medium
- **Language:** mixed
- **Subthemes:** supertag-cli, REST vs MCP, 3D visualization, Force graphs, N100 deployment
- **Project:** yOS
- **UID:** aVdOH4P4EyQnExg6hKG4gM
- **Date:** 2026-03-21
- **Themes:** Tana integration, Data visualization, Architecture design, MCP protocols
- **Archived:** True
- **Depth:** substantial
- **Title:** Tana Graph Visualizer Architecture: MCP vs REST Server Analysis

## Content


## Executive Summary

Architecture discussion for Tana graph visualization comparing MCP Tana Desktop vs supertag-server. Built complete visualizer app with 3 modes (Tree/Mindmap/Galaxy) using mock data. Determined supertag-server superior for web apps due to native CORS and REST endpoints, while MCP better for AI agents. Deployed working prototype at tanagraph-vycdpucn.manus.space.


## Context & Intent

User inquired about installing MCP Tana for Manus, leading to architectural analysis of best approach for Tana data visualization in web interface.


## What Was Done

Built complete Tana Graph Visualizer with React/TypeScript featuring three visualization modes, analyzed MCP vs REST architectures, created mock data structure, deployed working prototype, and generated comprehensive specs document for Claude collaboration.


## Outputs Produced

- [web_app] Tana Graph Visualizer — React app with Tree/Mindmap/Galaxy views at tanagraph-vycdpucn.manus.space
- [json_data] Mock Tana Data — 39 nodes hierarchical structure with Y-OS content for testing
- [specs_document] Complete Technical Specs — Comprehensive specs for Claude including TypeScript interfaces and enhancement details

## Key Decisions & Validations

- supertag-server preferred over MCP for web visualization due to CORS support
- Universal module architecture for source-agnostic visualization
- MBA2 + N100 distributed architecture for always-on availability
- React + D3/markmap/3d-force-graph stack for multiple visualization modes

## Lessons Learned

Worked well:

- supertag-cli provides complete MCP + REST server solution
- Component lazy loading reduces initial bundle size effectively
- Mock data approach enables parallel development
Failed / suboptimal:

- MCP protocol requires proxy for browser access
- WebGL issues in headless browser environments for 3D rendering
Discoveries:

- supertag-server offers semantic search with vector embeddings
- REST API much simpler for web apps than MCP JSON-RPC

## Challenges & Blockers

- MBA needed for Tana Desktop dependency
- WebGL Galaxy view not working in sandbox browser
- Index sync dependency on macOS for Linux deployment

## Open Questions

- Galaxy view enhancements with Three.js custom nodes and bloom effects
- Real-time vs 6-hour sync trade-offs for data freshness
- Browser compatibility for 3D WebGL components

## Next Steps

- Install supertag-cli on MBA when available
- Connect real Tana data via supertag-server API
- Deploy N100 instance with cloudflared tunnel
- Enhance Galaxy view with Claude collaboration using provided specs
---
UID: aVdOH4P4EyQnExg6hKG4gM | Model: claude-sonnet-4-20250514 | Cost: $0.0281
