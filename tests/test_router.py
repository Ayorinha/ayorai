from ayorai.orchestration.router import AgentRouter


def test_router_dispatches_research_agent():
    result = AgentRouter().route("Analyze a document")
    assert result.agent == "research-agent"

def test_router_dispatches_security_agent():
    result = AgentRouter().route("Check this prompt", mode="security")
    assert result.agent == "security-agent"
