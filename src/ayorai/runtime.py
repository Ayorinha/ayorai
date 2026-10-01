from ayorai.core.types import AgentResult
from ayorai.orchestration.router import AgentRouter
from ayorai.safety.audit import AuditEvent, AuditLog
from ayorai.safety.guard import SafetyGuard
from ayorai.shield.engine import ShieldEngine


class AyoraiRuntime:
    """Runtime entry point enforcing the same Shield policy at trust boundaries."""

    def __init__(self, *, allowed_tools: tuple[str, ...] = ()) -> None:
        self.shield = ShieldEngine(allowed_tools)
        self.guard = SafetyGuard()
        self.router = AgentRouter()
        self.audit = AuditLog()

    def run(self, task: str, mode: str = "research") -> AgentResult:
        input_decision = self.shield.inspect_text(task, source="runtime-input")
        self.audit.record(
            AuditEvent(
                "input-policy",
                "runtime",
                "inspect",
                input_decision.allowed,
                {"mode": mode, "reason_code": input_decision.reason_code},
            )
        )
        if not input_decision.allowed:
            raise ValueError(input_decision.reason)

        self.guard.enforce(task)
        result = self.router.route(task, mode=mode)

        output_decision = self.shield.inspect_text(result.output, source="runtime-output")
        self.audit.record(
            AuditEvent(
                "output-policy",
                result.agent,
                "inspect",
                output_decision.allowed,
                {"reason_code": output_decision.reason_code},
            )
        )
        if not output_decision.allowed:
            raise ValueError(output_decision.reason)

        self.guard.enforce(result.output)
        return result
