from .interfaces import CoreInterface


class BedrockAgentCore(CoreInterface):
    """Simplified stub for Bedrock AgentCore.

    In a real application this would contain the business logic for the
    Bedrock agent.  Here it simply echoes the request so other components can be
    wired together during development.
    """

    def execute(self, request: str) -> str:
        """Pretend to process a request and return a response."""
        return f"Bedrock executed: {request}"
