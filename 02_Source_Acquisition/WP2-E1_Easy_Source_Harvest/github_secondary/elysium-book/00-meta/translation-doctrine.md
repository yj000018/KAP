# ELYSIUM: Translation Doctrine

Translations of ELYSIUM must prioritize conceptual architecture over literal wording, while maintaining the rigorous, diagnostic tone of the English source.

## Core Rules

1. **Preserve Conceptual Architecture**: Do not localize the ontology in ways that alter the underlying system. The 7 Foundations, 38 Facets, and 12 Matrix Steps must map 1:1 across all languages.
2. **Preserve Technical Metadata**:
   - Preserve Markdown structure (headers, lists, bolding).
   - Preserve YAML front matter exactly (translate only the `title` field; leave keys and IDs intact).
   - Preserve module IDs (e.g., `P01_OPENING`).
3. **Immutable Terms**: `ELYSIUM`, `yOS`, and `FCS` must remain unchanged in all languages.
4. **Style & Tone**: Prefer elegant, literary French and Italian, but *never* at the cost of conceptual precision. Maintain technical consistency across all chapters.

## Specific Terminology Guidelines

- **"Agency"**: Remains *Agency* in French and Italian for now. (Alternatives like *agentivité* or *capacità d'azione* should only be used in explanatory notes, not as the primary term).
- **"Civilizational"**: Translate as *civilisationnel* (FR) and *civilizzazionale* (IT).
- **"Metabolic"**: Translate literally. It is a core structural concept, not just a metaphor.
- **"Operating system"**: Translate literally (*système d'exploitation*, *sistema operativo*) while preserving the metaphor.
- **"Foundation"**: Translate as *Fondation* (FR) / *Fondazione* (IT) when referring to the Seven Foundations.
- **"Facet"**: Translate as *Facette* (FR) / *Faccetta* (IT).
- **"Vision"**: Translate as *Vision* (FR) / *Visione* (IT).
- **"Consciousness"**: Translate as *Conscience* (FR) / *Coscienza* (IT).

## Translation Review States
Translations must pass through these lifecycle states in the YAML metadata:
1. `raw_translation`: Initial AI or human draft.
2. `terminology_checked`: Verified against the Canonical Glossary.
3. `stylistically_reviewed`: Checked for ELYSIUM voice and rhythm.
4. `conceptually_reviewed`: Verified for ontological fidelity.
5. `final`: Approved for compilation.
