# yOS Program Pattern

## Overview
This repository implements the **FCS (Fractal Content Studio)** pattern within **yOS**. It is designed to be a living, programmatic architecture rather than a static folder of documents.

## Core Principles
1. **Metadata as State**: The YAML front matter in every module is the single source of truth for the project's state. It replaces external tracking spreadsheets.
2. **Deterministic Translation**: Translations are deterministic functions of the source module + the canonical glossary + the translation doctrine.
3. **Modular Compilation**: The final book is an artifact compiled from the source modules, not a document that is edited directly.

## Manus / AI Agent Interaction Rules
When Manus or another agent interacts with this repository:
1. **Always read `00-meta` first**: Before drafting or revising, the agent must load the `ontology-map.md`, `style-guide.md`, and `glossary-canonical.md` into context.
2. **Update Status**: If an agent changes a module's status (e.g., from `drafting` to `draft`), it must also update `00-meta/manuscript-status.md`.
3. **Strict YAML**: Agents must never break the YAML schema. Missing fields should be marked `null`, not deleted.

## Integration with yOS
This pattern allows yOS to treat book production as a managed program. Future scripts can:
- Auto-generate PDF/EPUB artifacts via CI/CD pipelines when modules reach `final` status.
- Trigger translation tasks automatically when an English module is updated.
- Generate web-ready Markdown for Notion or direct publishing.
