# Y-OS Cognitive Spine

## Status

Canonical architectural principle — proposed through the Y-PIE foundation PR.

## Purpose

Define the common cognitive sequence that organizes Y-OS across modalities, knowledge systems, reasoning engines, agents and applications.

Y-PIE is the first major implementation of this sequence for visual perception, but the sequence belongs to Y-OS as a whole.

## Canonical sequence

```text
Reality
  ↓
Perception
  ↓
Observations
  ↓
Evidence
  ↓
Knowledge Objects
  ↓
Knowledge Graph
  ↓
Reasoning
  ↓
Capabilities
  ↓
Agents
  ↓
Actions
  ↓
Feedback
  └──────────────→ Perception / Knowledge / Policy
```

This sequence is the **Y-OS Cognitive Spine**.

## Meaning of each layer

### Reality

The external or internal state from which signals originate.

Examples:
- visual scenes;
- conversations;
- documents;
- applications;
- devices;
- environments;
- events;
- human decisions;
- system state.

Reality is never stored directly. Y-OS only receives mediated signals about it.

### Perception

Modality-specific processing that converts raw signals into structured observations.

Examples:
- Y-PIE for images;
- future video, audio, document, spatial and sensor engines;
- connector-specific parsers;
- deterministic extractors;
- machine-learning perception models.

Perception must preserve uncertainty and source provenance.

### Observations

Claims directly grounded in a source or measurable transformation.

Examples:
- OCR text detected in an image;
- a timestamp found in metadata;
- dominant colors;
- a face region;
- a code symbol found in a repository;
- a meeting date extracted from a calendar event.

An observation is not automatically canonical truth.

### Evidence

Observations packaged with enough context to support, reject or revise a knowledge claim.

Every evidence item should include:
- source identity;
- extraction method;
- model or algorithm version;
- timestamp;
- confidence semantics;
- applicable policy;
- validation state.

### Knowledge Objects

Structured candidate entities, events, concepts, relations, decisions or memories derived from evidence.

Knowledge Objects are typed and versioned. They may remain local to a perception engine until KAP accepts, resolves or rejects them.

### Knowledge Graph

The shared canonical graph governed by KAP.

It owns:
- canonical identities;
- cross-modal relations;
- contradiction preservation;
- lifecycle and supersession;
- source-to-knowledge traceability;
- routing into downstream reasoning and memory systems.

No modality engine may create a competing canonical graph.

### Reasoning

Processes that compare, infer, synthesize, plan, critique or explain using knowledge and evidence.

KRE and other reasoning systems operate here.

Reasoning outputs remain distinguishable from source observations and canonical assertions.

### Capabilities

Stable, composable operations exposed by Y-OS.

Examples:
- compare assets;
- retrieve a project history;
- identify contradictions;
- curate a visual collection;
- produce a decision brief;
- recommend a next action.

Capabilities describe what Y-OS can do, not how a service is deployed.

### Agents

Goal-directed actors that select and compose capabilities under policy.

ART governs routing and orchestration concerns here.

Agents do not own canonical knowledge and must not bypass capability contracts.

### Actions

Effects on external or internal systems.

Examples:
- create or update an artifact;
- apply a tag;
- schedule an event;
- modify a repository;
- control an environment;
- present a recommendation;
- request human validation.

Actions require explicit permissions, reversibility classification and auditability.

### Feedback

Observed consequences, user corrections and evaluation results that improve perception, knowledge, policies and models.

Feedback must not silently rewrite history. It creates new evidence, corrections or superseding assertions.

## Ownership map

| Layer | Primary ownership |
|---|---|
| Reality adapters | source connectors and environment interfaces |
| Perception | modality engines such as Y-PIE |
| Observations and evidence | producing engine, under KAP contracts |
| Knowledge Objects and canonical graph | KAP |
| Reasoning | KRE and specialist reasoning engines |
| Capability registry | Y-OS architecture governance |
| Agent routing and orchestration | ART |
| Actions | authorized executors and applications |
| Feedback and evaluation | shared governance with provenance |

## Architectural invariants

1. **Evidence before assertion.**
2. **Perception is modality-specific; knowledge is shared.**
3. **KAP owns canonical identities and the common graph.**
4. **Reasoning never masquerades as observation.**
5. **Agents compose capabilities; they do not bypass contracts.**
6. **Actions are policy-controlled and auditable.**
7. **Feedback creates revisions, not silent historical mutation.**
8. **Every layer must be replaceable behind stable contracts.**
9. **A component may skip unused internal stages operationally, but may not collapse their semantics.**
10. **Complexity is admitted only when it protects a real invariant or unlocks measured value.**

## Anti-patterns

The following are prohibited:

- raw source data written directly as canonical knowledge;
- LLM output stored as fact without provenance;
- a perception engine maintaining an isolated permanent truth graph;
- agents mutating sources without an action policy;
- capabilities tied irreversibly to one vendor or deployment topology;
- feedback overwriting prior model outputs without version history;
- introducing a service solely to mirror a conceptual layer.

## Minimal implementation rule

The cognitive spine is a semantic architecture, not a mandate for ten services.

The first Y-PIE implementation may be a modular monolith with a batch runner and one database, provided that it preserves the boundaries among:

```text
Observation != Interpretation != Assertion != Action
```

This distinction is mandatory even when all stages execute in one process.

## Extension to future modalities

Future engines should implement the same contract:

```text
Source signal
  -> modality perception
  -> observations and evidence bundles
  -> KAP knowledge resolution
  -> shared reasoning and capabilities
```

This allows photo, video, audio, document, spatial, sensor and application-state perception to enrich one Personal Knowledge Genome rather than form separate silos.

## Decision consequence for Y-PIE

Y-PIE becomes:

- the visual perception and visual intelligence implementation of the spine;
- a producer of evidence-backed visual Knowledge Object candidates;
- a specialist provider of visual comparison, curation, memory and Visual DNA capabilities;
- never the owner of the universal canonical graph.

## Review gate

Any future Y-OS architecture proposal must identify:

1. the spine layer or layers it serves;
2. the data or control contract at each boundary;
3. the source of truth;
4. evidence and provenance behavior;
5. failure and fallback behavior;
6. permission and reversibility for actions;
7. why the proposal cannot be implemented more simply.
