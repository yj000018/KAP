# Deduplication and Merge Policy

## Core Principle

KAP deduplicates at the claim level, not at the source level. Source fragments are always preserved intact. Deduplication happens during synthesis, not during acquisition.

## What Is NOT Deduplication

The following are NOT deduplication — they are evolution tracking:

1. Same topic discussed at different times → temporal evolution, not duplicate
2. Same idea at different maturity levels → maturity progression, not duplicate
3. Same concept in different contexts → context variants, not duplicate
4. Same decision with different rationale → evidence accumulation, not duplicate

## What IS Deduplication

True duplicates are:

1. Exact same text appearing in multiple sources (copy-paste)
2. Same session exported to multiple formats (Notion + Manus + local MD)
3. Backup copies of the same document
4. Re-imports of already-acquired content

## Deduplication Levels

| Level | Action | Example |
|---|---|---|
| Exact duplicate | Link to canonical, mark as `duplicate_of` | Same MD file in 2 locations |
| Near-duplicate (>90% overlap) | Preserve both, link as `variant_of`, flag for review | Slightly edited copy |
| Thematic overlap (<90%) | Preserve both independently | Two sessions on same topic |
| Cross-source echo | Preserve both, link as `echo_of` | Notion page that quotes a Manus session |

## Merge Strategy

### Phase 1: Fragment Preservation (Acquisition)
All sources are acquired verbatim. No merge at this stage.

### Phase 2: Claim Extraction (Normalization)
Atomic claims are extracted from fragments. Claims are deduplicated:
- Same claim from multiple sources → single claim with multiple source references
- Similar claims → linked as variants

### Phase 3: Thought Line Synthesis (Merge)
Claims are grouped into Thought Lines. The merge produces:
- Current Best Understanding (synthesis of all supporting claims)
- Evolution history (chronological progression)
- Contradiction map (conflicting claims)
- Confidence level (based on evidence weight)

## Merge Rules

1. **Never merge across maturity levels** — keep early intuitions separate from validated decisions
2. **Never merge across time without timestamps** — chronology is sacred
3. **Never auto-resolve contradictions** — flag for human review
4. **Always preserve provenance** — every synthesis points back to sources
5. **Prefer implementation evidence** — what was built > what was planned
6. **Prefer explicit decisions** — gate approvals > informal discussions

## Cross-Source Merge

When the same topic appears in Manus + Notion + ChatGPT + Obsidian:

1. Each source fragment is preserved independently
2. Claims are extracted from each
3. Claims are compared for overlap, contradiction, evolution
4. A unified Thought Line synthesis is produced
5. The synthesis cites all contributing sources
6. Contradictions are flagged with source attribution

## Merge Output Format

```yaml
thought_line_synthesis:
  id: TL-XXX
  title: "Topic name"
  current_best: "Synthesized current understanding"
  sources:
    - fragment_id: FRAG-001
      source_type: manus
      date: 2026-01-15
      contribution: "First mention of concept"
    - fragment_id: FRAG-042
      source_type: notion
      date: 2026-03-20
      contribution: "Validated architecture"
  evolution:
    - date: 2026-01-15
      position: "Initial idea"
      maturity: seed
    - date: 2026-03-20
      position: "Refined approach"
      maturity: validated_architecture
  contradictions: []
  impasses:
    - "Tried approach Z, failed because..."
  confidence: high
  review_status: validated
```
