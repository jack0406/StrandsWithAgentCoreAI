from .base import Tool
from ..agents.sub_agents import StrandsAgent
import logging

logger = logging.getLogger(__name__)


class StrandsAgentTool(Tool):
    """Tool wrapper for a Strands Agent."""

    def __init__(self, agent: StrandsAgent) -> None:
        self.agent = agent

    def run(self, query: str) -> str:
        logger.debug("StrandsAgentTool received query: %s", query)
        return self.agent.respond(query)
