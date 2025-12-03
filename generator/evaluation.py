#!/usr/bin/env python3
"""
generator/evaluation.py — Evaluation Engine for SSWG.

Provides a lightweight, async-friendly evaluation framework that
delegates actual metric logic to registered callables.
"""

from __future__ import annotations

import asyncio
import logging
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger("generator.evaluation")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
logger.addHandler(handler)


class EvaluationEngine:
    """Handles evaluation of workflow phases, modular and async-friendly."""

    def __init__(self) -> None:
        self._evaluators: Dict[str, Callable[[Dict[str, Any]], Any]] = {}

    def register_evaluator(
        self,
        phase_name: str,
        func: Callable[[Dict[str, Any]], Any],
    ) -> None:
        """
        Register an evaluator function for a specific phase.

        Args:
            phase_name:
                Phase identifier.
            func:
                Evaluation function that accepts a context dict and returns
                arbitrary metrics (e.g., scores, flags, comments).
        """
        self._evaluators[phase_name] = func
        logger.info("Registered evaluator for phase: %s", phase_name)

    async def evaluate_phase(
        self,
        phase_name: str,
        context: Dict[str, Any],
    ) -> Any:
        """
        Evaluate a single phase asynchronously.

        Args:
            phase_name:
                Phase to evaluate.
            context:
                Context for evaluation.

        Returns:
            Evaluation result, or None if no evaluator is registered.
        """
        evaluator = self._evaluators.get(phase_name)
        if evaluator is None:
            logger.warning("No evaluator registered for phase: %s", phase_name)
            return None

        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(
            None,
            evaluator,
            context,
        )

    async def evaluate_all(
        self,
        context: Dict[str, Any],
        phases: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """
        Evaluate all registered phases or a subset asynchronously.

        Args:
            context:
                Workflow context shared across evaluations.
            phases:
                Optional subset of phases to evaluate. If None, all registered
                evaluators are used.

        Returns:
            Mapping of phase_name -> evaluation result.
        """
        phases_to_eval = phases or list(self._evaluators.keys())
        results: Dict[str, Any] = {}

        for phase in phases_to_eval:
            results[phase] = await self.evaluate_phase(phase, context)

        return results
