"""Coordinator agent that delegates requests to registered tools."""

from typing import Dict
import logging

from .tools.base import Tool


logger = logging.getLogger(__name__)


class GeoAIAgent:
    """Receive external requests and route them to sub-tools."""

    def __init__(self) -> None:
        self._tools: Dict[str, Tool] = {}

    def register_tool(self, name: str, tool: Tool) -> None:
        """Register a tool by name."""
        self._tools[name] = tool
        logger.debug("Registered tool %s", name)

    def handle_request(self, tool_name: str, *args, **kwargs) -> str:
        """Dispatch a request to the specified tool."""
        tool = self._tools.get(tool_name)
        if not tool:
            raise ValueError(f"Unknown tool '{tool_name}'")
        logger.info("Routing request to tool %s", tool_name)
        return tool.run(*args, **kwargs)
