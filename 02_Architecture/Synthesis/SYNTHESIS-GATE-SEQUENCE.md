# Synthesis Gate Sequence

## Overview

The synthesis pipeline transforms raw acquired sources into exploitable knowledge through a controlled sequence of gates. Each gate has prerequisites, outputs, and review checkpoints.

## Gate Sequence

```
ACQUISITION-COMPLETE-GATE
    ↓
FRAGMENT-NORMALIZATION-GATE
    ↓
CLAIM-EXTRACTION-GATE
    ↓
THOUGHT-LINE-SEEDING-GATE
    ↓
DECISION-THREAD-RECONSTRUCTION-GATE
    ↓
IMPASSE-REGISTRY-SEED-GATE
    ↓
CONTRADICTION-DETECTION-GATE
    ↓
CURRENT-BEST-KNOWLEDGE-PILOT-GATE
    ↓
HUMAN-REVIEW-GATE
    ↓
EXPLOITATION-LAYER-GENERATION-GATE
    ↓
SCALE-UP-GATE
```

## Gate Details

### ACQUISITION-COMPLETE-GATE

**Prerequisites:** All source connectors have completed their acquisition runs.

**Checks:**
- Manus factsheets: complete (194/194)
- Notion pages: census complete, pilot pages acquired
- ChatGPT conversations: export processed
- Obsidian vaults: scanned and indexed
- GitHub repos: metadata indexed
- Web references: captured

**Output:** Acquisition completion report with coverage metrics.

### FRAGMENT-NORMALIZATION-GATE

**Prerequisites:** ACQUISITION-COMPLETE-GATE passed.

**Purpose:** Normalize all acquired fragments into a standard format with consistent metadata.

**Checks:**
- All fragments have: id, source_type, title, created_at, content_hash
- All fragments are stored in canonical location
- No orphan fragments (all linked to source registry)
- Deduplication pass complete (exact duplicates linked)

**Output:** Normalized fragment corpus + deduplication report.

### CLAIM-EXTRACTION-GATE

**Prerequisites:** FRAGMENT-NORMALIZATION-GATE passed.

**Purpose:** Extract atomic claims from fragments. Each claim is a single assertable statement.

**Checks:**
- Claims extracted from pilot sample (10% of corpus)
- Each claim has: id, text, source_fragments, confidence, domain
- Quality review on sample (precision > 80%)
- No hallucinated claims (all traceable to source)

**Output:** Claim corpus (pilot) + extraction quality report.

### THOUGHT-LINE-SEEDING-GATE

**Prerequisites:** CLAIM-EXTRACTION-GATE passed.

**Purpose:** Identify initial Thought Lines by clustering related claims.

**Checks:**
- Minimum 10 Thought Lines identified
- Each has: id, title, domain, initial claims, maturity level
- No orphan claims (all assigned to at least one Thought Line)
- Human review of Thought Line titles and groupings

**Output:** Initial Thought Line Registry.

### DECISION-THREAD-RECONSTRUCTION-GATE

**Prerequisites:** THOUGHT-LINE-SEEDING-GATE passed.

**Purpose:** Identify and reconstruct decision threads from the corpus.

**Checks:**
- Minimum 20 decisions identified
- Each has: id, text, status, decided_at, rationale
- Supersession relationships mapped
- Active vs superseded clearly marked

**Output:** Decision Thread Registry.

### IMPASSE-REGISTRY-SEED-GATE

**Prerequisites:** DECISION-THREAD-RECONSTRUCTION-GATE passed.

**Purpose:** Document known dead ends, failed approaches, and rejected options.

**Checks:**
- Minimum 10 impasses documented
- Each has: id, description, why_failed, what_replaced_it
- Linked to relevant Thought Lines and Decisions

**Output:** Impasse Registry.

### CONTRADICTION-DETECTION-GATE

**Prerequisites:** All previous gates passed.

**Purpose:** Systematically detect contradictions across the corpus.

**Checks:**
- All claim pairs checked for contradiction
- Contradictions classified by type
- Explicit reversals auto-resolved
- Implicit contradictions flagged for review

**Output:** Contradiction report + resolution queue.

### CURRENT-BEST-KNOWLEDGE-PILOT-GATE

**Prerequisites:** CONTRADICTION-DETECTION-GATE passed.

**Purpose:** Generate CBK entries for top 10 Thought Lines.

**Checks:**
- 10 CBK entries generated
- Each follows CBK protocol
- Each has confidence level
- Each cites sources
- Each acknowledges contradictions/gaps

**Output:** Pilot CBK corpus.

### HUMAN-REVIEW-GATE

**Prerequisites:** CBK-PILOT-GATE passed.

**Purpose:** Architect reviews pilot CBK entries for quality and accuracy.

**Checks:**
- All 10 entries reviewed
- Corrections applied
- Quality threshold met (>80% accuracy)
- Feedback incorporated into extraction/synthesis prompts

**Output:** Validated CBK pilot + quality metrics.

### EXPLOITATION-LAYER-GENERATION-GATE

**Prerequisites:** HUMAN-REVIEW-GATE passed.

**Purpose:** Generate both human (Obsidian) and AI (JSON indexes) exploitation layers.

**Checks:**
- Obsidian vault generated with all views
- JSON indexes generated for all registries
- Cross-references working (wikilinks resolve)
- Dataview queries functional
- AI query patterns tested

**Output:** Exploitation layers (Obsidian vault + JSON indexes).

### SCALE-UP-GATE

**Prerequisites:** EXPLOITATION-LAYER-GENERATION-GATE passed.

**Purpose:** Apply the validated pipeline to the full corpus.

**Checks:**
- Full claim extraction complete
- All Thought Lines populated
- All CBK entries generated
- Full exploitation layers generated
- Performance metrics acceptable

**Output:** Complete KAP knowledge system.
