---
source_id: KAP-WP2-M6C-Manus_Memory_Sessions-33d35e21
notion_page_id: 33d35e21-8cf8-8169-be25-cd581c14d737
notion_database_id: 5e51ded4-0b46-4a68-acc2-4e90886a2499
title: "Building UniversalChatThemeCanon: Complex Web App with Notion Integration"
database_name: Manus_Memory_Sessions
acquired_at: 2026-07-01T19:03:19Z
acquisition_method: Notion_Blocks_API_v1
canonical_status: not_canonical
limitations: block_content_only_no_media_downloads
---

# Building UniversalChatThemeCanon: Complex Web App with Notion Integration

**Page ID:** `33d35e21-8cf8-8169-be25-cd581c14d737`  
**Database:** Manus_Memory_Sessions  
**Created:** 2026-04-09  
**Last Edited:** 2026-04-09  

## Properties

- **Length:** long
- **Language:** en
- **Subthemes:** React Development, Node.js Backend, Database Design, File Processing, Error Handling, MCP Integration, Public API Scraping
- **Project:** yOS
- **UID:** v8eOAc3FDJPskd0MpdgRCQ
- **Date:** 2026-02-07
- **Themes:** Full-Stack Development, Web Application Architecture, Notion API Integration, Skill Creation
- **Archived:** True
- **Depth:** substantial
- **Title:** Building UniversalChatThemeCanon: Complex Web App with Notion Integration

## Content


## Executive Summary

Built UniversalChatThemeCanon, a sophisticated web application for processing ChatGPT conversation exports and extracting thematic knowledge using hybrid lexical-semantic analysis. The app features multi-ZIP upload, customizable theme configuration with yOS profile integration, and LLM-powered canonization with support for GPT-4/Claude/Gemini. Created a reusable skill for complex web app development and implemented Notion integration with multiple fallback strategies.


## Context & Intent

User requested to plan and generate a web application based on detailed requirements, then create a reusable skill for the development process, and finally add Notion link import functionality


## What Was Done

Developed complete full-stack web application with React frontend, Node.js backend, SQLite database, and comprehensive feature set. Created structured development workflow skill with 6-phase approach. Implemented Notion integration with API-first approach, fallback to public scraping, and error handling for various authentication scenarios.


## Outputs Produced

- [web_application] UniversalChatThemeCanon — Full-featured web app for ChatGPT conversation processing and thematic extraction
- [skill] Complex Web App Builder — Reusable skill for structured web application development with Notion integration support
- [database_schema] Application Database — Complete SQLite schema with users, projects, jobs, themes, and API keys tables
- [api_integration] Notion Integration — Multi-strategy Notion content import with API and scraping fallbacks

## Key Decisions & Validations

- Chose web app over mobile app based on user preference
- Implemented database-backed architecture for multi-user support
- Used hybrid lexical-semantic analysis instead of pure embeddings for reliability
- Removed @xenova/transformers dependency to fix native module crashes
- Switched from MCP to direct Notion SDK for better control
- Abandoned public scraping due to JavaScript-rendered content limitations

## Lessons Learned

Worked well:

- Structured 6-phase development workflow with todo.md tracking
- Direct API integration over MCP for external services
- Removing problematic native dependencies to fix server crashes
- Progressive error handling with multiple fallback strategies
Failed / suboptimal:

- MCP integration proved unreliable for Notion access
- Simple HTTP scraping ineffective for JavaScript-rendered Notion pages
- Initial URL validation too strict for custom workspace domains
Discoveries:

- Notion public pages require JavaScript execution for content access
- Native module dependencies can cause server instability in Manus environment
- Custom Notion workspace domains (notion.site) need special handling in URL validation

## Challenges & Blockers

- Server crashes due to @xenova/transformers native module conflicts
- Notion MCP integration failing with workspace permission issues
- Public Notion pages not accessible via simple HTTP scraping
- JSON parsing errors from malformed API responses during scraping attempts

## Open Questions

- Should the app support Puppeteer-based scraping for JavaScript-rendered content?
- How to best guide users through Notion integration setup process?
- What's the optimal balance between API functionality and user configuration complexity?

## Next Steps

- Add API Keys management settings page for user token configuration
- Implement markdown file upload as alternative to Notion integration
- Create step-by-step Notion integration setup guide in UI
- Add real-time progress tracking for long-running processing jobs
- Build export preview functionality for canonized content review
---
UID: v8eOAc3FDJPskd0MpdgRCQ | Model: claude-sonnet-4-20250514 | Cost: $0.0344
