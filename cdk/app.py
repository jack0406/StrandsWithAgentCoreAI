#!/usr/bin/env python3
import aws_cdk as cdk

from agent_stack import AgentStack


app = cdk.App()
AgentStack(app, "AgentStack")
app.synth()
