# KAP-ARCH-1: Project Knowledge Layer

**Program:** KAP
**Sprint:** KAP-ARCH-1
**Date:** 2026-07-02

## Overview
The Project Knowledge Layer defines how active projects maintain their state, history, and context within the Git/MD repository. It replaces the previous reliance on Notion for project tracking.

## 1. The Project Fact Sheet

Every active project must have a canonical `Project_Fact_Sheet.md` stored at the root of its project directory in Git.

### Structure of the Fact Sheet
- **Metadata (YAML):** Status, Owner, Start Date, Target Date, Tags.
- **Executive Summary:** The core objective and current state in 3 sentences.
- **Architecture/Design Decisions:** Canonized rules specific to the project.
- **Active Blockers:** What is currently preventing progress.
- **Milestones/Roadmap:** High-level sequence of work packages.
- **Related Sessions:** Links to all `session_card.md` files that contributed to the project.

## 2. The Project Delta Process

Projects are not static. They evolve through sessions.
- **Input:** When an agent starts a session for a project, it must first read the `Project_Fact_Sheet.md`.
- **Output:** When a session concludes, the LMP v2 pipeline (or equivalent) must compute the delta (what changed) and update the `Project_Fact_Sheet.md`.

## 3. Separation of Project State vs. Task State

- **Task State:** Managed by Manus (e.g., the current execution loop). Ephemeral.
- **Session State:** Managed by the Archive Pipeline (`session_card.md`). Immutable once archived.
- **Project State:** Managed by the Project Fact Sheet. Living, mutable, and authoritative.

## 4. No Implicit Project Context

Agents must not rely on their own hidden context window to remember project state across sessions. The Project Fact Sheet is the only authorized mechanism for context continuity across sessions.
