import pytest

from ayorai.tools.registry import ToolRegistry, ToolSpec


def test_tool_registry_executes_registered_tool():
    registry = ToolRegistry()
    registry.register(ToolSpec("echo", "Echo input", lambda value: value))
    assert registry.execute("echo", value="ok") == "ok"


def test_tool_registry_rejects_duplicate_names():
    registry = ToolRegistry()
    spec = ToolSpec("echo", "Echo input", lambda value: value)
    registry.register(spec)

    with pytest.raises(ValueError, match="already registered"):
        registry.register(spec)


def test_tool_registry_rejects_unknown_tool():
    with pytest.raises(KeyError, match="Unknown tool"):
        ToolRegistry().execute("missing")


def test_tool_registry_returns_sorted_names():
    registry = ToolRegistry()
    registry.register(ToolSpec("zeta", "Z", lambda: None))
    registry.register(ToolSpec("alpha", "A", lambda: None))
    assert registry.names() == ("alpha", "zeta")
