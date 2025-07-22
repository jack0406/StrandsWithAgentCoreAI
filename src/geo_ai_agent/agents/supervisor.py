import logging
from typing import Dict, Callable, Union

from ..tools import (
    Tool,
    SubAgentTool,
    StrandsAgentTool,
    BedrockAgentCoreTool,
    MCPServerTool,
)
from ..agents.sub_agents import SubAgent, StrandsAgent
from ..core import BedrockAgentCore, MCPServer
from ..tools.decorators import tool as tool_decorator

logger = logging.getLogger(__name__)


class GeoAIAgent:
    """Coordinator agent that delegates requests to registered tools."""

    def __init__(self) -> None:
        self._tools: Dict[str, Tool] = {}

    def _wrap(self, obj: Union[Tool, SubAgent, StrandsAgent, BedrockAgentCore, MCPServer, Callable[..., str]]) -> Tool:
        """Convert various component types into a ``Tool`` instance."""
        if isinstance(obj, Tool):
            return obj
        if isinstance(obj, SubAgent):
            return SubAgentTool(obj)
        if isinstance(obj, StrandsAgent):
            return StrandsAgentTool(obj)
        if isinstance(obj, BedrockAgentCore):
            return BedrockAgentCoreTool(obj)
        if isinstance(obj, MCPServer):
            return MCPServerTool(obj)
        if callable(obj):
            return tool_decorator(obj)
        raise TypeError(f"Unsupported tool type: {type(obj)!r}")

    def register_tool(self, name: str, tool: Union[Tool, SubAgent, StrandsAgent, BedrockAgentCore, MCPServer, Callable[..., str]]) -> None:
        """Register a tool or component by name."""
        wrapped = self._wrap(tool)
        self._tools[name] = wrapped
        logger.debug("Registered tool %s", name)

    def handle_request(self, tool_name: str, *args, **kwargs) -> str:
        """Dispatch a request to the specified tool."""
        tool = self._tools.get(tool_name)
        if not tool:
            raise ValueError(f"Unknown tool '{tool_name}'")
        logger.info("Routing request to tool %s", tool_name)
        return tool.run(*args, **kwargs)


