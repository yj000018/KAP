# Evaluation and Calibration Protocol

## Purpose

Define how Y-PIE capabilities are measured, compared, calibrated and promoted without relying on subjective impressions.

## Core rule

No AI capability may move from `specified` to `production` without:

1. a declared task;
2. a representative evaluation set;
3. ground-truth or adjudication rules;
4. metrics;
5. failure thresholds;
6. subgroup analysis;
7. model and prompt provenance;
8. rollback criteria.

## Evaluation layers

### 1. Deterministic technical analysis

Examples: dimensions, blur, exposure, OCR regions, dominant colors.

Metrics:
- absolute or relative error;
- precision/recall where applicable;
- reproducibility;
- runtime and memory;
- failure rate by format.

### 2. Functional classification

Examples: Art, Memory, Utility, Screenshot, Document, Product Research.

Metrics:
- per-class precision, recall and F1;
- confusion matrix;
- calibration error;
- abstention quality;
- correction rate in human review.

Minimum MVP emphasis:
- screenshots;
- documents;
- product research;
- utility images.

### 3. Similarity and duplicate detection

Metrics:
- pairwise precision/recall;
- cluster purity;
- false merge rate;
- protected-asset error rate;
- best-variant agreement with human judgment.

A false merge between unrelated assets is considered more severe than a missed relation.

### 4. Artistic analysis

Artistic judgments are not treated as objective truth.

Evaluate:
- inter-rater agreement;
- consistency under paraphrase and rerun;
- ranking stability;
- explanation usefulness;
- corpus-relative distinctiveness;
- sensitivity to genre, culture and medium.

Scores must identify their reference frame:
- generic model prior;
- selected reference corpus;
- personal-library calibration;
- project-specific calibration.

### 5. Emotional and biographical significance

The system evaluates probable significance, not internal human states.

Metrics:
- recall on user-protected memories;
- false low-value classification rate;
- calibration against explicit feedback;
- abstention on ambiguous cases;
- explanation traceability.

Any destructive workflow must optimize for extremely low false-negative protection errors rather than aggregate accuracy.

### 6. Visual DNA

Visual DNA claims require longitudinal evidence.

Evaluate:
- trait stability across resampling;
- temporal robustness;
- sensitivity to corpus composition;
- usefulness to the user;
- explanatory evidence;
- distinction between persistent trait, temporary period and dataset artifact.

## Evaluation corpus

The initial corpus must include at least:

- 100 art images;
- 100 personal memories;
- 100 screenshots or product-research images;
- 100 documents and receipts;
- 100 ordinary or low-quality images;
- duplicate and near-duplicate groups;
- edited and unedited variants;
- protected people, animals, places and events;
- difficult ambiguous examples.

The corpus is versioned. Test assets must not silently move between train, calibration and evaluation partitions.

## Human adjudication

For subjective tasks:

1. collect independent labels where practical;
2. allow `uncertain` and multi-label outputs;
3. preserve disagreement;
4. separate personal preference from general aesthetic judgment;
5. record adjudication rationale.

## Calibration

Every probabilistic score must be checked for calibration.

A score of 0.8 should mean approximately 80% empirical correctness under the score's declared semantics and evaluation domain.

Scores that are not calibrated must be labelled as rankings or heuristics, not probabilities.

## Abstention

Abstention is a first-class success condition.

The system should return `unknown`, `ambiguous` or `needs_review` when:
- evidence is insufficient;
- models disagree materially;
- the asset is outside the evaluated domain;
- privacy or safety policy prevents inference.

## Promotion gates

```text
specified
  -> prototype passes smoke tests
prototyped
  -> evaluation corpus results recorded
evaluated
  -> thresholds and failure analysis accepted
production
  -> monitoring, rollback and version pinning active
```

## Regression policy

Any model, prompt, preprocessing or ontology change triggers targeted regression tests.

A release is blocked if it:
- increases protected-memory risk;
- breaks idempotency or provenance;
- materially degrades a priority MVP class;
- changes score semantics without a version change;
- produces untraceable knowledge assertions.

## Reporting template

Each evaluation report records:
- capability and version;
- dataset version;
- model/prompt/preprocessing versions;
- metrics and confidence intervals;
- subgroup failures;
- representative false positives and negatives;
- known domain limits;
- decision: reject, research, calibrate, promote or rollback.
