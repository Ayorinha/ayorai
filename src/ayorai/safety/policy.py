from dataclasses import dataclass


@dataclass(frozen=True)
class PolicyDecision:
    allowed: bool
    reason: str
    risk: str = "low"

class PolicyEngine:
    def evaluate(self, text: str) -> PolicyDecision:
        normalized = " ".join(text.lower().split())
        if "ignore previous instructions" in normalized or "disable safety" in normalized:
            return PolicyDecision(False, "Prompt injection pattern detected.", "high")
        return PolicyDecision(True, "No blocked policy pattern detected.")
