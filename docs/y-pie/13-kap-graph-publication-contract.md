# KAP Graph Publication Contract

## Purpose

Define the minimum contract by which Y-PIE contributes visual knowledge to KAP without creating a competing canonical graph.

## Ownership

Y-PIE owns:
- visual assets and analysis runs;
- observations, embeddings, scores and hypotheses;
- temporary clusters and review queues;
- evidence bundles prepared for publication.

KAP owns:
- canonical entities and identifiers;
- canonical assertions;
- cross-modal graph relations;
- contradiction handling;
- long-term knowledge lifecycle;
- routing into KRE, ART and downstream applications.

## Publication unit

Y-PIE publishes an `EvidenceBundle`.

```yaml
bundle_id: uuid
producer: y-pie
asset_id: immich-or-pie-id
analysis_run_id: uuid
observations: []
interpretations: []
proposed_relations: []
source_provenance: {}
model_provenance: {}
confidence: {}
privacy_class: private
created_at: timestamp
```

## Observation versus assertion

An observation may be published as evidence without becoming canonical knowledge.

Examples:
- OCR detected text;
- dominant palette;
- face region;
- timestamp from EXIF;
- embedding neighbor.

An interpretation is always marked as model-generated:
- probable emotional significance;
- likely project relevance;
- symbolic motif;
- artistic style;
- inferred event.

KAP decides whether an interpretation becomes an assertion.

## Required provenance

Every published item must include:
- originating asset;
- derivative used;
- algorithm or model identifier;
- model version;
- prompt version when applicable;
- analysis timestamp;
- confidence semantics;
- human-validation state;
- applicable policy version.

## Entity resolution loop

```text
Y-PIE proposes entity or relation
  -> KAP resolves or creates canonical entity
  -> KAP returns canonical identifier
  -> Y-PIE stores mapping
  -> later runs reuse mapping but remain revisable
```

Y-PIE must not silently invent permanent person, place, project or concept identifiers.

## Idempotency

Publication must be idempotent by:

```text
producer + asset_id + analysis_run_id + observation_id
```

Retries must not duplicate graph assertions.

## Revision model

New analysis never overwrites historical evidence. It creates a new version and may supersede a previous interpretation.

Allowed statuses:
- active;
- superseded;
- rejected;
- human-confirmed;
- withdrawn.

## Contradictions

Conflicting model results are preserved as separate evidence. Y-PIE may report disagreement but cannot collapse it into a single truth without policy or human validation.

## Privacy boundary

Sensitive face, health, location, family and personal-memory signals remain private by default. KAP publication must preserve or increase privacy restrictions, never weaken them.

## Failure behavior

If KAP is unavailable:
- Y-PIE continues local analysis;
- evidence bundles remain queued;
- no canonical identifiers are fabricated;
- Immich review functions continue;
- publication retries are bounded and observable.

## MVP posture

The MVP may write no graph assertions. It only validates bundle generation and stores bundles locally for later KAP ingestion.

## Acceptance criteria

- schema validation succeeds;
- repeated publication is idempotent;
- all interpretations carry model provenance;
- no source asset mutation;
- no canonical entity creation outside KAP;
- failed publication does not block local review;
- privacy class survives round trip.
