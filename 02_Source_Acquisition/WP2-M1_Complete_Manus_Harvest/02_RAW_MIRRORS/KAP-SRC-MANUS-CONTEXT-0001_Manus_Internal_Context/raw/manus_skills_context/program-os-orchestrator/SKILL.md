---
name: program-os-orchestrator
description: Use this skill to orchestrate complex, multi-phase programs (like research, canonicalization, or content generation) using the Program OS pattern. It provides workflows for sequential execution, state management, multi-model review, and persistence.
---

# Program OS Orchestrator

This skill encapsulates the "Program OS" pattern—a highly structured, sequential workflow for executing complex, multi-stage tasks reliably. It was originally extracted from the ELYSIUM Civilizational Ontology canonicalization process.

Use this skill when you need to execute a "mega-prompt" or a large project that requires strict orchestration, validation gates, and state tracking.

## Core Principles

1. **Strict Sequential Execution**: Never maximize parallelism across different conceptual stages. Each stage must finish before the next begins.
2. **Single Source of Truth**: Maintain a `PROGRAM_STATE` and `DOCUMENTATION_REGISTRY` to track progress.
3. **Validation Gates**: Implement checkpoints (e.g., Chief Architect Audits) after critical blocks of work.
4. **Multi-Model Workflows**: Use specialized models for different roles (e.g., ChatGPT for drafting, Claude for reviewing).
5. **Persistence**: Ensure outputs are properly versioned (Git) and pushed to long-term memory (Mem0/Notion).

## Workflow Overview

When orchestrating a Program OS project, follow these steps:

1. **Setup Program Office**: Create the core tracking files.
2. **Execute Sequential Stages**: Run the work in defined batches.
3. **Multi-Model Review**: Route outputs to reviewer models (e.g., Claude) for QA.
4. **Canonicalization & Audits**: Run integrity checks and generate audit reports.
5. **Persistence & Packaging**: Commit to Git, push to Mem0, and package deliverables.

## 1. Setup Program Office

Initialize the directory structure and core tracking files.

```bash
mkdir -p PROJECT_NAME/00_PROGRAM_OFFICE
```

Required files (see `templates/` for schemas):
- `PROGRAM_STATE.md` / `.json`: Tracks current phase, pass, and overall status.
- `DOCUMENTATION_REGISTRY.md` / `.json`: Tracks the status of all generated artifacts.
- `DECISION_LOG.md`: Records key architectural decisions.
- `RISK_REGISTER.md`: Tracks potential blockers.

## 2. Execute Sequential Stages

Break the project into explicit stages. **Do not execute multiple stages simultaneously.**

Example Stage progression:
- Stage 1: Recovery/Audit of previous work
- Stage 2: Generation Block A
- Stage 3: Validation Gate A
- Stage 4: Generation Block B
- Stage 5: Validation Gate B

Write specific Python scripts for each stage to ensure reproducibility.

## 3. Multi-Model Review Workflow

For high-quality outputs, use a "Draft → Review → Revise" pipeline.

1. **Architect (Draft)**: Generate the initial content.
2. **Reviewer (Claude)**: Critique the content using the Anthropic API. Use `claude-sonnet-4-6` for standard reviews and `claude-opus-4-8` for heavy architectural reviews.
3. **Architect (Revise)**: Integrate the critique.

*Note: See `references/api_routing_protocol.md` for details on setting up the Anthropic API call.*

## 4. Canonicalization & Audits

Before finalizing a "Pass" or phase, run comprehensive audits:

- **Package Integrity Audit**: Check for missing or zero-byte files.
- **Canonical Facts Lock**: Verify that no stale claims exist across the corpus.
- **State Synchronization**: Ensure the Program State matches the actual file system.

Generate a `FINAL_AUDIT.md` report documenting the results of these checks.

## 5. Persistence & Packaging

Ensure the work is securely persisted.

1. **Git Versioning**:
   ```bash
   git init
   git add -A
   git commit -m "Pass completion"
   git tag pass-X.X
   git bundle create backup.bundle --all
   ```
2. **GitHub Push** (if public/authorized): Push to the remote repository.
3. **Mem0 Persistence**: Push canonical facts to cross-session memory. *(Note: If Mem0 timeouts occur due to telemetry, set `POSTHOG_DISABLED=true`, `MEM0_TELEMETRY=false`, and `ANONYMIZED_TELEMETRY=false` in the environment).*
4. **Packaging**: Create a clean ZIP file containing the repository and all final reports.

## Reference Materials

- **`templates/program_os_schemas.md`**: JSON schemas for State, Registry, and Logs.
- **`references/api_routing_protocol.md`**: Guide for executing the multi-model review pipeline using the Anthropic API.
