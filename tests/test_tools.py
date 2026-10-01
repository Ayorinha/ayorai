import pytest

from ayorai.shield.engine import ShieldEngine
from ayorai.tools.registry import ToolRegistry, ToolSpec


def test_tool_registry_executes_registered_tool():
    registry = ToolRegistry()
    registry.register(ToolSpec("echo", "Echo input", lambda value: value))
    assert registry.execute("echo", value="ok") == "ok"


def test_tool_registry_enforces_allowlist():
    registry = ToolRegistry(ShieldEngine({"echo"}))
    registry.register(ToolSpec("echo", "Echo input", lambda value: value))
    assert registry.execute("echo", value="ok") == "ok"


def test_tool_registry_rejects_unauthorized_execution():
    registry = ToolRegistry(ShieldEngine())
    registry.register(ToolSpec("echo", "Echo input", lambda value: value))
    with pytest.raises(PermissionError, match="explicit allowlist"):
        registry.execute("echo", value="blocked")


def test_tool_registry_rejects_duplicate_registration():
    registry = ToolRegistry()
    registry.register(ToolSpec("echo", "Echo input", lambda value: value))
    with pytest.raises(ValueError, match="already registered"):
        registry.register(ToolSpec("echo", "Duplicate", lambda value: value))


def test_tool_registry_rejects_unknown_execution():
    registry = ToolRegistry()
    with pytest.raises(KeyError, match="Unknown tool"):
        registry.execute("missing")


def test_tool_registry_returns_sorted_names():
    registry = ToolRegistry()
    registry.register(ToolSpec("zeta", "Z", lambda: None))
    registry.register(ToolSpec("alpha", "A", lambda: None))
    assert registry.names() == ("alpha", "zeta")


def test_tool_registry_detects_definition_drift():
    shield = ShieldEngine({"echo"})
    registry = ToolRegistry(shield)
    registry.register(ToolSpec("echo", "Echo input", lambda value: value))
    registry._tools["echo"] = ToolSpec("echo", "Changed", lambda value: value)
    with pytest.raises(PermissionError, match="Trusted tool metadata changed"):
        registry.execute("echo", value="blocked")
