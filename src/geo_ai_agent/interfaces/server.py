from abc import ABC, abstractmethod


class ServerInterface(ABC):
    """Interface for servers that accept commands."""

    @abstractmethod
    def send_command(self, command: str) -> str:
        """Handle a command and return a result."""
        raise NotImplementedError
