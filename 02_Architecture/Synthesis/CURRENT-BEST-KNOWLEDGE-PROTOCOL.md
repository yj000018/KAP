# Current Best Knowledge Protocol

## Purpose

The Current Best Knowledge (CBK) layer provides the most up-to-date, validated understanding of any topic in the KAP corpus. It is the primary interface for both human navigation and AI agent querying.

## What CBK Is

CBK is a living synthesis that:

1. Represents the latest validated position on a topic
2. Cites all supporting evidence
3. Acknowledges uncertainty and open questions
4. Links to superseded positions (for context)
5. Links to impasses (for negative knowledge)
6. Is machine-readable AND human-readable
7. Has explicit confidence levels
8. Has explicit review triggers

## What CBK Is NOT

CBK is NOT:

1. A static summary (it evolves with new evidence)
2. A replacement for source fragments (sources are always preserved)
3. An opinion (it must be evidence-based)
4. Automatically generated without review (human validation required)
5. The only view (historical, evolution, and contradiction views coexist)

## CBK Structure

```yaml
cbk_entry:
  id: CBK-XXX
  thought_line_id: TL-XXX
  title: "Topic"
  domain: architecture | tooling | workflow | philosophy | project
  
  current_position:
    summary: "One paragraph synthesis"
    detailed: "Full explanation with nuance"
    confidence: high | medium | low | contested
    last_validated: ISO date
    validated_by: human | gate | implementation_evidence
  
  key_decisions:
    - decision_id: DEC-XXX
      status: active
      summary: "Decision text"
  
  active_claims:
    - claim_id: CLM-XXX
      text: "Claim text"
      evidence_count: N
  
  superseded_positions:
    - position: "Old position"
      superseded_at: ISO date
      reason: "Why it was replaced"
  
  impasses:
    - impasse_id: IMP-XXX
      summary: "What was tried and failed"
  
  open_questions:
    - "Question that remains unresolved"
  
  sources:
    - fragment_id: FRAG-XXX
      source_type: manus | notion | chatgpt | obsidian | git | web
      date: ISO date
      relevance: primary | supporting | historical
  
  review_triggers:
    - "Review if new Notion architecture session appears"
    - "Review after PILOT-ACQUISITION-GATE completes"
  
  ai_summary: "Machine-optimized one-line summary for agent routing"
  human_summary: "Human-optimized paragraph for dashboard display"
```

## CBK Generation Protocol

### Step 1: Identify Thought Line
Select a Thought Line that has sufficient evidence for synthesis.

### Step 2: Gather Evidence
Collect all source fragments, claims, decisions, and impasses related to this Thought Line.

### Step 3: Chronological Ordering
Order all evidence by timestamp. Identify evolution events.

### Step 4: Contradiction Detection
Flag any contradictions between sources. Classify by type.

### Step 5: Synthesis Draft
Generate a draft synthesis that:
- States the current best understanding
- Cites key evidence
- Acknowledges contradictions
- Notes open questions
- Sets confidence level

### Step 6: Human Review
Present synthesis to Architect for validation. Options:
- Approve as-is
- Request revision
- Flag as contested
- Request more evidence

### Step 7: Publication
Approved CBK entries are published to:
- Human exploitation layer (Obsidian graph, dashboards)
- AI exploitation layer (machine-readable indexes)

### Step 8: Review Scheduling
Set review triggers based on:
- Time-based (review every N months)
- Event-based (review when new evidence appears)
- Gate-based (review at specific gate milestones)

## Confidence Levels

| Level | Meaning | Required Evidence |
|---|---|---|
| high | Strong consensus, implementation evidence | 3+ sources aligned, no contradictions |
| medium | Good evidence but some gaps | 2+ sources, minor gaps |
| low | Limited evidence or early stage | 1-2 sources, no validation |
| contested | Active contradiction unresolved | Contradicting sources, pending review |

## Update Protocol

When new evidence arrives:

1. Check if it affects any existing CBK entry
2. If yes: re-run synthesis with new evidence included
3. If contradiction: flag for review
4. If supersession: update CBK, move old position to superseded
5. If confirmation: increase confidence, add source reference
6. Log the update in Evolution Ledger
