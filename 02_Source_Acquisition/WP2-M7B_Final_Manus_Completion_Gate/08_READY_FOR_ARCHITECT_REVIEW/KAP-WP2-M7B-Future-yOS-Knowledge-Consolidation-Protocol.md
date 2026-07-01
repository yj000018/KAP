# KAP WP2-M7B — Future yOS Knowledge Consolidation Protocol

**Generated:** 2026-07-01T21:34:15Z

## 8.1 Future Sprint Closure Requirements
Every future sprint must return:
- sprint ID
- root folder
- files created
- files modified
- files intentionally ignored
- local-only files remaining
- commit hash
- push status
- GitHub URL
- blockers
- recommended next sprint

## 8.2 Future Knowledge Consolidation Loop
`detect → classify → place → source card → manifest → checksum → git add → commit → push → verify GitHub → update registry → ready_for_normalization`

## 8.3 Failure Prevention
| risk | prevention | gate |
|---|---|---|
| files outside KAP | Always write directly to `/home/ubuntu/KAP/` | Execution script |
| ZIP-only outputs | ZIPs are banned as primary outputs | Output format rules |
| final answer not written to file | All reports must be `.md` | Output format rules |
| narrow `git add` | Use `kap_commit_push.sh` or `git add .` | Git script |
| PAT scope issue | Ensure PAT has `workflow` scope if Actions needed | Pre-flight check |
| local-only scripts | Save scripts to `KAP/scripts/` | Execution script |
| duplicate reports | Overwrite existing or use strict naming | Execution script |
| unverified GitHub visibility | Return commit hash and URL | Final response |
