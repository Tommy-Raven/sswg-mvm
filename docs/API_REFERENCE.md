# API Reference

## Main Classes & Functions
| Module | Function | Description |
|--------|-----------|-------------|
| `generator.main` | `create_workflow()` | Initializes workflow pipeline |
| `generator.recursion_manager` | `run_cycle()` | Handles recursion logic |
| `ai_evaluation.semantic_analysis` | `compare()` | Returns semantic delta score |
| `ai_monitoring.telemetry` | `record()` | Logs recursion metrics |

## Example API Call
```python
from generator.main import create_workflow
wf = create_workflow(user_params)