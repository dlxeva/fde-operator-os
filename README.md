<div align="center">

# Applied AI Operator OS

Turn field ambiguity into a production-worthy AI operating loop, then return field learning into reusable delivery and product capability.

[中文说明](./README.zh-CN.md)

![FDE Operator OS Banner](./assets/readme/banner-en.svg)

</div>

## What This Repository Does

`fde-operator-os` is an operator-grade skill and playbook for Forward Deployed Engineers, Applied AI leads, solution architects, and delivery owners.

It helps a team:

- qualify whether an AI opportunity deserves delivery effort
- reconstruct operational reality from cases and evidence
- define business objects, states, actions, authority, and proof
- compress a broad idea into one judgeable operator loop
- pass production-readiness gates before live deployment
- turn field signals into reusable assets and product inputs

Here, FDE describes an operating role: translating field uncertainty across customer mission, system design, production operation, and reusable capability.

## 60-Second Start

```text
Use $fde-operator-os.

Run one bounded loop only:
- Scenario: warehouse exception closure
- Operator: floor supervisor
- Trigger: exception alert arrives
- Output: confirmed closure task with audit record

Produce the core artifacts through POC Acceptance Contract.
Stop before Delivery Architecture when evidence is thin.
```

Start with one operator, one trigger, one business object, and one output. Expand after the loop is evidenced and owned.

## Delivery Chain And Gates

| Stage | Decision | Primary artifact | Gate |
|---|---|---|---|
| 1. Mission Qualification | Is this worth committing to? | Mission Brief | G0 Mission Fit |
| 2. Operational Reality Capture | Do we understand the real loop? | Operational Reality Map, Case Replay Pack, Reality Capture Gate | G1 Evidence Sufficiency |
| 3. System Framing | What bottleneck and boundary matter now? | System Problem Frame | — |
| 4. State, Action & Evidence Model | What can the system read, decide, change, and prove? | State, Action & Evidence Model | — |
| 5. Intervention & Pilot Design | Can a bounded pilot prove or disprove value? | Minimum Viable Loop, POC Acceptance Contract, Eval Pack | G2 Pilot Contract |
| 6. Delivery Architecture | Can the loop enter live work with controlled risk? | Day-2 Operations Plan, Production Readiness Review | G3 Production Readiness |
| 7. Expansion Logic | Should the loop repeat or expand? | Expansion Roadmap | G4 Replication And Asset Promotion |

A post-delivery Asset Distillation overlay converts case learning into reusable templates, evals, skills, controls, tools, and roadmap inputs.

## Four Control Loops

The seven stages are sequenced work. Four control loops run across them:

1. **Customer value** — mission fit -> operator adoption -> measurable workflow impact.
2. **System quality** — real cases -> evals -> regression gates -> production traces.
3. **Production reliability** — readiness -> telemetry -> incident response -> postmortem.
4. **Product learning** — field signal -> pattern -> reusable asset or roadmap decision.

See [`references/fde-practice-system.md`](./references/fde-practice-system.md) for evidence hierarchy, constraint classification, decision rights, cadence, and measurement.

## Skill Suite

The root skill is the canonical doctrine and router. Lighter skills handle common request shapes:

- [`mission-qualifier`](./skills/mission-qualifier/) — early opportunity qualification
- [`reality-capture`](./skills/reality-capture/) — workflow reconstruction and evidence sufficiency
- [`pilot-designer`](./skills/pilot-designer/) — bounded pilot, acceptance, and eval design
- [`deployment-readiness`](./skills/deployment-readiness/) — production launch review and deployment rescue

## Artifact System

The repository now treats artifact quality as an enforceable contract.

- [`contracts/artifacts.json`](./contracts/artifacts.json) is the machine-readable source for artifact names, required fields, stages, gates, aliases, strict examples, and cross-artifact sources of truth.
- [`contracts/case-manifest.schema.json`](./contracts/case-manifest.schema.json) defines the index format for example and benchmark cases.
- [`tools/validate_repo.py`](./tools/validate_repo.py) detects template drift, missing example fields, broken links, invalid aliases, unknown gate references, and incomplete case manifests.
- [`.github/workflows/validate.yml`](./.github/workflows/validate.yml) runs validation and unit tests on pushes and pull requests.

Run locally:

```bash
python tools/validate_repo.py
python -m unittest discover -s tests -v
```

The validator uses only the Python standard library.

## Core Artifacts

Core decision artifacts:

- Mission Brief
- Operational Reality Map
- System Problem Frame
- State, Action & Evidence Model
- AI Intervention Design
- Minimum Viable Loop
- POC Acceptance Contract
- Expansion Roadmap

Execution and control artifacts:

- Case Replay Pack
- Reality Capture Gate
- Eval Pack
- Governance And Risk Overlay
- Day-2 Operations Plan
- Production Readiness Review
- Field Signal Log
- Asset Distillation Log

Templates live in [`assets/templates/`](./assets/templates/).

## Example Case

[`examples/synthetic-exception-closure-ai/`](./examples/synthetic-exception-closure-ai/) contains a synthetic end-to-end case with:

- qualification, reality, framing, pilot, and acceptance artifacts
- production-readiness and field-signal artifacts
- a machine-readable `case-manifest.json`
- reusable patterns, eval cases, product feedback, and asset distillation

Additional compact examples:

- [`examples/first-run-minimal-loop/`](./examples/first-run-minimal-loop/)
- [`examples/synthetic-public-safety-ai/`](./examples/synthetic-public-safety-ai/)
- [`examples/case-pack-template/`](./examples/case-pack-template/)

## Install And Invoke

Copy the repository into a compatible skill directory, or reuse its doctrine, references, contracts, and templates in another agent runtime.

Codex-style example:

```powershell
Copy-Item -Recurse .\fde-operator-os "$HOME\.codex\skills\"
```

Typical invocations:

```text
Use $fde-operator-os to qualify this AI opportunity and select one operator loop.
Use reality-capture to reconstruct the real workflow and evidence gaps.
Use pilot-designer to define the bounded pilot, acceptance contract, and eval pack.
Use deployment-readiness to make a go, conditional-go, or no-go launch decision.
```

Optional short wrappers live under [`aliases/`](./aliases/). Runtime guidance is in [`references/runtime-portability.md`](./references/runtime-portability.md).

## Repository Map

```text
fde-operator-os/
├── SKILL.md                  # canonical doctrine and router
├── skills/                   # focused execution skills
├── references/               # doctrine, heuristics, practice system, failures
├── assets/templates/         # operator and control artifacts
├── contracts/                # machine-readable artifact and case contracts
├── examples/                 # synthetic cases and regression examples
├── tools/                    # repository validator
├── tests/                    # validator tests
├── .github/workflows/        # CI validation
├── aliases/                  # runtime wrappers
└── agents/                   # host-facing metadata
```

## Design Standard

- qualify before designing
- model observed work and exception paths
- define actions, authority, evidence, audit, and rollback together
- judge pilots through representative evals and business acceptance
- treat production adoption and workflow impact as delivery outcomes
- make launch, incident, containment, support, and rollback decisions explicit
- route field signals through evidence, classification, destination, and ownership
- leave reusable assets behind

## Status

The core doctrine remains stable. The repository is actively refined through Applied AI and FDE delivery practice, with validation intended to keep templates, skills, examples, and documentation aligned as the method evolves.

## License

MIT
