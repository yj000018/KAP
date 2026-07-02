# KAP Dry-Run Policy

**Version:** 1.0  
**Gate:** CONNECTOR-IMPLEMENTATION-GATE  

## 1. What is a Dry-Run?
A dry-run is a connector execution that fetches **metadata only** — no full content, no body ingestion, no corpus creation. It validates that the connector mechanics work (auth, pagination, schema) without triggering acquisition.

## 2. Allowed Metadata/Sample Limits
- Maximum 200 items per dry-run.
- Metadata fields only (id, title, timestamps, size, type).
- No message bodies, document content, or conversation text.

## 3. Forbidden During Dry-Run
- Full task/conversation/document body ingestion.
- Broad semantic extraction.
- Writing to canonical knowledge branches (`03_Normalized_Knowledge/`, `04_Distillation/`).
- Deletion or mutation of source systems.
- Creating ZIPs as primary output.

## 4. Output Isolation
All dry-run outputs must be written to `[connector]/_dry_runs/` only. Never to canonical branches.

## 5. Access-Limited Dry-Runs
If credentials are unavailable, the dry-run must:
- Print `[SKIP] <credential> not set — access-limited dry-run`.
- Document the access gap in the Gate Report.
- Not block the gate if the script and schema are complete.

## 6. Credential Handling
- API keys via environment variables only.
- Never store credentials in committed files.
- Use `.gitignore` to exclude raw export files (e.g., `conversations.json`).

## 7. WP3 Verification
Before completing a dry-run, confirm: "No WP3 acquisition was performed."

## 8. Escalation to Guardian Architect
If a dry-run reveals unexpected data volume, sensitive content, or scope ambiguity, stop and escalate via a `HOLD` status in the Gate Report.
