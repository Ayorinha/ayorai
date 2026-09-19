from __future__ import annotations
from io import BytesIO
from pathlib import Path
from typing import Any
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from PIL import Image, UnidentifiedImageError
from ocr.oneocr import OcrEngine

app = FastAPI(title="AYORAI Offline OCR", version="0.4.0", description="Local-only OneOCR API.")
_ENGINE: OcrEngine | None = None

def get_engine() -> OcrEngine:
    global _ENGINE
    if _ENGINE is None:
        _ENGINE = OcrEngine()
    return _ENGINE

@app.get("/health")
def health() -> dict[str, Any]:
    runtime = Path(__file__).resolve().parents[1] / "runtime" / "oneocr"
    return {"status":"ok","offline":True,"engine":"Microsoft OneOCR runtime",
            "runtime_available":all((runtime/n).is_file() for n in ("oneocr.dll","oneocr.onemodel","onnxruntime.dll"))}

@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return """<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AYORAI OCR</title><style>body{font-family:system-ui;background:#07111f;color:#e8f1ff;max-width:900px;margin:40px auto;padding:20px}main{border:1px solid #1d4f72;border-radius:18px;padding:28px;background:#0b1728}button{background:#18c6d8;border:0;padding:12px 20px;border-radius:10px;font-weight:700}textarea{width:100%;min-height:260px;margin-top:18px;background:#020812;color:#e8f1ff;border:1px solid #1d4f72;border-radius:10px;padding:12px;box-sizing:border-box}#status{margin:14px 0;color:#8de9f2}</style></head><body><main><h1>AYORAI · Offline OCR</h1><p>Reconhecimento local. A imagem não é enviada para a internet.</p><input id="file" type="file" accept="image/*"> <button id="run">Reconhecer</button><div id="status"></div><textarea id="out" readonly placeholder="Texto reconhecido..."></textarea></main><script>run.onclick=async()=>{const f=file.files[0];if(!f)return;status.textContent="Processando...";out.value="";try{const r=await fetch("/v1/ocr",{method:"POST",headers:{"Content-Type":f.type},body:await f.arrayBuffer()});const j=await r.json();if(!r.ok)throw Error(j.detail||"Falha");out.value=j.text||"";status.textContent="Concluído. Linhas: "+(j.lines?.length??0)}catch(e){status.textContent="Erro: "+e.message}}</script></body></html>"""

@app.post("/v1/ocr")
async def ocr(request: Request) -> dict[str, Any]:
    content_type = request.headers.get("content-type", "")
    if not content_type.startswith("image/"):
        raise HTTPException(415, "Envie uma imagem com Content-Type image/*.")
    data = await request.body()
    if not data:
        raise HTTPException(400, "Imagem vazia.")
    try:
        image = Image.open(BytesIO(data))
        result = get_engine().recognize_pil(image)
        result.update({"engine":"Microsoft OneOCR runtime","offline":True,"language":"pt-BR"})
        return result
    except UnidentifiedImageError as exc:
        raise HTTPException(400, "Arquivo de imagem inválido.") from exc
    except Exception as exc:
        raise HTTPException(503, str(exc)) from exc
