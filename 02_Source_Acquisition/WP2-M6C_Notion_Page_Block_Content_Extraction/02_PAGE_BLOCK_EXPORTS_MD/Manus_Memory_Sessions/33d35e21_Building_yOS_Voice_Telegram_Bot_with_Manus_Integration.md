---
source_id: KAP-WP2-M6C-Manus_Memory_Sessions-33d35e21
notion_page_id: 33d35e21-8cf8-8121-a856-cc1e2f576cec
notion_database_id: 5e51ded4-0b46-4a68-acc2-4e90886a2499
title: "Building yOS Voice Telegram Bot with Manus Integration"
database_name: Manus_Memory_Sessions
acquired_at: 2026-07-01T19:03:19Z
acquisition_method: Notion_Blocks_API_v1
canonical_status: not_canonical
limitations: block_content_only_no_media_downloads
---

# Building yOS Voice Telegram Bot with Manus Integration

**Page ID:** `33d35e21-8cf8-8121-a856-cc1e2f576cec`  
**Database:** Manus_Memory_Sessions  
**Created:** 2026-04-09  
**Last Edited:** 2026-04-09  

## Properties

- **Length:** long
- **Language:** mixed
- **Subthemes:** STT/TTS Pipeline, Manus API Connection, Railway vs Fly.io Comparison, Secret Management, Cross-Platform Deployment
- **Project:** yOS
- **UID:** E4On9Cc51voDTaa5tuK5Cd
- **Date:** 2026-02-22
- **Themes:** Voice Interface Development, Telegram Bot Architecture, Deployment Infrastructure, API Integration
- **Archived:** True
- **Depth:** substantial
- **Title:** Building yOS Voice Telegram Bot with Manus Integration

## Content


## Executive Summary

Built and deployed a complete yOS voice interface Telegram bot with STT (Whisper), LLM processing via Manus API, and TTS (OpenAI). Initially deployed with isolated GPT-4o, then rebuilt for full Manus integration with access to all MCPs and memory systems. Evaluated multiple deployment platforms (Railway, Fly.io, Render) before settling on Fly.io. Established permanent secret management in Notion.


## Context & Intent

Create a voice interface to yOS/Manus system via Telegram, allowing vocal interaction with the same capabilities as text-based Manus conversations. The goal was to extend yOS with natural voice input/output while maintaining full access to memory, tools, and knowledge systems.


## What Was Done

Developed a complete Telegram voice bot with Whisper STT, Manus API integration, and OpenAI TTS. Configured deployment infrastructure on Fly.io with proper secret management. Updated yOS canon documentation in Notion. Rebuilt the architecture twice: first with isolated GPT-4o, then with full Manus API integration for complete tool access.


## Outputs Produced

- [application] yOS Voice Telegram Bot — Complete voice interface with STT/TTS pipeline connected to Manus API
- [infrastructure] Fly.io Deployment Configuration — Production deployment setup with environment variables and secrets
- [documentation] yOS Canon Update — Updated canonical yOS infrastructure documentation in Notion
- [security] Centralized Secret Management — Permanent API key storage in Notion with secure sandbox backup

## Key Decisions & Validations

- Chose Fly.io over Railway due to direct CLI deployment without GitHub requirement
- Selected OpenAI TTS over Hume due to MCP API access limitations
- Rebuilt architecture from isolated GPT-4o to full Manus API integration
- Implemented permanent secret storage in Notion for cross-session persistence
- Used French as primary language with voice onyx for professional tone

## Lessons Learned

Worked well:

- Modular STT/LLM/TTS pipeline allows easy component swapping
- Fly.io CLI deployment is streamlined once token is available
- Manus API integration provides full tool access as intended
- Notion-based secret management ensures permanence across sandbox resets
Failed / suboptimal:

- Railway requires GitHub connection which blocks direct deployment
- Hume AI MCP keys cannot be used directly from external bots
- Initial isolated GPT-4o approach defeated the purpose of yOS integration
- Notion API updates through MCP layer are slower than expected
Discoveries:

- Manus has a public API (api.manus.ai) with full capability access
- Fly.io requires credit card even for free tier usage
- Render.com has sleep issues for long-polling bots on free tier
- Voice interface latency (30s-2min) is acceptable for complex Manus tasks

## Challenges & Blockers

- Credit card requirement for Fly.io deployment
- MCP API access limitations for external tools
- Asynchronous Manus API requires polling and user feedback during processing
- Platform comparison complexity for deployment infrastructure choice

## Open Questions

- Why is Notion API slow through MCP when direct API calls are fast?
- Can Manus API response times be optimized for voice interactions?
- Should voice interface have different timeout handling than text interface?

## Next Steps

- Add credit card to Fly.io account and complete production deployment
- Test complete voice workflow with complex Manus tasks
- Investigate Notion MCP performance issues
- Consider adding voice interface status indicators during long tasks
- Document voice bot usage patterns and optimize for common use cases
---
UID: E4On9Cc51voDTaa5tuK5Cd | Model: claude-sonnet-4-20250514 | Cost: $0.0467
