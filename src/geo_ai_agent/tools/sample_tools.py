"""Sample tools demonstrating different implementations."""

from .base import Tool
from .decorators import tool
from ..core import MCPServer


class EchoTool(Tool):
    """Simple tool that echoes provided text."""

    def run(self, text: str) -> str:
        return f"Echo: {text}"


# Example MCP server used by the decorated tool
_mcp_server = MCPServer()


@tool
def mcp_status() -> str:
    """Return the status from the MCP server."""
    return _mcp_server.send_command("status")


__all__ = ["EchoTool", "mcp_status"]
