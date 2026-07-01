# FCS Book Production Model for yOS

This repository is not just a book; it is a reusable **Fractal Content Studio (FCS)** program pattern integrated into **yOS**. It treats book production as a software engineering process.

## 1. Program Structure
The repository is fractal. It separates:
- **Meta/Architecture** (`00-meta`): The rules, ontology, and state.
- **Source Code** (`01-source-en`): The canonical English manuscript.
- **Localization** (`02-translations-*`): The parallel language branches.
- **Build Artifacts** (`04-compiled`): The readable outputs.
- **Logic/Functions** (`07-prompts`): The AI instructions that operate on the source.

## 2. Module Lifecycle
Every Markdown file in `01-source` or `02-translations` is a module. It moves through states defined in its YAML front matter:
`not_started` -> `drafting` -> `draft` -> `in_review` -> `final`

## 3. Metadata Schema
The YAML front matter is the API for the book. It allows scripts or AI agents to query:
- What foundation does this chapter cover?
- Is the French translation up to date with the English source?
- What is the exact word count of Phase III?

## 4. Translation Pipeline
Translations are not separate books; they are localized instances of the source modules.
1. English module reaches `final` state.
2. AI Agent reads `translation-prompt-template.md`, `glossary-canonical.md`, and `PXX_SOURCE.md`.
3. AI Agent outputs `PXX_SOURCE_FR.md`.
4. Human or AI reviews against `translation-doctrine.md`.

## 5. AI-Agent Roles
Within yOS, Manus (or other agents) act as:
- **Production Engineer**: Compiling drafts, updating `manuscript-status.md`.
- **Translator**: Executing the translation pipeline.
- **Reviewer**: Checking modules against the `style-guide.md` and `ontology-map.md`.

## 6. Generalization
This architecture can be cloned for *any* complex, multi-lingual, structured knowledge project in yOS. By replacing the `ontology-map.md` and `glossary-canonical.md`, the same directory structure and prompt templates can produce a technical manual, a policy framework, or a new philosophical treatise.
