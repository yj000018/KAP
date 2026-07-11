# Y-PIE Agent Operating Guide

## Mission guardrail

Y-PIE is the visual cognitive system of Y-OS and a KAP perception engine. Do not reduce it to a photo organizer, tagging script or Immich extension.

## Mandatory architectural rules

1. KAP owns canonical knowledge and the shared Knowledge Graph.
2. PIE owns visual observations, analyses, embeddings, clusters and recommendations.
3. Every inference must retain provenance and confidence.
4. Observation, interpretation, value and action are separate schema layers.
5. No destructive automation is enabled by default.
6. Original files are never mutated in early phases.
7. Components must be model-vendor independent.
8. Jobs must be idempotent, resumable and versioned.
9. Personal calibration must override generic priors when explicit feedback exists.
10. Durable decisions require an ADR or RFC.

## Before implementation

An agent must:
- read this file and the canon index;
- identify the relevant phase and exit criteria;
- confirm the KAP boundary;
- identify affected schemas and contracts;
- list safety and migration implications;
- avoid coding speculative later-phase features into the MVP.

## Change workflow

1. Create or update specification.
2. Add ADR for durable architectural choice.
3. Define acceptance tests.
4. Implement the smallest coherent slice.
5. Validate on a representative fixture corpus.
6. Report model, cost, privacy and failure implications.
7. Update roadmap status.

## Prohibited shortcuts

- direct writes to KAP internal tables;
- single opaque `quality_score` replacing dimensional scores;
- deleting assets based only on similarity or blur;
- storing only final labels without raw model output/provenance;
- coupling canonical schemas to one provider response format;
- silently overwriting conflicting interpretations;
- assuming `yos-bus` or another transport is canonical without an approved ADR.

## Definition of done

A feature is complete only when it includes:
- contract/schema;
- implementation;
- tests;
- observability;
- failure behavior;
- migration/version notes;
- privacy classification;
- documentation;
- rollback path.
