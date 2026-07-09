# Reality Capture Gate

## Use

Use as a living checklist that tracks whether enough real operational evidence has been collected to advance past Stage 5 into Stage 6 Delivery Architecture. Open it during Stage 2 and keep it current through Stage 5.

This gate exists because a common failure mode is to reach architecture on the strength of a narrated plan, stakeholder rhetoric, or inferred cases — and then discover the real loop does not match the design. The gate makes that risk explicit and trackable before architecture commitments are made.

## Required Fields

- Real cases collected (clean / ugly / disputed / handoff-failure)
- Named owners assigned (operating owner / exception owner / review owner)
- Baseline metrics measured (not estimated)
- Knowledge base readiness (whitelists / price tables / templates / rules structured and loaded)
- Boundary calibration (what counts as in-scope vs exception, evidenced by samples)
- Reviewer load confirmed (can the named reviewer actually absorb the pilot volume)
- Open gating items with owner and due state

## Optional Fields

- Evidence source pointer for each collected case
- Confidence posture (evidence-sufficient / partial / thin)
- Re-collection plan for thin or inferred items

## Typical Anti-Pattern

The team proceeds to architecture using only the stakeholder briefing deck or an ideal-state process map, with every reality item still marked "to be collected." The gate is treated as a formality rather than a real stop condition.

## Completion Standard

Every required field is backed by at least one concrete, non-inferred piece of evidence (a real sample, a named person, a measured number), OR is explicitly carried as an open gating item with an owner. No field is silently smoothed over. When the gate is green, Stage 6 can proceed on real ground; when it is red or partial, Stage 6 stays paused with the gaps named.

## Evidence Sufficiency Posture

Use this coarse posture to communicate status, not to replace the checklist:

- **Evidence-sufficient**: every required field has real evidence. Proceed to Stage 6.
- **Partial**: some fields have real evidence, others are inferred or pending. Proceed to Stage 6 only for the parts backed by evidence; carry the rest as explicit assumptions or pause those sections.
- **Thin**: most fields are inferred or narrative-only. Do not enter Stage 6. Keep the gate open, name the gaps, and re-collect before resuming.

## Template

```md
# Reality Capture Gate

## Real Cases Collected
- Clean case: [collected / inferred] — source:
- Ugly case: [collected / inferred] — source:
- Disputed case: [collected / inferred] — source:
- Handoff-failure case: [collected / inferred] — source:

## Named Owners
- Operating owner: [named / pending] —
- Exception owner: [named / pending] —
- Review owner (technical): [named / pending] —
- Review owner (price / financial): [named / pending] —

## Baseline Metrics Measured
- Current cycle time: [measured / estimated] — value:
- Current error / rework rate: [measured / estimated] — value:
- Current volume: [measured / estimated] — value:
- New-operator independent output share: [measured / estimated] — value:

## Knowledge Base Readiness
- Whitelist / allowed combinations: [structured+loaded / partial / not started]
- Disallowed combinations: [structured+loaded / partial / not started]
- Price table / pricing rules: [structured+loaded / partial / not started]
- Templates (quote / plan): [structured+loaded / partial / not started]
- Standard scenario packages: [structured+loaded / partial / not started]

## Boundary Calibration
- In-scope definition: [sample-backed / asserted]
- Exception exit definition: [sample-backed / asserted]
- Calibrated against: [N real historical samples / none]

## Reviewer Load
- Named reviewer capacity confirmed: [yes / no / unknown]
- Pilot volume estimate: [measured / estimated]

## Sufficiency Posture
- Overall: [evidence-sufficient / partial / thin]

## Open Gating Items
- Item: — owner: — state: [blocking / non-blocking]
- Item: — owner: — state: [blocking / non-blocking]
```
