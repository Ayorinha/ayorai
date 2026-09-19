from ayorai.core.types import AgentResult
from ayorai.orchestration.router import AgentRouter
from ayorai.safety.audit import AuditEvent, AuditLog
from ayorai.safety.guard import SafetyGuard

class AyoraiRuntime:
    def __init__(self) -> None:
        self.guard = SafetyGuard()
        self.router = AgentRouter()
        self.audit = AuditLog()

    def run(self, task: str, mode: str = "research") -> AgentResult:
        allowed = self.guard.validate(task)
        self.audit.record(
            AuditEvent("input-policy", "runtime", "validate", allowed, {"mode": mode})
        )
        self.guard.enforce(task)

        result = self.router.route(task, mode=mode)
        output_allowed = self.guard.validate(result.output)
        self.audit.record(
            AuditEvent("output-policy", result.agent, "validate", output_allowed)
        )
        self.guard.enforce(result.output)
        return result
