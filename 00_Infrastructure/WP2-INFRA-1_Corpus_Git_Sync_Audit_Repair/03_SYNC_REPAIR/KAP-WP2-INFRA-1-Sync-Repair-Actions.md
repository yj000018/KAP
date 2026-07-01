# KAP-WP2-INFRA-1-Sync-Repair-Actions

| action_id | source_path | target_path | action | git_added | committed | pushed | notes |
|---|---|---|---|---|---|---|---|
| R001 | `/home/ubuntu/KAP/` | `/home/ubuntu/KAP/.git/` | git init -b main | YES | YES | NO | Commit: `b0fb8414ebbc` |
| R002 | All sprint folders | KAP corpus | git add -A (3924 files) | YES | YES | NO | Push blocked: no remote |
| R003 | Embedded repos | .gitignore | Excluded session-navigator submodules | YES | YES | NO | Prevents submodule conflicts |
| R004 | Large raw JSON | .gitignore | Excluded *_raw.json + manus_all_tasks_raw.json | YES | YES | NO | Reduces repo size |
| R005 | ZIPs | .gitignore | Excluded *.zip from Git tracking | YES | YES | NO | ZIPs are secondary snapshots |
