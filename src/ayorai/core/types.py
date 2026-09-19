from dataclasses import dataclass, field
from typing import Any

@dataclass
class AgentMessage:
    role: str
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class AgentResult:
    agent: str
    output: str
    metadata: dict[str, Any] = field(default_factory=dict)
