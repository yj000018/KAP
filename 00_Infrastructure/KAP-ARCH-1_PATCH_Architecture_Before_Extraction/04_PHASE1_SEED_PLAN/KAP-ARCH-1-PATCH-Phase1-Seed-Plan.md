# KAP-ARCH-1-PATCH — Phase 1 Seed Plan

**Purpose:** Define how to later choose the minimum useful seed corpus for yOS/MyOS self-knowledge, without bulk extraction.

*Note: This is a planning file only. No extraction is authorized.*

## Seed Candidates

| candidate_seed | purpose | source_family | why_needed | bulk_required | recommended_scope | approval_required |
|---|---|---|---|---|---|---|
| KAP-ARCH-1 outputs | Core architecture | GitHub KAP | Defines the machine | NO | Full folder | YES |
| KAP-ARCH-1-PATCH | Current roadmap | GitHub KAP | Defines the limits | NO | Full folder | YES |
| WP0-CORE-1 | Core engine | GitHub KAP | Defines pipelines | NO | Full folder | YES |
| WP1-R | Source registry | GitHub KAP | Defines what exists | NO | Full folder | YES |
| Guardian Architect role | Agent definition | GitHub KAP | Defines authority | NO | Single file | YES |
| Protocol Registry | Execution rules | GitHub KAP | Defines how to act | NO | Single file | YES |
| Pipeline Registry | Data flow | GitHub KAP | Defines how to process | NO | Single file | YES |
| Connector Readiness Matrix | Access state | GitHub KAP | Defines what is open | NO | Single file | YES |
| Selected yOS project state | Context | GitHub yOS | Defines active work | NO | Selected only | YES |
| Selected Manus sessions | Core knowledge | Manus Sessions | High-value insights | NO | Top 10 only | YES |

## Seed Rules

1. Seed corpus must be minimal.
2. Seed corpus must be enough for yOS to find/recover more.
3. Seed corpus must avoid bulk acquisition.
4. Seed corpus must be Git/MD first.
5. Seed corpus must preserve provenance.
6. Seed corpus is not WP3.
7. Seed corpus is not Mem0 injection.
8. Seed corpus must be approved before extraction.
