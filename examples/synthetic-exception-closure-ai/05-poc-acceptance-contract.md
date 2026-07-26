# POC Acceptance Contract

- **POC objective**: Prove that one exception category can move through a faster and more auditable review-to-resolution loop while human approval remains mandatory.
- **Baseline**:
  - measure current review-to-task time on at least 50 historical or live cases
  - measure intake completeness, evidence acceptance, overdue reconciliation effort, and coordinator disagreement rate
  - record the share of eligible cases handled first through chat or private spreadsheets
- **Success criteria**:
  - median review-to-task time improves by at least 30% against the measured baseline
  - at least 80% of eligible pilot submissions enter the review queue by week two
  - coordinators accept or lightly edit the AI draft on at least 75% of in-scope cases
  - closure records with acceptable evidence reach at least 90%
  - overdue items remain visible without private spreadsheet reconciliation for pilot cases
- **Failure criteria**:
  - any critical demo-killing case creates or closes a task without required human approval
  - coordinators bypass the queue for more than 40% of eligible cases after week two
  - review-to-task effort remains within 10% of baseline
  - evidence quality fails to improve materially
  - audit fields or source evidence are missing from more than 2% of pilot actions
- **Measurement window**: Four weeks after a one-week calibration period, targeting 100-200 eligible submissions.
- **Demo path**:
  1. Show a clear in-scope submission.
  2. Show an ambiguous submission routed for human review.
  3. Show coordinator approval, edit, rejection, and task creation.
  4. Show closure evidence review.
  5. Show audit trail, overdue visibility, and rollback to manual handling.
- **Eval pack link**: [`07-eval-cases.md`](./07-eval-cases.md), expanded into the standard Eval Pack format before launch review.
- **Required evidence**:
  - measured baseline and pilot timing comparison
  - accepted, edited, rejected, uncertain, and demo-killing cases
  - evidence-quality comparison before and after
  - operator adoption and bypass data
  - sample audit records and failure traces
  - weekly regression results
- **Review cadence**: Weekly pilot review; immediate review after any critical failure or rollback trigger.
- **Rollback condition**: Pause AI drafting and return to the manual path when a critical unauthorized action occurs, audit integrity fails, or two critical eval failures appear in one weekly run.
- **Required reviewer**: Regional operations coordinator, technical evaluation owner, and program manager as business acceptance owner.
- **Decision gate**: G2 passes after baseline, representative eval coverage, acceptance thresholds, authority, audit, and rollback are locked. G3 remains pending until Production Readiness Review.
- **Known exclusions**:
  - multi-category support
  - autonomous task creation
  - enterprise reporting redesign
  - expansion beyond the pilot coordinator cohort
- **Decision after review**: Proceed to Production Readiness Review only when repeatable trust, measurable time savings, adoption, evidence quality, audit integrity, and regression stability meet the thresholds above.
