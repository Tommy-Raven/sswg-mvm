#!/usr/bin/env python3
"""
ai_cores/evaluation_core.py — Shared evaluation helpers for SSWG MVM.
"""

from __future__ import annotations

from typing import Dict, Iterable, List

__all__ = ["evaluate_clarity", "fit_scores", "summarize_checkpoints"]


def evaluate_clarity(workflow: Dict[str, object]) -> Dict[str, float]:
    """Compute a simple clarity score for workflow phases."""
    scores: Dict[str, float] = {}

    for phase in workflow.get("phases", []) or []:
        if not isinstance(phase, dict):
            continue

        text = phase.get("ai_task_logic") or phase.get("description") or ""
        phase_id = phase.get("id") or phase.get("phase_id") or "<unnamed>"

        words = len(str(text).split())
        raw_score = words / 10.0
        score = max(0.0, min(1.0, raw_score))
        scores[str(phase_id)] = score

    if not scores:
        return {"clarity_score": 0.0}

    avg = sum(scores.values()) / len(scores)
    return {"clarity_score": avg}


def fit_scores(scores: Iterable[float]) -> tuple[float, float]:
    """Return min/max bounds for score normalization."""
    score_list: List[float] = list(scores)
    if not score_list:
        return 0.0, 1.0
    min_score = min(score_list)
    max_score = max(score_list)
    if min_score == max_score:
        min_score -= 0.5
        max_score += 0.5
    return min_score, max_score


def summarize_checkpoints(history: List[object]) -> Dict[str, object]:
    """Summarize evaluation checkpoint history."""
    if not history:
        return {"checkpoints": 0, "last_passed": False, "regressions": {}}
    last = history[-1]
    return {
        "checkpoints": len(history),
        "last_passed": getattr(last, "passed", False),
        "last_name": getattr(last, "name", None),
        "regressions": getattr(last, "regressions", {}),
        "rollback_recommended": getattr(last, "rollback_recommended", False),
    }
