"""Demonstration of the geo_ai_agent package."""

import logging

from .agents import GeoAIAgent, GeoQueryAgent
from .core import BedrockAgentCore, MCPServer, configure_logging
from .tools import SubAgentTool, BedrockAgentCoreTool, MCPServerTool


def main() -> None:
    configure_logging(logging.INFO)
    agent = GeoAIAgent()

    agent.register_tool("geo_query", SubAgentTool(GeoQueryAgent()))
    agent.register_tool("bedrock", BedrockAgentCoreTool(BedrockAgentCore()))
    agent.register_tool("mcp", MCPServerTool(MCPServer()))

    logging.getLogger(__name__).info(agent.handle_request("geo_query", "Hello"))
    logging.getLogger(__name__).info(agent.handle_request("bedrock", "process"))
    logging.getLogger(__name__).info(agent.handle_request("mcp", "command"))


if __name__ == "__main__":
    main()
