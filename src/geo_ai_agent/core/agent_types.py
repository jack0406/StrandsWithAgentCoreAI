from enum import Enum, auto


class AgentType(Enum):
    """Enumeration of available agent types."""

    GEO_QUERY = auto()
    BEDROCK = auto()
    MCP_SERVER = auto()
