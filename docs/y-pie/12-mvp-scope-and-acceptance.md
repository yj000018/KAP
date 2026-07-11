# Y-PIE MVP Scope and Acceptance

## Goal

Deliver the smallest useful visual intelligence loop on top of Immich without introducing a second media platform, a second canonical knowledge graph or irreversible automation.

## MVP user outcome

For a representative batch of personal photos, art images, screenshots, products and documents, Y-PIE must:

1. identify the dominant functional category;
2. produce a concise description;
3. extract deterministic technical signals;
4. calculate general visual embeddings;
5. expose similar-image groups;
6. write safe review tags and albums to Immich;
7. preserve full provenance and confidence;
8. allow all generated metadata to be recomputed or removed.

## Included capabilities

### Ingestion

- read assets and metadata from Immich;
- maintain a stable Y-PIE asset identifier mapped to the Immich asset identifier;
- process originals only through read access or temporary derivatives;
- detect new, changed and already-analyzed assets;
- retain source metadata and analysis version.

### Deterministic analysis

- file hash and perceptual hash;
- format, dimensions, orientation and file size;
- date, device and location when available;
- sharpness, blur, exposure and brightness indicators;
- dominant colors and basic palette descriptors;
- screenshot heuristics;
- OCR text when available through an approved local or Immich-provided capability.

### Semantic analysis

One primary functional category:

- art;
- personal memory;
- person or portrait;
- utility;
- screenshot;
- document;
- product research;
- project reference;
- inspiration;
- other or uncertain.

Up to five secondary descriptors may be produced. Classification must retain probabilities, model identity and prompt or inference configuration.

### Similarity

- exact duplicate detection;
- near-duplicate candidate detection;
- generic visual nearest neighbors;
- grouping sufficient for human review;
- no automatic selection or deletion of a winner.

### Safe write-back

Permitted:

- Y-PIE-owned tags;
- Y-PIE-owned albums or review queues;
- generated description in a clearly namespaced field if supported safely;
- analysis status.

Forbidden:

- original-file modification;
- deletion;
- archive or favorite changes;
- face naming;
- album removal;
- overwrite of user-authored metadata.

## Explicit non-goals

The MVP does not include:

- Visual DNA;
- artistic truth scoring;
- emotional-value truth claims;
- graph database deployment;
- Neo4j;
- autonomous KAP publication;
- event-driven microservices;
- Kubernetes;
- distributed model serving;
- custom Immich fork;
- mobile application;
- automatic pruning;
- continuous personal model training.

## Minimum topology

```text
Immich
  |
  | read assets / write namespaced review metadata
  v
Y-PIE batch worker
  |
  +-- deterministic analyzers
  +-- one semantic model adapter
  +-- one embedding model adapter
  |
  v
PostgreSQL Y-PIE schema
```

A queue is optional. A periodic batch command is the default.

## Representative evaluation corpus

Minimum initial corpus: 400 human-selected images.

- 100 art or creative images;
- 100 personal memories and people;
- 100 screenshots, product research and documents;
- 100 ordinary, ambiguous, low-quality or mixed images.

The corpus must include difficult cases:

- artwork saved as screenshots;
- product images with people;
- aesthetically strong utility images;
- emotionally important low-quality images;
- multiple edits or crops of the same image;
- screenshots containing photos;
- AI-generated visual art;
- scanned documents and receipts.

## Acceptance criteria

### Functional

- every supported asset receives a completed or explicit failed analysis state;
- re-running the same version is idempotent;
- a failed model call does not lose deterministic results;
- each result references source asset, model, configuration and timestamp;
- generated Immich metadata is namespaced and removable.

### Quality

On the calibrated evaluation corpus:

- screenshot precision >= 95%;
- document precision >= 90%;
- product-research precision >= 90%;
- primary functional category macro precision >= 85%;
- exact duplicate recall = 100% for byte-identical files;
- near-duplicate candidate precision >= 90% for the reviewed top candidates;
- zero protected original-file mutation;
- zero automatic deletion.

### Operational

- a single command can analyze a bounded batch;
- execution can resume after interruption;
- logs identify asset and stage without exposing sensitive image content;
- costs and model usage are measurable;
- analysis versions can coexist;
- rollback means removing generated metadata and deactivating an analysis version, not restoring media files.

## Exit decision

The MVP is complete only when it is useful for daily review in Immich. A technically functioning pipeline with poor review ergonomics does not pass.

The next phase may begin only after:

1. category corrections are measured;
2. similarity groups are judged useful;
3. metadata write-back is proven reversible;
4. at least two review sessions have been completed by the user;
5. architectural changes required by the MVP have been recorded as ADRs.