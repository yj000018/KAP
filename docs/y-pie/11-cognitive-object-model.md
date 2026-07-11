# Y-PIE Cognitive Object Model

## Purpose

Define the smallest stable set of cognitive objects required to transform visual media into evidence-backed knowledge without collapsing perception, interpretation and truth into one layer.

## Reference chain

```text
Reality
  -> Capture
  -> Asset
  -> Observation
  -> Interpretation
  -> Hypothesis
  -> Assertion candidate
  -> KAP knowledge object
  -> Reasoning output
```

Each transition must preserve provenance, confidence and reversibility.

## Core objects

### 1. VisualAsset

A managed representation of an image or image-bearing object.

Required fields:

- `asset_id`
- `source_system`
- `source_asset_id`
- `content_hash`
- `media_type`
- `capture_time`
- `ingested_at`
- `original_locator`
- `derivative_locator`
- `source_metadata`
- `protection_flags`

A VisualAsset is not knowledge. It is evidence-bearing media.

### 2. Observation

A machine- or human-produced statement about directly detectable properties.

Examples:

- image dimensions are 4032 x 3024;
- dominant palette contains dark blue and warm beige;
- OCR detected a product name;
- three face regions are present;
- the image is probably a screenshot.

Observations should be as close as possible to measurable evidence.

Required fields:

- `observation_id`
- `asset_id`
- `observation_type`
- `value`
- `confidence`
- `method`
- `model_or_rule_version`
- `evidence_region`
- `created_at`

### 3. Interpretation

A contextual reading derived from observations.

Examples:

- likely product-research screenshot;
- likely personal memory;
- composition has strong negative space;
- image may belong to an organic-architecture series.

Interpretations are explicitly model-dependent and may conflict.

### 4. Hypothesis

A higher-order proposition that requires multiple observations, contextual knowledge or corpus comparison.

Examples:

- this image is a hidden artistic gem;
- this work marks a stylistic transition;
- this recurring spiral may be part of the user's visual vocabulary;
- this event likely has high biographical significance.

Hypotheses must never masquerade as direct observations.

### 5. EvidenceBundle

A reproducible package containing the evidence supporting an interpretation or hypothesis.

It contains:

- referenced assets;
- source regions;
- observations;
- model outputs;
- prompts when applicable;
- feature vectors or stable references to them;
- calibration version;
- counterevidence;
- provenance chain.

### 6. AssertionCandidate

A proposition eligible for publication to KAP.

Examples:

- asset depicts a known person;
- asset belongs to project CasaTAO;
- image is a variant of another asset;
- visual series expresses a recurring symbolic motif.

An AssertionCandidate includes lifecycle state:

```text
proposed -> reviewed -> accepted | rejected | superseded
```

### 7. FeedbackEvent

An explicit user or trusted-system correction.

Examples:

- recategorized Utility to Art;
- marked false face identity;
- protected image from pruning;
- selected one image as series hero;
- rejected an archetype interpretation.

FeedbackEvents are immutable training and calibration evidence.

### 8. DecisionRecommendation

A non-destructive proposed action.

Allowed initial actions:

- keep;
- favorite candidate;
- add to collection;
- stack;
- archive candidate;
- review;
- delete candidate.

The object must include reasons, confidence, policy checks and blocking flags.

## Epistemic classes

Every generated statement must belong to exactly one class:

1. `measured`
2. `detected`
3. `inferred`
4. `hypothesized`
5. `human_asserted`
6. `canonically_accepted`

This prevents a model-generated aesthetic interpretation from being treated like a measured EXIF value.

## Confidence model

Confidence is not a universal probability. It must identify its basis:

- detector confidence;
- classifier confidence;
- calibrated empirical precision;
- human confidence;
- consensus confidence;
- corpus-relative stability.

Store both numeric score and confidence type.

## Contradictions

Conflicting interpretations are preserved, not overwritten.

Example:

```yaml
claim: primary_category
candidates:
  - value: art
    confidence: 0.66
    source: vision-model-a
  - value: project_reference
    confidence: 0.74
    source: vision-model-b
resolution: unresolved
```

## Object ownership

| Object | Primary owner |
|---|---|
| VisualAsset | Y-PIE |
| Observation | Y-PIE |
| Interpretation | Y-PIE |
| Hypothesis | Y-PIE |
| EvidenceBundle | Y-PIE |
| AssertionCandidate | Y-PIE until publication |
| Canonical knowledge assertion | KAP |
| Cross-modal entity | KAP |
| Reasoning result | KRE or consuming agent |
| FeedbackEvent | Y-PIE with KAP reference |

## Non-goals

This model does not require:

- a separate graph database for Y-PIE;
- a universal ontology before MVP;
- all objects to be exposed in Immich;
- LLM processing for every asset;
- immediate publication of every interpretation to KAP.

## MVP subset

The MVP implements only:

- VisualAsset;
- Observation;
- Interpretation;
- EvidenceBundle;
- DecisionRecommendation;
- FeedbackEvent.

Hypothesis and AssertionCandidate publication may remain disabled until the KAP integration contract is tested.