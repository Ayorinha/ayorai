from ayorai.agents.analyst import AnalystAgent
from ayorai.agents.researcher import ResearchAgent
from ayorai.agents.reviewer import ReviewerAgent
from ayorai.agents.security import SecurityAgent
from ayorai.core.types import AgentMessage, AgentResult


class AgentRouter:
    def __init__(self) -> None:
        self.agents = {
            "research": ResearchAgent(),
            "analysis": AnalystAgent(),
            "security": SecurityAgent(),
            "review": ReviewerAgent(),
        }

    def route(self, task: str, mode: str = "research") -> AgentResult:
        if mode not in self.agents:
            raise ValueError(f"Unknown agent mode: {mode}")
        return self.agents[mode].run(AgentMessage(role="user", content=task))
