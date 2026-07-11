# AI Models, Scoring and Calibration

## Model architecture

Y-PIE uses a routed ensemble rather than one universal model.

### Deterministic/local models
- metadata parsing;
- OCR;
- image quality metrics;
- color and composition features;
- perceptual hashes;
- face/object detection;
- embeddings and clustering.

### Multimodal reasoning models
Used selectively for:
- nuanced classification;
- art critique;
- symbolism and conceptual interpretation;
- memory-context hypotheses;
- project alignment;
- narrative and curation.

### Personal calibration models
Learn ranking and classification corrections from validated user decisions.

## Score families

### Technical
- sharpness
- exposure
- noise
- resolution
- compression
- face quality
- crop integrity

### Artistic
- aesthetic impact
- compositional strength
- originality relative to corpus
- abstraction
- conceptual depth
- symbolic density
- color harmony
- visual coherence
- series strength
- curation priority

### Memory
- probable emotional intensity
- biographical importance
- uniqueness of moment
- relationship significance
- nostalgia potential
- preservation priority

### Operational
- utility value
- expiration probability
- duplicate probability
- redundancy
- review priority
- delete-candidate probability

## Scoring principles

1. No universal composite score is canonical.
2. Every score includes confidence and calibration version.
3. Artistic value is not inferred from technical quality alone.
4. Emotional value remains a hypothesis until personally calibrated.
5. Corpus-relative originality is distinct from universal originality.
6. Recommendations must expose reason codes.

## Example recommendation

```yaml
recommendation: retain_best_variant
confidence: 0.91
reasons:
  - near_duplicate_group
  - stronger_expression
  - higher_technical_quality
  - no_unique_metadata_loss
safety_blocks:
  - user_favorite_present
  - meaningful_person_detected
```

## Multi-model adjudication

High-value art or ambiguous memory assets may be evaluated by multiple models. Agreement, disagreement and rationale are stored. A judge model may summarize disagreement but cannot erase minority interpretations.

## Calibration loop

1. collect explicit corrections;
2. create balanced evaluation sets;
3. measure precision/recall by category;
4. calibrate confidence;
5. update personal ranking model;
6. run regression suite;
7. deploy as a versioned policy.

## Evaluation metrics

- classification precision/recall;
- false-delete-candidate rate;
- best-variant agreement;
- user correction rate;
- calibration error;
- cluster stability;
- retrieval relevance;
- Visual DNA trait stability;
- cost per 1,000 assets;
- latency per pipeline stage.
