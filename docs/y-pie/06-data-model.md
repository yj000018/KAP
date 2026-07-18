# Data Model and Provenance

## Core rule

Raw observations and model runs are immutable. User-facing current state is a projection derived from versioned evidence.

## Principal records

### `assets`
Stable visual identity independent of source path.

Fields:
- `asset_id`
- `content_hash`
- `perceptual_hash`
- `source_system`
- `source_id`
- `media_type`
- `created_at_source`
- `ingested_at`
- `status`

### `asset_variants`
Original, edited, resized, RAW/JPEG pairs, Live Photo components and generated derivatives.

### `analysis_runs`
- model and version;
- prompt/template version;
- pipeline version;
- input derivative;
- parameters;
- start/end time;
- cost and runtime;
- raw output;
- validation status.

### `observations`
Atomic machine observations with confidence and optional image region.

### `scores`
Named dimensions, scale, value, confidence and calibration version.

### `embeddings`
Embedding family, model, vector reference and normalization metadata.

### `clusters`
Cluster method, parameters, members, centroid, stability and semantic label.

### `relations`
Typed relationship between PIE objects, with evidence and confidence.

### `reviews`
Human decision, prior value, corrected value, reason and reviewer.

### `recommendations`
Action proposal, policy version, reason set, confidence and lifecycle state.

### `publication_records`
Tracks claims published to KAP and their resolution state.

## Provenance envelope

Every derived field must be traceable through:

```text
projection
  → observation/score
  → analysis run
  → model + prompt + pipeline
  → input derivative
  → source asset
```

## Versioning

- schemas use semantic versions;
- model upgrades create new analysis runs;
- score calibration changes do not rewrite history;
- projections declare the policy and model set used;
- ontology terms carry stable IDs separate from labels.

## Deletion and retention

Deleting an operational projection must not delete source evidence. Asset deletion requests are represented as lifecycle events and must respect source-system policy, quarantine and KAP retention rules.

## Portability

Canonical exports:
- JSONL for full fidelity;
- Parquet for analytics;
- XMP for portable image-adjacent metadata;
- CSV only for simplified review/export.

## Privacy classes

Each record may inherit or refine:
- public;
- private;
- sensitive;
- highly_sensitive;
- restricted_model_processing.
