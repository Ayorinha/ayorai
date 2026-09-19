# AYORAI — Agentic Intelligence & AI Safety

AYORAI is an applied AI engineering framework for modular agentic systems with explicit orchestration, safety controls, memory, RAG, MCP and tool governance.

## Engineering goals
- deterministic agent contracts
- multi-agent orchestration
- prompt-injection and policy defenses
- auditable execution context
- retrieval and tool interfaces without vendor lock-in
- automated tests and CI
- offline document intelligence for sensitive workflows

## Offline OCR API

The repository now includes the foundation for a **Windows-first, local-only OCR API**. The HTTP layer is Python/FastAPI, while the production OCR boundary is designed as a native C++ bridge.

```
Image
  ↓
FastAPI /v1/ocr
  ↓
C++ native bridge
  ↓
OneOCR runtime (Windows)
  ↓
text + lines + words + bounding boxes + confidence
  ↓
JSON
```

### Local API

Create the Python environment:

```powershell
python -m venv .venv
.venv\\Scripts\\Activate.ps1
pip install -r api/requirements.txt
```

Build the native bridge on Windows:

```powershell
cmake -S native -B native/build
cmake --build native/build --config Release
```

Start the API:

```powershell
uvicorn api.main:app --host 127.0.0.1 --port 8000
```

Health check:

```text
GET http://127.0.0.1:8000/health
```

OCR request:

```powershell
curl.exe -X POST http://127.0.0.1:8000/v1/ocr \
  -H "Content-Type: image/png" \
  --data-binary "@document.png"
```

The API is intentionally bound to `127.0.0.1` in the example so document images remain on the local machine.

> Important: the OneOCR runtime is a Windows component and is not bundled by AYORAI. The native bridge must be completed/built against the local OneOCR runtime before `/v1/ocr` can perform recognition.

## Architecture
```
User → Safety Guard → Planner → Router → Specialized Agents
                                      ├─ Research
                                      ├─ Analyst
                                      ├─ Security
                                      └─ Reviewer
                 → Memory / RAG / MCP / Tools → Safety → Result
```

## Repository structure
- `src/ayorai/agents` — specialized agents
- `src/ayorai/core` — shared contracts
- `src/ayorai/orchestration` — planning and routing
- `src/ayorai/safety` — policy and risk controls
- `src/ayorai/memory` — state interfaces
- `src/ayorai/rag` — retrieval interfaces
- `src/ayorai/mcp` — tool/context adapters
- `src/ayorai/tools` — governed tools
- `api` — local OCR HTTP boundary
- `native` — C++ OCR bridge
- `tests` — automated tests

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Status
Foundation rebuilt with multi-agent contracts, orchestration, safety, memory, RAG, MCP, tool governance and an offline OCR API foundation.

## Author
Anderson Leon Ayora — AYORAI · Applied Intelligence
