# Y-PIE Cognitive Model

## Purpose

This document defines how Y-PIE transforms visual input into evidence-backed knowledge contributions for KAP.

## Reference chain

```text
Reality
  -> Capture
  -> Observation
  -> Feature
  -> Interpretation
  -> Hypothesis
  -> Knowledge proposal
  -> KAP validation
  -> Reasoning
```

The chain is intentionally layered so that low-level facts remain separable from model-generated interpretations.

## Cognitive object classes

### Asset

A stable reference to an image or image-bearing object. The asset is not knowledge; it is source material.

Required properties:
- source identifier;
- content hash;
- source system;
- capture/import time;
- media type;
- dimensions and technical metadata;
- provenance chain.

### Observation

A machine- or human-produced statement directly grounded in the asset.

Examples:
- the image contains two detected faces;
- dominant hue is blue;
- OCR returned a product name;
- sharpness score is 0.71.

Observations must include:
- method;
- model/tool version;
- confidence where applicable;
- spatial or temporal region;
- evidence reference.

### Feature

A normalized measurable representation used by downstream capabilities.

Examples:
- embedding vector;
- color histogram;
- blur metric;
- face embedding;
- OCR token set;
- composition descriptor.

Features are implementation-level artifacts and are not automatically exposed as user-facing knowledge.

### Interpretation

A semantic reading produced from one or more observations.

Examples:
- likely screenshot of product research;
- probable personal memory;
- abstract geometric artwork;
- image belongs to a visually coherent series.

Interpretations are always model-relative and reversible.

### Hypothesis

A higher-order explanation that may combine visual evidence with KAP context.

Examples:
- this image may belong to the Elysium visual language;
- this series may mark a creative transition period;
- this image may have high emotional significance because of person, place and event context.

Hypotheses must never be silently promoted to fact.

### Knowledge proposal

A structured package submitted to KAP for canonical graph integration.

A proposal includes:
- subject;
- predicate;
- object/value;
- evidence bundle;
- confidence;
- provenance;
- scope;
- validity interval if relevant;
- reversibility status;
- conflict references.

## Epistemic levels

| Level | Meaning | Example |
|---|---|---|
| L0 | Source fact | file hash, EXIF date |
| L1 | Direct observation | OCR text, dominant color |
| L2 | Model interpretation | screenshot, portrait, artwork |
| L3 | Cross-asset inference | same series, duplicate, lineage |
| L4 | Personal-context hypothesis | emotionally significant memory |
| L5 | Creative-cognitive hypothesis | emerging personal visual language |

Higher levels require stronger provenance, explicit confidence and more conservative automation.

## Confidence model

Confidence is multidimensional, not a single universal number.

Recommended fields:
- model confidence;
- evidence sufficiency;
- cross-model agreement;
- corpus support;
- user calibration support;
- temporal stability;
- decision risk.

A deletion recommendation may require lower uncertainty than a search tag, even when both use the same underlying interpretation.

## Human feedback

Human feedback is recorded as an additional evidence source, not as destructive replacement of previous model outputs.

Feedback types:
- confirm;
- reject;
- relabel;
- protect;
- merge;
- split;
- mark ambiguous;
- assign project or meaning.

## Re-analysis

Every interpretation must be reproducible and replaceable.

Re-analysis rules:
1. preserve prior result history;
2. attach model and prompt versions;
3. recompute only affected derived objects;
4. never mutate source files;
5. allow rollback to a previous analysis snapshot.

## Failure behavior

If a model is unavailable or uncertain:
- retain technical metadata;
- mark semantic analysis as pending;
- do not fabricate labels;
- do not block unrelated capabilities;
- do not degrade to destructive action.

## Architectural consequence

Y-PIE is not a monolithic classifier. It is an evidence-producing cognitive pipeline whose outputs remain inspectable, versioned and governable before entering the KAP canonical knowledge layer.
