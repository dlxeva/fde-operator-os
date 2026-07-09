# Mission Brief

## Use

Use for early qualification when the team must decide whether this is a real AI delivery opportunity.

## Required Fields

- Opportunity name
- Operator mission
- Operational pain with consequence
- Target outcome
- Accountable owner
- Observable success metric
- Key constraints
- Go / no-go posture

## Optional Fields

- Strategic context
- Executive sponsor
- Time window
- Political sensitivity
- Verification path (what evidence must be collected before go is confirmed — useful when qualification is conditional)

## Typical Anti-Pattern

The brief talks about "AI transformation" but cannot name a single operator, bottleneck, or proof metric.

## Completion Standard

A new operator should be able to explain why this opportunity matters, who owns it, and what would count as proof.

## Template

```md
# Mission Brief

- **Opportunity**:
- **Operator mission**:
- **Operational pain**:
- **Consequence if unresolved**:
- **Target outcome**:
- **Accountable owner**:
- **Success metric(s)**:
- **Critical constraints**:
- **Go / no-go view**:
- **Unknowns requiring validation**:
```

## Filled Example

A condensed example so first-time users can see what a completed Mission Brief looks like. Derived from `examples/synthetic-exception-closure-ai/`.

```md
# Mission Brief

- **Opportunity**: Exception-review-to-resolution loop for recurring operational issues
- **Operator mission**: Help coordinators move from inconsistent screenshot review to a more reliable exception qualification and closure loop
- **Operational pain**: Exceptions are reviewed inconsistently, closure proof is weak, and overdue items are tracked outside the official system
- **Consequence if unresolved**: Repeat exceptions, weak auditability, slower closure, and growing reporting overhead
- **Target outcome**: Reduce time from submission to resolution task creation while improving evidence quality for closure
- **Accountable owner**: Regional operations coordinator
- **Success metric(s)**:
  - reduce median review-to-task time by 30%
  - increase closure records with acceptable evidence to 90%
  - reduce manually reconciled overdue items
- **Critical constraints**:
  - human approval remains required before task creation
  - existing tasking tool remains system of record
  - phase-one scope must fit one exception category
- **Go / no-go view**: Go, if one recurring exception category can be piloted with the existing form and tasking workflow
- **Unknowns requiring validation**:
  - current false-positive rate for frontline submissions
  - whether closure evidence standards are consistent across coordinators
```

Note what makes this example work: it names a concrete owner, a measurable failure cost, observable metrics, and a bounded go condition. A brief that says "AI transformation" but cannot name any of these is the anti-pattern.
