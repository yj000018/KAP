# Session Navigator Skill

## Overview

The **Session Navigator** skill offers a comprehensive solution for managing the lifecycle of Manus sessions. It allows users to visualize, organize, merge, archive, and search sessions, transforming scattered conversations into a structured knowledge base.

## Capabilities

- **Visualize**: Display sessions in a hierarchical tree view.
- **Organize**: Tag, categorize, and group sessions by project.
- **Fuse**: Merge related sessions into MASTER SESSIONS.
- **Archive**: Save sessions to Notion with structured summaries.
- **Search**: Planned semantic search via a vector database.
- **Close**: Mark sessions as completed with a final synthesis.

## Core Workflows

### CLOSE
- Convert session title to lowercase.
- Append `(closed YYYY-MM-DD)` suffix.
- Add final synthesis.
- Session becomes read-only.

### ARCHIVE
- Perform CLOSE workflow.
- Export content to Notion.
- Extract metadata and generate a structured summary.
- Embed in vector DB for future search.

### FUSION
- Perform CLOSE workflow.
- Merge sessions into a MASTER SESSION.
- Preserve information with minimal loss (<5%).
- Add Table of Contents and cross-references.
- Link to source sessions.

## Usage

### Generate Session Tree JSON

```bash
cd /home/ubuntu/skills/session-navigator/data/scripts
python3 generate_sessions_tree_v3_enriched.py > sessions.json
```

### Run Fusion Engine

```bash
cd /home/ubuntu/skills/session-navigator/fusion
python3 fusion_engine.py
```

### View Tree (UI)

Upload the generated JSON to the tree view webapp.

## Structure

```
session-navigator/
├── SKILL.md
├── README.md
├── data/
│   ├── scripts/
│   ├── examples/
│   └── backups/
├── fusion/
│   ├── fusion_engine.py
│   ├── templates/
│   └── validators/
├── ui/
│   ├── client/
│   └── server/
├── integrations/
│   ├── notion_archiver.py
│   ├── vector_db_client.py
│   └── git_backup.py
├── docs/
│   ├── architecture.md
│   ├── yos_terminology_and_session_organization.md
│   ├── test_results.md
│   └── fusion_validation_report.md
└── tests/
    └── integration_tests.md
```

## Dependencies

- **Python**: `beautifulsoup4`, `requests`, `json`, `re`, `collections`
- **Node.js**: React, TypeScript, Flask
- **External Services**: Notion API, Vector DB (planned)

## Configuration

- **Notion Integration**: Set up via `memory-manager` skill.
- **Git Backup**: Automatic backups in `/home/ubuntu/.manus_sessions_backup/`.

## Fusion Modes

1. **Manual**: Select sessions, merge, preview, validate, execute.
2. **Semi-Auto**: Command-based semantic search and merge proposal.
3. **Full Auto**: Scheduled analysis and fusion proposals.

## Metrics & Validation

- **Info loss**: <5%
- **Readability**: Flesch score >60
- **Broken links**: 0
- **Compression**: 20-40% optimal

## Known Limitations

1. **Content synthesis**: Placeholder-based, pending OpenAI API integration.
2. **Vector DB**: Not implemented yet.
3. **UI integration**: Tree view needs connection to fusion engine.

## Roadmap

- Integrate OpenAI API for synthesis.
- Implement vector DB for semantic search.
- Connect UI to fusion engine.
- Add automated clustering.

## API Limitations

### Context

The Manus API has undocumented restrictions affecting automation.

- **POST /tasks**: Requires 'prompt' field.
- **PUT /tasks/:id**: Not supported (405 Method Not Allowed).
- **PATCH /tasks/:id**: Untested, potential alternative.

### Practical Consequences

- **Automatic**: Session listing, content retrieval, master session creation, semantic search, content merging.
- **Manual**: Renaming sessions, adding structured synthesis, marking sources, adding archival tags.

### Workaround

- **Hybrid Workflow**: Automatic merge and master session creation, manual archival via UI.

### Future Solutions

- Investigate PATCH support.
- Use Notion for archival.
- Request PUT/PATCH support from Manus.

## Lessons Learned

- Successful merging of five sessions into a master session.
- Manual steps required due to API limitations.
- Importance of correct API parameter usage for task creation.

## Final Results

- **Master Session Created**: ID Ch2kVPS24j3LuhyAvDy5BL
- **Strategy**: Chronological
- **System Operational**: CLI, API, Web
- **API Limitations**: Identified and documented
- **Manual Steps**: Detailed in MERGE_EXECUTION_REPORT.md
