# Y-PIE Capability Catalog

## Purpose

Define Y-PIE by reusable capabilities rather than by a large set of tightly coupled modules.

A capability describes what the system can do. A service, model, workflow or UI may implement one or more capabilities.

## Design rules

Every capability must be:

- useful independently;
- composable;
- observable;
- replaceable;
- versioned;
- callable without hidden state where practical.

Capabilities should not imply deployment topology.

## Capability groups

### A. Acquire

#### `register_asset`
Create or update the stable identity of a visual asset from Immich or another source.

#### `read_source_metadata`
Read source timestamps, location, albums, favorites, camera data and source-specific flags.

#### `produce_derivative`
Create a bounded analysis derivative without mutating the original.

#### `detect_change`
Determine whether source content or metadata requires re-analysis.

### B. Observe

#### `measure_technical_properties`
Dimensions, resolution, blur, exposure, noise, compression, orientation and image integrity.

#### `extract_text`
OCR with regions and confidence.

#### `detect_visual_regions`
Faces, objects, document areas, screens and salient regions.

#### `extract_palette`
Dominant colors, temperature, luminosity, saturation and palette descriptors.

#### `extract_embedding`
Produce a versioned vector representation for a declared purpose.

### C. Describe

#### `caption_asset`
Generate a concise factual description.

#### `classify_function`
Estimate primary functional category: Art, Memory, Utility, Screenshot, Document, Product Research or Other.

#### `assign_attributes`
Attach secondary semantic, stylistic and contextual descriptors.

#### `estimate_quality`
Keep technical, aesthetic and preservation quality separate.

### D. Compare

#### `find_exact_duplicates`
Content identity or exact encoded duplicate detection.

#### `find_near_duplicates`
Same scene, edit, crop, burst or minor variation detection.

#### `find_semantic_neighbors`
Content or concept similarity.

#### `find_style_neighbors`
Palette, composition, texture and visual-language similarity.

#### `rank_variants`
Recommend strongest variants while preserving protected assets.

### E. Organize

#### `cluster_assets`
Create temporary, versioned groups from declared similarity spaces.

#### `detect_series`
Infer intentional or emergent visual series.

#### `assign_series_role`
Hero, anchor, supporting, transition, detail, experiment or redundant variant.

#### `build_review_queue`
Produce a human-actionable queue with reasons and safety flags.

### F. Remember

#### `link_person_place_event`
Propose links to KAP entities using evidence and entity-resolution feedback.

#### `estimate_memory_significance`
Estimate probable emotional or biographical importance without claiming certainty.

#### `protect_memory`
Apply explicit safety policy preventing destructive recommendations.

#### `detect_unique_moment`
Estimate rarity inside an event or life context.

### G. Understand Art

#### `analyze_composition`
Balance, visual hierarchy, negative space, symmetry, rhythm and depth.

#### `estimate_abstraction`
Literal-to-nonfigurative spectrum with explanation.

#### `analyze_color_language`
Palette harmony, contrast strategy and corpus-relative palette traits.

#### `estimate_artistic_impact`
Multidimensional, model-relative evaluation; never a universal truth score.

#### `estimate_originality_relative_to_corpus`
Distinctiveness relative to the user's own library and selected reference corpus.

#### `detect_symbolic_motifs`
Propose recurring symbols or archetypes with uncertainty.

### H. Learn Visual DNA

#### `extract_visual_traits`
Build stable trait vectors from validated observations.

#### `detect_recurring_motifs`
Find motifs persistent across time, series and projects.

#### `detect_creative_periods`
Identify gradual evolution, rupture and return.

#### `compare_project_languages`
Describe overlaps and distinctions between CasaTAO, Elysium, KOSMOS and other projects.

#### `explain_personal_similarity`
Explain why an image aligns or conflicts with learned personal visual language.

### I. Curate

#### `recommend_collection`
Select a coherent set under declared goals and constraints.

#### `find_hidden_gems`
Identify high-value, low-visibility assets.

#### `detect_collection_gaps`
Find missing transitions, weak redundancy or absent themes.

#### `generate_visual_narrative`
Order images into an evidence-based story or sequence.

### J. Recommend

#### `recommend_keep`
Strong preservation recommendation.

#### `recommend_stack`
Group variants while retaining access.

#### `recommend_archive`
Non-destructive removal from active review surfaces.

#### `recommend_delete_candidate`
Quarantine candidate only, subject to policy and human review.

### K. Publish Knowledge

#### `build_evidence_bundle`
Package observations, provenance and model versions.

#### `propose_kap_assertion`
Produce a contract-compliant candidate for KAP.

#### `receive_entity_resolution`
Accept canonical identifiers and corrections from KAP.

#### `expose_query_surface`
Provide stable query APIs to KRE, ART and applications.

## MVP capability set

The MVP is limited to:

1. `register_asset`
2. `read_source_metadata`
3. `produce_derivative`
4. `measure_technical_properties`
5. `extract_text`
6. `extract_palette`
7. `extract_embedding`
8. `caption_asset`
9. `classify_function`
10. `assign_attributes`
11. `estimate_quality`
12. `find_exact_duplicates`
13. `find_near_duplicates`
14. `build_review_queue`
15. `recommend_keep`
16. `recommend_stack`
17. `recommend_delete_candidate`
18. `build_evidence_bundle`

Everything else is post-MVP unless required to evaluate architecture.

## Capability maturity states

```text
proposed -> specified -> prototyped -> evaluated -> production -> deprecated
```

A capability cannot enter production without:

- contract;
- acceptance tests;
- observability;
- failure behavior;
- privacy classification;
- fallback path.