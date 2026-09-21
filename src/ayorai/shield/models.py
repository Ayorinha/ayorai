from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(frozen=True)
class ShieldDecision:
    allowed: bool
    risk: RiskLevel
    reason_code: str
    reason: str
    controls: tuple[str, ...] = ()
    metadata: dict[str, Any] = field(default_factory=dict)

    def as_dict(self) -> dict[str, Any]:
        return {
            "allowed": self.allowed,
            "risk": self.risk.value,
            "reason_code": self.reason_code,
            "reason": self.reason,
            "controls": list(self.controls),
            "metadata": dict(self.metadata),
        }
