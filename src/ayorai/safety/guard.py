class SafetyGuard:
    """Deterministic baseline guard; contextual defenses are layered above it."""

    blocked_patterns = (
        "ignore previous instructions",
        "ignore all previous instructions",
        "reveal system prompt",
        "reveal the system prompt",
        "disable safety",
        "bypass safety",
        "developer message",
    )

    def validate(self, text: str) -> bool:
        normalized = " ".join(text.lower().split())
        return not any(pattern in normalized for pattern in self.blocked_patterns)

    def enforce(self, text: str) -> str:
        if not self.validate(text):
            raise ValueError("Safety policy rejected the content.")
        return text
