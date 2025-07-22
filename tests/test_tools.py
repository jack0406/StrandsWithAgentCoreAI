import sys, os
sys.path.insert(0, os.path.abspath("src"))
import pytest

from geo_ai_agent import (
    GeoAIAgent,
    GeoQueryAgent,
    BedrockAgentCore,
    MCPServer,
    StrandsAgent,
)
from geo_ai_agent.tools import EchoTool, mcp_status


def test_echo_tool():
    tool = EchoTool()
    assert tool.run("ping") == "Echo: ping"


def test_mcp_status():
    # mcp_status returns a string from MCPServer stub
    assert "MCP server executed" in mcp_status.run()


def test_agent_integration():
    agent = GeoAIAgent()
    agent.register_tool("echo", EchoTool())
    agent.register_tool("status", mcp_status)

    assert agent.handle_request("echo", "hi") == "Echo: hi"
    res = agent.handle_request("status")
    assert "MCP server executed" in res


def test_auto_wrapping():
    agent = GeoAIAgent()
    agent.register_tool("geo", GeoQueryAgent())
    agent.register_tool("bedrock", BedrockAgentCore())
    agent.register_tool("mcp", MCPServer())
    agent.register_tool("strands", StrandsAgent())

    assert "Geo query response" in agent.handle_request("geo", "x")
    assert "Bedrock executed" in agent.handle_request("bedrock", "cmd")
    assert "MCP server executed" in agent.handle_request("mcp", "cmd")
    assert "Strands response" in agent.handle_request("strands", "y")

