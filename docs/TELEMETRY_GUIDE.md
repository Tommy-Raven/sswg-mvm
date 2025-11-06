
# Telemetry & Logging Guide

Telemetry provides real-time insight into recursion depth, iteration speed, and quality metrics.

## 🧭 Modules
- `ai_monitoring/telemetry.py` — Collects runtime metrics.
- `ai_monitoring/structured_logger.py` — Outputs structured JSON logs.
- `ai_monitoring/cli_dashboard.py` — Displays live summaries in terminal.

## 🧩 Metrics Tracked
- Recursion depth
- Semantic delta score
- Workflow quality score
- Memory usage
- Generation time per cycle

## Example Log Format
```json
{
  "iteration": 3,
  "depth": 2,
  "semantic_score": 0.87,
  "quality_score": 9.1,
  "timestamp": "2025-11-03T16:00Z"
}
