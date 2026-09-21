from dataclasses import dataclass
from enum import Enum
from typing import Any

from ayorai.shield.models import RiskLevel, ShieldDecision


class AssetSensitivity(str, Enum):
    PUBLIC = "public"
    INTERNAL = "internal"
    SENSITIVE = "sensitive"
    RESTRICTED = "restricted"


@dataclass(frozen=True)
class ProtectedAction:
    action: str
    asset: str
    sensitivity: AssetSensitivity
    impact: RiskLevel
    metadata: dict[str, Any] | None = None


class HighImpactActionGuard:
    """Adds explicit authorization gates around sensitive or high-impact actions."""

    def evaluate(self, action: ProtectedAction, *, human_approval: bool = False) -> ShieldDecision:
        requires_approval = (
            action.sensitivity in {AssetSensitivity.SENSITIVE, AssetSensitivity.RESTRICTED}
            or action.impact in {RiskLevel.HIGH, RiskLevel.CRITICAL}
        )
        if requires_approval and not human_approval:
            return ShieldDecision(
                allowed=False,
                risk=action.impact,
                reason_code="HIGH_IMPACT_APPROVAL_REQUIRED",
                reason="High-impact action requires an explicit approval signal.",
                controls=("least-privilege", "human-approval", "sensitive-data-boundary"),
                metadata={"action": action.action, "asset": action.asset},
            )
        return ShieldDecision(
            allowed=True,
            risk=action.impact,
            reason_code="ALLOW_APPROVED_ACTION",
            reason="Action satisfies the configured approval policy.",
            controls=("least-privilege", "sensitive-data-boundary"),
            metadata={"action": action.action, "asset": action.asset},
        )
