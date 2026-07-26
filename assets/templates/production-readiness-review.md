# Production Readiness Review

## Use

Use before a pilot enters a live operator workflow or before a late-stage deployment expands its authority, volume, or user cohort.

## Required Fields

- Launch scope
- Production owner
- Target operator cohort and adoption plan
- Service and workflow objectives
- Eval baseline and regression gate
- Observability and audit coverage
- Incident trigger and severity model
- Support and escalation path
- Security, privacy, and compliance posture
- Data and source-of-truth readiness
- Containment boundary
- Fallback and rollback path
- Capacity and cost guardrail
- Training and runbook readiness
- Launch decision and blockers

## Optional Fields

- Launch window
- Dependency freeze window
- Change-management notes
- Communications plan
- Post-launch review date

## Typical Anti-Pattern

A polished demo is treated as launch approval while ownership, monitoring, incident response, containment, adoption, and rollback remain implicit.

## Completion Standard

A reviewer outside the build team can make a `go`, `conditional-go`, or `no-go` decision and can identify every blocker, owner, mitigation, and proof required before launch.

## Template

```md
# Production Readiness Review

- **Launch scope**:
- **Production owner**:
- **Target operator cohort and adoption plan**:
- **Service and workflow objectives**:
- **Eval baseline and regression gate**:
- **Observability and audit coverage**:
- **Incident trigger and severity model**:
- **Support and escalation path**:
- **Security, privacy, and compliance posture**:
- **Data and source-of-truth readiness**:
- **Containment boundary**:
- **Fallback and rollback path**:
- **Capacity and cost guardrail**:
- **Training and runbook readiness**:
- **Launch decision and blockers**:

## Readiness Decision Table

| Area | Posture | Evidence | Blocker | Owner | Due / next proof |
|---|---|---|---|---|---|
| Workflow | ready / conditional / blocked | ... | ... | ... | ... |
| Evaluation | ready / conditional / blocked | ... | ... | ... | ... |
| Reliability | ready / conditional / blocked | ... | ... | ... | ... |
| Governance | ready / conditional / blocked | ... | ... | ... | ... |
| Adoption | ready / conditional / blocked | ... | ... | ... | ... |

## Decision

- Decision: go / conditional-go / no-go
- Approver:
- Conditions:
- Re-review trigger:
```
