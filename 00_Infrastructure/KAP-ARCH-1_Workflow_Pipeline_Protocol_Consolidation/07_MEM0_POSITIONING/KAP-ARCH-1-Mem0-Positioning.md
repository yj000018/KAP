# KAP-ARCH-1: Mem0 Positioning

**Program:** KAP
**Sprint:** KAP-ARCH-1
**Date:** 2026-07-02

## Overview
Mem0 is a critical component of the KAP ecosystem, but its role must be strictly bounded to prevent noise and context degradation. This document defines the exact positioning and usage rules for Mem0.

## 1. Mem0 is the Semantic Active Memory

Mem0 is not a database, not a log file, and not an archive. It is the **Semantic Active Memory** for agents.
It is designed to provide immediate, relevant context for active tasks, not to store the entire history of the universe.

## 2. The "Distilled Only" Rule

This is the most critical rule governing Mem0:
**Mem0 receives ONLY validated, distilled, semantic memory candidates.**

### What goes IN Mem0:
- Synthesized project states (e.g., "Project X is blocked by Y").
- Core user preferences and operational rules.
- High-level architectural decisions.
- Distilled facts extracted from long sessions.

### What stays OUT of Mem0:
- Raw conversation transcripts.
- Source code files.
- API keys, credentials, or secrets.
- Unfiltered personal data (emails, logs).
- Temporary task states ("I am currently downloading X").

## 3. The Injection Pipeline (WP5)

Mem0 injection is not an automatic side-effect of acquisition. It is a deliberate, downstream process managed by WP5 (KAP-to-Mem0 Instillation).

1. **Acquisition (WP2):** Raw data is acquired and saved to Git.
2. **Distillation (WP4):** Raw data is processed into Memory Candidates (JSON schema).
3. **Injection (WP5):** Memory Candidates are reviewed and pushed to Mem0 via the Mem0 Sync Pipeline.

## 4. The YOS Memory Bridge Exception

The `yOS Memory Bridge` (iOS/Shortcut capture to Mem0 via Webhook) is the only authorized direct-to-Mem0 pipeline. However, it must be strictly monitored to ensure it only captures semantic intents, not raw noise.
