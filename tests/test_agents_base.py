from ayorai.agents.base import BaseAgent
from ayorai.core.types import AgentMessage, AgentResult


class EchoAgent(BaseAgent):
    name = "echo-agent"

    def run(self, message: AgentMessage) -> AgentResult:
        return AgentResult(agent=self.name, output=message.content)


def test_base_agent_contract_can_be_implemented():
    result = EchoAgent().run(AgentMessage(role="user", content="hello"))
    assert result.agent == "echo-agent"
    assert result.output == "hello"
