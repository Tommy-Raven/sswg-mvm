"""
Comprehensive test — ensures end-to-end workflow lifecycle passes
through generation → validation → evaluation → export.
"""

from ai_core.orchestrator import Orchestrator
from ai_validation.schema_validator import validate_workflow
from ai_evaluation.quality_metrics import evaluate_clarity
from ai_visualization.export_manager import export_workflow
import os


def test_full_workflow_cycle(tmp_path):
    orch = Orchestrator()
    wf = orch.run({"purpose": "E2E test", "audience": "Testers"})

    valid, err = validate_workflow(wf)
    assert valid, err

    metrics = evaluate_clarity(wf)
    assert metrics["clarity_score"] > 0

    exports = export_workflow(wf, export_mode="json")
    for f in exports.values():
        assert os.path.exists(f)
