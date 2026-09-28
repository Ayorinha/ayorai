import pytest

from ayorai.core.types import AgentMessage, AgentResult, ExecutionContext


def test_agent_message_and_result_defaults():
    message = AgentMessage(role="user", content="hello")
    result = AgentResult(agent="test-agent", output="ok")

    assert message.metadata == {}
    assert result.metadata == {}
    assert result.risk == "low"


def test_execution_context_defaults_and_history():
    context = ExecutionContext(request_id="req-1")
    context.history.append(AgentResult(agent="test-agent", output="ok"))

    assert context.metadata == {}
    assert len(context.history) == 1


def test_frozen_agent_message_rejects_mutation():
    message = AgentMessage(role="user", content="hello")

    with pytest.raises((AttributeError, TypeError)):
        message.content = "changed"
