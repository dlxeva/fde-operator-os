# Field Signal Log

- **Signal ID and date**: FSL-001 — synthetic pilot week one
- **Source and workflow context**: Coordinator review queue; ambiguous submissions for the target exception category.
- **Operator or stakeholder**: Two operations coordinators and one frontline submitter.
- **Observation and source evidence**: Coordinators repeatedly open the unofficial chat group to interpret location context before deciding disposition. Evidence includes three case traces, chat references, and coordinator edits that add the same missing location detail.
- **Impact, severity, and frequency**: Medium impact; adds 3-5 minutes per ambiguous case; observed in 9 of 40 calibration cases.
- **Constraint class**: `data-readiness` with a secondary `change-management` component.
- **Current workaround**: Coordinator asks the submitter in chat, then copies the answer into the task note.
- **Reusable pattern hypothesis**: Exception-intake loops need an evidence-completeness check and structured clarification path before model-quality changes are considered.
- **Product, skill, or delivery implication**: Add required location validation and a clarification state to the intake schema; add missing-context cases to the Eval Pack; add intake completeness to future Reality Capture Gate reviews.
- **Destination and promotion status**: `promote` to reusable data-readiness checklist, Eval Pack cases, and product backlog item for clarification-state support.
- **Owner and next proof**: Technical evaluation owner; test the structured location field and clarification state against the 40-case calibration set, then measure chat usage in week two.

## Related Evidence

- Incident / eval case: E-AMB-004 through E-AMB-012
- Affected object, state, or action: Submission object; `received -> needs-clarification -> ready-for-review`
- Trace / artifact pointer: Synthetic calibration run R-002
- Confidence: high for this loop, medium for cross-domain reuse
- Cross-customer recurrence: unproven; retain the reusable pattern as a candidate until another case confirms it
