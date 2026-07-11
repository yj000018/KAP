# Pipelines and Lifecycle

## Processing stages

### Stage 0 — Discovery
Detect new or changed assets without modifying originals.

### Stage 1 — Normalization
Resolve stable identity, hashes, source metadata, variants, timestamps, EXIF and derivatives.

### Stage 2 — Fast local perception
Run inexpensive local analysis on all eligible assets:
- OCR;
- blur/noise/exposure;
- dominant colors;
- screenshot/document detection;
- face/object candidates;
- generic embedding;
- exact and near-duplicate signals.

### Stage 3 — Semantic interpretation
Assign functional classes, captions, objects, scenes, activities, styles and concept candidates.

### Stage 4 — Specialist routing
Only qualifying assets enter specialized flows:
- art intelligence;
- memory intelligence;
- document/utility handling;
- product research;
- project relevance;
- sensitive-content policy.

### Stage 5 — Corpus-relative analysis
Compute nearest neighbors, clusters, series, best variants, novelty and lineage using the full or scoped corpus.

### Stage 6 — Scoring and recommendation
Combine observations, personal calibration and safety policies into explainable recommendations.

### Stage 7 — Human review
Review queues for ambiguous, important or potentially destructive decisions.

### Stage 8 — KAP publication
Publish evidence-backed claims and relations through the integration contract.

### Stage 9 — Learning
Convert validated corrections into calibration data and preference-model updates.

## Routing strategy

```text
100% metadata + fast local analysis
20–40% richer local semantic analysis
5–15% deep multimodal analysis
1–3% premium multi-model critique
```

Percentages are configurable and should be determined by corpus composition, hardware, privacy and budget.

## Job requirements

Every job must be:
- idempotent;
- resumable;
- observable;
- bounded by policy;
- versioned;
- independently retryable;
- safe under duplicate delivery.

## Initial batches

Calibration corpus:
- 100 art images;
- 100 strong memories;
- 100 utility/screenshots/products;
- 100 ordinary or low-quality photos.

The first production run must be limited and read-only except for non-destructive tags/albums.

## Reprocessing triggers

- new model version;
- ontology change;
- calibration update;
- user correction;
- new KAP context;
- asset edit or replacement;
- project ontology update.

## Write-back policy

Allowed initially:
- tags;
- albums;
- descriptions;
- review queues.

Disallowed initially:
- source-file mutation;
- automatic favorite changes;
- automatic archive;
- automatic deletion.
