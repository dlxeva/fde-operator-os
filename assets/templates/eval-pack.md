# Eval Pack

## Use

Use when the team must convert pilot acceptance into representative tasks, repeatable trials, explicit graders, and regression evidence.

## Required Fields

- Evaluation objective
- Golden cases
- Failure cases
- Edge cases
- Ambiguous cases
- Human review rubric
- Baseline comparison
- Acceptance threshold
- Regression check
- Demo-killing cases
- Evidence required
- Review owner

## Optional Fields

- Sampling notes
- Dataset split
- Trial count
- Confidence split
- Rerun cadence
- Production-trace sampling plan

## Typical Anti-Pattern

The team agrees on success criteria in prose, tests only polished demo cases, and has no repeatable task, grader, trace, or regression record.

## Completion Standard

A reviewer can run or inspect the eval pack, compare it with baseline behavior, and decide whether the pilot is acceptable without renegotiating the goal.

## Template

```md
# Eval Pack

- **Evaluation objective**:
- **Golden cases**:
- **Failure cases**:
- **Edge cases**:
- **Ambiguous cases**:
- **Human review rubric**:
- **Baseline comparison**:
- **Acceptance threshold**:
- **Regression check**:
- **Demo-killing cases**:
- **Evidence required**:
- **Review owner**:

## Eval Case Table

| Case ID | Class | Input / task | Expected outcome | Grader | Failure severity | Source evidence |
|---|---|---|---|---|---|---|
| E-001 | golden / failure / edge / ambiguous / demo-killing | ... | ... | deterministic / model / human | low / medium / high / critical | ... |

## Evaluation Run Log

| Run ID | Build / model | Dataset version | Trials | Pass rate | Critical failures | Trace pointer | Decision |
|---|---|---|---:|---:|---:|---|---|
| R-001 | ... | ... | ... | ... | ... | ... | pass / hold / fail |

## Production Sampling Plan

- Sampling trigger:
- Trace fields retained:
- Review cadence:
- Promotion rule from production failure to regression case:
```
