# Failure Patterns

Each pattern below follows a three-step correction structure so the operator can diagnose, recover, and verify — not just recognize the smell:

- **Self-check**: the question that reveals whether you are inside this pattern right now
- **Recover**: the stage or artifact to return to, and the narrowing move to make
- **Verify**: the observable signal that confirms the pattern is resolved before moving forward

## Pattern 1: AI Theater

Symptoms:

- the team optimizes for executive excitement
- no operational owner is identified
- success is defined as "a good demo"

Correction:

- **Self-check**: can you name a single operator whose weekly work changes if this ships, and a measurable failure cost if it does not?
- **Recover**: return to Stage 1 Mission Qualification. Restate the loop as operator + trigger + measurable outcome. If no operator or failure cost can be named, the correct output is a no-go or not-now, not a smaller pilot.
- **Verify**: the Mission Brief now names an accountable owner and an observable success metric. A skeptical reviewer would agree this is a real loop, not a showcase.

## Pattern 2: Taxonomy Without Control

Symptoms:

- ontology work produces nouns but no state transitions
- action permissions are unclear
- artifacts look complete but no system can run from them

Correction:

- **Self-check**: does every object in your model have at least one action with a defined owner, authority level, and evidence requirement for state change?
- **Recover**: return to Stage 4. For each object, ask what action changes its state, who has authority to take it, and what evidence must accompany the transition. Remove objects that have no action or state consequence.
- **Verify**: a technical reader can infer what the system reads, what it can change, and what proof advances the loop — without you narrating it.

## Pattern 3: Idealized Process Capture

Symptoms:

- only official SOPs are documented
- no exception path, escalation path, or workaround exists in the design

Correction:

- **Self-check**: does your reality map contain at least one clean case, one ugly case, and one observed shadow workflow outside the official system?
- **Recover**: return to Stage 2. Collect ugly cases, disputed cases, and handoff failures explicitly. If stakeholders only describe the ideal path, ask "show me the last time this broke" and trace that case.
- **Verify**: another operator could replay how the work actually moves without interviewing the original stakeholder.

## Pattern 4: Pilot Bloat

Symptoms:

- the first pilot requires multi-system integration, broad model scope, and organization-wide adoption
- edge cases dominate before the core loop is proven

Correction:

- **Self-check**: does your pilot require three or more external system integrations, or broad org adoption, before it can show any value?
- **Recover**: return to Stage 5. Cut scope until one loop — trigger, AI judgment, single output, human confirmation — can be tested end-to-end. Defer integrations and edge cases to after the core loop is proven.
- **Verify**: the pilot can demonstrate value with a single interface and a bounded input set. Edge cases are logged as future scope, not current blockers.

## Pattern 5: Autonomy Before Trust

Symptoms:

- the design gives AI write authority before clear fallback rules
- humans cannot see why a decision happened

Correction:

- **Self-check**: if the model is wrong today, can a human see why, stop it, and reverse the action? Is the audit trail defined before or after write access?
- **Recover**: return to Stage 5 and the Governance And Risk Overlay. Downgrade write-capable surfaces to advisory or gated. Add auditability and a fallback path before restoring any write authority.
- **Verify**: every AI-influenced action has a defined human confirmation point, an audit record, and a rollback condition that still works on a bad model day.

## Pattern 6: No Day-2 Owner

Symptoms:

- no one owns exceptions, model drift, or operational metrics after launch
- degradation is discovered through user complaints

Correction:

- **Self-check**: is there a named person (not a team) who owns exception handling, drift monitoring, and review cadence after the pilot launches?
- **Recover**: return to Stage 6. Name the operating owner and exception owner in the Day-2 Operations Plan before finalizing delivery architecture. If no owner can be named, the loop is not delivery-ready.
- **Verify**: the loop could run for 30 days without the original builder being present in every exception.

## Pattern 7: Premature Scale

Symptoms:

- leadership wants rollout before the pilot proves repeatability
- expansion criteria are vague or political

Correction:

- **Self-check**: are the expansion criteria based on observed repeatability and measured outcomes, or on leadership enthusiasm and account ambition?
- **Recover**: return to Stage 7. Define replication conditions and explicit stop/go gates. If the pilot success criteria do not map to expansion criteria, close that gap before any rollout commitment.
- **Verify**: the team can explain what must be proven before broader rollout and why the next expansion step is the right one — in evidence, not narrative.

## Pattern 8: No Asset Return

Symptoms:

- delivery artifacts solve the current account but leave nothing reusable
- lessons stay inside recap decks, chat logs, or one operator's memory
- the next similar project starts from zero

Correction:

- **Self-check**: at project close, can another operator reuse any artifact from this case without the original operator explaining it live?
- **Recover**: run the Post-Delivery Asset Distillation overlay. For each candidate, name the reuse target, source evidence, owner, and destination. Reject candidates that cannot stand alone without project context.
- **Verify**: at least one promoted asset is defined with owner, proof, and a concrete next reuse context.

## Pattern 9: Eval Theater

Symptoms:

- success criteria exist but no representative test cases exist
- demo cases are cherry-picked
- failure cases are not collected

Correction:

- **Self-check**: do you have golden, failure, edge, ambiguous, and demo-killing cases — or only cases that make the system look good?
- **Recover**: return to Stage 5. Build or complete the Eval Pack with failure and ambiguous cases before the demo. If failure cases cannot be collected, the acceptance threshold is not yet credible.
- **Verify**: a reviewer can run or inspect the eval pack and decide whether the pilot is acceptable without renegotiating the goal.

## Pattern 10: Governance Fog

Symptoms:

- AI authority is vague
- human-in-the-loop is claimed but not located
- no audit or rollback path exists

Correction:

- **Self-check**: for every AI-influenced action, can you point to where authority transfers to the human, where the audit record is written, and how the action is reversed?
- **Recover**: complete the Governance And Risk Overlay before any write-capable or operationally influential action. Locate every human confirmation point concretely; do not leave it as "a human is somewhere in the loop."
- **Verify**: the delivery team can explain who is responsible for every AI-influenced action and how that action can be reviewed, stopped, or reversed.

## Pattern 11: Day-2 Collapse

Symptoms:

- pilot works only while the builder is present
- exceptions have no owner
- degradation is discovered through user complaints

Correction:

- **Self-check**: if the original builder left tomorrow, would exceptions, drift signals, and review cadence still be handled by someone?
- **Recover**: complete the Day-2 Operations Plan. Define monitoring signals, manual fallback mode, support path, and operator adoption signal with named owners. If any of these is missing, the pilot is a demo, not a delivery.
- **Verify**: the loop can run for 30 days without the original builder present in every exception, and degradation is detected by monitoring before it reaches users.
