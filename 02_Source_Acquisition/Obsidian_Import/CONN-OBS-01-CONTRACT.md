# Connector Contract — CONN-OBS-01

**Source:** Obsidian / Local Markdown  **Gate:** CONNECTOR-IMPLEMENTATION-GATE

| Field | Value |
|---|---|
| 1. Source Identity | Local Obsidian vault (filesystem) |
| 2. Scope | Vault structure scan, frontmatter audit, wikilink mapping. No merge. |
| 3. Authentication | Local filesystem — provide vault path via `--vault` argument |
| 4. Data Types | Markdown note metadata (path, size, frontmatter, wikilinks) |
| 5. Metadata Fields | path, size_bytes, folder, has_frontmatter, wikilinks |
| 6. Extraction Method | Recursive filesystem walk + regex parsing |
| 7. Transformation | Frontmatter detection, wikilink extraction |
| 8. Storage Targets | `_dry_runs/` only during this gate |
| 9. Deduplication | By file path |
| 10. Validation | JSON schema `obsidian_note_metadata.schema.json` |
| 11. Failure Modes | Skip unreadable files; log encoding errors |
| 12. Security/Privacy | No vault content committed to Git; index JSON only |
| 13. Git Persistence | Index JSON committed; vault files excluded via .gitignore |
| 14. Acquisition Boundary | **NO** — scan only; no merge into KAP knowledge branches |
| 15. Review Gate | PILOT-ACQUISITION-GATE (future) |
| 16. Next Allowed Action | Dry-run scan; merge requires PILOT-ACQUISITION-GATE |
