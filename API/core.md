# 🧬 Core API (ai_core/)  
### Orchestrator, Phase Controller, Module Registry

---

# 🎛 Orchestrator

## `class Orchestrator:`
Central coordination engine for workflow creation and validation.

### Key Methods

#### `run(user_config, recursive=False)`
- Generates workflow  
- Validates schema  
- Saves workflow to memory  
- (Optional) performs recursive expansions  
- Triggers telemetry + dashboard updates  

---

# 🧩 Phase Controller

## `class PhaseController`
Executes transformation phases in order.

### Responsibilities:
- manage input/output between phases  
- track internal phase metadata  
- unify phase schemas  

---

# 📦 Module Registry

## `class ModuleRegistry`
In future releases this will:

- map modules to dependencies  
- enforce uniqueness & naming constraints  
- support plugin loading  

Currently implemented as a placeholder.

---

# 📄 Workflow Object

## `class Workflow`
A lightweight container for:

```python
workflow_id: str  
params: dict  
results: dict  
```

Primary method:

### `run_all_phases()`
Executes P1 → P3 mock phases (MVM-minimal).
