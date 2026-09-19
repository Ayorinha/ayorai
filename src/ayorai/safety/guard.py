class SafetyGuard:
    """Minimal policy gate for agent inputs and outputs."""

    blocked_patterns = ("ignore previous instructions",)

    def validate(self, text: str) -> bool:
        normalized = text.lower()
        return not any(pattern in normalized for pattern in self.blocked_patterns)
