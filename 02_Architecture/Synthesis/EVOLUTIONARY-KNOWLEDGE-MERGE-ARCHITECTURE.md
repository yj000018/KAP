# Evolutionary Knowledge Merge Architecture

## 1. Purpose

KAP is not an archive. KAP is an evolutionary knowledge system.

The goal is not to preserve documents. The goal is to reconstruct:

1. What was thought
2. When it was thought
3. Why it was thought
4. What superseded it
5. What was rejected
6. What became canonical
7. What remains uncertain
8. What should guide future action

## 2. Long-Term Value Proposition

KAP transforms a fragmented multi-source corpus (Notion, Manus, ChatGPT, Obsidian, Git, Web) into a navigable, queryable, evolving body of knowledge that serves both human deep thinking and AI agent exploitation.

The system preserves not just conclusions but the reasoning trails, dead ends, and decision rationale that make knowledge actionable rather than merely stored.

## 3. Why KAP Is Not a Flat Archive

Sources overlap. The same idea appears across multiple sessions, documents, and tools at different maturity levels. A flat archive would:

- Lose chronology and evolution
- Collapse early intuitions with mature decisions
- Erase dead ends (which are valuable negative knowledge)
- Treat all sources as equal regardless of maturity
- Make it impossible to answer "why did we choose this?"

## 4. Source Overlap Problem

| Overlap Type | Example | Risk If Unmanaged |
|---|---|---|
| Same topic, different maturity | Y-OS architecture discussed in 30+ sessions | Confusion about current state |
| Contradicting positions | Decision A in session X, reversed in session Y | Acting on outdated info |
| Duplicate content | Same text in Notion + Manus + Obsidian | Noise, wasted processing |
| Partial supersession | Old approach partially valid, partially replaced | Losing the valid parts |
| Implementation vs concept | Conceptual design vs actual code/config | Treating plans as facts |

## 5. Architecture Layers

### 5.1 Source Fragment Layer
Every acquired source unit (page, session, note, document) retains full provenance. Fragments are never overwritten by synthesis.

### 5.2 Claim Layer
Atomic statements extracted from fragments. Each claim has a status (candidate → supported → canonical / superseded / rejected) and links to supporting/contradicting evidence.

### 5.3 Thought Line Layer
Living intellectual threads that group recurring themes across time and sources. Not tags — they have maturity levels, current best understanding, and evolution history.

### 5.4 Decision Thread Layer
Tracks decisions, reversals, supersessions, and rationale. Answers "what did we decide, why, and is it still valid?"

### 5.5 Evolution Ledger Layer
Chronological record of how thought evolved. Each event captures before/after positions and reasons for change.

### 5.6 Impasse Registry Layer
Dead ends, bad approaches, traps. Prevents repeating mistakes. Each impasse includes why it failed and what replaced it.

### 5.7 Current Best Knowledge Layer
Synthesized current best understanding for each Thought Line. Points back to all evidence. Never erases history.

### 5.8 Human Exploitation Layer
Dashboards, maps, decision trails, timeline views, project briefs — designed for human navigation and deep thinking.

### 5.9 AI Exploitation Layer
Machine-readable registries, routing indexes, decision graphs, claim indexes — designed for agent querying and task routing.

## 6. Human Exploitation Model

### Required Views

1. **Project Overview View** — all projects with status, key decisions, open questions
2. **Current Best Understanding View** — latest validated position on any topic
3. **Decision Trail View** — chronological decisions with rationale and supersession
4. **Evolution Timeline View** — how thinking evolved on a topic
5. **Impasse / Dead-End View** — what was tried and rejected, and why
6. **Source Provenance View** — where knowledge comes from
7. **Next Action / Open Question View** — what needs resolution

### Required Structures

```
Dashboards/
Maps/
Current_Best/
Decision_Trails/
Impasse_Maps/
Project_Briefs/
Timeline_Views/
Review_Queues/
```

## 7. AI Exploitation Model

### Required Capabilities

- Retrieve current best understanding for topic X
- Retrieve source evidence for claim Y
- Detect superseded claims
- Avoid repeating rejected approaches
- Route tasks to correct project/domain
- Identify uncertainty
- Generate project briefs
- Answer "why" questions with provenance
- Compare old vs current positions

### Required Structures

```
machine_readable_registries/
routing_indexes/
decision_graphs/
thought_line_graphs/
source_fragment_indexes/
claim_indexes/
synthesis_indexes/
review_queues/
```

### Query Patterns

```
Given topic X → return current best synthesis + active decisions + impasses
Given document Y → classify into thought lines, detect superseded ideas
Given new source Z → decide whether it updates a thought line or is noise
Given old recommendation R → check whether still valid
```

## 8. Merge Principles

1. **Provenance first** — never merge without preserving source identity
2. **Chronology preserved** — timestamps are sacred
3. **Supersession explicit** — old positions are not deleted, they are marked superseded
4. **Evidence-based** — claims require source fragments
5. **Maturity-aware** — early intuitions ≠ validated decisions
6. **Contradiction-tolerant** — contradictions are flagged, not hidden
7. **Human-reviewable** — all automated synthesis is reviewable

## 9. Chronology and Supersession Principles

- Every fragment has `created_at` and `extracted_at`
- Every claim has `first_seen_at` and `last_seen_at`
- Every decision has `decided_at` and optionally `superseded_at`
- Newer does NOT automatically mean correct
- Implementation evidence outweighs conceptual proposals
- Explicit reversals outweigh implicit contradictions

## 10. Deduplication Policy

KAP does not collapse knowledge by deduplication alone. KAP preserves provenance, chronology, maturity, decision status, and supersession relationships before any merge.

- Exact duplicates: link to canonical, mark others as `duplicate_of`
- Near-duplicates: preserve both, link as `variant_of`
- Old vs new: preserve both, mark supersession relationship
- Never delete historical variants

## 11. Contradiction Policy

| Situation | Action |
|---|---|
| Explicit reversal (documented) | Mark old as `superseded`, new as `active` |
| Implicit contradiction | Flag as `contested`, require human review |
| Implementation vs concept | Prefer implementation evidence |
| Newer vs older (no explicit reversal) | Flag for review, do not auto-resolve |
| Source reliability difference | Weight by source type and maturity |

## 12. Current Best Knowledge Model

Each synthesis includes:
1. Current position
2. Rationale
3. Key sources
4. Active decisions
5. Superseded alternatives
6. Impasses
7. Unresolved questions
8. Confidence level
9. Human summary
10. Agent summary
11. Review triggers

## 13. Gate Sequence

See `SYNTHESIS-GATE-SEQUENCE.md` for full details.

## 14. Risks

| Risk | Severity | Mitigation |
|---|---|---|
| Losing chronology during merge | HIGH | Mandatory timestamps on all objects |
| Over-deduplication | HIGH | Preserve variants, link don't delete |
| Treating old as current | HIGH | Supersession logic mandatory |
| Hallucinated synthesis | MEDIUM | All synthesis must cite sources |
| Missing provenance | MEDIUM | Fragment layer is immutable |
| AI retrieval confusion | MEDIUM | Clear canonical vs historical markers |

## 15. Future Implementation Notes

- Phase 1: Architecture design (this gate) — DONE
- Phase 2: Source Fragment Model — define exact schemas and indexing
- Phase 3: Thought Line Seeding — identify initial thought lines from existing corpus
- Phase 4: Claim Extraction Pilot — test extraction on small sample
- Phase 5: Decision Thread Reconstruction — map existing decisions
- Phase 6: Impasse Registry Seed — document known dead ends
- Phase 7: Current Best Knowledge Pilot — generate first syntheses
- Phase 8: Human/AI Review — validate quality
- Phase 9: Scale-Up — apply to full corpus
