# Y-PIE Program Operating Model

## Purpose

This document defines how Y-PIE progresses quickly in parallel without becoming an over-coupled program.

## Operating principle

> Think broadly, build narrowly, validate continuously.

Y-PIE may maintain a long-range cognitive architecture while implementing only the smallest coherent capability slice at any given time.

## Five-stream limit

No more than five active streams may exist simultaneously.

### Stream 1 — Canon and cognitive architecture

Owns:
- vision;
- principles;
- system boundaries;
- ontology;
- ADRs;
- KAP ownership contracts.

Produces specifications, not production services.

### Stream 2 — Core MVP

Owns:
- Immich adapter;
- asset registry;
- metadata extraction;
- technical analysis;
- baseline semantic classification;
- persistence;
- review-oriented write-back.

This is the primary delivery stream until Phase 1 exits.

### Stream 3 — Visual intelligence research

Owns research specifications and offline experiments for:
- similarity;
- art intelligence;
- memory significance;
- Visual DNA;
- curation;
- narrative generation.

Research results do not enter production without an explicit promotion gate.

### Stream 4 — KAP integration

Owns contracts only:
- evidence bundles;
- canonical knowledge publication;
- entity-resolution feedback;
- graph projection;
- KRE and ART access.

This stream must not duplicate Y-PIE business logic.

### Stream 5 — UX and human review

Owns:
- review queues;
- correction flow;
- confidence display;
- comparison surfaces;
- progressive disclosure;
- accessibility and interaction cost.

## Capacity allocation

Default allocation during the foundation and MVP period:

| Stream | Share |
|---|---:|
| Canon and cognitive architecture | 15% |
| Core MVP | 40% |
| Visual intelligence research | 20% |
| KAP integration | 15% |
| UX and human review | 10% |

Allocation is directional, not a staffing commitment.

## Work item rules

Every work item must declare:
- owner stream;
- user or system value;
- inputs and outputs;
- dependencies;
- acceptance criteria;
- reversibility;
- evidence produced;
- explicit non-goals.

A work item spanning more than two streams must be decomposed unless an ADR justifies the coupling.

## Capability model

Y-PIE is organized around reusable capabilities rather than permanent microservices.

Canonical capability verbs:
- observe;
- describe;
- classify;
- compare;
- cluster;
- remember;
- relate;
- curate;
- recommend;
- learn;
- explain.

A capability may initially live in a single modular application. Service extraction is permitted only when operational evidence demonstrates the need.

## Science → capability → feature

Every advanced function must map through three layers:

```text
Research method
  ↓
Reusable capability
  ↓
User-facing feature
```

Example:

```text
Corpus-relative representation learning
  ↓
Visual-language similarity capability
  ↓
"Show images that feel most like my work"
```

Research names must not leak directly into the user interface unless useful.

## Promotion gates

A research capability may enter the MVP or production path only if it has:
1. a defined input and output schema;
2. an evaluation set;
3. baseline and target metrics;
4. confidence and failure semantics;
5. cost and latency measurements;
6. a rollback strategy;
7. a human-review path where impact is subjective or risky.

## Complexity budget

Phase 1 permits:
- one deployable PIE application;
- one PostgreSQL database;
- one batch scheduler;
- one Immich adapter;
- optional local model runtime;
- optional external vision provider behind one interface.

Phase 1 forbids unless proven necessary:
- Kubernetes;
- independent graph database;
- event-streaming platform;
- service mesh;
- multiple queues;
- microservice decomposition;
- custom primary photo-management UI;
- autonomous destructive actions.

## Decision cadence

- ADR: durable architectural decisions.
- RFC: substantial proposals requiring evaluation.
- Experiment note: bounded research result.
- Issue: executable unit of work.
- PR: reviewed change to canon or implementation.

## Definition of done

A milestone is complete only when:
- its acceptance criteria pass;
- documentation matches actual behavior;
- observability exists;
- rollback or disablement is possible;
- known failure modes are recorded;
- no unresolved ownership conflict remains.

## Anti-patterns

Reject:
- building a custom platform before validating the workflow;
- creating separate stores for every analysis type;
- treating model output as fact;
- embedding product rules inside prompts only;
- coupling KAP graph publication to batch analysis completion;
- introducing distributed infrastructure to solve hypothetical scale;
- adding a module without a concrete capability and user flow.
