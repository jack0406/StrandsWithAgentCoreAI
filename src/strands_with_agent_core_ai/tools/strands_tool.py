from .base import Tool
from ..strands_agent import StrandsAgent
import logging

logger = logging.getLogger(__name__)


class StrandsAgentTool(Tool):
    """Tool wrapper for a Strands Agent."""

    def __init__(self, agent: StrandsAgent) -> None:
        self.agent = agent

    def run(self, query: str) -> str:
        """Pass the query through to the Strands agent."""
        logger.debug("StrandsAgentTool received query: %s", query)
        return self.agent.respond(query)
