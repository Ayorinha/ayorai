from ayorai.agents.base import BaseAgent
from ayorai.core.types import AgentMessage, AgentResult

class AnalystAgent(BaseAgent):
    name = "analyst-agent"

    def run(self, message: AgentMessage) -> AgentResult:
        return AgentResult(
            agent=self.name,
            output=f"Analysis task received: {message.content}",
            metadata={"task_type": "analysis"},
        )
