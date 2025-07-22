"""Simplified stub for Strands Agent."""

from ...interfaces import AgentInterface


class StrandsAgent(AgentInterface):
    """Pretend Strands agent that echoes the query it receives."""

    def respond(self, query: str) -> str:
        return f"Strands response: {query}"
