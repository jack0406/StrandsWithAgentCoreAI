from abc import ABC, abstractmethod
import logging
from typing import Any

from ..agents.sub_agents.sub_agent import SubAgent
from ..agents.sub_agents.strands_agent import StrandsAgent
from ..core import BedrockAgentCore, MCPServer

logger = logging.getLogger(__name__)


class Tool(ABC):
    """Base interface for all tools."""

    @abstractmethod
    def run(self, *args, **kwargs) -> str:
        """Execute the tool and return a string result."""
        raise NotImplementedError


class SubAgentTool(Tool):
    """Tool wrapper for a sub-agent."""

    def __init__(self, agent: SubAgent) -> None:
        self.agent = agent

    def run(self, query: str) -> str:
        logger.debug("SubAgentTool received query: %s", query)
        return self.agent.respond(query)


class StrandsAgentTool(Tool):
    """Tool wrapper for a Strands Agent."""

    def __init__(self, agent: StrandsAgent) -> None:
        self.agent = agent

    def run(self, query: str) -> str:
        logger.debug("StrandsAgentTool received query: %s", query)
        return self.agent.respond(query)


class BedrockAgentCoreTool(Tool):
    """Tool wrapper for Bedrock AgentCore."""

    def __init__(self, core: BedrockAgentCore) -> None:
        self.core = core

    def run(self, request: str) -> str:
        logger.debug("BedrockAgentCoreTool running request: %s", request)
        return self.core.execute(request)


class MCPServerTool(Tool):
    """Tool wrapper for MCP servers."""

    def __init__(self, server: MCPServer) -> None:
        self.server = server

    def run(self, command: str) -> str:
        logger.debug("MCPServerTool sending command: %s", command)
        return self.server.send_command(command)


__all__ = [
    "Tool",
    "SubAgentTool",
    "StrandsAgentTool",
    "BedrockAgentCoreTool",
    "MCPServerTool",
]
