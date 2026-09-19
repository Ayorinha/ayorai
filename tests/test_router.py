from ayorai.orchestration.router import AgentRouter

def test_router_dispatches_research_agent():
    result = AgentRouter().route("Analyze a document")
    assert result.agent == "research-agent"
