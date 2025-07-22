from .agent_types import AgentType
from .logging import configure_logging


class BedrockAgentCore:
    """Simplified stub for Bedrock AgentCore."""

    def execute(self, request: str) -> str:
        return f"Bedrock executed: {request}"


class MCPServer:
    """Simplified stub for an MCP server."""

    def send_command(self, command: str) -> str:
        return f"MCP server executed: {command}"


__all__ = [
    "AgentType",
    "configure_logging",
    "BedrockAgentCore",
    "MCPServer",
]
