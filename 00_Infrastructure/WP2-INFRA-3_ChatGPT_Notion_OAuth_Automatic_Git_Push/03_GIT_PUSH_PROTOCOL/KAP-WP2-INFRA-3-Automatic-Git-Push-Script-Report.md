# KAP WP2-INFRA-3 — Automatic Git Push Script Report

**Generated:** 2026-07-01T21:00:47Z

| script_path | executable | tested | test_result | notes |
|---|---|---|---|---|
| `/home/ubuntu/KAP/00_Infrastructure/scripts/kap_commit_push.sh` | YES (chmod 755) | YES (INFRA-3 validation test) | PASS | Accepts sprint_folder, sprint_id, commit_msg |

## Usage

```bash
/home/ubuntu/KAP/00_Infrastructure/scripts/kap_commit_push.sh \
  /home/ubuntu/KAP/02_Source_Acquisition/WP2-M7_Mem0 \
  WP2-M7 \
  "KAP: complete WP2-M7 Mem0 export"
```

## Behavior

1. Validates inputs and folder existence
2. Sets PAT in remote URL
3. Checks for changes in sprint folder
4. `git add <sprint_folder>`
5. `git commit -m "<message>"`
6. `git push origin main`
7. Writes `GIT_PUSH_PROOF.md` in sprint folder
8. Exits with error code on failure
