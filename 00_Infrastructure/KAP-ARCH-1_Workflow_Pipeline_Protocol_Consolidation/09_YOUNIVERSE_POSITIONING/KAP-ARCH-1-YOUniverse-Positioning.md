# KAP-ARCH-1: YOUniverse Positioning

**Program:** KAP
**Sprint:** KAP-ARCH-1
**Date:** 2026-07-02

## Overview
YOUniverse is the downstream visualization, interaction, and sense-making interface for the user's personal and system data. This document clarifies its relationship with KAP.

## 1. KAP is the Engine, YOUniverse is the Glass

- **KAP (Knowledge Acquisition Pipeline):** The backend. It acquires, normalizes, distills, and stores knowledge in Git/MD. It is ugly, structural, and machine-first.
- **YOUniverse:** The frontend. It reads from Git/MD and presents the data through the 7-domain chakra model (MVP1). It is beautiful, interactive, and human-first.

## 2. Unidirectional Data Flow

**Rule:** YOUniverse is read-only.
- It does not acquire data.
- It does not modify the Git/MD corpus.
- If the user interacts with YOUniverse (e.g., adding a tag or note), that interaction must be captured by a separate ingest pipeline (e.g., via Webhook to KAP), processed, and committed to Git before it appears in YOUniverse.

## 3. Phasing: System First, Personal Later

Currently, KAP is focused on **System/Project Knowledge** (yOS, MyOS, architectural decisions).
YOUniverse requires **Personal Knowledge** (emails, calendar, health, Readwise).

Therefore, full YOUniverse integration is deferred to **Phase 3** of the KAP roadmap. The existing MVP1 remains active but will not receive new personal data pipelines until Phase 3.

## 4. The 7-Domain Model

The 7-domain model established in MVP1 remains canon:
1. Root (Health/Physical)
2. Sacral (Wealth/Resources)
3. Solar Plexus (Creation/Work)
4. Heart (Relationships/Social)
5. Throat (Expression/Output)
6. Third Eye (Learning/Input)
7. Crown (Spirituality/Purpose)

When KAP Phase 3 begins, all personal data sources must be mapped to one of these 7 domains in the Domain Routing Matrix.
