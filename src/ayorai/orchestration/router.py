from ayorai.agents.researcher import ResearchAgent
from ayorai.core.types import AgentMessage, AgentResult

class AgentRouter:
    def __init__(self) -> None:
        self.agents = {"research": ResearchAgent()}

    def route(self, task: str) -> AgentResult:
        message = AgentMessage(role="user", content=task)
        return self.agents["research"].run(message)
