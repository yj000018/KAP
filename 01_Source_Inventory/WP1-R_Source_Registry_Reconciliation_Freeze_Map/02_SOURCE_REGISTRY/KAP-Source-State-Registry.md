# KAP Source State Registry v2.0

**Sprint:** WP1-R + Addendum
**Generated:** 2026-07-02
**Addendum:** Source Lifecycle & Project Knowledge Phase Correction

This registry is a **living catalog** — sources can be activated, deactivated, deferred, excluded, or added without redesigning KAP.

## Current Active Scope: PHASE_1_YOS_MYOS_SELF_KNOWLEDGE

| source_id | source_name | wp2_branch | activation_status | scope_phase | primary_domain | connector_status | enabled | acquisition_priority | source_status | risk_level | next_action |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SRC-MANUS-01 | Manus Sessions API | WP2-MANUS | ACTIVE_NOW | PHASE_1_YOS_MYOS_SELF_KNOWLEDGE | YOS_CORE | AVAILABLE_NOW | YES | HIGH | BASELINE_CAPTURED | HIGH | Execute WP2-MANUS-FINAL |
| SRC-CHATGPT-01 | ChatGPT History | WP2-CHATGPT | DEFERRED_LATER | PHASE_1_YOS_MYOS_SELF_KNOWLEDGE | YOS_CORE | NEEDS_EXPORT | NO | MEDIUM | DEFERRED | LOW | None |
| SRC-CLAUDE-01 | Claude History | WP2-CLAUDE | DEFERRED_LATER | PHASE_1_YOS_MYOS_SELF_KNOWLEDGE | YOS_CORE | NEEDS_EXPORT | NO | MEDIUM | DEFERRED | LOW | None |
| SRC-GEMINI-01 | Gemini History | WP2-GEMINI | DISABLED_BY_NON_USE | OPTIONAL_FUTURE | YOS_CORE | NEEDS_EXPORT | NO | LOW | DEFERRED | LOW | None |
| SRC-GROK-01 | Grok History | WP2-GROK | DEFERRED_LATER | OPTIONAL_FUTURE | YOS_CORE | NEEDS_EXPORT | NO | LOW | DEFERRED | LOW | None |
| SRC-PERPLEXITY-01 | Perplexity History | WP2-PERPLEXITY | DEFERRED_LATER | PHASE_2_PROJECT_KNOWLEDGE_AND_STATE | PROJECT_KNOWLEDGE | NEEDS_EXPORT | NO | LOW | DEFERRED | LOW | None |
| SRC-NOTION-01 | Notion YOS Workspaces | WP2-NOTION | BLOCKED_CONNECTOR | PHASE_1_YOS_MYOS_SELF_KNOWLEDGE | YOS_CORE | AVAILABLE_BUT_DISABLED | NO | HIGH | REOPEN_REQUIRED | HIGH | Enable Notion connector |
| SRC-MEM0-01 | Mem0 Global Context | WP2-MEM0 | BLOCKED_CONNECTOR | PHASE_1_YOS_MYOS_SELF_KNOWLEDGE | YOS_CORE | AVAILABLE_BUT_DISABLED | NO | HIGH | REOPEN_REQUIRED | HIGH | Enable Mem0 connector |
| SRC-GITHUB-01 | YOS Monorepo | WP2-GITHUB | ENABLED_READY | PHASE_1_YOS_MYOS_SELF_KNOWLEDGE | YOS_CORE | AVAILABLE_NOW | NO | HIGH | DISCOVERED | MEDIUM | Execute WP2-GITHUB |
| SRC-OBSIDIAN-01 | Y-WORLD Vault | WP2-OBSIDIAN | ENABLED_READY | PHASE_1_YOS_MYOS_SELF_KNOWLEDGE | YOS_CORE | AVAILABLE_NOW | NO | MEDIUM | DISCOVERED | LOW | Execute WP2-OBSIDIAN |
| SRC-LOCAL-FILES-01 | Manus Skills Directory | WP2-LOCAL-FILES | ACTIVE_NOW | PHASE_1_YOS_MYOS_SELF_KNOWLEDGE | YOS_CORE | AVAILABLE_NOW | YES | HIGH | BASELINE_VERIFIED | LOW | None |
| SRC-WEBSITES-01 | Deployed YOS Websites | WP2-WEBSITES | ACTIVE_NOW | PHASE_2_PROJECT_KNOWLEDGE_AND_STATE | PROJECT_KNOWLEDGE | AVAILABLE_NOW | YES | MEDIUM | BASELINE_VERIFIED | LOW | None |
| SRC-LOGS-TELEMETRY-01 | yOS Telemetry | WP2-LOGS-TELEMETRY | DEFERRED_TELEMETRY | PHASE_4_TELEMETRY_AND_SENSORS | TELEMETRY | FUTURE_CONNECTOR | NO | LOW | DEFERRED | LOW | None |
| SRC-HOME-AUTOMATION-01 | Home Assistant Logs | WP2-HOME-AUTOMATION | DEFERRED_TELEMETRY | PHASE_4_TELEMETRY_AND_SENSORS | TELEMETRY | FUTURE_CONNECTOR | NO | LOW | DEFERRED | LOW | None |
| SRC-OTHER-01 | Emails and Calendar | WP2-OTHER | DEFERRED_YOUNIVERSE | PHASE_3_YOUNIVERSE_PERSONAL_DATA | YOUNIVERSE | EXCLUDED | NO | LOW | EXCLUDED | LOW | None |

## Lifecycle Activation Status Legend

| value | meaning |
|---|---|
| ACTIVE_NOW | Source is currently in acquisition scope |
| ENABLED_READY | Source can be acquired but is not current priority |
| DISABLED_BY_CHOICE | Deliberately disabled |
| DISABLED_BY_LOW_QUALITY | Disabled because outputs are not valuable enough |
| DISABLED_BY_NON_USE | Disabled because source is not actively used |
| DEFERRED_LATER | Future source, not now |
| DEFERRED_YOUNIVERSE | Future personal/life/user/environment source |
| DEFERRED_TELEMETRY | Future logs/sensors/monitoring source |
| BLOCKED_AUTH | Needs authentication |
| BLOCKED_CONNECTOR | Needs connector/adaptor |
| EXCLUDED_BY_POLICY | Excluded unless Architect explicitly changes scope |
| REQUIRES_ARCHITECT_DECISION | Cannot decide automatically |

## Scope Phase Legend

| scope_phase | definition |
|---|---|
| PHASE_1_YOS_MYOS_SELF_KNOWLEDGE | Consolidate yOS/MyOS knowledge about itself |
| PHASE_2_PROJECT_KNOWLEDGE_AND_STATE | Consolidate dynamic project knowledge, state, deltas, assets, resources |
| PHASE_3_YOUNIVERSE_PERSONAL_DATA | Personal/life/user/environment data |
| PHASE_4_TELEMETRY_AND_SENSORS | Logs, sensors, monitoring, home automation, event streams |
| OPTIONAL_FUTURE | Possible future source, not needed now |
| EXCLUDED | Out of scope unless manually reopened |
