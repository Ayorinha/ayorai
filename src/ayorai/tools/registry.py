from dataclasses import dataclass
from typing import Any, Callable

from ayorai.shield.engine import ShieldEngine


@dataclass(frozen=True)
class ToolSpec:
    name: str
    description: str
    handler: Callable[..., Any]


class ToolRegistry:
    """Tool execution registry with an optional mandatory Shield boundary."""

    def __init__(self, shield: ShieldEngine | None = None) -> None:
        self._tools: dict[str, ToolSpec] = {}
        self._shield = shield

    def register(self, spec: ToolSpec) -> None:
        if spec.name in self._tools:
            raise ValueError(f"Tool already registered: {spec.name}")
        if self._shield is not None:
            decision = self._shield.inspect_tool_definition(spec.name, spec.description)
            if not decision.allowed and decision.reason_code != "ALLOW":
                raise PermissionError(decision.reason)
            self._shield.register_tool_definition(spec.name, spec.description)
        self._tools[spec.name] = spec

    def execute(self, name: str, **kwargs: Any) -> Any:
        if name not in self._tools:
            raise KeyError(f"Unknown tool: {name}")
        if self._shield is not None:
            decision = self._shield.authorize_tool(name)
            if not decision.allowed:
                raise PermissionError(decision.reason)
            spec = self._tools[name]
            integrity = self._shield.inspect_tool_definition(spec.name, spec.description)
            if not integrity.allowed:
                raise PermissionError(integrity.reason)
        return self._tools[name].handler(**kwargs)

    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._tools))
