# KAP WP1-S1: Blockers & Access Report

| blocker_id | source_family | blocker | impact | proposed_resolution | requires_yannick | urgency |
|---|---|---|---|---|---|---|
| BLK-001 | Notion | Notion connector is disabled in `~/.manus/config/config.json`. | Cannot programmatically query the `Manus Memory Hub` to inventory session archives, explicit knowledge, or project contexts. | Enable the Notion connector via `manus-config config save` after updating the configuration. | Yes (to authorize/authenticate connector) | High |
| BLK-002 | Mem0 | Mem0 connector is disabled in `~/.manus/config/config.json`. | Cannot query the associative memory layer to verify sync status or identify gaps. | Enable the Mem0 connector and provide `MEM0_API_KEY`. | Yes (to provide API key) | Medium |
| BLK-003 | GitHub | GitHub connector is disabled (raw API used as workaround). | Limited to public repositories only. Private repositories (if any) are invisible. Rate limits apply. | Enable the GitHub connector via `manus-config config save`. | Yes (to authorize/authenticate connector) | Medium |
| BLK-004 | ChatGPT | No programmatic access to ChatGPT history. | Potential loss of context packs, initialization prompts, and architectural discussions held outside Manus. | Define a manual export strategy or utilize existing context packs stored in Notion/GitHub. | Yes (to perform manual export) | Low |
| BLK-005 | YOS Repo | Extreme divergence between `main`, `master`, and `y-os-doctrine` branches. | Unclear which branch represents the canonical architectural truth, risking ingestion of deprecated concepts. | Architect must explicitly declare the canonical branch hierarchy for WP2 ingestion. | Yes (architectural decision) | High |
