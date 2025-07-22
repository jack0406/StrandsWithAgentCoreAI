import sys, os
sys.path.insert(0, os.path.abspath("cdk"))
import pytest

aws_cdk = pytest.importorskip("aws_cdk", reason="aws_cdk not installed")

from agent_stack import AgentStack
from aws_cdk import App


def test_stack_synth():
    app = App()
    stack = AgentStack(app, "TestStack")
    assembly = app.synth()
    template = assembly.get_stack_by_name("TestStack").template
    assert "Resources" in template

