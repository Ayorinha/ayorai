from ayorai.agents.base import BaseAgent
from ayorai.core.types import AgentMessage, AgentResult

class ResearchAgent(BaseAgent):
    name = "research-agent"

    def run(self, message: AgentMessage) -> AgentResult:
        return AgentResult(
            agent=self.name,
            output=f"Research task received: {message.content}",
        )
