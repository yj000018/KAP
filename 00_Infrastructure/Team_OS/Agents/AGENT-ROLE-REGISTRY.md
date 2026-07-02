# KAP Agent Role Registry

**Version:** 1.0  
**Gate:** AGENT-ROLE-GATE  

This registry defines the canonical roles, authorities, and boundaries of all agents operating within the KAP ecosystem.

| Agent ID | Agent Name | Role Type | Status | Authority Level | Allowed Actions | Forbidden Actions | Required Outputs | Gate Involvement | Owner / Supervisor |
|---|---|---|---|---|---|---|---|---|---|
| AGT-ARCH-01 | ChatGPT Guardian Architect | Architect | Active | Decision | Strategic architecture, Gate validation, MPM generation | Execution within KAP folder structure | MPMs, Gate Acceptances | All Gates | Human (Yannick) |
| AGT-EXEC-01 | Manus Executor | Executor | Active | Execution | File creation/update in KAP, Gate execution, Connector implementation | WP3 Acquisition, ZIP creation as primary corpus | Gate Reports, Markdown/JSON files | All Gates | Guardian Architect |
| AGT-CONN-01 | Connector Builder Agent | Builder | Proposed | Execution | Build connector scripts, test APIs | Full acquisition without authorization | Connector Scripts | CONNECTOR-IMPLEMENTATION-GATE | Manus Executor |
| AGT-AUDIT-01 | Source Auditor Agent | Auditor | Proposed | Advisory | Metadata verification, Deduplication check | Data mutation | Audit Reports | SOURCE-ACQUISITION-GATE | Guardian Architect |
| AGT-CURA-01 | Corpus Curator Agent | Curator | Proposed | Execution | Markdown normalization, Classification | Original source deletion | Normalized MD files | NORMALIZATION-GATE | Guardian Architect |
| AGT-GIT-01 | Git Persistence Auditor | Auditor | Proposed | Review | File existence checks, Git status checks | None | Git Proofs | All Gates | Manus Executor |
