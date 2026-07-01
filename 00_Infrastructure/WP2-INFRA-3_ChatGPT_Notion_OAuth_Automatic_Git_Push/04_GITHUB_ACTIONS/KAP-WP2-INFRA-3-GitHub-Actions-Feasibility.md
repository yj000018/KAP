# KAP WP2-INFRA-3 — GitHub Actions Feasibility

**Generated:** 2026-07-01T21:00:47Z

## Assessment

GitHub Actions is **useful and safe** for KAP corpus validation. It runs automatically after every `git push` from Manus.

| capability | feasible | implemented | notes |
|---|---|---|---|
| Structure validation (key folders exist) | YES | ✅ YES | Checks 00_Infrastructure, 02_Source_Acquisition |
| Sprint inventory count | YES | ✅ YES | Counts sprint folders automatically |
| JSON validation | YES | ✅ YES | `python3 -m json.tool` on all .json files |
| Changed files listing | YES | ✅ YES | `git diff HEAD~1 HEAD` |
| Corpus summary (file count, size) | YES | ✅ YES | `find` + `du` |
| Auto-push from Manus | N/A | N/A | Manus pushes; Actions validates after |
| Issue creation on missing files | POSSIBLE | NOT YET | Can add in INFRA-4 |
| Checksum validation | POSSIBLE | NOT YET | Can add in INFRA-4 |

## Workflow Location

`.github/workflows/kap-corpus-validate.yml`

## Key Distinction

> GitHub Actions **validates** after push. It does NOT push for Manus.
> Manus must always commit + push first using `kap_commit_push.sh`.
> Actions then runs automatically and provides a validation report in the GitHub Actions tab.

## Trigger

Runs on every push to `main` branch — zero configuration needed after initial push.
