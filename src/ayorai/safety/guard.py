import re


class SafetyGuard:
    """Lightweight deterministic policy gate for agent inputs and outputs."""

    blocked_patterns = (
        "ignore previous instructions",
        "ignore all previous instructions",
        "reveal system prompt",
        "disable safety",
    )

    @staticmethod
    def normalize(text: str) -> str:
        """Normalize whitespace and punctuation for deterministic matching."""
        normalized = re.sub(r"[^a-z0-9]+", " ", text.lower())
        return " ".join(normalized.split())

    def validate(self, text: str) -> bool:
        normalized = self.normalize(text)
        return not any(pattern in normalized for pattern in self.blocked_patterns)

    def enforce(self, text: str) -> str:
        if not self.validate(text):
            raise ValueError("Safety policy rejected the content.")
        return text
