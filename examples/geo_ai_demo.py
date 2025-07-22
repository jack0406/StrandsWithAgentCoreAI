"""Demonstrates integrating GeoAIAgent with agent and server tools."""

from geo_ai_agent import (
    GeoAIAgent,
    StrandsAgent,
    BedrockAgentCore,
    MCPServer,
    StrandsAgentTool,
    BedrockAgentCoreTool,
    MCPServerTool,
)

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    agent = GeoAIAgent()

    # register tools so the agent can route requests
    agent.register_tool("strands", StrandsAgentTool(StrandsAgent()))
    agent.register_tool("bedrock", BedrockAgentCoreTool(BedrockAgentCore()))
    agent.register_tool("mcp", MCPServerTool(MCPServer()))

    logger.info(agent.handle_request("strands", "Hello"))
    logger.info(agent.handle_request("bedrock", "process"))
    logger.info(agent.handle_request("mcp", "command"))


if __name__ == "__main__":
    main()
