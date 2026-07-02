# KAP Source Branch Mapping

**Version:** 1.0  
**Gate:** CONNECTOR-DESIGN-GATE  

This document maps external source categories to their canonical KAP branches and defines the rules for classification and conflict resolution.

| Source Category | Target KAP Branch / Folder | Mapping Rules | Classification Rules | Conflict Rules | Exclusion Rules |
|---|---|---|---|---|---|
| **Manus** | `02_Source_Acquisition/Manus/` | Map by Task UID. Extract factsheets and durable outputs. | Classify by project tag if present in title/metadata. | Overwrite older factsheets if UID matches. | Exclude tasks < 10 messages unless marked durable. Exclude "New task". |
| **ChatGPT** | `02_Source_Acquisition/ChatGPT/` | Map by Conversation ID. | Classify by project name mentioned in first 3 prompts. | Append new messages to existing conversation files. | Exclude conversations < 3 turns. |
| **Notion** | `02_Source_Acquisition/Notion/` | Map by Notion Page ID to preserve hierarchy. | Classify by parent database or workspace. | Notion is legacy; Git overwrites Notion if conflict exists. | Exclude empty pages. |
| **Obsidian** | `02_Source_Acquisition/Obsidian_Import/` | Map by folder structure. | Maintain original vault hierarchy. | Obsidian imports take precedence over Notion for identical topics. | Exclude `.obsidian/` config files. |
| **Google Drive** | `02_Source_Acquisition/GDrive/` | Map by File ID. Convert Docs to MD, Sheets to CSV. | Classify by parent folder. | Append version timestamp if duplicate names exist. | Exclude shared-with-me files not owned by user. |
| **Mem0** | `02_Source_Acquisition/Mem0_Export/` | Map by Memory ID. | Classify by entity/topic. | Mark as "Memory-Derived" (lower confidence). | Exclude system-generated meta-memories. |
| **Git Repos** | `02_Source_Acquisition/Git_Repos/` | Map by Repo Name. | Classify by repository topic. | Fetch latest commit; do not rewrite history. | Exclude `node_modules`, `.git/`, binary blobs. |
| **Web Sources** | `02_Source_Acquisition/Web_References/` | Map by Domain/Slug. | Classify by topic. | Snapshot by date. | Strictly whitelist only; exclude generic scraping. |
