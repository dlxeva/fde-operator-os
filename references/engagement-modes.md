# Engagement Modes

## Discovery Sprint

- **When to use**: early qualification, broad opportunity compression, or stakeholder-conflicted discovery where the team still needs the right loop
- **Starting stage**: Mission Qualification or Operational Reality Capture
- **Required artifacts**:
  - Mission Brief
  - Operational Reality Map
  - Case Replay Pack
  - Reality Capture Gate
  - System Problem Frame
- **Gate**: G0 Mission Fit and G1 Evidence Sufficiency
- **Stop condition**: one bounded loop is qualified, conditionally qualified, or explicitly rejected
- **Failure signal**: the team is still discussing broad opportunity space with no named operator or credible proof path
- **Recommended output depth**: light to medium; usually stop at Mission Qualification or System Framing

## Pilot Design

- **When to use**: the team already has a plausible loop and must define a credible pilot
- **Starting stage**: System Framing or State, Action & Evidence Model
- **Required artifacts**:
  - AI Intervention Design
  - Minimum Viable Loop
  - POC Acceptance Contract
  - Eval Pack
  - Governance And Risk Overlay
- **Gate**: G2 Pilot Contract
- **Stop condition**: the pilot can be judged, demoed, governed, and rolled back without renegotiating scope
- **Failure signal**: the pilot still depends on broad architecture promises or has no representative eval cases
- **Recommended output depth**: medium to deep

## Production Readiness

- **When to use**: a credible pilot is about to enter live operator work, expand its authority, or increase production volume
- **Starting stage**: Delivery Architecture
- **Required artifacts**:
  - POC Acceptance Contract
  - Eval Pack
  - Governance And Risk Overlay
  - Day-2 Operations Plan
  - Production Readiness Review
  - Field Signal Log
- **Gate**: G3 Production Readiness
- **Stop condition**: a reviewer records `go`, `conditional-go`, or `no-go` with evidence, blockers, owners, and re-review triggers
- **Failure signal**: launch approval depends on demo quality while ownership, adoption, observability, incidents, containment, or rollback remain implicit
- **Recommended output depth**: deep and evidence-backed

## Deployment Rescue

- **When to use**: a live or late-stage loop exists but trust, adoption, exceptions, quality, or degradation are breaking the system
- **Starting stage**: Operational Reality Capture at the failing loop
- **Required artifacts**:
  - Operational Reality Map
  - Case Replay Pack
  - Eval Pack updates
  - Day-2 Operations Plan
  - Governance And Risk Overlay
  - Production Readiness Review delta
  - Field Signal Log
  - relevant Failure Patterns review
- **Gate**: return to the earliest failed gate
- **Stop condition**: the break is explained as an operational loop problem with named fixes, owners, containment, fallback, and proof
- **Failure signal**: the team keeps proposing rebuilds without understanding the actual handoff, production trace, adoption, or day-2 failure
- **Recommended output depth**: medium to deep; emphasize evidence, containment, and verified recovery

## Post-Delivery Asset Distillation

- **When to use**: a pilot or live loop has produced enough evidence to promote reusable assets
- **Starting stage**: Post-Delivery Overlay
- **Required artifacts**:
  - Field Signal Log
  - Asset Distillation Log
  - relevant Eval Pack lessons
  - relevant Day-2 Operations lessons
  - relevant incident or postmortem lessons
- **Gate**: G4 Replication And Asset Promotion
- **Stop condition**: at least one reusable pattern, eval asset, governance check, operating template, skill, or product item is promoted with evidence and an owner
- **Failure signal**: the project closes with narrative debriefs only and no reusable assets or roadmap inputs
- **Recommended output depth**: medium
