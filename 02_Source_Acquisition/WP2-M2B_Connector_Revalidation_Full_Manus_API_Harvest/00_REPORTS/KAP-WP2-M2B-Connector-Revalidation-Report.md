# KAP WP2-M2B Connector Revalidation Report

| connector | status | auth_valid | accessible_objects | limitations | next_action |
|---|---|---|---|---|---|
| Manus API | OK | YES | 10,000+ tasks, 20 projects | Tasks paginated to 10k (cap hit) | Extract full details |
| Mem0 | OK | YES | 316 memories | None | None |
| GitHub | OK | YES (Public) | 20+ public repos | PAT verification timeout | Generate new PAT via UI |
| Notion (Y-world) | PARTIAL | YES | 100+ DBs | Sessions DB (5e51ded4) blocked | Share Sessions DB |
