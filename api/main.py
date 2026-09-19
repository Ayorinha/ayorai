from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException, Request

from api.ocr_backend import OneOCRBackend, OcrBackendError

app = FastAPI(
    title="AYORAI Offline OCR API",
    version="0.1.0",
    description="Local-first OCR API for sensitive document workflows.",
)

_BACKEND = OneOCRBackend(
    native_library=Path(os.getenv("AYORAI_OCR_DLL", "native/build/Release/ayorai_ocr.dll")),
    oneocr_dir=Path(os.getenv("AYORAI_ONEOCR_DIR", "oneocr")),
)


@app.get("/health")
def health() -> dict[str, Any]:
    return {
        "status": "ok",
        "offline": True,
        "engine": "ayorai-oneocr",
        "backend_available": _BACKEND.available,
    }


@app.post("/v1/ocr")
async def ocr(request: Request) -> dict[str, Any]:
    content_type = request.headers.get("content-type", "")
    if not content_type.startswith("image/"):
        raise HTTPException(status_code=415, detail="Send an image body with image/* content type.")

    image = await request.body()
    if not image:
        raise HTTPException(status_code=400, detail="Image body is empty.")

    try:
        return _BACKEND.recognize(image)
    except OcrBackendError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
