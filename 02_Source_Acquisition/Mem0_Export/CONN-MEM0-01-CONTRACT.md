# Connector Contract — CONN-MEM0-01

**Source:** Mem0 / Memory Systems  **Gate:** CONNECTOR-IMPLEMENTATION-GATE

| Field | Value |
|---|---|
| 1. Source Identity | Mem0 — `https://app.mem0.ai` |
| 2. Scope | Memory fact schema probe + confidence mapping. Memories = compressed state, not truth. |
| 3. Authentication | Token via `MEM0_API_KEY` env var |
| 4. Data Types | Memory facts (id, memory text, score) |
| 5. Metadata Fields | id, memory, score, confidence, warning |
| 6. Extraction Method | Mem0 REST API `/v1/memories/` |
| 7. Transformation | Confidence scoring; canonical truth warning flag |
| 8. Storage Targets | `_dry_runs/` only during this gate |
| 9. Deduplication | By memory `id` |
| 10. Validation | JSON schema `memory_fact_metadata.schema.json` |
| 11. Failure Modes | Log API errors; skip on 401/403 |
| 12. Security/Privacy | Token via env var only; never committed |
| 13. Git Persistence | Index JSON committed; credentials excluded |
| 14. Acquisition Boundary | **NO** — schema probe only; no canonicalization without source backing |
| 15. Review Gate | PILOT-ACQUISITION-GATE (future) |
| 16. Next Allowed Action | Dry-run probe; canonicalization requires PILOT-ACQUISITION-GATE + source verification |
