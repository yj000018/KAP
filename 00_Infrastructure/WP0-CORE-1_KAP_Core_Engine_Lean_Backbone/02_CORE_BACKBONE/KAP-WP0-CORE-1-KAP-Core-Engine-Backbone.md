# KAP Core Engine Backbone

**Sprint:** WP0-CORE-1
**Generated:** 2026-07-02

## 1. Overview

KAP Core Engine is the horizontal knowledge acquisition and assimilation backbone of yOS. It is not itself every downstream domain. It routes knowledge; it does not own all domains.

**Key Axioms:**
- YOUniverse is the downstream personal/life/user/environment domain.
- Mem0 receives only distilled validated candidates, not raw corpus.
- Git/KAP is the complete source of truth.
- WP3 remains suspended until WP0/WP1/WP2 readiness gates are satisfied.

## 2. The 5 Blocks of KAP Core Engine

### Block 1: Source Registry
| block | purpose | input | output | not_responsible_for |
|---|---|---|---|---|
| 1. Source Registry | Map the territory and track sync state. | User intent, new APIs, existing repos. | `source_registry.schema.json` | Fetching data. |

### Block 2: Acquisition & Preservation
| block | purpose | input | output | not_responsible_for |
|---|---|---|---|---|
| 2. Acquisition & Preservation | Fetch raw data, prove provenance, commit to Git. | Source Registry, APIs, UI fallbacks. | Raw files, `_SOURCE_CARD.md`, `acquisition_manifest.schema.json`. | Normalizing schemas or understanding content. |

### Block 3: Classification & Routing
| block | purpose | input | output | not_responsible_for |
|---|---|---|---|---|
| 3. Classification & Routing | Determine where the raw knowledge belongs. | Raw files. | `routing_manifest.schema.json` | Summarizing or rewriting content. |

### Block 4: Processing & Distillation
| block | purpose | input | output | not_responsible_for |
|---|---|---|---|---|
| 4. Processing & Distillation | Normalize to yOS schemas and extract high-value memory candidates. | Raw files + Routing Manifest. | Normalized MD, `memory_candidate.schema.json`. | Injecting into downstream systems. |

### Block 5: Gates & Delta
| block | purpose | input | output | not_responsible_for |
|---|---|---|---|---|
| 5. Gates & Delta | Ensure persistence and calculate deltas for continuous autonomous runs. | Previous State, New State. | `delta_manifest.schema.json`, Git Push. | Manual human review. |
