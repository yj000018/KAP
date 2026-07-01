---
name: session-synthesis
description: Generate a structured session card (fiche synthèse) for a single Manus session and archive it to Notion "Manus Memory — Sessions" AND push key facts to Mem0. Use when the user asks to synthesize, archive, or summarize a specific session, or at the end of a session to capture its essence. Part of the LLM Memory Pipeline (LMP). Always runs Mem0 push (Step 5) after Notion archiving.
---

# Session Synthesis

Generates a structured session card from a Manus session verbatim and archives it to Notion.

## Config

- **Notion Data Source ID**: `0720db9b-5e1d-41a2-bd0c-6721fe0dab94` (🗃️ Manus Memory — Sessions)
- **Cards dir**: `/home/ubuntu/manus_pipeline/session_cards/`
- **Export dir**: `/home/ubuntu/manus_pipeline/sessions_export/`
- **Model**: Claude Sonnet (`claude-sonnet-4-5`) via `ANTHROPIC_API_KEY`
- **Manus JWT**: refresh from browser if expired, store in `/home/ubuntu/manus_pipeline/.manus_token`

## Workflow

### Step 1 — Identify session UID

From Manus URL: `https://manus.im/app/<uid>` or from `all_sessions.json`.

### Step 2 — Collect verbatim

Run `scripts/collect_session.py` with the UID. Handles multi-segment sessions automatically.

### Step 3 — Generate card via Claude

Run `scripts/generate_card.py` with the UID. Output: `session_cards/<uid>_card.json`.

### Step 4 — Archive to Notion

Run `scripts/archive_to_notion.py`. Deduplication is automatic via `archived_uids.json`.

## Card Schema

```json
{
  "title": "Session title",
  "date": "YYYY-MM-DD",
  "depth_score": "landmark|substantial|standard|minor",
  "length_category": "xl|long|medium|short",
  "language": "fr|en|mixed",
  "project_hint": "yOS|eia|VISUAL_REALITY|DOMUS|GEN5|ODYSSEY|UNKNOWN",
  "themes": ["theme1"],
  "subthemes": ["subtheme1"],
  "executive_summary": "3-5 dense sentences",
  "context_and_intent": "Why this session was started",
  "what_was_done": "Actions taken",
  "outputs_produced": [{"type": "script|skill|page|config", "name": "...", "description": "..."}],
  "key_decisions": ["decision1"],
  "lessons_learned": {"worked_well": [], "failed_or_suboptimal": [], "discoveries": []},
  "challenges_and_blockers": ["challenge1"],
  "open_questions": ["question1"],
  "next_steps": ["step1"]
}
```

## Depth Score Guide

| Score | Criteria |
|---|---|
| `landmark` | Major architectural decision, new system built, paradigm shift |
| `substantial` | Significant progress, multiple outputs, complex problem solved |
| `standard` | Normal working session, moderate output |
| `minor` | Short session, test, quick task, trivial content |

## Notion Page Structure

- **Always open**: Executive Summary, Next Steps
- **Collapsed**: Context & Intent, What Was Done, Outputs, Key Decisions, Lessons Learned, Challenges, Open Questions
- **Properties**: Title, Date, Project, Depth, Length, Language, Themes, Subthemes, UID, Archived

## Step 5 — Push to Mem0 (MANDATORY after Step 4)

After every successful Notion archiving, ALWAYS push the session card to Mem0. This is non-optional — it ensures cross-session memory continuity in Y-OS.

```python
import os
from mem0 import MemoryClient
import json

client = MemoryClient(api_key=os.environ['MEM0_API_KEY'])

# Load the generated session card
with open(f'/home/ubuntu/manus_pipeline/session_cards/{uid}_card.json') as f:
    card = json.load(f)

# Build a rich text summary for Mem0 extraction
mem0_text = f"""
Session: {card['title']} ({card['date']})
Project: {card.get('project_hint', 'UNKNOWN')}
Depth: {card.get('depth_score', 'standard')}
Summary: {card.get('executive_summary', '')}
Key decisions: {'; '.join(card.get('key_decisions', []))}
Next steps: {'; '.join(card.get('next_steps', []))}
Lessons learned: {'; '.join(card.get('lessons_learned', {}).get('discoveries', []))}
"""

client.add(
    mem0_text,
    user_id="yannick",
    metadata={
        "source": "session_synthesis",
        "uid": uid,
        "project": card.get('project_hint', 'UNKNOWN'),
        "depth": card.get('depth_score', 'standard'),
        "type": "session_card"
    }
)
print(f"✅ Mem0: session {uid} pushed")
```

**Deduplication**: Mem0 handles semantic deduplication natively. No need to check UIDs manually.
**Async note**: Mem0 V3 `add()` is async — wait 5s before querying if needed.

## Notes

- Sessions with <50 words → marked `trivial`, skipped (no Claude call)
- Deduplication: check `archived_uids.json` before Notion archiving; Mem0 deduplicates automatically
- Cost: ~$0.01-0.05/session with Claude Sonnet + ~1 Mem0 add operation (free tier: 10k/month)
