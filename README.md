# StrandsWithAgentCoreAI

This package provides stub implementations of a Strands agent, a Bedrock
AgentCore, and an MCP server.  Each component is wrapped by a **Tool** so it can
be plugged into a larger agent system.

The entrypoint for the system is a simple `GeoAIAgent` that receives the
initial request and delegates to registered tools.  Additional sub‑agents or
servers can easily be added by registering their tools with the agent.

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
from strands_with_agent_core_ai import GeoAIAgent, Tool

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
