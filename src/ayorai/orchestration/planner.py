from ayorai.agents.planner import PlannerAgent
from ayorai.core.types import AgentMessage, AgentResult


class ExecutionPlanner:
    def __init__(self) -> None:
        self.agent = PlannerAgent()

    def plan(self, task: str) -> AgentResult:
        return self.agent.run(AgentMessage(role="user", content=task))
