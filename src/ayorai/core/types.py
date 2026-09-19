from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class AgentMessage:
    role: str
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class AgentResult:
    agent: str
    output: str
    metadata: dict[str, Any] = field(default_factory=dict)
    risk: str = "low"

@dataclass
class ExecutionContext:
    request_id: str
    metadata: dict[str, Any] = field(default_factory=dict)
    history: list[AgentResult] = field(default_factory=list)
