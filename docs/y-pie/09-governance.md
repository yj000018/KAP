# Safety, Privacy and Governance

## Safety posture

Y-PIE starts as an advisory system. It may classify, score, cluster and recommend. It does not perform irreversible actions without explicit policy and human authorization.

## Destructive-action ladder

### Level 0 — Observe
No write-back.

### Level 1 — Organize
Tags, albums, descriptions and review queues.

### Level 2 — Hide or archive proposal
Non-destructive recommendation only.

### Level 3 — Quarantine
Move candidates into a reversible, time-limited review state.

### Level 4 — Trash
Allowed only under explicit user-approved policy with recoverability.

### Level 5 — Permanent deletion
Manual confirmation required by default.

## Protected conditions

An asset is protected from automated destructive recommendation when any apply:
- favorite or manually rated;
- linked to a protected person, animal, event or project;
- unique timestamp/location combination;
- only representative of an event cluster;
- carries unique metadata or annotation;
- emotionally or biographically high-value hypothesis;
- unresolved identity or synchronization conflict;
- source backup health is unknown.

## Privacy

Processing policies are selected by privacy class. Sensitive assets may be restricted to local models. Face embeddings, health documents, private locations and intimate content require stricter storage and access controls.

## Consent and identity

Face recognition creates candidates, not canonical identities. Naming and cross-modal linking require authorized resolution through KAP.

## Auditability

All write-backs and recommendations record:
- actor;
- policy;
- evidence;
- previous state;
- new state;
- timestamp;
- rollback path.

## Model governance

Before model adoption:
- document license and data handling;
- test on representative corpus;
- measure category-specific failures;
- define fallback behavior;
- pin model version;
- provide rollback.

## Bias and subjectivity

Artistic and emotional outputs must be labeled as model interpretations. The interface must distinguish observation, hypothesis, personal calibration and user-validated knowledge.

## Backup dependency

Pruning features remain disabled unless source assets have verified backup and restoration procedures.
