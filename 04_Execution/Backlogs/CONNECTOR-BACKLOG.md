# KAP Connector Backlog

**Version:** 1.0  
**Gate:** CONNECTOR-DESIGN-GATE  

| Task ID | Connector | Priority | Dependencies | Risks | Required Credentials | Acquisition Allowed | Proposed Next Gate |
|---|---|---|---|---|---|---|---|
| CB-01 | Manus API Extractor | HIGH | None | Rate limits, pagination logic | Manus API Key | **NO** | CONNECTOR-IMPLEMENTATION-GATE |
| CB-02 | Notion API to Markdown | HIGH | None | Hierarchy flattening, block type support | Notion API Key | **NO** | CONNECTOR-IMPLEMENTATION-GATE |
| CB-03 | ChatGPT Export Parser | HIGH | None | JSON parsing of large export files | None (Local Export) | **NO** | CONNECTOR-IMPLEMENTATION-GATE |
| CB-04 | Google Drive Downloader | MEDIUM | Google Cloud Setup | Auth token expiration, binary files | Google OAuth Token | **NO** | CONNECTOR-IMPLEMENTATION-GATE |
| CB-05 | Mem0 API Sync | MEDIUM | None | Memory state drift | Mem0 API Key | **NO** | CONNECTOR-IMPLEMENTATION-GATE |
| CB-06 | Obsidian Vault Importer | LOW | Vault Access | Wikilink breakage | None (Local Files) | **NO** | CONNECTOR-IMPLEMENTATION-GATE |
| CB-07 | Web Reference Snapshotter | LOW | Whitelist Approval | Dynamic rendering, CAPTCHAs | None | **NO** | CONNECTOR-IMPLEMENTATION-GATE |
