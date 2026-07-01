---
source_id: KAP-WP2-M6C-Manus_Memory_Sessions-33d35e21
notion_page_id: 33d35e21-8cf8-81c7-83a2-ebe215fae9c8
notion_database_id: 5e51ded4-0b46-4a68-acc2-4e90886a2499
title: "Inner Compass - Full-Stack Spiritual Guidance App Development"
database_name: Manus_Memory_Sessions
acquired_at: 2026-07-01T19:03:19Z
acquisition_method: Notion_Blocks_API_v1
canonical_status: not_canonical
limitations: block_content_only_no_media_downloads
---

# Inner Compass - Full-Stack Spiritual Guidance App Development

**Page ID:** `33d35e21-8cf8-81c7-83a2-ebe215fae9c8`  
**Database:** Manus_Memory_Sessions  
**Created:** 2026-04-09  
**Last Edited:** 2026-04-09  

## Properties

- **Length:** long
- **Language:** mixed
- **Subthemes:** React/Next.js Frontend, tRPC API, OpenAI Integration, Authentication, Database Schema, Crisis Detection, Internationalization, Session Management
- **Project:** UNKNOWN
- **UID:** 89c3jrQUzeBPNU13kLjKpw
- **Date:** 2026-01-02
- **Themes:** Full-Stack Development, AI Integration, Multilingual Support, Spiritual Guidance, Progressive User Experience
- **Archived:** True
- **Depth:** landmark
- **Title:** Inner Compass - Full-Stack Spiritual Guidance App Development

## Content


## Executive Summary

Complete development of Inner Compass, a sophisticated spiritual guidance web application featuring three progressive AI-powered guidance modes (Teacher, Companion, Master) with OpenAI integration. Built full-stack architecture with React/Next.js frontend, tRPC API backend, comprehensive user authentication, and multilingual support for English, French, and Italian. Implemented advanced features including crisis detection, automatic session titling, daily guidance generation, progressive mode unlocking, and safety protocols.


## Context & Intent

User requested creation of a web app with detailed specifications provided in attached text file describing Inner Compass spiritual guidance platform


## What Was Done

Developed complete web application from scratch including database schema design, authentication system, three AI guidance modes with dynamic prompts, crisis detection system, daily guidance generator, resources library, multilingual UI with language selector, automatic session title generation, and comprehensive testing framework


## Outputs Produced

- [web_application] Inner Compass — Full-stack spiritual guidance platform with AI-powered conversations
- [database_schema] Spiritual guidance data model — Complete schema with users, profiles, sessions, messages, and resources
- [api_backend] tRPC API server — Type-safe API with OpenAI integration and guidance logic
- [frontend_ui] React/Next.js interface — Minimalist UI with three guidance modes and multilingual support
- [safety_system] Crisis detection & protocols — AI-powered crisis detection with professional resource recommendations
- [translation_system] Multilingual support — Complete French and Italian translations with language selector

## Key Decisions & Validations

- Chose tRPC over REST API for type safety and developer experience
- Implemented three progressive guidance modes with unlocking mechanics
- Integrated OpenAI with dynamic prompt assembly for personalized responses
- Built crisis detection system with safety protocols and professional resources
- Added multilingual support with comprehensive translation system
- Implemented automatic session title generation based on conversation content

## Lessons Learned

Worked well:

- tRPC provided excellent type safety and API development experience
- OpenAI integration with dynamic prompts created highly personalized guidance
- Progressive mode unlocking enhanced user engagement
- Crisis detection system provided important safety layer
Failed / suboptimal:

- Initial daily guidance query returned undefined causing tRPC errors
- Translation process was time-intensive for comprehensive multilingual support
Discoveries:

- tRPC queries cannot return undefined - must return null or data
- Dynamic prompt assembly allows sophisticated AI personality adaptation
- Crisis detection can be effectively implemented with keyword analysis and context awareness

## Challenges & Blockers

- tRPC undefined return value bug in daily guidance query
- Extensive translation requirements for complete multilingual support
- Balancing spiritual guidance authenticity with AI safety protocols

## Open Questions

- How to implement persistent language preferences across sessions
- Whether to add session search and filtering capabilities
- How to enhance the journaling and reflection features

## Next Steps

- Set up automated daily guidance generation with cron scheduling
- Add session search and filtering functionality
- Implement reflection journal feature for spiritual growth tracking
- Store language preferences in user profiles
- Consider conversation threading and branching capabilities
---
UID: 89c3jrQUzeBPNU13kLjKpw | Model: claude-sonnet-4-20250514 | Cost: $0.0269
