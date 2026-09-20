import json
from typing import Any
from .models import TaskSpec

SYSTEM_PROMPT = """You are AYORAI Hunter, a cautious software-engineering agent.
Turn a GitHub issue into an executable task specification. Do not invent requirements.
Return JSON only with repository, issue_number, title, objective, requirements,
acceptance_criteria, risk, confidence. Confidence must be 0..1 and risk must be
low, medium, high, or unknown. Lower confidence when the issue is ambiguous.
"""

def build_task_prompt(issue_url: str, issue_title: str, issue_body: str, repository: str, issue_number: int) -> str:
    return SYSTEM_PROMPT + "\nIssue URL: {}\nRepository: {}\nIssue: #{}\nTitle: {}\n\nBody:\n{}".format(issue_url, repository, issue_number, issue_title, issue_body)

def parse_task_spec(payload: str, *, issue_url: str) -> TaskSpec:
    data: dict[str, Any] = json.loads(payload)
    confidence = float(data.get("confidence", 0.0))
    if not 0.0 <= confidence <= 1.0:
        raise ValueError("confidence must be between 0 and 1")
    risk = str(data.get("risk", "unknown")).lower()
    if risk not in {"low", "medium", "high", "unknown"}:
        raise ValueError("invalid risk")
    return TaskSpec(issue_url=issue_url, repository=str(data["repository"]), issue_number=int(data["issue_number"]), title=str(data["title"]), objective=str(data["objective"]), requirements=[str(x) for x in data.get("requirements", [])], acceptance_criteria=[str(x) for x in data.get("acceptance_criteria", [])], risk=risk, confidence=confidence)
