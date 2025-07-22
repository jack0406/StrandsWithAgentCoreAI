"""Interfaces for sub-agents used by the supervisor."""

from abc import ABC, abstractmethod


class SubAgent(ABC):
    """Interface for agents capable of responding to text queries."""

    @abstractmethod
    def respond(self, query: str) -> str:
        """Return a response to the provided query."""
        raise NotImplementedError
