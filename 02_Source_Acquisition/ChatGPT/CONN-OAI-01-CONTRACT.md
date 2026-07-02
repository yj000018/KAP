# Connector Contract — CONN-OAI-01

**Source:** ChatGPT / OpenAI Conversations  **Gate:** CONNECTOR-IMPLEMENTATION-GATE

| Field | Value |
|---|---|
| 1. Source Identity | ChatGPT — `https://chat.openai.com` |
| 2. Scope | Metadata index from exported conversations.json; no API ingestion |
| 3. Authentication | File export (no API key required for parsing) |
| 4. Data Types | Conversation metadata (id, title, timestamps, message count) |
| 5. Metadata Fields | id, title, create_time, update_time, message_count, attachments |
| 6. Extraction Method | Parse `conversations.json` from ChatGPT data export |
| 7. Transformation | Index by title/date; detect attachments and artifacts |
| 8. Storage Targets | `_dry_runs/` only during this gate |
| 9. Deduplication | By conversation `id` |
| 10. Validation | JSON schema `chatgpt_conversation_metadata.schema.json` |
| 11. Failure Modes | Log and skip malformed conversations |
| 12. Security/Privacy | No API key required; export file must not be committed to Git |
| 13. Git Persistence | Index JSON committed; raw export file excluded via .gitignore |
| 14. Acquisition Boundary | **NO** — index only; no full conversation body ingestion |
| 15. Review Gate | PILOT-ACQUISITION-GATE (future) |
| 16. Next Allowed Action | Dry-run schema probe; full acquisition requires PILOT-ACQUISITION-GATE |
