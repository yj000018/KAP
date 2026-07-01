---
source_id: KAP-WP2-M6C-Manus_Memory_Sessions-33d35e21
notion_page_id: 33d35e21-8cf8-811c-a4c2-d358e8318e79
notion_database_id: 5e51ded4-0b46-4a68-acc2-4e90886a2499
title: "Creating Context Injection Skill (@ctx) for Project Development"
database_name: Manus_Memory_Sessions
acquired_at: 2026-07-01T19:03:19Z
acquisition_method: Notion_Blocks_API_v1
canonical_status: not_canonical
limitations: block_content_only_no_media_downloads
---

# Creating Context Injection Skill (@ctx) for Project Development

**Page ID:** `33d35e21-8cf8-811c-a4c2-d358e8318e79`  
**Database:** Manus_Memory_Sessions  
**Created:** 2026-04-09  
**Last Edited:** 2026-04-09  

## Properties

- **Length:** short
- **Language:** mixed
- **Subthemes:** project context injection, dev tool integration, git analysis, stack detection
- **Project:** yOS
- **UID:** lMztvgu67W1kF6KjuyVgna
- **Date:** 2026-03-30
- **Themes:** skill development, context automation, development workflow
- **Archived:** True
- **Depth:** substantial
- **Title:** Creating Context Injection Skill (@ctx) for Project Development

## Content


## Executive Summary

User requested creation of a @ctx skill to automatically inject project context into development workflows. Manus analyzed the requirements and created a skill that collects project name, stack, recent files, URL, database schema, and last task summary. The implementation includes a Python script for context collection and structured injection into the @dev skill to eliminate repetitive context setup.


## Context & Intent

Streamline development workflow by automatically injecting project context when working outside of project sessions, particularly for iOS usage and free chat sessions where context needs to be repeatedly provided to @dev.


## What Was Done

Created the @ctx skill with automated context collection including Python script for gathering project state, git history, stack detection, and database schema extraction. Implemented structured context block formatting for seamless integration with @dev workflow.


## Outputs Produced

- [skill] @ctx — Automated project context injection skill with SKILL.md documentation
- [script] collect_context.py — Python script for automatic project state collection and context formatting

## Key Decisions & Validations

- Focus on autonomous context collection without user prompts
- Structure output as [PROJECT CONTEXT] block for @dev injection
- Support both standalone @ctx and combined @ctx @dev usage
- Include 48-hour git history for recent changes tracking

## Lessons Learned

Worked well:

- Clear skill requirements led to direct implementation
- Structured planning with resource table
- Comprehensive context collection approach
Discoveries:

- Context injection can significantly reduce repetitive setup in development workflows

## Next Steps

- Test the @ctx skill in various project environments
- Validate integration with @dev workflow
- Consider extending context collection for other development tools
---
UID: lMztvgu67W1kF6KjuyVgna | Model: claude-sonnet-4-20250514 | Cost: $0.0138
