# KAP WP2-M8C — Tasks API vs Sessions API Separation

**Generated:** 2026-07-01T23:39:11

## Conclusion

In Manus, there is NO separate "sessions" API. Tasks = Sessions.

| concept | manus_equivalent | api_endpoint | notes |
|---|---|---|---|
| Session/Conversation | Task | GET /v2/task.list | Each task IS a session |
| Session messages | Task messages | GET /v2/task.listMessages | Requires task_id |
| Session ID | Task ID | task.id | e.g. D3fjbuEjnyThJ57BuonnhJ |
| Background subtask | Task with type=subtask | task.task_type | Wide Research Subtask = parallel map() subtask |

## Previous M8D Error Correction

The `all_tasks_raw.json` pagination artifact (12 titles × 100 repetitions) was caused by:
- Using wrong pagination cursor implementation
- The previous script restarted from the same position each time
- This sprint uses correct `last_id` cursor → returns 2,000 DISTINCT tasks

## Real Task Count: 2,000 distinct tasks
## Wide Research Subtasks: 2,000
## Real human sessions: 0
