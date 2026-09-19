# AYORAI — Offline OneOCR

Windows-first, local-only OCR integration for sensitive document workflows.

## Quick start

1. Download the repository ZIP.
2. Extract it.
3. Run INSTALL_AYORAI_OCR.bat.
4. Run START_AYORAI_OCR.bat.
5. Your browser opens http://127.0.0.1:8000.
6. Select an image and click Reconhecer.

This runnable path does not require a C++ compiler. It uses Python/FastAPI + Pillow and loads the local OneOCR runtime through ctypes.

The Microsoft runtime binaries are not committed or redistributed by AYORAI. The installer extracts oneocr.dll, oneocr.onemodel and onnxruntime.dll from the locally installed Snipping Tool package. Public OneOCR integrations document this same runtime layout. citeturn0search0turn0search2

## What is local

Image bytes are sent only to 127.0.0.1. OCR execution uses the local OneOCR runtime. No cloud OCR endpoint is configured.

Output includes text, lines, words, bounding boxes, confidence and image angle.

## Requirements

- Windows 10/11 x64
- Snipping Tool installed
- Python 3.11+; the installer can try winget when Python is missing
- Internet is only needed during setup to install Python packages; OCR itself runs locally.

## API

POST /v1/ocr with an image body and an image/* content type.

GET /health reports whether the three local runtime files are present.

## Important

The project integrates an unofficial OneOCR runtime discovered in recent Snipping Tool builds. Microsoft does not publish the internal OneOCR ABI as a supported public SDK. Windows updates may change the runtime. Verify the installed runtime on the target Windows machine before production use. citeturn0search2

Actual OCR accuracy must be benchmarked on real images; a passing API test is not an accuracy claim.
