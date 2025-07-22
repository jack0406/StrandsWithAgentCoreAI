from abc import ABC, abstractmethod

class AgentInterface(ABC):
    """Interface for agents capable of responding to text queries."""

    @abstractmethod
    def respond(self, query: str) -> str:
        """Return a response to the provided query."""
        raise NotImplementedError
