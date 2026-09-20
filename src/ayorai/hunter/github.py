import json
import os
import re
import urllib.request

ISSUE_RE = re.compile(r"github\\.com/([^/]+)/([^/]+)/issues/(\\d+)")

def parse_issue_url(url: str) -> tuple[str, int]:
    match = ISSUE_RE.search(url)
    if not match:
        raise ValueError("Expected a public GitHub issue URL")
    return f"{match.group(1)}/{match.group(2)}", int(match.group(3))

def fetch_issue(repository: str, issue_number: int) -> dict:
    token = os.getenv("GITHUB_TOKEN")
    url = f"https://api.github.com/repos/{repository}/issues/{issue_number}"
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "ayorai-hunter"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))
