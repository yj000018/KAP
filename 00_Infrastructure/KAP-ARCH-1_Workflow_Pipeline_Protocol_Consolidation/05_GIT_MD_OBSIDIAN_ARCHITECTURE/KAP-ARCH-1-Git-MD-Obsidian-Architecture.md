# KAP-ARCH-1: Git / MD / Obsidian Architecture

**Program:** KAP
**Sprint:** KAP-ARCH-1
**Date:** 2026-07-02

## Overview
This document defines the strict boundaries and relationships between Git, Markdown files, and Obsidian within the KAP ecosystem. It resolves previous ambiguities about where knowledge is stored versus where it is viewed.

## 1. The Repository Layer: Git + Markdown

**Status:** Canonical Source of Truth

Git and Markdown constitute the foundational storage layer of KAP. 
- **Git** provides version control, audit trails, and distribution.
- **Markdown** provides a universally readable, portable, and machine-parsable format.

### Rules
1. **Absolute Truth:** If it is not in Git, it does not exist in the KAP corpus.
2. **Format Constraint:** All knowledge objects must be stored as `.md` or `.json` files.
3. **No Hidden State:** No metadata can be stored exclusively in external databases or app-specific formats. All metadata must be in YAML front matter or JSON manifests.

## 2. The Consultation Layer: Obsidian

**Status:** Read-Only Navigation and Visualization Interface

Obsidian is positioned strictly as a local consultation and sense-making layer sitting *on top* of the Git/MD repository.

### Rules
1. **Obsidian is not a database:** It does not store knowledge; it only views the Markdown files managed by Git.
2. **No Obsidian-only features:** Do not rely on Obsidian plugins that create proprietary data structures (e.g., Dataview queries that cannot be read outside Obsidian).
3. **Unidirectional Flow:** Agents write to Git/MD. Obsidian reads from Git/MD. Agents do not interact with Obsidian directly.

## 3. Directory Structure Principles

To ensure Obsidian can navigate the Git repository effectively without breaking agent workflows:

1. **Flat Namespaces within Domains:** Avoid excessively deep folder hierarchies. Rely on tags and MOCs (Maps of Content) for navigation.
2. **Index Files:** Every major directory must have an `index.md` or `README.md` serving as an entry point.
3. **Standardized Naming:** Files must use kebab-case or explicit prefixes (e.g., `KAP-WP0-CORE-1-Execution-Report.md`) to ensure cross-platform compatibility.

## 4. The Role of Maps of Content (MOCs)

MOCs are the bridge between the flat file structure and human sense-making.
- Agents generate and update MOCs dynamically as new knowledge is acquired.
- Obsidian uses these MOCs as primary navigation hubs.
- MOCs must be standard Markdown links, not proprietary queries.
