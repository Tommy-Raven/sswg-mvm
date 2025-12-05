# SSWG-MVM Schema Overview

This directory defines the JSON Schemas that describe the core data model for the **SSWG Minimum Viable Model (MVM)**.

All schemas:

* Use **JSON Schema Draft 2020-12**
* Declare a stable **`$id`** under this repository’s `schemas/` path
* Use **relative `$ref` values** (e.g. `"metadata_schema.json"`) that are resolved
  against the local `schemas/` directory
* Are generally designed for **strict property inclusion**
  (`additionalProperties: false` where appropriate)

> **Note:** `$id` values use GitHub `tree` URLs as identifiers. Resolution is performed
> locally by `ai_validation/schema_validator.py` using `SCHEMAS_DIR` as the base path.

---

## Draft and Conventions

* `$schema` (all schemas):

  ```json
  "https://json-schema.org/draft/2020-12/schema"
  ```

* `$id` pattern (example):

  ```json
  "https://github.com/Tommy-Raven/SSWG-mvm1.0/tree/main/schemas/workflow_schema.json"
  ```

* `$ref` pattern (example):

  ```json
  { "$ref": "metadata_schema.json" }
  ```

  These are **relative filenames**, resolved to local files under `schemas/` by the
  validation layer.

* **Naming:**
  Filenames and `$id`s are kept in sync so schemas can be referenced unambiguously.

---

## Top-Level Workflow Schema

### `workflow_schema.json`

**Role:** Canonical definition of a full SSWG-MVM workflow.

**Key points:**

* **Type:** `object`

* **Required:** `workflow_id`, `version`, `metadata`, `phases`

* **Properties:**

  * `workflow_id` – string, constrained to `^[a-zA-Z0-9_-]+$`
  * `version` – string
  * `metadata` – `$ref`: `"metadata_schema.json"`
  * `phases` – array of `$ref`: `"phase_schema.json"`, `minItems: 1`
  * `modules` – array of `$ref`: `"module_schema.json"`
  * `semantics` – array of `$ref`: `"semantics_schema.json"`
  * `evaluation` – `$ref`: `"evaluation_schema.json"`
  * `recursion` – `$ref`: `"recursion_schema.json"`
  * `dependency_graph` – object with:

    * `nodes`: array of strings
    * `edges`: array of 2-element string arrays (`[from, to]`)

* **Extra fields:**
  `additionalProperties: false` – only declared properties are allowed.

**Used by:**

* `ai_validation/schema_validator.py` (`validate_workflow`)
* `ai_validation/regression_tests.py`
* `generator/main.py` (`process_workflow` → validation, graphing, refinement)

---

## Core Structural Schemas

### `phase_schema.json`

**Role:** Defines a single workflow phase.

**Key points:**

* **Type:** `object`

* **Required:** `id`, `title`, `tasks`

* **Properties:**

  * `id` – string
  * `title` – string
  * `description` – string (optional)
  * `tasks` – array of `$ref`: `"task_schema.json"`, `minItems: 1`
  * `subphases` – array of `$ref`: `"phase_schema.json"` (recursive)
  * `evaluation_schema` – `$ref`: `"evaluation_schema.json"`

* **Extra fields:**
  `additionalProperties: false`

**Referenced by:**

* `workflow_schema.json` → `phases[*]`

---

### `task_schema.json`

**Role:** Defines an **atomic instructional task**.

**Key points:**

* **Type:** `object`

* **Required:** `title`

* **Properties:**

  * `title` – string
  * `instruction` – string
  * `inputs` – array of strings
  * `outputs` – array of strings
  * `ai_task_logic` – string
  * `dependencies` – array of strings
  * `semantic_tag` – string
  * `evaluation_hint` – string

* **Extra fields:**
  `additionalProperties: false`

**Referenced by:**

* `phase_schema.json` → `tasks[*]`
* `module_schema.json` → `tasks[*]`

> **Note:** Some current workflows still use `id` / `description` for tasks;
> the schema is stricter and will flag these as validation issues until fully
> migrated.

---

### `module_schema.json`

**Role:** Describes a **reusable module** of tasks within or across workflows.

**Key points:**

* **Type:** `object`

* **Required:** `module_id`, `title`, `tasks`

* **Properties:**

  * `module_id` – string, `^[a-zA-Z0-9_-]+$`
  * `title` – string
  * `description` – string
  * `tasks` – array of `$ref`: `"task_schema.json"`
  * `dependencies` – array of strings (other module IDs/names)
  * `linked_phases` – array of strings (phase IDs)
  * `metadata` – `$ref`: `"metadata_schema.json"`

* **Extra fields:**
  `additionalProperties: false`

**Referenced by:**

* `workflow_schema.json` → `modules[*]`

---

## Metadata & Evaluation

### `metadata_schema.json`

**Role:** Generic metadata for workflows and modules.

**Key points:**

* **Type:** `object`

* **Required:** `purpose`, `audience`

* **Properties:**

  * `purpose` – string, `minLength: 3`
  * `audience` – string
  * `author` – string
  * `created` – `string` (`date-time` format)
  * `tags` – array of strings
  * `context_level` – enum: `conceptual`, `procedural`, `evaluative`

* **Extra fields:**
  `additionalProperties: true` (metadata can be expanded as needed)

**Referenced by:**

* `workflow_schema.json` → `metadata`
* `module_schema.json` → `metadata`

---

### `evaluation_schema.json`

**Role:** Defines **evaluation metrics** attached to a workflow or phase.

**Key points:**

* **Type:** `object`

* **Required:** `clarity_score`, `completeness_score`, `cohesion_score`

* **Properties:**

  * `clarity_score` – number `[0, 1]`
  * `completeness_score` – number `[0, 1]`
  * `cohesion_score` – number `[0, 1]`
  * `semantic_alignment` – number `[0, 1]`
  * `notes` – string (free-form comments)

* **Extra fields:**
  `additionalProperties: true` (allow extended metrics)

**Referenced by:**

* `workflow_schema.json` → `evaluation`
* `phase_schema.json` → `evaluation_schema`
* `recursion_schema.json` → `evaluation_schema`

---

## Recursion & Semantics

### `recursion_schema.json`

**Role:** Encodes settings for **recursive regeneration and self-evolution** of workflows.

**Key points:**

* **Type:** `object`

* **Required:** `depth_limit`, `trigger_condition`

* **Properties:**

  * `depth_limit` – integer, `min: 1`
  * `trigger_condition` – string (logic/condition description)
  * `regeneration_threshold` – number `[0, 1]`
  * `feedback_source` – string
  * `evaluation_schema` – `$ref`: `"evaluation_schema.json"`
  * `history_log` – array of strings

* **Extra fields:**
  `additionalProperties: false`

**Referenced by:**

* `workflow_schema.json` → `recursion`

> **Runtime note:** At the MVM stage, `generator/recursion_manager.py` uses a simpler
> runtime policy (`max_depth`, `min_improvement`) and writes `recursion_metadata`
> into workflows; this schema is the formal target for richer recursion
> configuration.

---

### `semantics_schema.json`

**Role:** Describes **semantic mappings** for terms used within workflows.

**Key points:**

* **Type:** `object`

* **Required:** `term`, `semantic_context`

* **Properties:**

  * `term` – string
  * `semantic_context` – string
  * `related_terms` – array of strings
  * `embedding_vector` – array of numbers
  * `confidence` – number `[0, 1]`

* **Extra fields:**
  `additionalProperties: true`

**Referenced by:**

* `workflow_schema.json` → `semantics[*]`

---

## Prompt and Ontology Schemas

### `prompt_schemas.json`

**Role:** Validates user prompts used to generate workflows.

**Key points:**

* **Type:** `object`
* **Required:** `purpose`, `target_audience`, `style`
* **Properties:**

  * `purpose` – string, `minLength: 3`
  * `target_audience` – enum: `beginner`, `intermediate`, `expert`
  * `delivery_mode` – array of enums: `text`, `code`, `visual`, `interactive`
  * `expansion_mode` – array of enums: `recursive`, `modular`, `adaptive`
  * `evaluation_method` – enum: `self-refinement`, `peer-review`, `simulation`
  * `style` – enum: `technical`, `friendly`, `wizardly`, `academic`

> **Filename note:** The schema is currently named `prompt_schemas.json`. If you
> prefer a singular name (`prompt_schema.json`), rename the file and update the
> `$id` accordingly.

---

### `ontology_schema.json`

**Role:** Defines an **ontology view** over workflows: semantic relationships between
phases, inputs/outputs, and dependency graphs.

**Key points:**

* **Type:** `object`
* **Required:** `workflow_id`, `purpose`, `target_audience`, `phases`, `dependency_graph`
* **Properties:**

  * `workflow_id` – string
  * `purpose` – string
  * `target_audience` – string
  * `phases` – array of objects with:

    * `id`, `title` – strings
    * `input`, `output` – arrays of strings
    * `submodules` – array (untyped placeholder)
    * `ai_task_logic` – string
    * `human_actionable` – string
  * `dependency_graph` – object with:

    * `nodes` – array of strings
    * `edges` – array of `[from, to]` string pairs
  * `evaluation_metrics` – array of strings

**Intended use:**

* Higher-level semantic analysis of workflows (e.g., mapping phases to conceptual
  spaces, cross-workflow reasoning).

---

## How These Schemas Are Used in MVM

* **Validation:**
  `ai_validation/schema_validator.py`:

  * Uses `Draft202012Validator`
  * Sets `base_uri` to `SCHEMAS_DIR.as_uri()` and resolves **relative `$ref`**
    (e.g. `"metadata_schema.json"`) to local files under `schemas/`.

* **Generation Pipeline:**
  `generator/main.py`:

  * Ingests a workflow/template,
  * Validates against `workflow_schema.json`,
  * Builds dependency graphs from `modules` / phases,
  * Runs a simple recursion/refinement step,
  * Exports JSON + Markdown.

* **Future Extensions:**

  * Templates currently follow a de facto structure
    (`template_id`, `title`, `description`, `phases[id/title/tasks[]]`, `metadata`)
    but are not yet governed by a dedicated `template_schema.json`.

---

## Adding New Schemas

When introducing a new schema:

1. Place it under `schemas/` as `*_schema.json`.
2. Set:

   * `$schema` to Draft 2020-12:

     ```json
     "https://json-schema.org/draft/2020-12/schema"
     ```
   * `$id` to the corresponding GitHub tree path, e.g.:

     ```json
     "https://github.com/Tommy-Raven/SSWG-mvm1.0/tree/main/schemas/new_schema.json"
     ```
3. Use **relative `$ref` filenames** for sibling schemas:

   ```json
   { "$ref": "workflow_schema.json" }
   ```
4. Decide on `additionalProperties` explicitly (`false` for strict control,
   `true` where extensibility is desired).
5. Optionally add regression examples under `tests/resources/` and wire them
   into `ai_validation/regression_tests.py`.

This keeps the SSWG-MVM data model coherent, versionable, and enforceable across
