# Thought Line Model

## Definition

A **Thought Line** is a living intellectual thread that groups recurring themes, evolving ideas, and related decisions across time and sources.

## How It Differs From a Tag

| Aspect | Tag | Thought Line |
|---|---|---|
| Structure | Flat label | Rich object with fields |
| Lifecycle | Static | Evolves through maturity levels |
| Content | None | Has current best understanding |
| History | None | Tracks evolution events |
| Decisions | None | Links to decision threads |
| Dead ends | None | Records impasses |
| Review | None | Has review triggers |

## How It Differs From a Project

| Aspect | Project | Thought Line |
|---|---|---|
| Scope | Bounded deliverable | Unbounded intellectual thread |
| Timeline | Start → End | Ongoing, potentially infinite |
| Completion | Can be "done" | Never "done", only more mature |
| Cross-cutting | Usually single domain | Can span multiple projects |
| Output | Artifacts | Understanding |

## Required Fields

```yaml
thought_line_id: TL-XXX
title: Human-readable title
domain: Primary domain (architecture, tooling, philosophy, etc.)
description: What this thought line represents
current_best_understanding: Latest validated synthesis
maturity_level: seed | exploratory | emerging_pattern | candidate_architecture | validated_architecture | canonical | deprecated
status: active | dormant | deprecated | under_review
source_fragments: [list of fragment IDs]
claims: [list of claim IDs]
decisions: [list of decision IDs]
dead_ends: [list of impasse IDs]
open_questions: [list of unresolved questions]
superseded_positions: [list of old positions with timestamps]
active_positions: [list of current positions]
last_validated_at: ISO date
next_review_gate: Gate that should review this
```

## Lifecycle

```
seed → exploratory → emerging_pattern → candidate_architecture → validated_architecture → canonical
                                                                                              ↓
                                                                                         deprecated
```

## Maturity Levels

| Level | Meaning | Evidence Required |
|---|---|---|
| seed | First mention, no validation | 1 source fragment |
| exploratory | Multiple mentions, no convergence | 3+ fragments |
| emerging_pattern | Pattern visible across sources | 5+ fragments, some alignment |
| candidate_architecture | Proposed structure/approach | Design document or decision |
| validated_architecture | Tested and confirmed | Implementation evidence |
| canonical | Accepted as current truth | Gate approval or explicit decision |
| deprecated | Superseded by newer thinking | Supersession event documented |

## Examples

- KAP Architecture (canonical)
- Source Acquisition Strategy (validated_architecture)
- Manus Execution Corpus (validated_architecture)
- Notion Memory Hub (candidate_architecture)
- Obsidian Markdown Pipeline (exploratory)
- ChatGPT Conversation Corpus (seed)
- Git/Markdown-first Persistence (canonical)
- Evolutionary Knowledge Merge (candidate_architecture)
- Y-OS Cognitive Infrastructure (validated_architecture)
- KOSMOS Ontology (exploratory)
- CasaTAO Intelligent House (exploratory)
- ELYSIUM Symbolic/Civilizational Framework (emerging_pattern)

## Connections

```
Thought Line ←→ Source Fragments (many-to-many)
Thought Line ←→ Claims (many-to-many)
Thought Line ←→ Decision Threads (many-to-many)
Thought Line ←→ Impasses (many-to-many)
Thought Line ←→ Evolution Events (one-to-many)
Thought Line → Current Best Synthesis (one-to-one)
```
