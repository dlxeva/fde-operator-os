---
name: reality-capture
description: Lightweight Applied AI skill for reconstructing how work actually happens through operational reality, case replay, and evidence sufficiency gating.
---

# Reality Capture

Use this skill when the main question is:

- how does the work actually move today
- what happens in clean, ugly, disputed, or handoff-failure cases
- where do responsibility, evidence, and workflow break in practice
- whether there is enough real evidence to move toward pilot or architecture work

## Scope

Stay focused on reality reconstruction and evidence sufficiency.

Primary outputs:

- `Operational Reality Map`
- `Case Replay Pack`
- `Reality Capture Gate`

## What To Capture

- core actors and responsibility chain
- current workflow as actually operated
- systems, channels, and shadow tools
- clean case replay
- ugly case replay
- disputed case
- handoff failure
- failure points and evidence available at the time
- open evidence gaps that would make later architecture speculative

## Reality Capture Gate

Open `assets/templates/reality-capture-gating.md` during this skill run when the output may feed pilot design or delivery architecture.

Use the gate to mark whether the current evidence posture is:

- `evidence-sufficient`
- `partial`
- `thin`

Do not smooth over missing cases, unnamed owners, estimated metrics, or uncollected sample artifacts. Carry each gap as an explicit gating item with an owner or a re-collection plan.

## Do Not Expand Into

- broad mission qualification unless needed for basic context
- full minimum viable loop design
- architecture or integration commitments
- expansion planning

## Completion Standard

Another operator should be able to replay how the work actually moves without interviewing the original stakeholder.

If the output will feed later delivery architecture, the Reality Capture Gate should also show which evidence is collected, inferred, or still blocking.

## Output Style

- reality over rhetoric
- concrete cases over abstract process language
- explicit missing evidence
- explicit distinction between what the case proves and does not prove
- explicit evidence posture before downstream design work

## Template Reference

This skill uses three core templates:

- `assets/templates/operational-reality-map.md`
- `assets/templates/case-replay-pack.md`
- `assets/templates/reality-capture-gating.md`

**Hermes**: `skill_view(name='fde-operator-os', file_path='assets/templates/<template-name>')`
**Codex / others**: read `assets/templates/<template-name>` relative to the skill root.
