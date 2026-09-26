import hashlib
import re
from collections.abc import Iterable

from ayorai.shield.models import RiskLevel, ShieldDecision


class ShieldEngine:
    """Deterministic policy layer for agent, tool and memory security checks.

    This is a control-plane foundation, not a claim of complete runtime security.
    Rules are intentionally inspectable and testable so deployments can add
    model-assisted detectors without replacing the enforcement boundary.
    """

    _INJECTION_PATTERNS = (
        "ignore previous instructions",
        "ignore all previous instructions",
        "reveal system prompt",
        "disable safety",
        "bypass security",
    )
    _SECRET_PATTERNS = (
        re.compile(r"(?:sk|pk)-[A-Za-z0-9_-]{20,}"),
        re.compile(r"(?i)bearer\\s+[A-Za-z0-9._~+/-]{20,}"),
    )

    def __init__(self, allowed_tools: Iterable[str] = ()) -> None:
        self.allowed_tools = frozenset(allowed_tools)
        self._trusted_tool_fingerprints: dict[str, str] = {}

    def inspect_text(self, text: str, *, source: str = "unknown") -> ShieldDecision:
        normalized = " ".join(text.lower().split())
        for pattern in self._INJECTION_PATTERNS:
            if pattern in normalized:
                return ShieldDecision(
                    allowed=False,
                    risk=RiskLevel.HIGH,
                    reason_code="ASI01_GOAL_HIJACKING",
                    reason="Potential instruction-hierarchy manipulation detected.",
                    controls=("input-boundary", "policy-enforcement"),
                    metadata={"source": source},
                )
        for pattern in self._SECRET_PATTERNS:
            if pattern.search(text):
                return ShieldDecision(
                    allowed=False,
                    risk=RiskLevel.HIGH,
                    reason_code="SENSITIVE_DATA_EXPOSURE",
                    reason="Potential credential material detected at a trust boundary.",
                    controls=("data-loss-prevention", "output-boundary"),
                    metadata={"source": source},
                )
        return ShieldDecision(
            allowed=True,
            risk=RiskLevel.LOW,
            reason_code="ALLOW",
            reason="No configured text policy violation detected.",
            controls=("input-boundary",),
            metadata={"source": source},
        )

    def authorize_tool(self, tool: str) -> ShieldDecision:
        if tool not in self.allowed_tools:
            return ShieldDecision(
                allowed=False,
                risk=RiskLevel.HIGH,
                reason_code="ASI02_TOOL_MISUSE",
                reason=f"Tool is not present in the explicit allowlist: {tool}.",
                controls=("least-privilege", "tool-allowlist"),
                metadata={"tool": tool},
            )
        return ShieldDecision(
            allowed=True,
            risk=RiskLevel.LOW,
            reason_code="ALLOW",
            reason="Tool is explicitly authorized.",
            controls=("least-privilege", "tool-allowlist"),
            metadata={"tool": tool},
        )

    def register_tool_definition(self, tool: str, description: str) -> str:
        """Register a canonical fingerprint for later MCP metadata drift checks."""
        fingerprint = self.fingerprint_tool_definition(tool, description)
        self._trusted_tool_fingerprints[tool] = fingerprint
        return fingerprint

    def inspect_tool_definition(self, tool: str, description: str) -> ShieldDecision:
        fingerprint = self.fingerprint_tool_definition(tool, description)
        trusted = self._trusted_tool_fingerprints.get(tool)
        if trusted is not None and trusted != fingerprint:
            return ShieldDecision(
                allowed=False,
                risk=RiskLevel.HIGH,
                reason_code="ASI04_SUPPLY_CHAIN_VULNERABILITY",
                reason="Trusted tool metadata changed after its security baseline was recorded.",
                controls=("tool-integrity", "supply-chain-boundary"),
                metadata={"tool": tool, "fingerprint": fingerprint},
            )
        return ShieldDecision(
            allowed=True,
            risk=RiskLevel.LOW,
            reason_code="ALLOW",
            reason="Tool metadata matches the current security baseline.",
            controls=("tool-integrity",),
            metadata={"tool": tool, "fingerprint": fingerprint},
        )

    def inspect_memory_write(self, content: str, *, trusted: bool = False) -> ShieldDecision:
        if trusted:
            return ShieldDecision(
                allowed=True,
                risk=RiskLevel.LOW,
                reason_code="ALLOW_TRUSTED_MEMORY",
                reason="Memory write originates from an explicitly trusted source.",
                controls=("memory-trust-boundary",),
            )
        decision = self.inspect_text(content, source="memory-write")
        if not decision.allowed:
            return ShieldDecision(
                allowed=False,
                risk=RiskLevel.HIGH,
                reason_code="ASI06_MEMORY_POISONING",
                reason="Untrusted memory content matched a configured safety rule.",
                controls=("memory-trust-boundary", "policy-enforcement"),
            )
        return ShieldDecision(
            allowed=False,
            risk=RiskLevel.MEDIUM,
            reason_code="UNTRUSTED_MEMORY_WRITE",
            reason="Memory writes require an explicit trust decision before persistence.",
            controls=("memory-trust-boundary",),
        )

    @staticmethod
    def fingerprint_tool_definition(tool: str, description: str) -> str:
        canonical = f"{tool}\\n{description}".encode("utf-8")
        return hashlib.sha256(canonical).hexdigest()
