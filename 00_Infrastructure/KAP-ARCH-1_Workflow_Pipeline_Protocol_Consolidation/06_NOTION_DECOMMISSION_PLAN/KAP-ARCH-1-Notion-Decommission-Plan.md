# KAP-ARCH-1: Notion Decommission Plan

**Program:** KAP
**Sprint:** KAP-ARCH-1
**Date:** 2026-07-02

## Overview
Notion was previously used as the primary knowledge hub (e.g., the 363-session corpus). It is now officially designated as a **Frozen Legacy Source**. This document outlines the plan to migrate its contents to Git/MD and decommission it as an active repository.

## 1. Current State
- **Corpus:** ~363 sessions archived in Notion.
- **Cut-off Date:** 2026-05-02. No new sessions have been archived to Notion since this date.
- **Status:** FROZEN. No new writes permitted.

## 2. Migration Strategy (WP2-NOTION)

The migration will be executed as a dedicated Work Package (WP2-NOTION).

### Phase 1: API Extraction
- Use the Notion API (via existing MCP or custom script) to extract all 363 session entries.
- Extract all properties: Title, Date, UID, Project, Themes, Subthemes, Length, Language, Depth, Summary, Decisions, Actions, Knowledge.

### Phase 2: Transformation
- Transform the flat Notion properties into the new Enhanced v2 Factsheet format (YAML metadata + Session Card).
- Map Notion fields to the new schema:
  - `Summary` → `Executive Summary`
  - `Decisions` + `Knowledge` → `Key Insights`
  - `Actions` → `Next Steps`

### Phase 3: Git Commit
- Save each transformed session as `{uid}_factsheet.md`.
- Commit the entire batch to the KAP GitHub repository under `03_Archived_Sessions/NOTION_LEGACY/`.

## 3. Decommissioning
Once the migration is verified (Gate: `NOTION_MIGRATION_COMPLETE`), the Notion databases will be marked as deprecated.
- Update Notion page titles to include `[DEPRECATED - MOVED TO GIT]`.
- Remove Notion API keys from active agent configurations.
- Do not delete the Notion pages immediately; keep them as read-only backups until Phase 4 (YOUniverse) is complete.
