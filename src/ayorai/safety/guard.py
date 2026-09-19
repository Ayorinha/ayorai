class SafetyGuard:
    """Lightweight deterministic policy gate for agent inputs and outputs."""

    blocked_patterns = (
        "ignore previous instructions",
        "ignore all previous instructions",
        "reveal system prompt",
        "disable safety",
    )

    def validate(self, text: str) -> bool:
        normalized = " ".join(text.lower().split())
        return not any(pattern in normalized for pattern in self.blocked_patterns)

    def enforce(self, text: str) -> str:
        if not self.validate(text):
            raise ValueError("Safety policy rejected the content.")
        return text
