from __future__ import annotations

import ctypes
import json
from pathlib import Path
from typing import Any


class OcrBackendError(RuntimeError):
    pass


class OneOCRBackend:
    """Thin local adapter over the AYORAI C++ native bridge.

    The bridge owns the OneOCR/Windows DLL interaction. Python only exposes
    the HTTP boundary and serializes the native JSON result.
    """

    def __init__(self, native_library: Path, oneocr_dir: Path) -> None:
        self.native_library = native_library
        self.oneocr_dir = oneocr_dir
        self._lib: ctypes.WinDLL | None = None

        if hasattr(ctypes, "WinDLL") and native_library.exists():
            try:
                self._lib = ctypes.WinDLL(str(native_library))
                self._lib.ayorai_ocr_json.restype = ctypes.c_void_p
                self._lib.ayorai_ocr_json.argtypes = [
                    ctypes.POINTER(ctypes.c_ubyte),
                    ctypes.c_size_t,
                ]
                self._lib.ayorai_ocr_free.argtypes = [ctypes.c_void_p]
            except OSError:
                self._lib = None

    @property
    def available(self) -> bool:
        return self._lib is not None and self.oneocr_dir.exists()

    def recognize(self, image: bytes) -> dict[str, Any]:
        if self._lib is None:
            raise OcrBackendError(
                "Native OCR bridge is not loaded. Build native/ on Windows and "
                "install the OneOCR runtime files under oneocr/."
            )

        if not self.oneocr_dir.exists():
            raise OcrBackendError("OneOCR runtime directory is missing.")

        buffer = (ctypes.c_ubyte * len(image)).from_buffer_copy(image)
        ptr = self._lib.ayorai_ocr_json(buffer, len(image))
        if not ptr:
            raise OcrBackendError("OneOCR returned no result.")

        try:
            payload = ctypes.string_at(ptr).decode("utf-8")
        finally:
            self._lib.ayorai_ocr_free(ptr)

        try:
            return json.loads(payload)
        except json.JSONDecodeError as exc:
            raise OcrBackendError("Native OCR returned invalid JSON.") from exc
