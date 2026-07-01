---
source_id: KAP-WP2-M6C-Manus_Memory_Sessions-33d35e21
notion_page_id: 33d35e21-8cf8-8186-8e42-d9992040eb12
notion_database_id: 5e51ded4-0b46-4a68-acc2-4e90886a2499
title: "Setting up Automated Development Skill for Complex Coding Tasks"
database_name: Manus_Memory_Sessions
acquired_at: 2026-07-01T19:03:19Z
acquisition_method: Notion_Blocks_API_v1
canonical_status: not_canonical
limitations: block_content_only_no_media_downloads
---

# Setting up Automated Development Skill for Complex Coding Tasks

**Page ID:** `33d35e21-8cf8-8186-8e42-d9992040eb12`  
**Database:** Manus_Memory_Sessions  
**Created:** 2026-04-09  
**Last Edited:** 2026-04-09  

## Properties

- **Length:** short
- **Language:** mixed
- **Subthemes:** Claude API integration, workflow optimization, project configuration
- **Project:** yOS
- **UID:** oTUmbMW66scKL6VBzyHRBB
- **Date:** 2026-03-30
- **Themes:** skill development, automation setup, coding workflow
- **Archived:** True
- **Depth:** substantial
- **Title:** Setting up Automated Development Skill for Complex Coding Tasks

## Content


## Executive Summary

User defined and refined a 'dev' skill that automatically delegates complex coding tasks to Claude API. The skill includes comprehensive system prompts for React/TypeScript/Three.js stack, specific formatting requirements, and three activation levels. Final step was configuring automatic activation via project instructions.


## Context & Intent

User wanted to create an automated workflow for delegating complex coding tasks (>30 lines) to Claude API while maintaining Manus as the orchestrator for integration, testing, and deployment.


## What Was Done

Created and refined a comprehensive 'dev' skill with system prompts, stack specifications (React 19, TypeScript, Vite, Tailwind 4, Three.js, SQLite), output formatting rules, and three activation levels. Provided final project instruction for automatic activation.


## Outputs Produced

- [skill_definition] dev skill v2 — Complete skill file with Claude API integration, system prompts, and activation levels
- [project_instruction] automatic dev activation — One-line instruction for automatic skill activation in project settings

## Key Decisions & Validations

- Use Claude Sonnet 4.5 with 8000 max tokens for complex coding tasks
- Implement three-tier activation system (automatic, explicit call, manual context)
- Enforce strict TypeScript and production-ready code requirements
- Mandate complete file outputs, never truncated code

## Lessons Learned

Worked well:

- Clear system prompt structure with stack specifications
- Structured output format for consistent integration
- Multi-level activation for different use cases
Discoveries:

- Importance of complete context injection for effective delegation
- Value of structured post-action workflows for error handling

## Next Steps

- Test the dev skill with actual complex coding tasks
- Monitor Claude API response quality and adjust system prompts if needed
- Expand skill library with similar delegation patterns for other specialized tasks
---
UID: oTUmbMW66scKL6VBzyHRBB | Model: claude-sonnet-4-20250514 | Cost: $0.0174
