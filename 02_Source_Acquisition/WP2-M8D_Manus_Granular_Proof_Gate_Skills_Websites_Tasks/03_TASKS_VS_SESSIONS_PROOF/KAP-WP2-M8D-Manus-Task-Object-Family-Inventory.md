# KAP WP2-M8D — Manus Task Object Family Inventory

**Generated:** 2026-07-01T22:46:22  
**Total objects in dump:** 10,000  
**Unique title patterns:** 12  

## ⚠️ Critical Finding: Pagination Artifact

The `all_tasks_raw.json` file contains only **12 unique titles** across 10,000 entries.  
This is a **pagination artifact** — the Manus API cursor returned the same 100 tasks repeated 100 times.

**Real unique sessions in this dump: 11** (excluding Wide Research Subtask)  
**The 363 Notion sessions remain the authoritative corpus.**

| family_id | title | count | classification | confidence | reason |
|---|---|---:|---|---:|---|
| TF-001 | Wide Research Subtask | 8,900 | BACKGROUND_OPERATIONAL_NOISE | 99% | Parallel processing sub-task generated b |
| TF-002 | Uploaded File Pasted_content_100.txt | 100 | DUPLICATE_AUTOMATION_RUN | 95% | Pagination artifact — same task repeated |
| TF-003 | Veille Bimensuelle MCP pour Y-OS (TECH-ARCHI) | 100 | DUPLICATE_AUTOMATION_RUN | 95% | Pagination artifact — same task repeated |
| TF-004 | Minimal macOS SwiftUI Menu-Bar App for Recent Downloads | 100 | DUPLICATE_AUTOMATION_RUN | 95% | Pagination artifact — same task repeated |
| TF-005 | -- yOS FULL STACK -- | 100 | DUPLICATE_AUTOMATION_RUN | 95% | Pagination artifact — same task repeated |
| TF-006 | Manus Continuity Pack Skill Instructions | 100 | DUPLICATE_AUTOMATION_RUN | 95% | Pagination artifact — same task repeated |
| TF-007 | Demo Examples for Manus' /continuity-pack Skill | 100 | DUPLICATE_AUTOMATION_RUN | 95% | Pagination artifact — same task repeated |
| TF-008 | Can you generate an SVG for the Y logo? | 100 | DUPLICATE_AUTOMATION_RUN | 95% | Pagination artifact — same task repeated |
| TF-009 | yOS Context Protocol & Pack | 100 | DUPLICATE_AUTOMATION_RUN | 95% | Pagination artifact — same task repeated |
| TF-010 | Domain Purchase Options for Elysium Institute | 100 | DUPLICATE_AUTOMATION_RUN | 95% | Pagination artifact — same task repeated |
| TF-011 | Fractal Content Studio Overview | 100 | DUPLICATE_AUTOMATION_RUN | 95% | Pagination artifact — same task repeated |
| TF-012 | How to Demo the /program-os-orchestrator Skill for Manu | 100 | DUPLICATE_AUTOMATION_RUN | 95% | Pagination artifact — same task repeated |
