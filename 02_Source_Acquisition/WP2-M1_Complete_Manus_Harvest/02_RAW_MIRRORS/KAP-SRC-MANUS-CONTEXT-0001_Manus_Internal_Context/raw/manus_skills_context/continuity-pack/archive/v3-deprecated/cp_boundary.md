# CP vs CSE — Boundary Definition

## Core Rule

**CP packages continuity. CSE reconstructs or synthesizes context.**

---

## CP Core — What it does

| Function | Description |
|----------|-------------|
| Generate CP | Package available context (session, theme, provided material) into a structured handover object |
| Receive / absorb CP | Internalize a CP without acting |
| QC / repair CP | Evaluate and fix a CP for completeness and transferability |

---

## CSE — What requires it

If the user asks for any of the following, respond:
> This requires **CSE — Context Synthesis Engine** — not CP Core.

| Request type | Why it needs CSE |
|--------------|-----------------|
| Multi-session synthesis | Requires corpus search and conflict resolution across sessions |
| Multi-LLM merge | Requires aggregating outputs from different LLMs |
| Recovery from fragmented sources | Requires deep search + reconstruction |
| Merge of multiple CPs | Requires conflict resolution and synthesis |
| Session → Project → Program aggregation | Requires hierarchical synthesis |
| Corpus search across Mem0 / Notion / Git | Requires retrieval + synthesis, not packaging |

---

## Decision Tree

```
User says "CP" or asks for a Continuity Pack
│
├─ "Generate CP" → CP Core Function 1
├─ "Absorb / receive this CP" → CP Core Function 2
├─ "QC / repair this CP" → CP Core Function 3
│
└─ "Merge CPs / recover context / aggregate sessions / search corpus"
   → "This requires CSE — Context Synthesis Engine — not CP Core."
```

---

## QC Checklist (10 checks — mandatory before CP output)

1. Does the Executive Handover match the actual user intent?
2. Is the scope explicit?
3. Are source layers separated and labeled?
4. Are external memories labeled with source and freshness?
5. Is depth declared?
6. Is target declared or explicitly neutral?
7. Is handover mode declared?
8. Are decisions separated from hypotheses?
9. Is staleness risk stated?
10. Could a new LLM continue without hidden memory?

---

## Quality Score Reference

| Score | Level | Meaning |
|-------|-------|---------|
| 0-5 | Incomplete | Missing critical sections, not transferable |
| 6-7 | Usable | Functional but fragile |
| 8-9 | Strong | Clear, complete, transferable |
| 10 | Excellent | Production-grade, zero ambiguity |
