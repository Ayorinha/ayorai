from ayorai.agents.base import BaseAgent
from ayorai.core.types import AgentMessage, AgentResult


class ReviewerAgent(BaseAgent):
    name = "reviewer-agent"

    def run(self, message: AgentMessage) -> AgentResult:
        return AgentResult(
            agent=self.name,
            output=f"Review completed for: {message.content}",
            metadata={"task_type": "review", "reviewed": True},
        )
