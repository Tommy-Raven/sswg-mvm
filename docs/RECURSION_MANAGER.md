# Recursion Manager

## Purpose
Central controller for managing recursive workflow expansion, depth limits, and stopping conditions.

## Responsibilities
- Track recursion depth and iteration count.
- Prevent infinite recursion loops.
- Interface with `semantic_scorer.py` to detect content stability.
- Manage recursion configuration parameters via `config/recursion.yml`.

## Example Configuration (`recursion.yml`)
```yaml
recursion:
  max_depth: 5
  min_delta_score: 0.15
  halt_on_no_improvement: true
  cache_reuse: true

Example Usage
from generator.recursion_manager import RecursionManager
rm = RecursionManager(max_depth=5)
rm.run_cycle(workflow)
