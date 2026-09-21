from dataclasses import dataclass

@dataclass(frozen=True)
class RiskAssessment:
    level: str
    score: int
    reasons: tuple[str, ...]

class RiskEngine:
    """Small deterministic risk layer; model-based scoring can be added later."""

    HIGH_IMPACT_TERMS = (
        "delete", "transfer", "wire", "send", "publish", "execute",
        "admin", "credential", "password", "secret", "production",
    )

    def assess(self, text: str) -> RiskAssessment:
        normalized = " ".join(text.lower().split())
        reasons: list[str] = []
        score = 0
        for term in self.HIGH_IMPACT_TERMS:
            if term in normalized:
                score += 10
                reasons.append(f"high-impact:{term}")
        if score >= 30:
            level = "high"
        elif score >= 10:
            level = "medium"
        else:
            level = "low"
        return RiskAssessment(level, min(score, 100), tuple(reasons))
