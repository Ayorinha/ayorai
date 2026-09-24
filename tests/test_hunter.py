from ayorai.hunter.github import parse_issue_url
from ayorai.hunter.planner import parse_task_spec

def test_parse_issue_url():
    assert parse_issue_url("https://github.com/Ayorinha/ayorai/issues/42") == ("Ayorinha/ayorai", 42)

def test_parse_task_spec():
    spec = parse_task_spec('{"repository":"A/B","issue_number":3,"title":"Fix","objective":"Do it","requirements":["x"],"acceptance_criteria":["y"],"risk":"low","confidence":0.9}', issue_url="https://github.com/A/B/issues/3")
    assert spec.repository == "A/B"
    assert spec.confidence == 0.9
