from ayorai.orchestration.pipeline import GovernedPipeline


def test_pipeline_keeps_plan_execution_and_review_history():
    context = GovernedPipeline().execute(
        "Analyze a document", request_id="test-1"
    )
    assert context.request_id == "test-1"
    assert [item.agent for item in context.history] == [
        "planner-agent",
        "research-agent",
        "reviewer-agent",
    ]
