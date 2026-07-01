# Session Navigator Skill

## Overview

The **Session Navigator** skill provides comprehensive lifecycle management for Manus sessions. It enables users to visualize, organize, fuse, archive, and search their sessions, transforming scattered conversations into a structured, navigable knowledge base.

## Capabilities

1. **Visualize**: Hierarchical tree view of all sessions
2. **Organize**: Tag, categorize, and group sessions by project
3. **Fuse**: Intelligently merge related sessions into MASTER SESSIONS
4. **Archive**: Save sessions to Notion with structured summaries
5. **Search**: Semantic search via vector database (planned)
6. **Close**: Mark sessions as completed with final synthesis

## Core Workflows

### CLOSE
Mark a session as completed:
- Title → lowercase
- Add `(closed YYYY-MM-DD)` suffix
- Append final synthesis
- Session becomes read-only

### ARCHIVE
CLOSE + Save to Notion:
- Export verbatim content
- Create Notion page in Memory Hub
- Extract metadata (tags, status, priority)
- Generate structured summary
- Embed in vector DB for search

### FUSION
CLOSE + Merge into MASTER SESSION:
- Combine related sessions intelligently
- Create new MAJUSCULE session
- Preserve all information (target <5% loss)
- Add ToC and cross-references
- Link to source sessions

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

Navigate to the tree view webapp (Session B deliverable) and upload the generated JSON.

## Structure

```
session-navigator/
├── SKILL.md                    # This file
├── README.md                   # User guide
├── data/
│   ├── scripts/                # Python scripts for data extraction
│   ├── examples/               # Sample JSON outputs
│   └── backups/                # Git-tracked backups
├── fusion/
│   ├── fusion_engine.py        # Core fusion logic
│   ├── templates/              # Master session templates
│   └── validators/             # Info loss & readability validators
├── ui/
│   ├── client/                 # React tree view (from Session B)
│   └── server/                 # Flask API server (from Session B)
├── integrations/
│   ├── notion_archiver.py      # Notion export logic
│   ├── vector_db_client.py     # Vector search (planned)
│   └── git_backup.py           # Automated Git backup
├── docs/
│   ├── architecture.md         # System architecture
│   ├── yos_terminology_and_session_organization.md
│   ├── test_results.md
│   └── fusion_validation_report.md
└── tests/
    └── integration_tests.md
```

## Dependencies

### Python
- `beautifulsoup4` (for HTML parsing)
- `requests` (for API calls)
- Standard library: `json`, `re`, `collections`

### Node.js (for UI)
- React
- TypeScript
- Flask (Python backend)

### External Services
- Notion API (via MCP)
- Vector DB (Chroma or Pinecone, planned)

## Configuration

### Notion Integration
Set up via `memory-manager` skill. Ensure Notion MCP server is configured.

### Git Backup
Automatic backups are stored in `/home/ubuntu/.manus_sessions_backup/`.

## Fusion Modes

### 1. Manual
Select sessions in tree view → Click "Merge" → Preview → Validate → Execute

### 2. Semi-Auto
Command: `"Regroup sessions about Project X"`
- Semantic search finds related sessions
- Proposes merge groups
- User validates each group

### 3. Full Auto (Scheduled)
Cron job (1x/week):
- Analyzes all non-archived sessions
- Detects similar clusters
- Proposes fusions
- User validates via notification

## Metrics & Validation

Every fusion is validated for:
- **Info loss**: Target <5%
- **Readability**: Flesch score >60
- **Broken links**: 0
- **Compression**: 20-40% optimal

## Known Limitations

1. **Content synthesis**: Current implementation uses placeholders. Full LLM-powered synthesis requires OpenAI API integration.
2. **Vector DB**: Not yet implemented. Semantic search is planned.
3. **UI integration**: Tree view webapp (Session B) needs to be connected to fusion engine.

## Roadmap

- [ ] Integrate OpenAI API for intelligent content synthesis
- [ ] Implement vector DB (Chroma) for semantic search
- [ ] Connect UI tree view to fusion engine
- [ ] Add automated clustering for full-auto mode
- [ ] Deploy to production environment

## Credits

**Created by**: Manus Agent  
**Date**: 2026-02-15  
**Source Sessions**:
- Session A: https://manus.im/share/sVUnGFiX7EYxQB47zcdsEA (Data Layer)
- Session B: https://manus.im/share/iDnRc9aX7GXxhoPKUQdsEY (UI Layer)

**Tags**: yOS, session-management, fusion, notion, tree-view, Manus

## Support

For issues or questions, refer to:
- `docs/architecture.md` for system design
- `docs/fusion_validation_report.md` for validation details
- `docs/yos_terminology_and_session_organization.md` for terminology

---

**Version**: 1.0 (Pilot)  
**Status**: Active Development
