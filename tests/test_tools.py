from ayorai.tools.registry import ToolRegistry, ToolSpec

def test_tool_registry_executes_registered_tool():
    registry = ToolRegistry()
    registry.register(ToolSpec("echo", "Echo input", lambda value: value))
    assert registry.execute("echo", value="ok") == "ok"


def test_tool_registry_rejects_duplicate_registration():
    registry = ToolRegistry()
    registry.register(ToolSpec("echo", "Echo input", lambda value: value))
    try:
        registry.register(ToolSpec("echo", "Duplicate", lambda value: value))
    except ValueError as exc:
        assert "already registered" in str(exc)
    else:
        raise AssertionError("duplicate registration should fail")


def test_tool_registry_rejects_unknown_execution():
    registry = ToolRegistry()
    try:
        registry.execute("missing")
    except KeyError as exc:
        assert "Unknown tool" in str(exc)
    else:
        raise AssertionError("unknown tool should fail")


def test_tool_registry_returns_sorted_names():
    registry = ToolRegistry()
    registry.register(ToolSpec("zeta", "Z", lambda: None))
    registry.register(ToolSpec("alpha", "A", lambda: None))
    assert registry.names() == ("alpha", "zeta")
