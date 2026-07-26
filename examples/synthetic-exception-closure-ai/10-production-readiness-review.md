# Production Readiness Review

- **Launch scope**: One exception category, one regional operations team, three coordinators, human-gated task creation, and 100-200 submissions across four weeks.
- **Production owner**: Regional operations coordinator, with the program manager as business escalation owner and the technical evaluation owner as quality owner.
- **Target operator cohort and adoption plan**: Three trained coordinators; shadow mode during calibration week; queue-first handling for eligible cases from week one; target 80% eligible-work adoption by week two.
- **Service and workflow objectives**: 95% of drafts available within two minutes during operating hours; 30% median review-to-task improvement; 90% acceptable closure evidence; no unauthorized task creation.
- **Eval baseline and regression gate**: Versioned pilot set includes golden, failure, edge, ambiguous, and demo-killing cases. Every behavior, model, prompt, rule, or data change must pass the critical-case regression set before release.
- **Observability and audit coverage**: Retain input reference, extracted fields, model result, confidence, rationale, coordinator edit, approval, task ID, closure decision, timestamps, build version, and error state.
- **Incident trigger and severity model**:
  - critical: unauthorized state change, missing approver, lost source evidence, or audit corruption
  - high: repeated incorrect in-scope disposition causing operational delay
  - medium: latency, queue, or metadata degradation with manual path available
- **Support and escalation path**: Coordinator reports through the pilot support channel; technical owner triages within the agreed window; critical incidents escalate immediately to production owner and program manager.
- **Security, privacy, and compliance posture**: Pilot reads only required submission fields, limits write access to approved task creation, uses operator identity for approval, and follows existing evidence-retention rules.
- **Data and source-of-truth readiness**: Triage guide, required metadata, allowed category boundary, task fields, and evidence standard are versioned. The tasking system remains the source of truth.
- **Containment boundary**: Single category, single region, three operators, human approval for every write, no autonomous closure, and no cross-region data access.
- **Fallback and rollback path**: Disable AI drafting while retaining structured intake and approval; coordinators complete review and task creation through the existing manual path; preserve traces for incident and eval review.
- **Capacity and cost guardrail**: Queue and reviewer capacity cover peak pilot volume; weekly review tracks inference cost, support time, and manual reconciliation burden against time saved.
- **Training and runbook readiness**: Coordinators complete scenario training for clear, uncertain, rejected, and rollback cases; support, incident, audit, and manual fallback steps are documented.
- **Launch decision and blockers**: `conditional-go`. Launch after the measured baseline, final 50-case regression run, coordinator training record, and alert routing test are complete. Any failed critical condition returns the decision to `no-go` pending re-review.

## Readiness Decision Table

| Area | Posture | Evidence | Blocker | Owner | Due / next proof |
|---|---|---|---|---|---|
| Workflow | conditional | bounded loop and acceptance contract | measured baseline pending | operations coordinator | baseline report before launch |
| Evaluation | conditional | representative case classes defined | final 50-case run pending | technical evaluation owner | signed regression result |
| Reliability | conditional | telemetry and fallback specified | alert routing test pending | technical owner | test incident |
| Governance | ready | human-gated write and audit fields defined | none | program manager | monitor |
| Adoption | conditional | cohort and target defined | training record pending | operations coordinator | completed scenario training |

## Decision

- Decision: conditional-go
- Approver: Program manager with production owner concurrence
- Conditions: close the four blockers above
- Re-review trigger: any critical incident, material authority change, category expansion, cohort expansion, or rollback condition
