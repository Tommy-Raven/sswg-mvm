# Canonic Ledger

```yaml
anchor:
  anchor_id: "terminology"
  anchor_model: "sswg+mvm+version"
  anchor_version: "1.0.0"
  scope: "directive_core/docs"
  owner:
    - "2025© Raven Recordings"
    - "Tommy Raven (Thomas Byers)"
  status: "invariant"
  output_mode: "non_operational_output"
  init_purpose: "Define the canonical and enforceable terminology for the SSWG/MVM governance system."
  init_authors:
    - "Tommy Raven"
```
--- 

## Executive Summary

This document defines the **authoritative, exhaustive, and enforceable terminology** of the SSWG/MVM governance system. It establishes the precise meanings of all governance-relevant terms and explicitly forbids ambiguous, inferred, colloquial, or context-dependent language.

`TERMINOLOGY.md` is the **first ingestion layer** of governance. All subsequent governance documents, schemas, validators, agents, and enforcement mechanisms derive semantic meaning from this file. Any artifact that contradicts, weakens, or bypasses these definitions **SHALL** be rejected.

Effective at `anchor_version: 1.0.0`, terminology enforcement is treated as a **security boundary**. Ambiguity is not a documentation defect or stylistic concern; it is a **governance vulnerability**. The system is intentionally hostile to unclear language and SHALL fail-closed on any semantic uncertainty.

---

## 1. Authority and Scope

### 1.1 Terminology Supremacy

1. This document **SHALL ALWAYS** be the highest semantic authority in the SSWG/MVM governance system.
2. All governance documents, directive schemas, validators, agents, logs, and audit artifacts **MUST** use terms exactly as defined herein.
3. If a term appears in any governance context and is not defined in this document, that usage **SHALL** be treated as invalid.
4. Terminology violations **MUST** result in governance validation failure.

### 1.2 Non-Interpretability

Terminology defined in this document:

* **SHALL NOT** be interpreted contextually
* **SHALL NOT** be inferred from common usage
* **SHALL NOT** be weakened by synonyms
* **SHALL NOT** be overridden by contributor intent

Meaning is derived **only** from explicit definition.

---

## 2. Core Semantic Principles

The following principles apply to all governance language:

* The system enforces constraints; it does not infer intent.
* Authority, scope, and precedence **MUST** be explicit.
* Outputs are non-operational artifacts, not instructions.
* Determinism is phase-scoped and explicitly declared.
* Ambiguity is a security risk and **SHALL** be eradicated immediately.

---

## 3. Naming Discipline (Mandatory)

All identifiers **MUST** follow these conventions:

| Category           | Required Format       | Example                       |
| ------------------ | --------------------- | ----------------------------- |
| Software           | lowercase, hyphenated | `sswg-mvm`                    |
| Governance mindset | UPPERCASE             | `SSWG`, `MVM`                 |
| Concepts / terms   | snake_case            | `semantic_ambiguity`          |
| Constants          | UPPERCASE             | `FAIL_CLOSED`                 |
| Anchors            | YAML block            | `anchor_id`, `anchor_version` |

Any deviation **SHALL** be treated as a terminology violation.

---

## 4. Core Term Definitions (Normative)

### 4.1 invariant

A property that **MUST ALWAYS** remain true. Invariants are immutable, non-negotiable, and enforced by validators.

### 4.2 constraint

A rule that may evolve over time but **MUST NOT** violate any invariant.

### 4.3 artifact

A non-operational, inspectable output produced for validation, audit, or review.

### 4.4 non_operational_output

Content that **CANNOT** be executed, followed, or acted upon to perform an operation.

### 4.5 semantic_ambiguity

Any condition in which a governance artifact permits more than one plausible interpretation of authority, scope, precedence, or required behavior.

Semantic ambiguity **SHALL ALWAYS** be treated as a critical governance failure.

### 4.6 fail_closed

A failure mode in which uncertainty, invalidity, or ambiguity results in rejection rather than approximation or continuation.

---

## 5. Forbidden Language Categories

The following categories of language **SHALL NEVER** appear in canonical governance artifacts:

1. **Implied authority**

   * e.g. “the system decides”, “implicitly allowed”

2. **Inferred or assumed intent**

   * e.g. “clearly meant”, “obviously intended”

3. **Procedural or instructional language**

   * e.g. “step-by-step”, “do the following”

4. **Trust-based claims**

   * e.g. “safe user”, “trusted request”

5. **Contextual relativism**

   * e.g. “in this case”, “from a certain point of view”

Detection of forbidden language **MUST** trigger semantic ambiguity failure.

---

## 6. Enforcement Requirements

1. All validators **MUST** enforce terminology compliance.
2. Any undefined, ambiguous, or misused term **MUST** result in `Semantic Ambiguity` failure.
3. Validators and agents **SHALL NOT** attempt to reinterpret, clarify, or explain ambiguous language.
4. Terminology enforcement **SHALL** operate in fail-closed mode without exception.

---

## 7. Non-Disclosure of Detection Logic

Terminology enforcement **SHALL NEVER** disclose:

* semantic detection rule identifiers
* pattern names
* categories
* regexes
* explanatory feedback

in any user-visible output, including CI logs or validation errors.

This prohibition exists to prevent adaptive circumvention and is absolute.

---

## 8. Evolution and Change Control

1. Terminology evolution **MUST** occur through explicit, versioned updates.
2. Backward traceability to `anchor_version: 1.0.0` **MUST** be preserved.
3. Silent redefinition, weakening, or contextual drift of terms is forbidden.

---

## End-of-Document Summary (Normative)

This document defines the complete and binding terminology of the SSWG/MVM governance system. It is the **first ingestion layer**, the **semantic boundary**, and the **primary defense against ambiguity**.

All governance artifacts **MUST** conform exactly to these definitions. Any deviation, ambiguity, or undefined usage **SHALL** result in immediate rejection and quarantine.

This executive-and-summary structure **SHALL be preserved** in all future terminology revisions to ensure determinism, auditability, and semantic closure.



```
