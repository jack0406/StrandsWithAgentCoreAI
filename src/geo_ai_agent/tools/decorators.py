from __future__ import annotations

from functools import wraps
from typing import Callable

from .base import Tool


def tool(func: Callable[..., str]) -> Tool:
    """Decorator turning a function into a :class:`Tool` instance."""

    class FunctionTool(Tool):
        def run(self, *args, **kwargs) -> str:
            return func(*args, **kwargs)

    FunctionTool.__name__ = func.__name__  # type: ignore[attr-defined]
    FunctionTool.__doc__ = func.__doc__
    return FunctionTool()

__all__ = ["tool"]
