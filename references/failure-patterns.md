# Failure Patterns

Each pattern uses a three-step correction structure:

- **Self-check** — reveal whether the pattern is active
- **Recover** — return to the right gate, stage, or artifact
- **Verify** — confirm the correction through observable proof

## Pattern 1: AI Theater

Symptoms:

- the team optimizes for executive excitement
- no operational owner is identified
- success is defined as a good demo

Correction:

- **Self-check**: can you name one operator whose recurring work changes and one measurable consequence if the loop stays unchanged?
- **Recover**: return to G0 Mission Fit. Restate the opportunity as operator + trigger + measurable outcome. Record `no-go` or `conditional-go` when no owner or proof path exists.
- **Verify**: the Mission Brief names an accountable owner, baseline, and observable success metric.

## Pattern 2: Taxonomy Without Control

Symptoms:

- the model contains nouns but no state transitions
- action permissions are unclear
- artifacts look complete while no system can run from them

Correction:

- **Self-check**: does every first-loop object have an action, authority level, and evidence requirement for state change?
- **Recover**: return to Stage 4. Define actions, owners, permissions, audit, evidence, and rollback. Remove objects with no action or state consequence.
- **Verify**: a technical reader can infer what the system reads, changes, proves, and reverses without live narration.

## Pattern 3: Idealized Process Capture

Symptoms:

- only official SOPs are documented
- exception, escalation, workaround, and shadow paths are missing

Correction:

- **Self-check**: does the reality map contain a real clean case, ugly case, disputed case, and observed shadow workflow?
- **Recover**: return to G1 Evidence Sufficiency. Replay recent failures and handoff breakdowns with source artifacts.
- **Verify**: another operator can reconstruct current work and exceptions without interviewing the original stakeholder.

## Pattern 4: Pilot Bloat

Symptoms:

- the first pilot needs broad integration, model scope, and organization-wide adoption
- edge cases dominate before the core loop is proven

Correction:

- **Self-check**: does the pilot require multiple external systems or broad adoption before it can show any value?
- **Recover**: return to Stage 5. Cut scope to one trigger, one AI judgment, one action or route, one human confirmation, and one output.
- **Verify**: the pilot can show value through a bounded input set and one operator interface.

## Pattern 5: Autonomy Before Trust

Symptoms:

- AI receives write authority before fallback and rollback are defined
- operators cannot inspect why an action occurred

Correction:

- **Self-check**: can a human see, stop, and reverse every AI-influenced action today?
- **Recover**: return to the Governance And Risk Overlay. Reduce authority to advisory or gated, add auditability, containment, fallback, and rollback.
- **Verify**: every AI-influenced action has a human confirmation point, trace, responsible owner, and reversible path.

## Pattern 6: No Day-2 Owner

Symptoms:

- no one owns exceptions, drift, support, or operational metrics after launch
- degradation reaches users before the team detects it

Correction:

- **Self-check**: is one named person accountable for exception handling, monitoring, review cadence, and support?
- **Recover**: return to Stage 6. Complete the Day-2 Operations Plan and Production Readiness Review.
- **Verify**: the loop can operate for 30 days without the original builder handling every exception.

## Pattern 7: Premature Scale

Symptoms:

- leadership requests rollout before repeatability is proven
- expansion criteria remain political or vague

Correction:

- **Self-check**: do expansion criteria come from observed repeatability, operating burden, and measured impact?
- **Recover**: return to G4. Define replication conditions, dependencies, stage gates, and reasons to hold.
- **Verify**: the team can explain the next expansion step through evidence and a go / hold decision.

## Pattern 8: No Asset Return

Symptoms:

- delivery artifacts solve one account and leave no reusable capability
- lessons stay inside recap decks, chat logs, or one operator's memory
- the next similar project starts from zero

Correction:

- **Self-check**: can another operator reuse an artifact from the case without a live explanation from the original operator?
- **Recover**: run the Asset Distillation overlay. Give each candidate source evidence, reuse target, destination, promotion status, and owner.
- **Verify**: at least one asset is promoted with proof and a concrete first reuse opportunity.

## Pattern 9: Eval Theater

Symptoms:

- success criteria exist without representative cases
- demo cases are cherry-picked
- failure, ambiguous, and demo-killing cases are absent

Correction:

- **Self-check**: can the team point to versioned tasks, expected outcomes, graders, traces, and regression results?
- **Recover**: return to G2. Build the Eval Pack from real cases and failure classes before the demo or launch review.
- **Verify**: an external reviewer can rerun or inspect the eval and make the same acceptance decision.

## Pattern 10: Governance Fog

Symptoms:

- AI authority is vague
- human-in-the-loop is claimed without a concrete transfer point
- audit, containment, and rollback are undefined

Correction:

- **Self-check**: for each action, where does authority transfer, where is the audit record, how is blast radius capped, and how is the action reversed?
- **Recover**: complete the Governance And Risk Overlay before any operationally influential action expands.
- **Verify**: responsibility, evidence, containment, escalation, and rollback are explainable for every action surface.

## Pattern 11: Day-2 Collapse

Symptoms:

- the pilot works only while the builder is present
- exceptions have no owner
- manual workarounds grow silently

Correction:

- **Self-check**: would support, drift review, exception handling, and change approval continue if the builder left tomorrow?
- **Recover**: complete the Day-2 Operations Plan. Add monitoring, fallback, support, adoption, maintenance burden, and feedback capture.
- **Verify**: degradation is detected by the operating system before it becomes a user complaint, and workarounds enter the Field Signal Log.

## Pattern 12: Production Readiness Theater

Symptoms:

- a successful demo is treated as launch approval
- ownership, incident triggers, containment, support, or rollback remain implicit
- the launch cohort and workflow objectives are undefined

Correction:

- **Self-check**: can an independent reviewer make a go, conditional-go, or no-go decision from documented evidence?
- **Recover**: run `deployment-readiness` and complete the Production Readiness Review across workflow, evaluation, reliability, governance, adoption, and support.
- **Verify**: every readiness area has a posture, evidence, blocker, owner, and next proof; the launch decision is explicit.

## Pattern 13: Adoption Blindness

Symptoms:

- the team measures model quality and ignores whether operators use the loop
- usage is counted without eligible-work denominator or workflow impact
- shadow workflows remain active after launch

Correction:

- **Self-check**: what share of eligible work enters the loop, returns to manual handling, or stays in shadow tools?
- **Recover**: define the target operator cohort, adoption signal, workflow objective, training plan, and feedback method in the Minimum Viable Loop, Day-2 Operations Plan, and Production Readiness Review.
- **Verify**: adoption, repeat use, eligible-work share, workflow impact, and workaround volume are reviewed alongside quality metrics.

## Pattern 14: Field Signal Dump

Symptoms:

- every customer request becomes a product request
- product, integration, data, policy, change-management, and delivery constraints are mixed together
- feedback has no evidence, recurrence rule, destination, or owner

Correction:

- **Self-check**: can each field observation be traced to source evidence, classified, and routed to a specific decision owner?
- **Recover**: create a Field Signal Log entry. Record impact, frequency, constraint class, workaround, reusable pattern hypothesis, destination, promotion status, owner, and next proof.
- **Verify**: promoted signals meet evidence and materiality thresholds; rejected signals remain closed with a reason; roadmap items can trace back to field evidence.
