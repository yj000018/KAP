---
name: continuity-pack
version: 0.1
description: "CP Core — generates reliable Continuity Packs from current or explicitly provided context. Use when the user says CP, asks for a Continuity Pack, or needs cross-LLM context transfer."
---

# yOS Continuity Protocol — CP Core v0.1

## Principle

**CP packages continuity.**

CP Core generates reliable Continuity Packs from current or explicitly provided context.
It does not receive, QC, recover, merge, aggregate, or synthesize as active user-facing functions.
Receive-only is handled inside the generated CP itself (Receiver Instruction section).
External memory is never used unless explicitly requested.
CSE handles search, merge, recovery, aggregation, and corpus synthesis.

---

## Function

CP Core does one thing: **generate a reliable Continuity Pack from the currently available context.**

---

## Trigger

Generate a CP when the user says any of:

- `CP`
- `CP de cette session`
- `CP sur ce thème`
- `CP pour Manus`
- `CP pour Claude`
- `CP court`
- `CP complet`

---

## Default Behavior

If unspecified, apply these defaults:

| Parameter | Default |
|-----------|---------|
| Scope | Current session |
| Source | Current session only |
| Target | Neutral |
| Depth | Standard |
| Mode | Receive-only |

---

## Optional Parameters

The user may override any default.

**Scope** — what to package:
`current session` · `theme inside current session` · `provided material` · `custom scope`

**Source** — where to pull context from:
`current session` · `user-provided material` · `Mem0` · `Notion` · `Obsidian` · `other`
> External sources are never used unless explicitly requested.

**Target** — intended receiver:
`neutral` · `ChatGPT` · `Manus` · `Claude` · `Notion/Git` · `other`

**Depth** — level of detail:
`light` · `standard` · `full`

**Custom Instruction** — free text, e.g.:
- `make it short`
- `focus only on architecture`
- `include decisions and open questions`
- `optimize for Manus`
- `exclude implementation details`

---

## Intent Confirmation

If the request is clear, auto-confirm briefly:

> Intent confirmed: CP from current session · source: current session only · depth: standard · target: neutral.

If ambiguous, ask **one** clarification question.

---

## Required CP Sections

Every CP must include all 11 sections:

1. Transfer Header
2. Executive Handover
3. Strategic Context
4. Scope & Boundaries
5. Current State
6. Decisions / Locked Points
7. Open Questions
8. Risks / Ambiguities
9. Next Recommended Action
10. Source Notes
11. Receiver Instruction

---

## Receiver Instruction (mandatory in every CP)

Every CP must contain this verbatim:

> This is a Continuity Pack. Absorb it as transferred context. Do not act on it yet. Do not produce new work unless explicitly asked. Treat it as the new starting point for future continuation.

---

## Negative Instruction Wording Rule

When writing "What the receiver must not do" in the Transfer Header, always use explicit negative form:

- **Correct:** `Do not reopen design decisions. Do not rely on archived v3 files unless explicitly asked.`
- **Incorrect:** `Reopen design decisions. Re-read v3 files.` ← ambiguous, reads as action instruction.

---

## Internal Quality Gate

Before outputting the CP, verify all 7 points:

1. Is the scope clear?
2. Is the source clear?
3. Is the current state accurate?
4. Are decisions separated from open questions?
5. Is the next action clear?
6. Is the receiver told not to act yet?
7. Could another LLM continue without guessing?

If any check fails, **do not output the CP**. Instead respond:

```
CP generation blocked: quality insufficient.
Reason: [short reason].
Please clarify: [one question].
```

---

## Hard Boundaries

If the user asks for multi-session search, cross-LLM recovery, corpus synthesis, merge of several sessions, project/program aggregation, or deep reconstruction from archives, respond:

> This requires **CSE — Context Synthesis Engine** — not CP Core.

---

## Core Rule

**Simple CP first. Reliability over power.**
No external memory unless requested. No polished CP if context is uncertain.
