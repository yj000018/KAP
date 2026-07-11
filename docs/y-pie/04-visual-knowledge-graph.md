# Visual Knowledge Graph Projection

## Principle

The Visual Knowledge Graph is not a separate graph database owned by Y-PIE. It is a visual projection of the canonical KAP Knowledge Graph, enriched by PIE-specific observations and similarity structures.

## Graph layers

### Asset layer
Visual assets, variants, regions, derivatives and source lineage.

### Perceptual layer
Detected people, objects, scenes, text, colors, shapes and spatial relationships.

### Context layer
Places, dates, events, devices, albums, projects and acquisition sources.

### Meaning layer
Concepts, symbols, archetypes, moods, narratives, styles and themes.

### Personal layer
Emotional significance, biographical relevance, preference signals, creative periods and Visual DNA traits.

## Node classes

- Asset
- Region
- Person
- Animal
- Place
- Event
- Object
- Concept
- Symbol
- Style
- Palette
- Geometry
- Series
- Collection
- Project
- CreativePeriod
- Narrative

## Edge families

### Evidential
- observed_in
- supported_by
- inferred_from

### Semantic
- depicts
- evokes
- symbolizes
- associated_with

### Structural
- variant_of
- duplicate_of
- member_of_series
- member_of_collection

### Similarity
- visually_similar
- stylistically_similar
- semantically_similar
- compositionally_similar

### Temporal and developmental
- precedes
- evolves_into
- revisits
- diverges_from
- influences

## Graph confidence

Edges carry:
- confidence;
- evidence count;
- source models;
- human validation state;
- temporal validity;
- scope: generic, personal or project-specific.

## Graph-derived capabilities

- image-to-concept navigation;
- concept-to-project discovery;
- visual lineage and series reconstruction;
- hidden bridge detection between projects;
- recurring archetype detection;
- visual influence mapping;
- cross-modal links to notes, conversations and documents;
- narrative and exhibition generation.

## Projection strategy

PIE keeps high-volume similarity matrices and transient clusters operationally. Only meaningful, thresholded or curated relations are published into KAP. This prevents the canonical graph from being flooded by millions of low-value nearest-neighbor edges.

## Initial implementation

PostgreSQL is sufficient for early relationship storage and vector neighbors. A dedicated graph database is deferred until graph traversal becomes a proven bottleneck or a major product surface.