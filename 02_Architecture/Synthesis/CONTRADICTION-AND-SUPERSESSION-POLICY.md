# Contradiction and Supersession Policy

## Purpose

This policy governs how KAP handles contradictions between sources, evolving positions, and explicit reversals of earlier decisions.

## Core Principle

Contradictions are information, not errors. They reveal evolution, context-dependence, or unresolved tensions. KAP preserves them rather than resolving them prematurely.

## Contradiction Types

| Type | Definition | Resolution |
|---|---|---|
| Explicit reversal | Source B explicitly states "we no longer do X, now we do Y" | Mark X as superseded, Y as active |
| Implicit contradiction | Source B says Y without referencing X, but Y contradicts X | Flag as contested, require review |
| Context-dependent | Both X and Y are valid in different contexts | Document both with context markers |
| Maturity difference | X is early intuition, Y is validated architecture | Prefer Y, preserve X as historical |
| Implementation vs concept | X is a plan, Y is what was actually built | Prefer Y (implementation evidence) |
| Temporal evolution | X was true in January, Y became true in June | Both valid for their timeframe |

## Supersession Rules

1. **Explicit supersession** requires documented evidence (a source that says "this replaces that")
2. **Implicit supersession** requires human review before marking old position as superseded
3. **Newer does NOT automatically supersede older** — recency alone is not evidence
4. **Implementation supersedes concept** — what was built outweighs what was planned
5. **Gate decisions supersede pre-gate positions** — formal gate approval is authoritative
6. **Reversals must document WHY** — a reversal without rationale is flagged for review

## Contradiction Detection

During merge and synthesis, the system must detect:

1. Same topic, different conclusions
2. Same decision, different outcomes
3. Same tool/approach, different evaluations
4. Same architecture, different implementations
5. Explicit "we changed" / "this replaces" / "no longer" statements

## Contradiction Resolution Workflow

```
1. Detect contradiction
2. Classify type (explicit/implicit/context/maturity/implementation/temporal)
3. If explicit reversal → auto-resolve (mark supersession)
4. If implementation vs concept → auto-resolve (prefer implementation)
5. If temporal evolution → preserve both with timestamps
6. If implicit/context/maturity → flag for human review
7. Human reviews → accepts resolution or documents as "contested"
8. Contested items remain visible in Current Best Knowledge with uncertainty marker
```

## Supersession Metadata

When a position is superseded:

```yaml
superseded_position:
  original_claim_id: CLM-XXX
  original_text: "We use tool X for task Y"
  superseded_at: 2026-05-15
  superseded_by: CLM-YYY
  supersession_type: explicit_reversal | implicit | maturity_upgrade
  evidence: [fragment IDs]
  rationale: "Tool X was replaced by tool Z because..."
  still_partially_valid: boolean
  valid_context: "Only valid when..."
```

## Never Delete

Superseded positions are NEVER deleted. They are:

1. Marked with status `superseded`
2. Linked to their replacement
3. Preserved in the Evolution Ledger
4. Available for historical queries
5. Useful as negative knowledge ("we tried this, it didn't work")
