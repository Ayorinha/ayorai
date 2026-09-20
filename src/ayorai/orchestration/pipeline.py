from ayorai.agents.reviewer import ReviewerAgent
from ayorai.core.types import AgentMessage, ExecutionContext
from ayorai.orchestration.planner import ExecutionPlanner
from ayorai.orchestration.router import AgentRouter


class GovernedPipeline:
    """Deterministic plan -> route -> review execution flow."""

    def __init__(self) -> None:
        self.planner = ExecutionPlanner()
        self.router = AgentRouter()
        self.reviewer = ReviewerAgent()

    def execute(
        self,
        task: str,
        mode: str = "research",
        request_id: str = "local",
    ) -> ExecutionContext:
        context = ExecutionContext(request_id=request_id)
        plan = self.planner.plan(task)
        context.history.append(plan)

        result = self.router.route(task, mode=mode)
        context.history.append(result)

        review = self.reviewer.run(
            AgentMessage(role="agent", content=result.output)
        )
        context.history.append(review)
        return context
