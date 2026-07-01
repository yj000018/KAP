# Reusable FCS Program Structure

This is the abstracted template for any future Fractal Content Studio (FCS) project within yOS.

```text
/program-name/
  README.md

  00-meta/
    project-brief.md
    core-ontology.md
    glossary.md
    style-guide.md
    status-tracker.md

  01-source/
    M01_MODULE_NAME.md
    M02_MODULE_NAME.md

  02-translations/
    fr/
      M01_MODULE_NAME_FR.md
    it/
      M01_MODULE_NAME_IT.md

  03-compiled/
    OUTPUT_DRAFT_EN.md
    OUTPUT_DRAFT_FR.md

  04-research/
    sources.md
    evidence.md

  05-review/
    editorial-notes.md

  06-prompts/
    generation-template.md
    translation-template.md
    review-template.md

  07-integration/
    yos-deployment-rules.md
```

## Usage
To start a new project, copy this directory tree. Define the `core-ontology.md` and `glossary.md` before writing any modules in `01-source`. Use the YAML metadata schema to track module status.
