from abc import ABC, abstractmethod

class CoreInterface(ABC):
    """Interface for agent cores that execute requests."""

    @abstractmethod
    def execute(self, request: str) -> str:
        """Process a request and return a result."""
        raise NotImplementedError
