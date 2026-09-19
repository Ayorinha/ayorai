from ayorai.agents.base import BaseAgent
from ayorai.core.types import AgentMessage, AgentResult


class PlannerAgent(BaseAgent):
    name = "planner-agent"

    def run(self, message: AgentMessage) -> AgentResult:
        return AgentResult(
            agent=self.name,
            output=f"Plan created for: {message.content}",
            metadata={"task_type": "planning", "steps": ["research", "analysis", "review"]},
        )
