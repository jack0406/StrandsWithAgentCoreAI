from abc import ABC, abstractmethod


class Tool(ABC):
    """Base interface for all tools."""

    @abstractmethod
    def run(self, *args, **kwargs):
        """Execute the tool and return a string result."""
        raise NotImplementedError
