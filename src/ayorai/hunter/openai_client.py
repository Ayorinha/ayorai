import json
import os
import urllib.request

class OpenAIResponsesClient:
    def __init__(self, model: str | None = None) -> None:
        self.model = model or os.getenv("AYORAI_OPENAI_MODEL", "gpt-5.6-mini")
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise RuntimeError("OPENAI_API_KEY is required")

    def respond(self, prompt: str) -> str:
        payload = json.dumps({"model": self.model, "input": prompt}).encode("utf-8")
        request = urllib.request.Request("https://api.openai.com/v1/responses", data=payload, headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(request, timeout=90) as response:
            body = json.loads(response.read().decode("utf-8"))
        if body.get("output_text"):
            return str(body["output_text"])
        for item in body.get("output", []):
            for content in item.get("content", []):
                if content.get("text"):
                    return str(content["text"])
        raise RuntimeError("Responses API returned no text output")
