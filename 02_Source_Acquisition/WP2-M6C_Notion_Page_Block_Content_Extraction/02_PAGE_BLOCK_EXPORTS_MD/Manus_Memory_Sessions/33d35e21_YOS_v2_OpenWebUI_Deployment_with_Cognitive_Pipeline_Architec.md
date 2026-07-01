---
source_id: KAP-WP2-M6C-Manus_Memory_Sessions-33d35e21
notion_page_id: 33d35e21-8cf8-818b-a533-e8a336a79121
notion_database_id: 5e51ded4-0b46-4a68-acc2-4e90886a2499
title: "YOS v2 OpenWebUI Deployment with Cognitive Pipeline Architecture"
database_name: Manus_Memory_Sessions
acquired_at: 2026-07-01T19:03:19Z
acquisition_method: Notion_Blocks_API_v1
canonical_status: not_canonical
limitations: block_content_only_no_media_downloads
---

# YOS v2 OpenWebUI Deployment with Cognitive Pipeline Architecture

**Page ID:** `33d35e21-8cf8-818b-a533-e8a336a79121`  
**Database:** Manus_Memory_Sessions  
**Created:** 2026-04-09  
**Last Edited:** 2026-04-09  

## Properties

- **Length:** xl
- **Language:** mixed
- **Subthemes:** OpenWebUI Integration, Cognitive Routing, Mission Pack Generation, Filter Functions, CSS Theming, Memory Systems
- **Project:** yOS
- **UID:** 3dQDL8hfPEfhAXCfMTGQ9p
- **Date:** 2026-03-06
- **Themes:** AI Architecture, UI/UX Development, System Deployment, Full Stack Implementation
- **Archived:** True
- **Depth:** landmark
- **Title:** YOS v2 OpenWebUI Deployment with Cognitive Pipeline Architecture

## Content


## Executive Summary

Comprehensive YOS v2 implementation including OpenWebUI customization via Filter Functions, full cognitive pipeline (Intent Analyzer, CRT, ART, Mission Builder), custom glass-themed UI with left/center/right rail layout, and permanent deployment on fly.io. Built complete memory system with 32 entries, TF-IDF/sentence-transformer retrieval, context injection, and mobile-responsive interface with debugging of iOS Safari click handlers.


## Context & Intent

Build production-ready YOS cognitive OS interface integrated with OpenWebUI, including custom theming, memory retrieval, context building, and permanent cloud deployment with full debugging of mobile issues.


## What Was Done

1) Confirmed OpenWebUI customization capabilities via Filter Functions 2) Built complete YOS pipeline with embedder, retriever, context builder, mission pack generator 3) Deployed OpenWebUI container with YOS filter 4) Rebuilt as YOS v2 with canonical UI design 5) Deployed permanently on fly.io with persistent storage 6) Fixed DNS/TLS issues for iOS 7) Debugged and fixed mobile UI click handlers and responsive layout


## Outputs Produced

- [software] YOS Filter Function — OpenWebUI Python filter for context injection and mission pack generation
- [web_application] YOS v2 UI — Glass-themed cognitive interface with left/center/right rail layout
- [deployment] Production YOS Instance — Live at https://yos-ui.fly.dev with persistent memory and auto-restart
- [api] YOS Backend API — FastAPI backend with intent analysis, CRT/ART routing, context building
- [memory_system] YOS Memory Store — 32-entry JSON memory with TF-IDF/transformer retrieval

## Key Decisions & Validations

- Use OpenWebUI Filter Functions as primary YOS integration point rather than external pipelines
- Deploy on fly.io with persistent volumes for permanent hosting
- Implement TF-IDF fallback embedder for lighter deployment vs sentence-transformers
- Switch from onclick handlers to addEventListener for iOS Safari compatibility
- Use canonical glass/violet/blue/pink theme with responsive mobile layout

## Lessons Learned

Worked well:

- OpenWebUI Filter Functions provide complete control over prompt injection
- fly.io deployment with persistent volumes works reliably for production
- TF-IDF embedder sufficient for PoC without heavy PyTorch dependency
- Memory system with 32 entries provides good context retrieval
Failed / suboptimal:

- onclick handlers with .call(this, event) don't work correctly on iOS Safari
- sentence-transformers too heavy for 512MB fly.io machines
- IPv6 DNS propagation on fly.io can take 30+ minutes causing TLS errors
- Desktop-first responsive design required mobile-specific layout fixes
Discoveries:

- OpenWebUI exposes 3 viable extension layers: Filter, Pipe, and Tools functions
- Global filters run on all models automatically without per-model configuration
- iOS Safari requires addEventListener pattern for reliable mobile click handling
- fly.io IPv4 is shared but IPv6 requires proper AAAA DNS record propagation

## Challenges & Blockers

- iOS Safari click handler compatibility requiring pattern changes
- fly.io DNS propagation delays causing TLS handshake failures
- Memory embedder size vs deployment constraints trade-offs
- GitHub PAT with insufficient scope blocking code repository updates

## Open Questions

- Should upgrade to OpenAI embeddings for better retrieval quality?
- How to handle memory expansion beyond current 32-entry limit?
- Whether to implement real Manus API bridge vs current mock endpoints?
- Custom domain setup and SSL certificate management for production use?

## Next Steps

- Add OpenAI API key as fly secret for upgraded embedding quality
- Expand memory store with additional project/session data
- Connect real Manus API endpoints in manus_bridge.py
- Implement custom domain with fly certs add command
- Add /reload-memory endpoint for post-restart index rebuilding
---
UID: 3dQDL8hfPEfhAXCfMTGQ9p | Model: claude-sonnet-4-20250514 | Cost: $0.0421
