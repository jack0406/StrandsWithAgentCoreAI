from .base import Tool
from ..bedrock_core import BedrockAgentCore
import logging

logger = logging.getLogger(__name__)


class BedrockAgentCoreTool(Tool):
    """Tool wrapper for Bedrock AgentCore."""

    def __init__(self, core: BedrockAgentCore) -> None:
        self.core = core

    def run(self, request: str) -> str:
        """Forward the request to the underlying Bedrock agent."""
        logger.debug("BedrockAgentCoreTool running request: %s", request)
        return self.core.execute(request)
