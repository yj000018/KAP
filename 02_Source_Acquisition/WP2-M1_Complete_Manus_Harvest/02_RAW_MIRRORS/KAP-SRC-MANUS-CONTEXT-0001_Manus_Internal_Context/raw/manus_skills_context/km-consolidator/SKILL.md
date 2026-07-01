---
name: km-consolidator
description: Audits, merges, compresses, and reorganizes Manus memory entries in Notion to maximize available Knowledge Quantity capacity. Use when the user hits memory limits, requests memory cleanup, or wants to consolidate past sessions into single project cards.
license: Complete terms in LICENSE.txt
---

# KM Consolidator (Knowledge Management)

This skill provides a structured workflow to optimize the Manus Memory Hub in Notion, specifically addressing the "Knowledge Quantity Limit" which is primarily driven by the **number of entries** rather than their individual length.

## Core Strategy

The primary goal is to **reduce the total number of entries** while preserving critical information.
1. **Merge** related entries (e.g., multiple conversation archives about the same project).
2. **Compress** verbose transcripts into structured syntheses.
3. **Archive** redundant or obsolete entries (change status, don't delete unless explicitly requested).

## Workflow

### 1. Audit Current State
Always start by auditing the current memory state to identify consolidation opportunities.

```bash
# Search for all entries in the Memory Hub
manus-mcp-cli tool call notion-search --server notion --input '{"query": "", "query_type": "internal", "data_source_url": "collection://94086d51-ac40-4027-b994-55c5681f72e5"}'
```
*Note: Use the exact data_source_url from the memory-manager constants if different.*

### 2. Identify Consolidation Targets
Look for:
- Multiple "📝 Conversation Archive" entries on the same topic.
- Project pages ("🎯 Projet / Thème") that can absorb related conversation archives.
- Very long entries (>10k characters) that can be summarized.

### 3. Execute Consolidation (The "Fusion" Protocol)

When merging multiple entries into one:

1. **Fetch** the content of all target entries using `notion-fetch`.
2. **Synthesize** the combined content using Claude Opus (prioritized for text processing).
3. **Create/Update** the master entry in Notion.
   - Use `notion-update-page` to append the synthesis to an existing Project page, OR
   - Use `notion-create-pages` to create a new "MASTER SESSION" or "MEGA PROJECT" entry.
4. **Archive** the old entries.
   - Use `notion-update-page` to change their "Statut" property to "Archivé".

#### Structure for Merged Entries
```markdown
# 📚 Synthèse Consolidée : [Topic]

## Vue d'Ensemble
[Executive summary of the combined knowledge]

## Points Clés (Consolidés)
- Point 1
- Point 2

## Historique des Décisions
- Date 1: Decision A
- Date 2: Decision B

## Sources (Archives)
- Link to original entry 1 (Archived)
- Link to original entry 2 (Archived)
```

### 4. Compression Rules

When compressing a single long entry:
- Remove raw transcripts or verbose dialogue.
- Keep the Table of Contents (ToC).
- Keep Decisions, Action Items, and core Concepts.
- Format strictly with bullet points and clear headers.

### 5. Validation and Reporting

After consolidation, verify the new entry count and report the gains to the user.

1️⃣ **Entries Reduced**: e.g., 6 entries merged into 2 (Gain: -4 entries)
2️⃣ **Space Saved**: e.g., 30k chars compressed to 15k chars
3️⃣ **Status**: Confirm old entries are marked "Archivé"

## Best Practices
- **Never delete** entries permanently unless explicitly asked. Changing status to "Archivé" is sufficient for the system to ignore them in active context loading.
- Always use the `Manus` tag on modified entries.
- Follow the `memory-manager` skill constants for exact Notion database IDs and property names.
