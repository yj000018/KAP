# Runtime and Deployment Topology

## Objective

Define a deployment that is simple enough for an MVP, but does not block later evolution.

## MVP topology

```text
Immich
  ├─ media store
  ├─ PostgreSQL
  └─ API
       ↓
Y-PIE batch worker
  ├─ ingestion adapter
  ├─ technical analyzers
  ├─ semantic classifier
  ├─ scoring rules
  └─ write-back adapter
       ↓
Y-PIE schema in PostgreSQL
```

