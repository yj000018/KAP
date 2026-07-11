# Y-PIE — Photo Intelligence Engine

## Status

Architecture canon — foundation draft.

## Mission

Y-PIE is the visual cognitive system of Y-OS. It transforms visual reality into structured perception, knowledge and reasoning inputs for KAP.

Core chain:

```text
Reality
  ↓
Perception
  ↓
Knowledge
  ↓
Reasoning
```

Y-PIE owns visual perception and visual intelligence. KAP owns the canonical knowledge graph and cross-modal knowledge model. Y-PIE publishes evidence-backed visual observations, interpretations and relations into KAP; it does not create a parallel knowledge silo.

## Founding principle

> Every item perceived by Y-OS, regardless of modality, must be transformed into linked knowledge objects in the common KAP graph rather than stored as isolated content.

## Product identity

- **Name:** Y-PIE
- **Expanded name:** Photo Intelligence Engine
- **System role:** Visual Cognitive System of Y-OS
- **KAP role:** visual acquisition, perception and interpretation engine
- **Strategic outcome:** a Personal Knowledge Genome enriched by a Visual DNA model

## Canon map

1. [Vision and principles](00-vision-and-principles.md)
2. [System architecture](01-system-architecture.md)
3. [KAP integration contract](02-kap-integration-contract.md)
4. [Visual ontology](03-visual-ontology.md)
5. [Visual Knowledge Graph projection](04-visual-knowledge-graph.md)
6. [Visual DNA and Personal Knowledge Genome](05-visual-dna.md)
7. [Data model and provenance](06-data-model.md)
8. [Pipelines and lifecycle](07-pipelines.md)
9. [AI models, scoring and calibration](08-ai-and-scoring.md)
10. [Safety, privacy and governance](09-governance.md)
11. [Roadmap and milestones](10-roadmap.md)
12. [Agent operating guide](AGENTS.md)
13. [Decision records](adr/README.md)
14. [Research tracks](research/README.md)

## Scope boundaries

Y-PIE is not merely:

- a photo organizer;
- an Immich plugin;
- a tagging pipeline;
- a duplicate cleaner;
- a single aesthetic scorer.

It is a long-lived visual cognition platform that supports:

- ingestion and normalization;
- visual perception;
- semantic interpretation;
- memory significance estimation;
- artistic and creative intelligence;
- similarity, series and lineage detection;
- visual language discovery;
- curation and narrative generation;
- pruning recommendations;
- publication of visual knowledge into KAP.

## Initial implementation posture

The canon precedes code. The first implementation must be small, reversible and observable:

1. read-only ingestion from Immich;
2. deterministic technical analysis;
3. semantic classification;
4. evidence and confidence capture;
5. write-back only as tags/albums/review queues;
6. no automatic deletion;
7. all results versioned and reproducible.
