from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class TaskSpec:
    issue_url: str
    repository: str
    issue_number: int
    title: str
    objective: str
    requirements: list[str] = field(default_factory=list)
    acceptance_criteria: list[str] = field(default_factory=list)
    risk: str = "unknown"
    confidence: float = 0.0

    def to_dict(self) -> dict[str, Any]:
        return self.__dict__.copy()
