# KAP Integration Contract

## Ownership boundary

Y-PIE owns:
- source-specific visual asset identity;
- visual observations and model outputs;
- embeddings, clusters and visual similarity;
- visual scoring and recommendations;
- review state and calibration examples.

KAP owns:
- canonical people, places, projects, events and concepts;
- entity resolution across modalities;
- canonical knowledge claims;
- the shared Knowledge Graph;
- retention and knowledge lifecycle policy;
- cross-modal Personal Knowledge Genome.

## Publication unit

Y-PIE publishes an evidence bundle, never an unsupported fact.

```yaml
claim:
  subject_ref: pie:asset:<uuid>
  predicate: depicts
  object_candidate: person:<candidate-id>
  confidence: 0.93
  status: hypothesis

evidence:
  source_asset: pie:asset:<uuid>
  region: [x, y, width, height]
  model: <model-id>
  model_version: <version>
  analysis_run: <run-id>
  observed_at: <timestamp>
```

## KAP lifecycle

1. receive PIE evidence bundle;
2. validate schema and provenance;
3. resolve candidate entities;
4. merge, reject or preserve as unresolved hypothesis;
5. link canonical entities back to the visual asset;
6. expose resulting knowledge to KRE and ART.

## Shared identifiers

- `pie:asset:<uuid>` — stable visual asset
- `pie:analysis:<uuid>` — immutable model run
- `kap:entity:<uuid>` — canonical KAP entity
- `kap:claim:<uuid>` — canonical or pending claim
- `kap:evidence:<uuid>` — evidence item

## Event interface

Y-PIE emits:
- `visual.asset.discovered`
- `visual.asset.normalized`
- `visual.analysis.completed`
- `visual.cluster.updated`
- `visual.hypothesis.created`
- `visual.review.corrected`
- `visual.preference.learned`
- `visual.knowledge.ready`

KAP emits:
- `knowledge.entity.resolved`
- `knowledge.claim.accepted`
- `knowledge.claim.rejected`
- `knowledge.entity.merged`
- `knowledge.context.updated`
- `knowledge.policy.changed`

## Anti-corruption layer

PIE must not depend directly on KAP internal tables. A versioned adapter converts PIE schemas into KAP contracts. This preserves independent evolution and prevents a visual-engine change from corrupting the canonical graph.

## Consistency model

- PIE analysis is eventually consistent with KAP.
- KAP remains authoritative for canonical identity.
- PIE may retain unresolved local candidates.
- conflicts are preserved with provenance, not silently overwritten.
- published claims are append-only; supersession creates a new claim state.
