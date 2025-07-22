"""Demonstrates tools defined via class and @tool decorator."""

import logging
from geo_ai_agent import GeoAIAgent, BedrockAgentCore, BedrockAgentCoreTool
from geo_ai_agent.tools import EchoTool, mcp_status, tool

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    agent = GeoAIAgent()
    agent.register_tool("echo", EchoTool())
    agent.register_tool("status", mcp_status)
    agent.register_tool(
        "bedrock",
        BedrockAgentCoreTool(BedrockAgentCore()),
    )

    logger.info(agent.handle_request("echo", "hi"))
    logger.info(agent.handle_request("status"))
    logger.info(agent.handle_request("bedrock", "process"))


if __name__ == "__main__":
    main()
