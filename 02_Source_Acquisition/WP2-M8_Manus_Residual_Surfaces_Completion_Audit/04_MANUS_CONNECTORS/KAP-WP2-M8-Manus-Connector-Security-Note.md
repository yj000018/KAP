# KAP WP2-M8 — Manus Connector Security Note

1. **Which connectors are active?** GitHub, Gmail, Google Calendar.
2. **Which connectors are disabled?** 102 other catalog connectors.
3. **Which connectors are useful for KAP?** GitHub (for persistence) and Notion (for source extraction).
4. **Which tokens exist?** GitHub PATs, Notion Bearer token, Mem0 API keys.
5. **Which raw tokens were captured locally?** Yes, in `/home/ubuntu/KAP/00_Infrastructure/credentials_restricted/MANUS_CONNECTORS_RAW_TOKENS_RESTRICTED.md`.
6. **Which redacted fingerprints were recorded?** GitHub (`ghp_...XCvX`, `ghp_...T0FC`), Notion (`ntn_...s7JL`).
7. **Which tokens expire soon?** GitHub PAT `ghp_...XCvX` expires July 31, 2026.
8. **Which connectors require manual re-auth?** GitHub (one of the PATs is invalid).
9. **What should yOS remember as connector capability map?** GitHub for git operations, Notion for knowledge extraction.
10. **Which credential files must remain local-only?** `MANUS_CONNECTORS_RAW_TOKENS_RESTRICTED.md` and `.json`.
