sswg-mvm; version 1.0+ (living document)
Date: 12-23-2025
Document title: Instruction Lifecycle
Author: Tommy Raven
Licensing: Raven Recordings ©️ see: *LICENSE.md*
(Document) Purpose: Define a universal lifecycle for instructions so creative artifacts move predictably from conception to retirement without conflicting versions or endless iteration. Establishes states, promotion gates, deprecation rules, and lineage safeguards aligned to the SSWG-MVM recursion and evaluation stack.

# Instruction Lifecycle — SSWG-MVM

## Overview

Instruction artifacts (schemas, prompts, workflows, playbooks, or policies) should evolve through explicit stages so teams can distinguish draft explorations from canonical guidance. This lifecycle sets the allowed states, promotion criteria, freezing rules, and archival expectations to prevent contradictory directions and to maintain historical traceability.

## Lifecycle states

| State      | Description | Entry requirements | Exit conditions | Allowed transitions |
| ---------- | ----------- | ------------------ | --------------- | ------------------- |
| **Draft**  | Exploratory instruction under active iteration. | Issue or request recorded; scope defined; owner assigned. | Meets validation gates for promotion; linked tests or exemplars captured. | Draft → Tested; Draft → Archived (if abandoned). |
| **Tested** | Instruction has been exercised in controlled runs with evidence. | Draft artifacts validated against schemas; at least one reproducible run with metrics logged. | Maintains stability across two consecutive runs; reviewers sign off on clarity and risk. | Tested → Canonical; Tested → Draft (if defects found); Tested → Archived (if superseded). |
| **Canonical** | Authoritative guidance used by default in pipelines and documentation. | Promotion ticket cites test evidence; version tag assigned; references wired into relevant modules/docs. | Replacement canonical approved or deprecation initiated; lineage anchors captured. | Canonical → Archived (when superseded); Canonical → Draft (only via formal revision request with new version ID). |
| **Archived** | Retired instruction retained for lineage and audit. | Decommission decision recorded with rationale; replacement (if any) linked. | None; archived items are immutable snapshots. | Archived → Draft (only by explicit resurrection ticket with new version lineage). |

## Promotion and freezing rules

- **Draft → Tested**
  - Minimum: schema validation passes, scope is stable, and acceptance criteria are written.
  - Evidence: attach at least one reproducible run (logs, metrics, or rendered artifacts) demonstrating the intended behavior.
  - Ownership: a maintainer or domain lead accepts stewardship for the test window.

- **Tested → Canonical**
  - Reliability: two consecutive green runs in representative environments; failure cases documented.
  - Review: peer review for clarity, safety, and alignment with platform constraints (schemas, recursion controls, evaluation harnesses).
  - Traceability: assign a version ID, update cross-references (schemas, CLI help, docs), and note any deprecated predecessors.

- **Freezing Canonical**
  - Canonical instructions are immutable except through a revision request that spawns a new **Draft** with an incremented version.
  - Emergency edits must include a retroactive incident record and immediate revalidation.

- **Deprecation and archival**
  - Trigger: a superior instruction reaches **Canonical** or the previous guidance is unsafe/obsolete.
  - Action: mark the old canonical as **Archived**, annotate the successor link, and remove it from defaults and templates.
  - Preservation: archive retains metadata (author, version, dates, decision record) and referenced artifacts.

## Change management workflow

1. **Propose** — File a change request identifying scope, risks, and intended success metrics; create or update the Draft with owners.
2. **Test** — Run controlled evaluations (unit tests, simulations, or dry runs) and attach metrics/logs in the recursion memory store.
3. **Review** — Peer review for correctness, clarity, bias/safety, and schema alignment; resolve conflicts against existing canonicals.
4. **Publish** — Promote to **Canonical**, broadcast location updates (docs, schemas, CLI help), and tag the version.
5. **Retire** — When superseded, archive the prior canonical with pointers to its successor and any migration notes.

## Lineage and provenance

- Record every state change with timestamps, approvers, and rationale in the evolution log (see [docs/EVOLUTION_LOGGING.md](./EVOLUTION_LOGGING.md)).
- Use deterministic version IDs and parent-child links so recursive generations can cite the instruction they followed.
- Store runnable exemplars and evaluation metrics alongside each Tested or Canonical record to make reruns verifiable.
- Keep human-readable summaries in docs while persisting machine-friendly metadata in the memory store for audits.

## Operational checklists

- **Before promoting to Tested:**
  - [ ] Scope and acceptance criteria written
  - [ ] Schema validation clean
  - [ ] Reproducible run captured with metrics

- **Before promoting to Canonical:**
  - [ ] Two consecutive green runs
  - [ ] Peer review complete
  - [ ] Version ID assigned and references updated

- **Before Archiving a Canonical:**
  - [ ] Successor (if any) linked
  - [ ] Decision rationale recorded
  - [ ] Defaults/templates updated to remove the retired instruction

Adhering to this lifecycle keeps instructions convergent, reduces conflicting guidance, and preserves the historical narrative needed for audits and future recursions.
