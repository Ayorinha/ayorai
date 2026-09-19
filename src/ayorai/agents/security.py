from ayorai.agents.base import BaseAgent
from ayorai.core.types import AgentMessage, AgentResult
from ayorai.safety.guard import SafetyGuard


class SecurityAgent(BaseAgent):
    name = "security-agent"

    def __init__(self) -> None:
        self.guard = SafetyGuard()

    def run(self, message: AgentMessage) -> AgentResult:
        safe = self.guard.validate(message.content)
        return AgentResult(
            agent=self.name,
            output="Content accepted by security policy." if safe else "Content rejected by security policy.",
            metadata={"task_type": "security", "safe": safe},
            risk="low" if safe else "high",
        )
