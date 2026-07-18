# Y-PIE System Architecture

## Position in Y-OS

```text
Reality
  ↓
Y-PIE perception and interpretation
  ↓
KAP knowledge acquisition and canonicalization
  ↓
KAP Knowledge Graph
  ↓
KRE reasoning and enrichment
  ↓
ART agents and applications
```

Y-PIE is a major Y-OS project and a first-class KAP perception engine. It has its own product identity, runtime and research program, while remaining subordinate to KAP contracts for canonical knowledge.

## Architectural layers

### 1. Source adapters
- Apple Photos export bridge
- Immich adapter
- filesystem and NAS adapter
- camera/import adapter
- generated-art adapter
- future video-frame adapter

### 2. Asset registry
Maintains stable asset identity, source lineage, hashes, variants, derivatives and synchronization state.

### 3. Perception layer
Deterministic and model-based extraction:
- EXIF and technical metadata
- OCR
- people and face references
- objects, scenes and spatial relations
- dominant colors and visual structure
- quality signals
- embeddings

### 4. Interpretation layer
Produces higher-order hypotheses:
- functional category
- memory significance
- artistic dimensions
- project relevance
- symbolism and concepts
- series membership
- visual lineage
- pruning recommendation

### 5. Personal learning layer
Learns from corrections, favorites, retained/deleted variants, project assignments, curation choices and explicit ratings.

### 6. KAP publication layer
Maps visual observations into KAP-compatible entities, relations, claims and evidence bundles.

### 7. Experience layer
- Immich review queues
- search and filters
- curation workbench
- similarity explorer
- Visual DNA dashboard
- agent/API access

## Core services

- `pie-ingest`: source synchronization and identity
- `pie-analyze`: technical and semantic analysis
- `pie-embed`: multimodal embeddings
- `pie-cluster`: similarity, series and lineage
- `pie-score`: value dimensions and recommendations
- `pie-learn`: preference calibration
- `pie-publish`: KAP mapping and write-back
- `pie-orchestrator`: jobs, policies, retries and cost routing
- `pie-api`: stable external contract
- `pie-review`: human validation surfaces

## Storage model

- original assets remain in source storage/Immich;
- PIE operational metadata lives in PostgreSQL;
- vector representations live in a vector-capable store, initially PostgreSQL;
- model outputs are immutable analysis runs;
- current projections are derived from those runs;
- KAP stores canonical entities and cross-modal relations;
- portable metadata exports use JSON and XMP where possible.

## Deployment topology

Initial:
- Immich server/NAS
- one PIE Docker Compose stack
- PostgreSQL
- local ML worker
- optional cloud multimodal provider

Scale-out:
- queue-backed workers
- GPU worker pool
- model router
- object storage
- distributed vector index
- independent review UI

## Failure boundaries

Y-PIE must continue to function when:
- a cloud model is unavailable;
- Immich API changes;
- one model produces malformed output;
- a job is interrupted;
- an asset is moved or re-imported;
- KAP is temporarily unavailable.

All jobs must be idempotent, resumable and versioned.