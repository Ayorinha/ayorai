from ayorai.orchestration.router import AgentRouter
from ayorai.safety.guard import SafetyGuard
from ayorai.core.types import AgentResult

class AyoraiRuntime:
    def __init__(self) -> None:
        self.guard = SafetyGuard()
        self.router = AgentRouter()

    def run(self, task: str, mode: str = "research") -> AgentResult:
        self.guard.enforce(task)
        result = self.router.route(task, mode=mode)
        self.guard.enforce(result.output)
        return result
