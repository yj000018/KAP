# Decision Thread Model

## Definition

A **Decision Thread** tracks a specific decision through its lifecycle: proposal, acceptance, implementation, and potential supersession or reversal.

Every Decision Thread answers:

1. What did we decide?
2. Why?
3. When?
4. Based on what evidence?
5. What alternatives were rejected?
6. Was this later superseded?
7. What is the current state?

## Required Fields

```yaml
decision_id: DEC-XXX
decision_title: Human-readable title
decision_text: Full statement of the decision
decision_type: architecture | workflow | tooling | source_policy | gate_policy | agent_role | data_model | security | normalization | merge_policy | project_direction
status: proposed | accepted | active | superseded | rejected | deprecated | under_review
decided_at: ISO date
decided_by: Agent or human who made/validated the decision
source_fragments: [fragment IDs that informed this decision]
rationale: Why this was chosen
accepted_option: The chosen approach
rejected_options: [list of alternatives considered and rejected]
tradeoffs: Known tradeoffs accepted
risks: Known risks accepted
supersedes: [decision IDs this replaces]
superseded_by: [decision ID that replaced this, if any]
related_thought_lines: [thought line IDs]
current_validity: valid | partially_valid | invalid | under_review
review_required: boolean
```

## Decision Statuses

| Status | Meaning |
|---|---|
| proposed | Under consideration, not yet accepted |
| accepted | Formally accepted but not yet implemented |
| active | Accepted and currently in force |
| superseded | Replaced by a newer decision |
| rejected | Considered and explicitly rejected |
| deprecated | No longer relevant (context changed) |
| under_review | Being reconsidered |

## Decision Types

| Type | Scope |
|---|---|
| architecture | System structure, layers, patterns |
| workflow | How work is done, processes |
| tooling | Which tools are used and why |
| source_policy | How sources are acquired and managed |
| gate_policy | Gate rules and sequences |
| agent_role | Agent responsibilities and boundaries |
| data_model | Data structures and schemas |
| security | Access, credentials, permissions |
| normalization | How content is standardized |
| merge_policy | How sources are combined |
| project_direction | Strategic project choices |

## Supersession

When a decision is superseded:

1. Old decision status → `superseded`
2. Old decision gets `superseded_by` field pointing to new decision
3. New decision gets `supersedes` field pointing to old decision
4. Both decisions remain in the registry
5. Rationale for change is documented in the new decision

## Reversals

A reversal is a special case of supersession where the new decision explicitly contradicts the old one. Reversals must include:

- Explicit statement that this reverses decision X
- Why the original decision was wrong or no longer valid
- What evidence triggered the reversal

## Relationship to Gates and MPMs

- Gates produce decisions (gate pass = decision to proceed)
- MPMs may reference decisions as context
- Decision Threads link back to the gate/MPM that produced them

## Relationship to Current Best Synthesis

Current Best Knowledge references active decisions as evidence. When a decision is superseded, the synthesis must be updated to reflect the new state.
