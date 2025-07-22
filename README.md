# StrandsWithAgentCoreAI

This package provides stub implementations of a Strands agent, a Bedrock
AgentCore, and an MCP server.  Each component is wrapped by a **Tool** so it can
be plugged into a larger agent system.

The entrypoint for the system is a simple `GeoAIAgent` that receives the
initial request and delegates to registered tools.  Additional sub‑agents or
servers can easily be added by registering their tools with the agent.  
Version 2 introduces automatic wrapping so you can register components
directly without manually creating tool wrappers.

## Example
Run the examples to see the tools in action:

```bash
python examples/basic_usage.py

# GeoAI agent demo
python examples/geo_ai_demo.py
```

## Adding new tools

Create a new class implementing the :class:`Tool` interface and register it
with the agent:

```python
from geo_ai_agent import GeoAIAgent, Tool

class MyTool(Tool):
    def run(self, text: str) -> str:
        return text.upper()

agent = GeoAIAgent()
agent.register_tool("upper", MyTool())
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(agent.handle_request("upper", "hello"))  # => HELLO
```

### Integrating sub-agents and servers

You can now register a sub-agent, Bedrock AgentCore, or MCP server directly
with `GeoAIAgent`.  The agent will wrap the component in the appropriate
tool automatically:

```python
from geo_ai_agent import GeoAIAgent, GeoQueryAgent, BedrockAgentCore, MCPServer

agent = GeoAIAgent()
agent.register_tool("geo", GeoQueryAgent())
agent.register_tool("bedrock", BedrockAgentCore())
agent.register_tool("mcp", MCPServer())

agent.handle_request("geo", "hi")      # uses GeoQueryAgent
agent.handle_request("bedrock", "run")  # uses BedrockAgentCore
agent.handle_request("mcp", "status")   # uses MCPServer
```
