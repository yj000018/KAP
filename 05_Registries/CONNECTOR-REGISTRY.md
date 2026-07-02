# KAP Connector Registry

**Version:** 1.0  
**Gate:** CONNECTOR-DESIGN-GATE  

| Connector ID | Source System | Status | Owner/Agent | Target Branches | Acquisition Auth | Last Validation | Risks | Notes |
|---|---|---|---|---|---|---|---|---|
| CONN-MANUS-01 | Manus | DESIGNED | Manus Executor | `02_Source_Acquisition/Manus/` | **NO** | 2026-07-02 | Pagination limits | Requires API key |
| CONN-NOTION-01 | Notion | DESIGNED | Manus Executor | `02_Source_Acquisition/Notion/` | **NO** | 2026-07-02 | Hierarchy loss | Requires API key |
| CONN-OAI-01 | ChatGPT | DESIGNED | Manus Executor | `02_Source_Acquisition/ChatGPT/` | **NO** | 2026-07-02 | Large JSON parsing | Processes local export |
| CONN-GDRIVE-01 | Google Drive | DESIGNED | Manus Executor | `02_Source_Acquisition/GDrive/` | **NO** | 2026-07-02 | OAuth expiry | Requires GCP project |
| CONN-MEM0-01 | Mem0 | DESIGNED | Mem0 Memory Layer | `02_Source_Acquisition/Mem0_Export/` | **NO** | 2026-07-02 | State drift | Requires API key |
| CONN-OBS-01 | Obsidian | DESIGNED | Obsidian Nav Layer | `02_Source_Acquisition/Obsidian_Import/` | **NO** | 2026-07-02 | Link breakage | Local filesystem |
| CONN-WEB-01 | Web URLs | DESIGNED | Manus Executor | `02_Source_Acquisition/Web_References/` | **NO** | 2026-07-02 | CAPTCHAs | Whitelist only |
