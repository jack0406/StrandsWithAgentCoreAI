from .interfaces import ServerInterface


class MCPServer(ServerInterface):
    """Simplified stub for an MCP server.

    This represents an external command processor.  The implementation can be
    swapped out for a real server without changing the interface presented to
    the rest of the system.
    """

    def send_command(self, command: str) -> str:
        """Pretend to send a command to the MCP server."""
        return f"MCP server executed: {command}"
