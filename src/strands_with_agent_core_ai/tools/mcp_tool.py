from .base import Tool
from ..mcp_server import MCPServer
import logging

logger = logging.getLogger(__name__)


class MCPServerTool(Tool):
    """Tool wrapper for MCP servers."""

    def __init__(self, server: MCPServer) -> None:
        self.server = server

    def run(self, command: str) -> str:
        """Send a command to the configured MCP server."""
        logger.debug("MCPServerTool sending command: %s", command)
        return self.server.send_command(command)
