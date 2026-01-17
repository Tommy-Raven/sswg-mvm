#!/usr/bin/env python3
"""
generator/exception_handler.py — Centralized Exception Handling for SSWG.

Provides decorators and helpers for wrapping sync and async callables
with logging, while making linting intent explicit.
"""

from __future__ import annotations

import logging
import traceback
from typing import Any, Callable, Optional

logger = logging.getLogger("generator.exception_handler")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
logger.addHandler(handler)


def handle_exceptions(
    func: Callable[..., Any],
    *,
    default_return: Optional[Any] = None,
    log_traceback: bool = True,
) -> Callable[..., Any]:
    """
    Decorator to wrap functions in a try/except block, logging exceptions.

    Args:
        func:
            Function to wrap.
        default_return:
            Return value if an exception occurs.
        log_traceback:
            Whether to log the full traceback at debug level.

    Returns:
        Wrapped function.
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except Exception as exc:  # pylint: disable=broad-exception-caught
            logger.error("Exception in %s: %s", func.__name__, exc)
            if log_traceback:
                traceback_text = traceback.format_exc()
                logger.debug("%s", traceback_text)
            return default_return

    return wrapper


async def async_handle_exceptions(
    coro_func: Callable[..., Any],
    *,
    default_return: Optional[Any] = None,
    log_traceback: bool = True,
) -> Callable[..., Any]:
    """
    Wrap an async coroutine function to safely catch exceptions.

    Args:
        coro_func:
            Async function to wrap.
        default_return:
            Value to return on exception.
        log_traceback:
            Whether to log the full traceback at debug level.

    Returns:
        Async wrapper function.
    """

    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return await coro_func(*args, **kwargs)
        except Exception as exc:  # pylint: disable=broad-exception-caught
            logger.error("Async exception in %s: %s", coro_func.__name__, exc)
            if log_traceback:
                traceback_text = traceback.format_exc()
                logger.debug("%s", traceback_text)
            return default_return

    return wrapper
