# ELYSIUM Book Repository

This is the Fractal Content Studio (FCS) repository for **ELYSIUM**, a civilizational ontology and transition map.

## Architecture
This repository treats book production as a software engineering process. It is designed for modular writing, parallel translation, and AI-assisted production within the yOS environment.

- `00-meta/`: The rules, ontology, glossary, and status trackers.
- `01-source-en/`: The canonical English manuscript modules.
- `02-translations-*/`: Localized modules (French, Italian).
- `04-compiled/`: Readable output drafts.
- `07-prompts/`: AI instructions for generating, translating, and reviewing content.

## Getting Started
1. Read `00-meta/book-brief.md` and `00-meta/ontology-map.md`.
2. Review the `00-meta/manuscript-status.md` to see current progress.
3. Use the templates in `07-prompts/` to generate or translate new modules.
