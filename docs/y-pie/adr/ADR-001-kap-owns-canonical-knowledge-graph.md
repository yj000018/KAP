# ADR-001 — KAP Owns the Canonical Knowledge Graph

- Status: Accepted
- Date: 2026-07-12
- Scope: Y-PIE / KAP boundary

## Context

Y-PIE generates visual observations, interpretations, similarities, clusters and knowledge candidates. A separate permanent visual graph would create duplicated identifiers, contradictory assertions and cross-modal fragmentation.

## Decision

KAP owns canonical entities, assertions and cross-modal graph relations.

Y-PIE owns:
- visual asset identities and source mappings;
- analysis runs;
- observations and model interpretations;
- embeddings and temporary clusters;
- evidence bundles;
- local review state.

Y-PIE may expose a Visual Knowledge Graph projection, but that projection is derived from Y-PIE evidence plus KAP canonical identifiers. It is not an independent source of canonical truth.

## Consequences

Positive:
- one canonical identity system;
- cross-modal reasoning remains possible;
- contradictions are governed centrally;
- Y-PIE can evolve models without rewriting canonical history.

Costs:
- entity-resolution feedback loop is required;
- local operation must tolerate delayed KAP publication;
- contracts and idempotency must be maintained.

## Rejected alternatives

### Independent Y-PIE graph

Rejected because it creates competing knowledge authority and synchronization complexity.

### Store all visual analysis directly in KAP

Rejected because high-volume model outputs, embeddings and temporary clusters are operational evidence rather than canonical knowledge.

## Guardrail

No Y-PIE component may silently create permanent person, project, place, event or concept identifiers outside KAP.
