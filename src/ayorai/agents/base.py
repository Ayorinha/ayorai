from abc import ABC, abstractmethod

from ayorai.core.types import AgentMessage, AgentResult


class BaseAgent(ABC):
    name = "base-agent"

    @abstractmethod
    def run(self, message: AgentMessage) -> AgentResult:
        """Execute the agent against an input message."""
        raise NotImplementedError
