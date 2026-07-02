# KAP Agent Handoff Protocol

**Version:** 1.0  
**Gate:** AGENT-ROLE-GATE  

## 1. Standard Handoff Packet Format
All handoffs between the Manus Executor and the ChatGPT Guardian Architect must occur via a standardized Markdown packet (e.g., Gate Report).

## 2. Required Context Fields
- Gate Name
- Execution Date
- Agent ID

## 3. Required Source/Gate References
- Previous Gate Status
- Governing MPM Reference

## 4. Required Output Paths
List of all files created or modified, with exact relative paths from the KAP root.

## 5. Required Final Status Format
Must use the exact string constant defined in the MPM (e.g., `AGENT_ROLE_GATE_PASS_READY_FOR_CONNECTOR_IMPLEMENTATION_GATE`).

## 6. Evidence
- Git commit hash.
- File existence verification.
- Output matrices.

## 7. Carried Forward Gaps
Minor gaps must be explicitly listed in the "Gaps & Blockers" section of the report to be carried forward to the next sprint.

## 8. Blocker Escalation
Blockers must trigger a `HOLD` status, stopping the pipeline until the Architect provides a remediation MPM.

## 9. Git Persistence Verification
The Executor must run `git status` and `git log` to verify commits before generating the final handoff packet.

## 10. Acquisition Authorization Check
The handoff packet must explicitly confirm: "No acquisition was performed."
