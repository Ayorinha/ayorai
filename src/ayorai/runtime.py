from ayorai.core.types import AgentResult
from ayorai.orchestration.router import AgentRouter
from ayorai.safety.audit import AuditEvent, AuditLog
from ayorai.safety.guard import SafetyGuard
from ayorai.safety.risk import RiskEngine

class AyoraiRuntime:
    def __init__(self) -> None:
        self.guard = SafetyGuard()
        self.risk = RiskEngine()
        self.router = AgentRouter()
        self.audit = AuditLog()

    def run(self, task: str, mode: str = "research") -> AgentResult:
        allowed = self.guard.validate(task)
        risk = self.risk.assess(task)
        self.audit.record(
            AuditEvent(
                "input-policy",
                "runtime",
                "validate",
                allowed,
                {"mode": mode, "risk": risk.level, "risk_score": risk.score},
            )
        )
        self.guard.enforce(task)

        result = self.router.route(task, mode=mode)
        output_allowed = self.guard.validate(result.output)
        self.audit.record(
            AuditEvent(
                "output-policy",
                result.agent,
                "validate",
                output_allowed,
                {"risk": risk.level, "risk_score": risk.score},
            )
        )
        self.guard.enforce(result.output)
        return result
