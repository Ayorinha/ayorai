from dataclasses import dataclass


@dataclass(frozen=True)
class Detection:
    detected: bool
    rule_id: str | None = None
    category: str | None = None
    reason: str | None = None


class SafetyGuard:
    """Deterministic text-level detection and blocking policy gate."""

    rules = (
        ("PI-001", "prompt_injection", ("ignore previous instructions", "ignore all previous instructions", "ignore your earlier rules", "forget the instructions above"), "Prompt-injection instruction override detected."),
        ("PI-002", "prompt_injection", ("reveal system prompt", "reveal the system prompt", "hidden system message", "internal policy", "confidential instructions"), "Protected instruction extraction detected."),
        ("PI-003", "prompt_injection", ("disable safety", "bypass your policy", "bypass security checks"), "Safety-control bypass attempt detected."),
        ("JB-001", "jailbreak", ("unrestricted agent", "no safety restrictions", "developer mode"), "Jailbreak or policy-bypass language detected."),
        ("TOOL-001", "tool_abuse", ("every available tool", "unapproved mcp tool", "not authorized"), "Unauthorized tool-use request detected."),
        ("RAG-001", "rag_poisoning", ("retrieved document", "retrieved source"), "Potential untrusted RAG instruction detected."),
        ("EXF-001", "data_exfiltration", ("private records", "confidential customer data", "external endpoint"), "Potential unauthorized data exfiltration detected."),
        ("AG-001", "multi_agent", ("impersonate the security agent", "tell the reviewer"), "Multi-agent identity or approval manipulation detected."),
        ("OUT-001", "output_manipulation", ("mark the unsafe operation as approved",), "Output-integrity manipulation detected."),
    )

    def detect(self, text: str) -> Detection:
        normalized = " ".join(text.lower().split())
        for rule_id, category, patterns, reason in self.rules:
            if any(pattern in normalized for pattern in patterns):
                return Detection(True, rule_id, category, reason)
        return Detection(False)

    def validate(self, text: str) -> bool:
        return not self.detect(text).detected

    def enforce(self, text: str) -> str:
        detection = self.detect(text)
        if detection.detected:
            raise ValueError(f"Safety policy rejected the content: {detection.rule_id}")
        return text
