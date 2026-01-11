# GOVERNANCE ROOT — INFORMATIONAL NOTICE (NON-AUTHORITATIVE)

⚠️ **This document is informational only. It is not authoritative.**

All authoritative governance for this repository is defined exclusively
in canonical **TOML** documents located under:

directive_core/docs/

This Markdown file exists solely to provide **human-readable context**
and **navigation assistance**. It defines **no rules**, **no precedence**,
and **no enforcement behavior**.

---

## What Is the Governance Root?

The governance root is the directory from which all canonical governance
documents are loaded, validated, and enforced.

For this repository:

- The governance root is **`directive_core/docs/`**
- All authoritative governance artifacts are TOML
- All validation is fail-closed and schema-driven

---

## Where Authority Actually Lives

Refer to the following authoritative documents:

- `SSWG_CONSTITUTION.toml` — supreme governance authority
- `GOVERNANCE_ROOT.toml` — authoritative root declaration
- `TERMINOLOGY.toml` — semantic authority
- `AGENTS.toml` — agent constraints
- `FORMAT_BOUNDARY_CONTRACT.toml` — format enforcement
- `ARCHITECTURE.toml` — system structure

---

## Important Boundary Notice

This document:

- Does **not** participate in governance ingestion
- Does **not** define validator behavior
- Does **not** override or amend the Constitution
- Does **not** grant authority of any kind

If this Markdown file conflicts with any TOML governance document,
the TOML document **always wins**.

---

For enforcement, validation, and audit behavior, see the TOML
counterpart:

directive_core/docs/GOVERNANCE_ROOT.toml


