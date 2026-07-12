# Y-OS Cognitive Layer Boundaries

## Status

Canonical architecture proposal.

## Purpose

Remove overlap between PIE, KAP and the cognition/reasoning layer by defining a strict sequential cognitive spine inspired by functional neuroscience.

## Canonical spine

```text
Reality
  -> Perception
  -> Knowledge
  -> Cognition
  -> Agency
  -> Action
  -> Feedback
  -> Reality / Perception
```

Canonical module mapping:

```text
Perception -> PIE — Perception Intelligence Engine
Knowledge  -> KAP — Knowledge Acquisition Platform
Cognition  -> CRE — Cognition & Reasoning Engine
Agency     -> ART — Agent Routing Table
Action     -> ACT — Action & Control Toolkit
```

The names identify cognitive responsibilities, not deployment units. The first implementation may remain a modular monolith.

## Foundational rule

> Every external input to Y-OS enters through PIE.

External input includes:

- user language and conversation;
- images and photographs;
- audio and video;
- documents and OCR sources;
- web pages and search results;
- APIs and structured feeds;
- weather, markets and telemetry;
- cameras and environmental sensors;
- Home Assistant and CasaTAO events;
- files, email, calendar and connected services.

PIE is the universal sensory boundary of Y-OS. Different sources use different perceptual adapters, but they share one contract.

Internal outputs between canonical Y-OS modules do not need to be re-perceived unless they leave and re-enter the trusted cognitive boundary.

## Complexity is not cognition

A computation may be expensive or model-heavy while remaining perceptual.

Examples that remain inside PIE:

- OCR and layout extraction;
- speech-to-text;
- object, face and scene detection;
- image embeddings;
- parsing an API response;
- extracting entities explicitly present in a text;
- normalizing timestamps, units and source metadata;
- detecting technical image quality;
- decoding a weather or market feed;
- identifying observable visual or acoustic features.

These operations answer:

> What signal arrived, and what is observably present in it?

They do not answer:

> What does this mean in the user’s life, what should be believed, or what should Y-OS do?

## PIE — Perception

### Biological analogy

Sensory organs, thalamic routing and modality-specific perceptual cortices.

### Responsibility

Transform heterogeneous external signals into normalized percepts, observations and evidence.

### PIE owns

- connectors and sensory adapters;
- source acquisition at the boundary;
- modality decoding;
- signal normalization;
- observable feature extraction;
- source and derivative provenance;
- confidence attached to perceptual observations;
- modality-specific embeddings;
- perceptual change detection;
- privacy classification at ingress.

### PIE outputs

```text
Percept
Observation
Evidence item
Source provenance
Confidence
Modality-specific representation
```

### PIE does not own

- durable semantic or episodic memory;
- canonical entity identity;
- the global Knowledge Graph;
- personal meaning or biographical significance;
- artistic judgement;
- cross-modal synthesis;
- hypothesis formation;
- planning or decision-making;
- agent or tool selection;
- external action.

PIE may propose low-level labels, but they remain observations or model interpretations, not canonical knowledge.

## KAP — Knowledge

### Biological analogy

Hippocampal and medial-temporal consolidation combined with semantic and episodic memory systems.

### Responsibility

Transform perceptual evidence into durable, contextualized and retrievable knowledge.

### KAP owns

- canonical identity resolution;
- Knowledge Objects;
- the shared Knowledge Graph;
- episodic and semantic memory;
- temporal and spatial context;
- cross-modal linkage;
- provenance chains;
- contradiction and revision history;
- consolidation and forgetting policy;
- Personal Knowledge Genome;
- retrieval of relevant prior knowledge;
- acceptance, rejection or qualification of proposed assertions.

### KAP outputs

```text
Canonical knowledge objects
Resolved entities
Context packages
Memory retrievals
Knowledge graph subgraphs
Evidence-backed assertions
```

### KAP does not own

- raw sensor decoding;
- modality-specific feature extraction;
- open-ended inference and simulation;
- ranking competing plans;
- deciding what action to take;
- routing agents or executing tools.

KAP answers:

> What does Y-OS know, how does it know it, and how is it connected to prior knowledge?

KAP does not answer:

> Given this knowledge, what conclusion or plan is best?

## CRE — Cognition

### Name

**CRE — Cognition & Reasoning Engine**

The cognitive-layer word is `Cognition`, so the acronym begins with `C`. Reasoning is a central capability inside cognition rather than a hidden secondary label.

### Biological analogy

Association cortex, working memory and prefrontal cognition.

### Responsibility

Operate on current percepts and retrieved knowledge to produce understanding, hypotheses, evaluations, plans and decisions.

### CRE owns

- working-context assembly;
- inference and deduction;
- analogy and comparison;
- cross-domain synthesis;
- causal reasoning;
- uncertainty-aware hypothesis generation;
- simulation and counterfactuals;
- evaluation and ranking;
- goal decomposition;
- planning;
- metacognitive critique;
- decision proposals;
- domain reasoning policies.

### CRE inputs

```text
Current percepts from PIE
Relevant knowledge and memory from KAP
Goals, constraints and values
Feedback from prior actions
```

### CRE outputs

```text
Interpretations
Hypotheses
Insights
Evaluations
Rankings
Plans
Decision proposals
Knowledge-update proposals
```

### CRE does not own

- canonical long-term memory;
- source ingestion;
- direct control of tools;
- agent/model routing;
- irreversible external execution.

CRE may discover new knowledge, but it submits that result back to KAP as a proposed assertion with evidence and provenance. KAP decides its canonical memory status.

CRE answers:

> Given what is perceived and known, what does it mean, what follows, and what should be considered or done?

## ART — Agency

### Biological analogy

Executive control and action-selection systems.

### Responsibility

Turn an approved intention or plan into an orchestrated course of execution.

ART owns:

- capability selection;
- agent selection;
- model routing;
- workflow decomposition;
- delegation and supervision;
- permission and budget enforcement;
- retries, escalation and cancellation;
- execution-state coordination.

ART does not decide the truth of knowledge and does not directly operate effectors.

## ACT — Action

### Biological analogy

Motor systems and effectors.

### Responsibility

Execute bounded operations against external systems.

ACT includes:

- APIs;
- browsers and Playwright;
- n8n workflows;
- shell and filesystems;
- email and calendar actions;
- GitHub operations;
- Home Assistant and CasaTAO control;
- publishing and media operations.

Every action must expose result, side effects, reversibility and audit data. Outcomes return to the cognitive loop through PIE.

## Sequential default, recurrent reality

The canonical direction is sequential:

```text
PIE -> KAP -> CRE -> ART -> ACT
```

The runtime is recurrent, not a rigid one-pass pipeline:

- CRE may request additional perception from PIE;
- CRE may query KAP repeatedly;
- KAP may request better evidence from PIE;
- ART may return execution constraints to CRE;
- ACT outcomes re-enter through PIE;
- feedback updates KAP knowledge and CRE policies.

These loops do not erase ownership boundaries.

## Photo intelligence as a vertical application

The photo and art system is not PIE itself. It is a vertical Y-OS application that composes the full spine.

```text
Photo / image source
  -> PIE: decode, OCR, faces, objects, embeddings, technical measures
  -> KAP: resolve people, places, projects, events, series and memory context
  -> CRE: evaluate artistic value, emotional significance, originality, curation and pruning
  -> ART: orchestrate tagging, review, publishing or archival workflows
  -> ACT: write tags, create albums, publish sites or perform approved operations
```

### Ownership migration from the earlier Y-PIE concept

The following remain in PIE:

- visual decoding;
- OCR;
- object, face and scene detection;
- visual embeddings;
- color, composition and technical measurements;
- observable style descriptors;
- source provenance.

The following move to KAP:

- canonical photo and artwork entities;
- people, place, event and project links;
- series and lineage as durable knowledge;
- Personal Knowledge Genome;
- Visual DNA as a versioned personal knowledge model;
- memory history and validated user preferences.

The following move to CRE:

- artistic-value evaluation;
- emotional and biographical significance estimates;
- corpus-relative originality;
- symbolic and archetypal interpretation;
- hidden-pattern discovery;
- Visual DNA inference and explanation;
- curation and narrative construction;
- best-variant and pruning recommendations;
- publication strategy.

The vertical photo application owns:

- user experience;
- domain workflow;
- review surfaces;
- application-specific policies;
- portfolio, gallery and publishing functions.

## Universal ingress contract

All PIE adapters must produce a common envelope:

```yaml
percept_id: uuid
source_id: string
modality: text | image | audio | video | document | api | sensor | spatial
captured_at: timestamp
received_at: timestamp
payload_reference: uri-or-object-id
observations: []
evidence: []
source_provenance: {}
confidence: {}
privacy_class: private
schema_version: string
```

This contract allows Y-OS to process a camera image, an email, a weather feed or a Bitcoin price through the same cognitive spine without pretending that their modality-specific processing is identical.

## Boundary tests

A capability belongs to PIE if its primary question is:

> What arrived, and what is observably present?

It belongs to KAP if its primary question is:

> What should be retained as knowledge, and how is it connected?

It belongs to CRE if its primary question is:

> What does this imply, how should it be evaluated, and what should be done?

It belongs to ART if its primary question is:

> Which agents, models and capabilities should execute the plan?

It belongs to ACT if its primary question is:

> How is the approved operation performed in the external world?

## Non-overlap invariant

No module may be canonical owner of another module’s output class:

- PIE cannot canonize knowledge;
- KAP cannot silently perform open-ended reasoning;
- CRE cannot silently rewrite canonical memory;
- ART cannot redefine the plan’s meaning;
- ACT cannot invent goals or permissions.

Implementations may share infrastructure, models or processes. Semantic ownership remains separate.
