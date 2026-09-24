from dataclasses import dataclass

from ayorai.safety.guard import SafetyGuard


@dataclass(frozen=True)
class PolicyDecision:
    allowed: bool
    reason: str
    risk: str = "low"


class PolicyEngine:
    """Policy decision layer backed by the same deterministic guard rules."""

    def __init__(self, guard: SafetyGuard | None = None) -> None:
        self.guard = guard or SafetyGuard()

    def evaluate(self, text: str) -> PolicyDecision:
        if not self.guard.validate(text):
            return PolicyDecision(False, "Prompt injection pattern detected.", "high")
        return PolicyDecision(True, "No blocked policy pattern detected.")
