"""Simple stub agent that echoes the query it receives."""

from ..sub_agent import SubAgent


class GeoQueryAgent(SubAgent):
    """Pretend agent responding to geo queries."""

    def respond(self, query: str) -> str:
        return f"Geo query response: {query}"
