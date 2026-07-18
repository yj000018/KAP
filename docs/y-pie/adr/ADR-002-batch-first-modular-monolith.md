# ADR-002 — Batch-First Modular Monolith for the MVP

- Status: Accepted
- Date: 2026-07-12
- Scope: PIE Core MVP

## Context

Y-PIE may eventually require queues, distributed workers, specialist models and interactive services. Introducing these before workload and failure characteristics are known would add operational complexity without proving value.

## Decision

The first implementation is a batch-first modular monolith:

```text
Immich adapter
  -> batch coordinator
  -> analysis capabilities
  -> PostgreSQL persistence
  -> review/write-back adapter
```

Internal boundaries are explicit Python packages and contracts, not separate network services.

Initial deployment may use:
- one Y-PIE application container;
- one PostgreSQL database;
- Immich as an external dependency;
- local model cache and bounded derivative storage.

## Extraction rule

A capability becomes a separate service only when at least one condition is demonstrated:
- independent scaling is required;
- hardware placement differs materially;
- failure isolation is necessary;
- release cadence differs;
- security boundary requires separation;
- a stable external consumer exists.

## Consequences

Positive:
- simpler development and debugging;
- transactional consistency;
- fewer deployment failure modes;
- easier schema evolution;
- faster MVP learning.

Costs:
- less horizontal scaling initially;
- care required to preserve internal boundaries;
- long model jobs must be bounded and resumable.

## Rejected alternatives

### Microservices from the start

Rejected as premature complexity.

### Pure n8n implementation

Rejected as the primary runtime because durable analysis state, typed contracts, testing and model lifecycle require an application core. n8n may orchestrate external workflows later.

### Event-driven architecture from the start

Rejected until polling and batch execution prove insufficient.

## Guardrail

The monolith must remain modular: no capability may depend directly on another capability's private storage or implementation details.
