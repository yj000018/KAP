# KAP Standard Sprint Completion Protocol

**Version:** 1.0  
**Established:** 2026-07-01  
**Authority:** WP2-INFRA-3  
**Applies to:** All future KAP sprints executed by Manus

---

## MANDATORY RULES

Every KAP sprint MUST:

1. **Execute** the new sprint — do not repackage old reports
2. **Write all outputs** into `/home/ubuntu/KAP/02_Source_Acquisition/<SPRINT_ID>_<NAME>/` or appropriate subfolder
3. **Create `.md` reports** for all human-readable outputs
4. **Create `.json` inventories** when structured data exists
5. **Create source cards / manifests / checksums** if source acquisition occurred
6. **Run git status** before committing
7. **Git add** the sprint folder only
8. **Commit** with standard message format
9. **Push** to GitHub
10. **Return proof** — no ZIP required unless explicitly requested

---

## COMMIT MESSAGE FORMAT

```
KAP: complete <SPRINT_ID> <short sprint name>
```

Examples:
- `KAP: complete WP2-M7 Mem0 full export`
- `KAP: complete WP2-INFRA-4 GitHub Actions validation`
- `KAP: complete WP3-A1 KAP architecture synthesis`

---

## AUTO-PUSH SCRIPT

Use the canonical script for every sprint:

```bash
/home/ubuntu/KAP/00_Infrastructure/scripts/kap_commit_push.sh <sprint_folder> <sprint_id> "<commit_message>"
```

---

## REQUIRED FINAL RESPONSE FORMAT

Every sprint must end with this exact table:

| field | value |
|---|---|
| execution_status | COMPLETE / PARTIAL / BLOCKED |
| root_folder | `/home/ubuntu/KAP/...` |
| files_created | N |
| commit_hash | `xxxxxxx` |
| push_success | YES / NO |
| repo_url | https://github.com/yj000018/KAP |
| blockers | none / description |
| recommended_next_sprint | WP2-XXX — Name |

Followed by exactly:

> KAP <SPRINT_ID> complete. <one-line description> ready for Architect review.

---

## FOLDER STRUCTURE (when applicable)

```
/home/ubuntu/KAP/02_Source_Acquisition/<SPRINT_ID>_<NAME>/
  00_REPORTS/
  01_MANIFESTS/
  02_RAW_MIRRORS/
  03_SOURCE_CARDS/
  04_REGISTRIES/
  05_CHECKSUMS/
  06_SCREENSHOTS/
  07_HTML_SNAPSHOTS/
  08_TEXT_EXTRACTS/
  09_JSON_EXPORTS/
  10_TASK_OUTPUTS/
  11_WEBSITE_CAPTURES/
  12_USER_INPUT_REQUESTS/
  13_BLOCKERS/
  14_READY_FOR_ARCHITECT_REVIEW/
```

Infrastructure sprints use `/home/ubuntu/KAP/00_Infrastructure/<SPRINT_ID>_<NAME>/`.

---

## WHAT IS NO LONGER REQUIRED

- ❌ ZIP bundles (GitHub is the transfer mechanism)
- ❌ Repackaging previous reports
- ❌ Harvesting sources already acquired
- ❌ Delivering ZIPs to chat unless user explicitly requests

---

## NOTION TOKEN (canonical)

`<NOTION_TOKEN_IN_MANUS_SECRETS>`

Bot: MANUS | Workspace: Y-world | Access: FULL (100+ DBs)

## GITHUB PAT (canonical)

`<GITHUB_PAT_IN_MANUS_SECRETS>`

Repo: https://github.com/yj000018/KAP | Expires: Jul 31 2026
