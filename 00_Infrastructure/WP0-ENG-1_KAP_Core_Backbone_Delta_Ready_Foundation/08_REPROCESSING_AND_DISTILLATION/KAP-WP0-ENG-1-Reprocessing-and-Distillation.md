# KAP Reprocessing & Distillation Protocols

**Program:** KAP — Knowledge Assimilation Program
**Sprint:** WP0-ENG-1
**Status:** Canonical Reference

## 1. Objective

To define how KAP handles schema changes, reprocessing of historical data, and the distillation of raw knowledge into high-value active memory.

## 2. Reprocessing Protocol

Because KAP strictly separates raw acquisition (WP2) from normalization (WP3), we can reprocess the entire historical corpus without ever hitting the source APIs again.

### 2.1 Triggers for Reprocessing
- A new yOS schema is introduced (e.g., adding a mandatory `impact_score` field to session cards).
- A bug is discovered in a previous WP3 normalization script.
- A new distillation model (WP4) is deployed.

### 2.2 Reprocessing Workflow
1. **Freeze WP2:** Pause all new acquisitions.
2. **Branching:** Create a new Git branch for the reprocessing effort.
3. **Run WP3/WP4:** Execute the new normalization/distillation scripts against the existing raw files in the Git repository.
4. **Diff & Audit:** Compare the new normalized outputs against the old ones.
5. **Update Registries:** Update the Asset Tracking Registry to point to the new schema versions.
6. **Merge & Push:** Commit the changes to the main branch.

## 3. Distillation Protocol (WP4)

Raw transcripts and documents are too noisy for active AI memory (context windows). Distillation compresses knowledge while retaining semantic value.

### 3.1 Distillation Rules
- **No Hallucination:** Distillation must only compress, never invent.
- **Traceability:** Every distilled fact must contain a reference (pointer) back to the raw source file and line/section.
- **Format:** Distilled knowledge must be structured (JSON or heavily structured Markdown) with clear entities, decisions, and outcomes.

### 3.2 Distillation Outputs
- **Executive Summaries:** 3-5 bullet points capturing the essence of a session.
- **Entity Extraction:** Identifying projects, people, and concepts (e.g., "Elysium", "WP0-ENG-1").
- **Decision Logs:** Extracting explicit architectural or strategic decisions made during the session.
