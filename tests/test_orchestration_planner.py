from ayorai.orchestration.planner import ExecutionPlanner


def test_execution_planner_returns_agent_result():
    result = ExecutionPlanner().plan("Analyze a document")

    assert result.agent == "planner-agent"
    assert "Analyze a document" in result.output
    assert result.metadata["task_type"] == "planning"
