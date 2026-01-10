This appendix **normatively captures** what the validator enforces, without leaking implementation details or rule identifiers.

---

# Appendix A — Governance Validation & Ambiguity Extermination Framework

## A.1 Purpose and Authority

This appendix formalizes the **governance validation framework** that enforces the SSWG/MVM constitutional doctrine that:

> **Ambiguity is a security vulnerability, not a stylistic concern.**

This appendix is **normative**. Its provisions are **binding** on all governance documents, validators, agents, tooling, and future extensions operating under `directive_core/`.

Failure to comply with this appendix **SHALL** result in immediate rejection and quarantine of the offending artifact.

---

## A.2 Canonical Governance Validation Surface

Governance validation operates exclusively within the following canonical surface:

* **Authoritative governance documents**
  Located at:
  `directive_core/docs/`
  Format: **pure TOML only**

* **Governance definitions and invariants**
  Located at:
  `directive_core/definitions/`
  Format: **pure TOML only**

Any governance artifact outside these locations **SHALL NOT** be considered authoritative.

---

## A.3 Canonical Ledger Header Invariant

### A.3.1 Header Format Requirement

Every authoritative governance document **MUST** contain **exactly one** canonical ledger header defined as a TOML `[anchor]` table.

The canonical ledger header:

* **MUST** be written in TOML
* **MUST NOT** be written in YAML, JSON, or Markdown
* **MUST** appear exactly once per document
* **MUST** include all required anchor fields
* **MUST** correctly declare its authority status

Any document violating these conditions **SHALL** be rejected with an `Invalid Canonical Header` failure.

---

## A.4 Governance Ingestion Order Invariant

Governance documents **MUST** be ingested in a strictly ordered sequence.

The ingestion order is **authoritative**, **non-negotiable**, and **fail-closed**.

If any required document is:

* missing,
* malformed,
* duplicated,
* or out of order,

then governance ingestion **SHALL FAIL** immediately.

No partial ingestion is permitted.

---

## A.5 Ledger Format Invariant

### A.5.1 Authoritative Format Rule

All **authoritative governance artifacts**:

* **MUST** be written in **pure TOML**
* **MUST NOT** include YAML blocks
* **MUST NOT** include YAML code fences
* **MUST NOT** rely on Markdown for authority

Markdown (`.md`) governance documents **SHALL NOT** be invariant and **SHALL ONLY** be treated as `non_operational_output`.

### A.5.2 Machine Authority Rule

Machines **SHALL ONLY** consume governance authority from **pure TOML** sources.

YAML **MAY** be used only as:

* a human-authored, pre-authoritative input format
* subject to mandatory normalization and ambiguity gating

YAML **SHALL NEVER** be authoritative.

---

## A.6 Semantic Ambiguity Extermination Doctrine

### A.6.1 Definition

**Semantic ambiguity** is defined as any language that allows:

* multiple interpretations,
* implied authority,
* contextual exceptions,
* interpretive permission,
* inferred intent,
* or delegated responsibility.

Ambiguity **SHALL** be treated as a **security defect**.

---

### A.6.2 Mandatory Ambiguity Gate

All governance ingestion **MUST** pass through a **Semantic Ambiguity Gate** prior to normalization or enforcement.

The gate:

* **MUST** operate deterministically
* **MUST** fail-closed
* **MUST** reject on any ambiguity match
* **MUST NOT** expose internal rule identifiers or trigger names in user-visible output

The only permitted public failure label is:

> **Semantic Ambiguity**

---

### A.6.3 Extermination Semantics

When ambiguity is detected:

1. The artifact **SHALL** be immediately rejected
2. The artifact **SHALL** be quarantined
3. The artifact **SHALL NOT** proceed to normalization
4. No interpretive repair is permitted

Ambiguity **SHALL NOT** be waived, softened, interpreted, or contextualized.

---

## A.7 Ambiguity Gate Governance Structure

The Ambiguity Gate **MUST** be governed by three distinct TOML artifacts:

1. **Specification (Non-authoritative)**

   * Descriptive only
   * Documents intent and trigger classes
   * Not enforceable

2. **Invariant (Authoritative)**

   * Declares ambiguity intolerance as immutable
   * Binds enforcement to governance ingestion

3. **Policy (Authoritative)**

   * Defines the exact trigger patterns
   * Enforced deterministically

All three artifacts **MUST** be present.
Absence of any one **SHALL** result in governance failure.

---

## A.8 Prohibition on Ambiguous Language Constructs

Language patterns including, but not limited to:

* “allow unless explicitly waived”
* “may be interpreted as”
* “under special circumstances”
* “depending on context”
* “reasonable interpretation”
* “except in this case”

are **explicitly forbidden** in authoritative governance documents.

Any appearance of such language **SHALL** trigger ambiguity failure.

---

## A.9 Validator Binding Requirement

All validators operating under `directive_core/`:

* **MUST** enforce this appendix
* **MUST** fail-closed on violation
* **MUST** remain deterministic
* **MUST NOT** expose enforcement internals
* **MUST NOT** attempt corrective interpretation

Validators **SHALL** prefer rejection over repair.

---

## A.10 End-of-Appendix Summary (Normative)

This appendix codifies the SSWG/MVM principle that **clarity is security** and **ambiguity is contamination**.

By enforcing:

* pure TOML authority,
* strict ingestion order,
* canonical headers,
* and immediate ambiguity extermination,

the governance system remains deterministic, auditable, and resistant to semantic drift.

Any artifact that violates these principles is **non-canonical** and **SHALL NOT** be admitted.

---
