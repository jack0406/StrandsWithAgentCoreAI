"""Example showing individual tools in isolation."""

from geo_ai_agent import (
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
    strands_tool = StrandsAgentTool(StrandsAgent())
    bedrock_tool = BedrockAgentCoreTool(BedrockAgentCore())
    mcp_tool = MCPServerTool(MCPServer())

    logger.info(strands_tool.run("Hello"))
    logger.info(bedrock_tool.run("process"))
    logger.info(mcp_tool.run("command"))


if __name__ == "__main__":
    main()
