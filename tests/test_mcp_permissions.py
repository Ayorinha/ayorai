import pytest

from ayorai.mcp.adapter import SafeMCPAdapter

def test_mcp_denies_unapproved_tool():
    adapter = SafeMCPAdapter({"search"})
    with pytest.raises(PermissionError):
        adapter.call("shell", {"command": "id"})

def test_mcp_allows_explicit_tool():
    adapter = SafeMCPAdapter({"search"})
    assert adapter.call("search", {"query": "ai"})["tool"] == "search"
