# Visual Ontology

## Design rule

The ontology separates observation, interpretation, value and action. These must never be collapsed into one tag.

## Core entities

- VisualAsset
- AssetVariant
- Region
- PersonCandidate
- ObjectCandidate
- PlaceCandidate
- EventCandidate
- ConceptCandidate
- StyleCandidate
- Series
- Collection
- ProjectReference
- AnalysisRun
- Claim
- Evidence
- ReviewDecision

## Observation dimensions

### Technical
- format
- dimensions
- resolution
- sharpness
- blur
- noise
- exposure
- compression damage
- dynamic range
- crop integrity

### Visual
- dominant colors
- palette family
- brightness
- saturation
- contrast
- composition
- symmetry
- negative space
- texture
- geometry
- orientation

### Semantic
- objects
- people
- animals
- scenes
- activities
- text/OCR
- environment
- spatial relations

## Functional classes

Primary classes:
- art
- personal_memory
- person_portrait
- utility
- document
- screenshot
- product_research
- project_reference
- inspiration
- place
- event
- other
- unknown

Secondary classes are multi-valued and extensible.

## Value dimensions

Each is scored independently with confidence:
- technical_quality
- aesthetic_impact
- artistic_significance
- originality_relative
- abstraction
- conceptual_depth
- symbolic_density
- emotional_resonance
- biographical_importance
- utility_value
- project_relevance
- uniqueness
- preservation_priority

## Relations

- depicts
- contains
- located_at
- captured_during
- belongs_to_series
- variant_of
- duplicate_of
- visually_similar_to
- stylistically_similar_to
- conceptually_similar_to
- inspired_by
- associated_with_project
- evokes
- contradicts
- supersedes

## Action recommendations

- preserve
- favorite
- promote_to_collection
- stack
- archive
- review
- quarantine
- delete_candidate
- retain_best_variant

No ontology term authorizes deletion by itself.

## Controlled extensibility

New classes require:
1. definition;
2. examples and counterexamples;
3. parent relation;
4. expected evidence;
5. model/rule source;
6. migration impact;
7. review owner.
