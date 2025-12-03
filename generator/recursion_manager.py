#!/usr/bin/env python3
"""
generator/recursion_manager.py — Recursion policy and refinement.

Provides a small abstraction that decides whether to recurse and how to
annotate a workflow for the next recursive step.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class RecursionPolicy:
    """
    Configuration for recursion decisions.

    Attributes:
        max_depth:
            Maximum allowed recursion depth.
        min_improvement:
            Minimum score_delta required to justify another recursion step.
    """
    max_depth: int = 2
    min_improvement: float = 1.0


class RecursionManager:
    """
    Decide whether to recurse and generate refined workflow variants.

    At MVM stage, refinement is non-destructive and only annotates metadata.
    """

    def __init__(self, policy: Optional[RecursionPolicy] = None) -> None:
        self.policy = policy or RecursionPolicy()

    def should_recurse(self, depth: int, score_delta: float) -> bool:
        """
        Decide if another recursion step is warranted.

        Args:
            depth:
                Current recursion depth (0-based).
            score_delta:
                Improvement score compared to a previous version.

        Returns:
            True if we should recurse further, False otherwise.
        """
        if depth >= self.policy.max_depth:
            return False
        return score_delta >= self.policy.min_improvement

    def refine_workflow(
        self,
        workflow_data: Dict[str, Any],
        evaluation_report: Dict[str, Any],
        depth: int,
    ) -> Dict[str, Any]:
        """
        Create a minimally adjusted copy of workflow_data for the next recursion step.

        For the MVM, this simply attaches recursion metadata and returns a
        shallow copy of the input workflow.
        """
        refined_workflow = dict(workflow_data)
        recursion_metadata = refined_workflow.setdefault("recursion_metadata", {})
        recursion_metadata["depth"] = depth
        recursion_metadata["last_evaluation"] = evaluation_report
        return refined_workflow
