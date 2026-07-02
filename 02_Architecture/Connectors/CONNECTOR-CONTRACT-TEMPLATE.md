# KAP Connector Contract Template

**Version:** 1.0  
**Gate:** CONNECTOR-DESIGN-GATE  

Every KAP connector must satisfy this contract before proceeding to the Implementation Gate.

## 1. Source Identity & Scope
- **Source System:** [Name of the external system]
- **Data Types:** [e.g., Markdown, JSON, PDF, CSV]
- **Scope Limits:** [What is explicitly EXCLUDED from extraction]

## 2. Authentication & Access
- **Auth Method:** [e.g., API Key, OAuth, Local File Access]
- **Credential Storage:** Must use 1Password / Manus Internal Secrets.
- **Access Level:** Read-only preferred.

## 3. Extraction & Transformation
- **Extraction Method:** [e.g., REST API pagination, local file read]
- **Metadata Fields Required:** [e.g., Source URL, Original Author, Creation Date]
- **Transformation Method:** [How data is converted to canonical Markdown/JSON]
- **Deduplication Strategy:** [How the connector prevents duplicate ingestion]

## 4. Storage & Persistence
- **Storage Target:** `02_Source_Acquisition/[System_Name]/`
- **Git Persistence:** All outputs must be committed to the KAP Git repository.
- **Format:** Pure Markdown (`.md`) or JSON (`.json`). No ZIPs as primary output.

## 5. Validation & Failure Handling
- **Validation Rules:** [How to verify the extraction succeeded]
- **Failure Modes:** [e.g., Rate limits, API changes]
- **Retry Policy:** Must implement K5 staggered retry (2x fast, 1x 1min, 1x 5min).
- **Security/Privacy:** [Handling of PII or sensitive data]

## 6. Review Gates
- **Implementation Approved By:** [Role, e.g., Guardian Architect]
- **Acquisition Authorized By:** [Role, e.g., Guardian Architect]
