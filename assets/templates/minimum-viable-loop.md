# Minimum Viable Loop

## Use

Use to define the pilot as one end-to-end operating loop with a credible manual path, ownership model, feedback path, and rollback boundary.

## Required Fields

- Trigger input
- Baseline manual path
- AI judgment or transformation
- Action or routing step
- Human confirmation step
- Output / write-back
- Feedback / verification
- Archive / audit
- Required integrations
- Operating owner
- Operator adoption signal
- Day-2 maintenance burden
- Drift / degradation signal
- Rollback condition
- Manual fallback mode

## Optional Fields

- Latency target
- Volume assumption
- Cost guardrail

## Typical Anti-Pattern

The pilot proves model capability while leaving the real operating loop, fallback path, adoption signal, and maintenance burden undefined.

## Completion Standard

Another delivery lead can turn this artifact into a runbook, an eval plan, and a launch-readiness review without renegotiating the loop boundary.

## Template

```md
# Minimum Viable Loop

- **Trigger input**:
- **Baseline manual path**:
- **AI judgment / transformation**:
- **Action / routing**:
- **Human confirmation**:
- **Output / write-back**:
- **Feedback / verification**:
- **Archive / audit**:
- **Required integrations**:
- **Operator interface**:
- **Operating owner**:
- **Operator adoption signal**:
- **Day-2 maintenance burden**:
- **Drift / degradation signal**:
- **Rollback condition**:
- **Fallback mode**:
- **Latency target**:
- **Volume assumption**:
- **Cost guardrail**:
```
