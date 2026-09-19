from abc import ABC, abstractmethod
from typing import Any

class MCPAdapter(ABC):
    @abstractmethod
    def call(self, tool: str, arguments: dict[str, Any]) -> Any:
        raise NotImplementedError

class SafeMCPAdapter(MCPAdapter):
    def __init__(self, allowed_tools: set[str] | None = None) -> None:
        self.allowed_tools = allowed_tools or set()

    def call(self, tool: str, arguments: dict[str, Any]) -> dict[str, Any]:
        if tool not in self.allowed_tools:
            raise PermissionError(f"Tool not allowed: {tool}")
        return {"tool": tool, "arguments": arguments}
