# WP0 Gap Register

**Sprint:** WP0-CORE-1
**Generated:** 2026-07-02

| gap_id | gap | risk | blocking_before_wp3 | recommended_fix |
|---|---|---|---|---|
| GAP-01 | GitHub Actions PAT workflow scope issue if still present | HIGH | YES | Test push with PAT, ensure workflow scope is granted. |
| GAP-02 | WP1 not yet reconciled as global freeze map | MEDIUM | YES | Run WP1-R to initialize Source Registry instances. |
| GAP-03 | WP2-MANUS residuals still pending if M8B/M8C/M8D-PATCH not complete | HIGH | YES | Execute WP2-MANUS-FINAL to close remaining sessions. |
| GAP-04 | Remote Manus filesystem/source surface must be explicitly covered or declared covered | LOW | NO | Declare in WP1 if files are in scope or deferred. |
| GAP-05 | Source registry instances not yet created for all source branches | HIGH | YES | Generate `source_registry.schema.json` files per branch in WP1-R. |
| GAP-06 | Delta process not yet tested | MEDIUM | NO | Test delta script on WP2-MANUS after baseline freeze. |
