from aws_cdk import (
    Stack,
    aws_iam as iam,
)
from constructs import Construct


class AgentStack(Stack):
    """CDK stack provisioning the Bedrock agent and roles."""

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Role assumed by Bedrock to execute the agent
        agent_role = iam.Role(
            self,
            "AgentRole",
            assumed_by=iam.ServicePrincipal("bedrock.amazonaws.com"),
        )
        agent_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AmazonBedrockFullAccess")
        )

        # Role for external clients to invoke the agent
        client_role = iam.Role(
            self,
            "ClientRole",
            assumed_by=iam.AccountPrincipal(self.account),
        )
        client_role.add_to_policy(
            iam.PolicyStatement(
                actions=["bedrock:InvokeModel"],
                resources=["*"],
            )
        )

        self.agent_role = agent_role
        self.client_role = client_role
