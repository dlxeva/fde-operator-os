---
name: reality-capture
description: Lightweight Applied AI skill for reconstructing how work actually happens through operational reality and case replay.
---

# Reality Capture

Use this skill when the main question is:

- how does the work actually move today
- what happens in clean, ugly, disputed, or handoff-failure cases
- where do responsibility, evidence, and workflow break in practice

## Scope

Stay focused on reality reconstruction.

Primary outputs:

- `Operational Reality Map`
- `Case Replay Pack`

## What To Capture

- core actors and responsibility chain
- current workflow as actually operated
- systems, channels, and shadow tools
- clean case replay
- ugly case replay
- disputed case
- handoff failure
- failure points and evidence available at the time

## Do Not Expand Into

- broad mission qualification unless needed for basic context
- full minimum viable loop design
- architecture or integration commitments
- expansion planning

## Completion Standard

Another operator should be able to replay how the work actually moves without interviewing the original stakeholder.

## Output Style

- reality over rhetoric
- concrete cases over abstract process language
- explicit missing evidence
- explicit distinction between what the case proves and does not prove

## Template Reference

This skill uses two core templates:

- `assets/templates/operational-reality-map.md`
- `assets/templates/case-replay-pack.md`

**Hermes**: `skill_view(name='fde-operator-os', file_path='assets/templates/<template-name>')`
**Codex / others**: read `assets/templates/<template-name>` relative to the skill root.

