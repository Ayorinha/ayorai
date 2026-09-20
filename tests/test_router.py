import pytest

from ayorai.orchestration.router import AgentRouter


def test_router_dispatches_research_agent():
    result = AgentRouter().route("Analyze a document")
    assert result.agent == "research-agent"


def test_router_dispatches_security_agent():
    result = AgentRouter().route("Check this prompt", mode="security")
    assert result.agent == "security-agent"


def test_router_rejects_unknown_mode():
    with pytest.raises(ValueError, match="Unknown agent mode"):
        AgentRouter().route("Analyze a document", mode="unknown")
