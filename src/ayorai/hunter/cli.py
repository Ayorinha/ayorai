import argparse
import json
from .github import fetch_issue, parse_issue_url
from .openai_client import OpenAIResponsesClient
from .planner import build_task_prompt, parse_task_spec

def main() -> int:
    parser = argparse.ArgumentParser(description="AYORAI Hunter task analyzer")
    parser.add_argument("issue_url")
    parser.add_argument("--model", default=None)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    repository, issue_number = parse_issue_url(args.issue_url)
    issue = fetch_issue(repository, issue_number)
    prompt = build_task_prompt(args.issue_url, issue.get("title", ""), issue.get("body") or "", repository, issue_number)
    raw = OpenAIResponsesClient(args.model).respond(prompt)
    spec = parse_task_spec(raw, issue_url=args.issue_url)
    print(json.dumps(spec.to_dict(), indent=2, ensure_ascii=False) if args.json else spec.to_dict())
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
