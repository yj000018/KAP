# KAP Pipeline Access Gaps Backlog

**Gate:** PIPELINE-FEASIBILITY-GATE  
**Version:** 1.0  
**Date:** 2026-07-02

| Gap ID | Pipeline | Gap | Impact | Required Decision / Credential / Tool | Blocking? | Owner | Next Action |
|---|---|---|---|---|---|---|---|
| GAP-001 | PIPE-NOTION-01 | Notion API token returns 401 Unauthorized | HIGH — Notion probe impossible | Refresh `NOTION_API_KEY` or clarify workspace (Yannick vs y-World vs namaste-welfare) | YES for Notion probe | Yannick | Regenerate integration token in correct workspace; update env var |
| GAP-002 | PIPE-OAI-01 | No `conversations.json` export available in sandbox | HIGH — ChatGPT probe impossible | Manual export from chat.openai.com/settings → upload to sandbox | YES for ChatGPT probe | Yannick | Export data from ChatGPT settings; upload `conversations.json` |
| GAP-003 | PIPE-OBS-01 | Obsidian vault not accessible from sandbox | HIGH — Obsidian probe impossible | Mount vault or provide path via `--vault` argument | YES for Obsidian probe | Yannick | Provide vault path or sync vault to sandbox |
| GAP-004 | PIPE-GDRIVE-01 | No `GDRIVE_OAUTH_TOKEN` available | HIGH — GDrive probe impossible | Set up GCP project + OAuth2 credentials; export token | YES for GDrive probe | Yannick | Create GCP project; enable Drive API; generate OAuth2 token |
| GAP-005 | PIPE-MANUS-01 | API returns max 200 tasks; 178/200 are subtasks (noise) | MEDIUM — census limited to recent 200 tasks | Implement subtask filter + cursor pagination beyond 200 | NO — metadata census works within limits | AGT-EXEC-01 | Refine `manus_metadata_census.py` with deeper pagination |
| GAP-006 | PIPE-MEM0-01 | Memory facts have no source linking | MEDIUM — cannot verify canonical truth | Implement source-linking protocol in future pilot | NO — confidence mapper flags this | AGT-EXEC-01 | Design source-linking schema for PILOT-ACQUISITION-GATE |
| GAP-007 | ALL | No acquisition authorization exists for any pipeline | STRUCTURAL — all acquisition blocked | Guardian Architect must authorize PILOT-ACQUISITION-GATE | YES for any acquisition | ChatGPT Guardian Architect | Submit gate reports for review; await authorization |
