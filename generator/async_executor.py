#!/usr/bin/env python3
"""
Asynchronous Task Executor for SSWG MVM.

Provides helpers for running synchronous and asynchronous functions concurrently,
with structured logging and safe error handling at task boundaries.
"""

from __future__ import annotations

import asyncio
import logging
from typing import Any, Awaitable, Callable, Coroutine, Iterable, List, Union

logger = logging.getLogger("async_executor")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
logger.addHandler(handler)

AsyncTaskType = Union[Callable[..., Awaitable[Any]], Coroutine[Any, Any, Any]]


async def run_task(task: AsyncTaskType, *args: Any, **kwargs: Any) -> Any:
    """
    Run a single asynchronous task (function or coroutine object) with logging.

    Returns:
        The task result, or None if the task raised an exception.
    """
    try:
        if callable(task):
            result = await task(*args, **kwargs)
        else:
            result = await task
        return result
    except Exception as exc:  # pylint: disable=broad-exception-caught
        logger.error(
            "Task %s failed: %s",
            getattr(task, "__name__", repr(task)),
            exc,
        )
        return None


async def run_tasks_concurrently(
    tasks: Iterable[AsyncTaskType],
    *args: Any,
    **kwargs: Any,
) -> List[Any]:
    """
    Run multiple async tasks concurrently.

    Args:
        tasks:
            Iterable of async callables or coroutine objects.

    Returns:
        List of task results, with failures converted to None.
    """
    coroutines: List[Coroutine[Any, Any, Any]] = []
    for task_item in tasks:
        if callable(task_item):
            coroutines.append(task_item(*args, **kwargs))
        else:
            coroutines.append(task_item)

    results: List[Any] = await asyncio.gather(
        *coroutines,
        return_exceptions=True,
    )
    for index, result_item in enumerate(results):
        if isinstance(result_item, Exception):
            logger.error(
                "Task #%d failed during concurrent execution: %s",
                index,
                result_item,
            )
            results[index] = None
    return results


def run_sync(task: AsyncTaskType, *args: Any, **kwargs: Any) -> Any:
    """
    Convenience wrapper to run a single async task from synchronous code.
    """
    return asyncio.run(run_task(task, *args, **kwargs))


def run_all_sync(
    tasks: Iterable[AsyncTaskType],
    *args: Any,
    **kwargs: Any,
) -> List[Any]:
    """
    Convenience wrapper to run multiple async tasks from synchronous code.
    """
    return asyncio.run(run_tasks_concurrently(tasks, *args, **kwargs))
