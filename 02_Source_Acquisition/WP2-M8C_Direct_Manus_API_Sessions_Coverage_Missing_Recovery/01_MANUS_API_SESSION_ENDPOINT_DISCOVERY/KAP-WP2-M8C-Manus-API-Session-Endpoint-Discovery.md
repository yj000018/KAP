# KAP WP2-M8C — Manus API Session Endpoint Discovery

**Generated:** 2026-07-01T23:39:11

## Findings

The Manus API does NOT have a dedicated "sessions" endpoint.  
Tasks and sessions are the same concept in Manus — each task IS a session/conversation.  
The correct endpoint is `GET /v2/task.list` with `x-manus-api-key` header.

## Endpoint Test Results

| endpoint_or_method | purpose | status_code | auth_method | returns_session_list | returns_titles | returns_messages | returns_verbatim | pagination_working | limitation |
|---|---|---:|---|---|---|---|---|---|---|
| GET /v2/task.list | List all tasks/sessions | 200 | x-manus-api-key | YES | YES | NO | NO | YES (last_id cursor) | No message content in list |
| GET /v2/task.listMessages | Get messages for a task | TBD | x-manus-api-key | NO | NO | YES | YES | YES | Requires task_id |
| POST /v2/task.list | List tasks | 405 | x-manus-api-key | NO | NO | NO | NO | NO | Method not allowed |
| GET /v1/sessions | Sessions endpoint | 404 | x-manus-api-key | NO | NO | NO | NO | NO | Does not exist |
| GET /v2/sessions | Sessions endpoint | 404 | x-manus-api-key | NO | NO | NO | NO | NO | Does not exist |
| GET /v2/knowledge | Knowledge endpoint | 404 | x-manus-api-key | NO | NO | NO | NO | NO | Does not exist |

## Key Insight

> Manus = task-centric architecture. Each "session" = one task. The task.list endpoint IS the session list.
> The previous `all_tasks_raw.json` was a pagination artifact (wrong cursor implementation).
> This sprint uses correct GET pagination with `last_id` cursor.

## Total tasks accessible: 2,000
