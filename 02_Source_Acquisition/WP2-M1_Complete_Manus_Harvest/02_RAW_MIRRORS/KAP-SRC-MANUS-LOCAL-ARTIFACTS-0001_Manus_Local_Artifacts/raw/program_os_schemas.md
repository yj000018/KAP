# Program OS Schemas

These schemas define the core tracking files used in the Program Office.

## 1. PROGRAM_STATE.json

```json
{
  "project_name": "Project Name",
  "current_phase": "Phase Description",
  "pass": "X.Y",
  "status": "STATUS_ENUM",
  "last_updated": "YYYY-MM-DDTHH:MM:SS",
  "key_metrics": {
    "total_documents": 0,
    "completed_documents": 0,
    "validation_gates_passed": 0
  }
}
```

## 2. DOCUMENTATION_REGISTRY.json

```json
{
  "registry": [
    {
      "id": "DOC-01",
      "title": "Document Title",
      "path": "path/to/document.md",
      "status": "DRAFT | REVIEW_PENDING | REVISED | CANONICAL",
      "last_updated": "YYYY-MM-DDTHH:MM:SS",
      "dependencies": ["DOC-00"]
    }
  ]
}
```

## 3. API_CALL_LOG.json

```json
{
  "logs": [
    {
      "timestamp": "YYYY-MM-DDTHH:MM:SS",
      "model": "claude-sonnet-4-6",
      "purpose": "Review DOC-01",
      "status": "SUCCESS | FAILED",
      "tokens_used": 1500,
      "error_message": null
    }
  ]
}
```
