from .interfaces import AgentInterface


class StrandsAgent(AgentInterface):
    """Simplified stub for Strands Agent.

    This agent simply echoes the query it receives.  It can be replaced with a
    more capable implementation without changing the surrounding infrastructure.
    """

    def respond(self, query: str) -> str:
        """Pretend to respond to a query."""
        return f"Strands response: {query}"
