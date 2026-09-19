from ayorai.tools.registry import ToolRegistry, ToolSpec

def test_tool_registry_executes_registered_tool():
    registry = ToolRegistry()
    registry.register(ToolSpec("echo", "Echo input", lambda value: value))
    assert registry.execute("echo", value="ok") == "ok"
