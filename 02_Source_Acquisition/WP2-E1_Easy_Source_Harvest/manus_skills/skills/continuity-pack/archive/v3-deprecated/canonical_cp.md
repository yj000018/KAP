# [CP Title]

## CP Metadata

```yaml
protocol: yos-continuity-protocol
protocol_version: "3.0"
generated_by: [Manus / Claude / ChatGPT / etc.]
generated_at: [YYYY-MM-DD HH:MM UTC]
source_session: [Name or N/A]
source_project: [Project name or N/A]
source_scope: [session | theme | provided material | custom]
source_layers: [current_session | mem0 | notion | obsidian | user_provided]
target: [neutral | chatgpt | manus | claude | notion | other]
handover_mode: [receive_only | execute]
depth: [light | standard | full]
source_freshness:
  current_session: fresh | not_used
  external_memory: fresh | unknown | stale_possible | dated (YYYY-MM-DD)
  user_provided: fresh | not_used
staleness_risk: low | medium | high
confidence: low | medium | high
qc_score: [0-10 or "pending"]
```

---

## 0. Transfer Header

| Field | Value |
|-------|-------|
| CP Type | [Session / Theme / Provided Material / Custom] |
| Source Scope | [What information was used to generate this CP] |
| Target Use | [Why this CP was created / where it goes next] |
| Intended Receiver | [Target LLM, Agent, User, or System — or "Neutral"] |
| Current State | [One-line status] |
| Continuity Depth | [Light / Standard / Full] |
| Confidence Level | [Low / Medium / High] |
| Staleness Risk | [Low / Medium / High] |
| Handover Mode | [receive_only / execute] |
| What the receiver must do | [Primary directive] |
| What the receiver must not do | [Boundaries] |
| Next Recommended Action | [The immediate next step] |

## Source Metadata

| Field | Value |
|-------|-------|
| Source Session Name | [Name or N/A] |
| Source LLM / Tool | [Manus / Claude / ChatGPT / etc.] |
| Source Date | [YYYY-MM-DD] |
| Source Project | [Project name or N/A] |
| Source Confidence | [Low / Medium / High] |
| Source Completeness | [Partial / Substantial / Complete] |

## Source Layering

### Current Live Session
- [Extracted from current session — or "Not used"]

### External Memory
- Source: [Mem0 / Notion / Obsidian / etc. — or "Not used"]
- Freshness: [known: YYYY-MM-DD | unknown | stale_possible]
- Confidence: [low / medium / high]
- Notes: [any caveats about reliability or age]

> If primarily external-memory based: **This CP is primarily based on recovered external memory, not the current live session.**

### User-Provided Material
- [Explicitly provided by user — or "None"]

## Receiver Instruction

> [receive_only]: This is a Continuity Pack. Absorb it as transferred context. Do not act on it yet. Do not produce new work unless explicitly asked. Treat it as the new starting point for future continuation.

> [execute]: This is a Continuity Pack. Read it fully, then execute the Next Recommended Action immediately.

---

## 1. Executive Handover

- **Where are we?** [Current position in the overall timeline]
- **Why does this exist?** [Trigger for this work]
- **What are we trying to accomplish?** [Immediate goal]
- **What has already been done?** [Completed milestones]
- **What remains to be done?** [Pending milestones]
- **What should the receiver do now?** [Specific instruction]
- **What should the receiver not reopen?** [Locked decisions]

## 2. Strategic Context

- **Vision:** [High-level vision]
- **Deeper Purpose:** [Why we are doing this]
- **Strategic Importance:** [Impact on the broader ecosystem]
- **Why this continuity matters:** [Risk of context loss]

## 3. Scope & Boundaries

- **Included:** [What is covered]
- **Excluded:** [What is explicitly out of bounds]

## 4. Current Architecture

[System design, components, or structural state relevant to the handover.]

## 5. Decision Register

| # | Decision | Context | Status |
|---|----------|---------|--------|
| 1 | [Decision] | [Why it was made] | Locked / Open |

> Locked = do not reopen. Open = still in play.

## 6. Terminology Register

| Term | Canonical Definition |
|------|---------------------|
| [Term] | [Definition in this context] |

## 7. Work Done / Not Done

### Completed
- [Task 1]

### Pending
- [Task 2]

## 8. Open Questions

- [Question: who answers it, what blocks on it]

## 9. Risks / Ambiguities

- [Risk: description and mitigation]

## 10. Backlog / Next Work

1. [Action Item 1]
2. [Action Item 2]

## 11. Reference Map

| Type | Reference | Location |
|------|-----------|----------|
| File | [Name] | [Path or URL] |
| Notion | [Page] | [URL] |

## 12. Resume Instructions

[Step-by-step instructions for the receiver to initialize and begin. Written for zero prior context.]
