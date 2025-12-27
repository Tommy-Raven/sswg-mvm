---
anchor_id: invariants-doc
anchor_version: "1.0"
scope: documentation
owner: sswg
status: draft
---

# Canonical invariants source

`invariants.yaml` is the canonical source of truth for sswg/mvm invariants.
`root_contract.yaml` must reference `invariants.yaml` and mirror its invariant
entries exactly; parity is enforced by `scripts/validate_root_contracts.py`.
