from __future__ import annotations

import ctypes
import os
from ctypes import POINTER, Structure, byref, c_char, c_char_p, c_float, c_int32, c_int64, c_ubyte
from pathlib import Path

from PIL import Image

MODEL_NAME = "oneocr.onemodel"
DLL_NAME = "oneocr.dll"
MODEL_KEY = b'kj)TGtrK>f]b[Piow.gU+nC@s""""""4'
ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = Path(os.getenv("AYORAI_ONEOCR_DIR", str(ROOT / "runtime" / "oneocr")))

c_int64_p = POINTER(c_int64)
c_float_p = POINTER(c_float)
c_ubyte_p = POINTER(c_ubyte)

class ImageStructure(Structure):
    _fields_ = [("type", c_int32), ("width", c_int32), ("height", c_int32),
                ("_reserved", c_int32), ("step_size", c_int64), ("data_ptr", c_ubyte_p)]

class BoundingBox(Structure):
    _fields_ = [("x1", c_float), ("y1", c_float), ("x2", c_float), ("y2", c_float),
                ("x3", c_float), ("y3", c_float), ("x4", c_float), ("y4", c_float)]

BoundingBoxP = POINTER(BoundingBox)
DLL_FUNCTIONS = [
    ("CreateOcrInitOptions", [c_int64_p], c_int64),
    ("OcrInitOptionsSetUseModelDelayLoad", [c_int64, c_char], c_int64),
    ("CreateOcrPipeline", [c_char_p, c_char_p, c_int64, c_int64_p], c_int64),
    ("CreateOcrProcessOptions", [c_int64_p], c_int64),
    ("OcrProcessOptionsSetMaxRecognitionLineCount", [c_int64, c_int64], c_int64),
    ("RunOcrPipeline", [c_int64, POINTER(ImageStructure), c_int64, c_int64_p], c_int64),
    ("GetImageAngle", [c_int64, POINTER(c_float)], c_int64),
    ("GetOcrLineCount", [c_int64, c_int64_p], c_int64),
    ("GetOcrLine", [c_int64, c_int64, c_int64_p], c_int64),
    ("GetOcrLineContent", [c_int64, POINTER(c_char_p)], c_int64),
    ("GetOcrLineBoundingBox", [c_int64, POINTER(BoundingBoxP)], c_int64),
    ("GetOcrLineWordCount", [c_int64, c_int64_p], c_int64),
    ("GetOcrWord", [c_int64, c_int64, c_int64_p], c_int64),
    ("GetOcrWordContent", [c_int64, POINTER(c_char_p)], c_int64),
    ("GetOcrWordBoundingBox", [c_int64, POINTER(BoundingBoxP)], c_int64),
    ("GetOcrWordConfidence", [c_int64, POINTER(c_float)], c_int64),
    ("ReleaseOcrResult", [c_int64], None),
    ("ReleaseOcrInitOptions", [c_int64], None),
    ("ReleaseOcrPipeline", [c_int64], None),
    ("ReleaseOcrProcessOptions", [c_int64], None),
]

class OcrEngine:
    def __init__(self):
        if os.name != "nt":
            raise RuntimeError("AYORAI OneOCR backend requires Windows.")
        for name in (DLL_NAME, MODEL_NAME, "onnxruntime.dll"):
            if not (CONFIG_DIR / name).is_file():
                raise RuntimeError(f"Missing {name}: {CONFIG_DIR}")
        kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        kernel32.SetDllDirectoryW(str(CONFIG_DIR))
        self.ocr_dll = ctypes.WinDLL(str(CONFIG_DIR / DLL_NAME))
        for name, argtypes, restype in DLL_FUNCTIONS:
            fn = getattr(self.ocr_dll, name)
            fn.argtypes, fn.restype = argtypes, restype
        self.init_options = c_int64()
        self._check(self.ocr_dll.CreateOcrInitOptions(byref(self.init_options)), "Init options failed")
        self._check(self.ocr_dll.OcrInitOptionsSetUseModelDelayLoad(self.init_options, 0), "Model loading failed")
        model = ctypes.create_string_buffer(str(CONFIG_DIR / MODEL_NAME).encode())
        key = ctypes.create_string_buffer(MODEL_KEY)
        self.pipeline = c_int64()
        self._check(self.ocr_dll.CreateOcrPipeline(model, key, self.init_options, byref(self.pipeline)), "Pipeline creation failed")
        self.process_options = c_int64()
        self._check(self.ocr_dll.CreateOcrProcessOptions(byref(self.process_options)), "Process options failed")
        self._check(self.ocr_dll.OcrProcessOptionsSetMaxRecognitionLineCount(self.process_options, 1000), "Line count config failed")

    def __del__(self):
        try:
            if getattr(self, "ocr_dll", None):
                self.ocr_dll.ReleaseOcrProcessOptions(self.process_options)
                self.ocr_dll.ReleaseOcrPipeline(self.pipeline)
                self.ocr_dll.ReleaseOcrInitOptions(self.init_options)
        except (AttributeError, OSError):
            return

    @staticmethod
    def _check(code, message):
        if code != 0:
            raise RuntimeError(f"{message} (code {code})")

    def recognize_pil(self, image: Image.Image):
        if any(x < 50 or x > 10000 for x in image.size):
            return {"text": "", "text_angle": None, "lines": [], "error": "Unsupported image size."}
        image = image.convert("RGBA")
        b, g, r, a = image.split()
        bgra = Image.merge("RGBA", (b, g, r, a))
        data = bgra.tobytes()
        ptr = (c_ubyte * len(data)).from_buffer_copy(data)
        structure = ImageStructure(3, bgra.width, bgra.height, 0, bgra.width * 4, ptr)
        result_handle = c_int64()
        self._check(self.ocr_dll.RunOcrPipeline(self.pipeline, byref(structure), self.process_options, byref(result_handle)), "OCR execution failed")
        try:
            return self._parse(result_handle)
        finally:
            self.ocr_dll.ReleaseOcrResult(result_handle)

    def _text(self, handle, fn):
        value = c_char_p()
        if fn(handle, byref(value)) == 0 and value:
            return value.value.decode("utf-8", errors="ignore")
        return None

    def _box(self, handle, fn):
        value = BoundingBoxP()
        if fn(handle, byref(value)) != 0 or not value:
            return None
        b = value.contents
        return {k: float(getattr(b, k)) for k in ("x1","y1","x2","y2","x3","y3","x4","y4")}

    def _parse(self, result):
        count = c_int64()
        self._check(self.ocr_dll.GetOcrLineCount(result, byref(count)), "Reading line count failed")
        lines = []
        for i in range(count.value):
            line_handle = c_int64()
            if self.ocr_dll.GetOcrLine(result, i, byref(line_handle)) != 0:
                continue
            words_count = c_int64()
            self._check(self.ocr_dll.GetOcrLineWordCount(line_handle, byref(words_count)), "Reading word count failed")
            words = []
            for j in range(words_count.value):
                word_handle = c_int64()
                if self.ocr_dll.GetOcrWord(line_handle, j, byref(word_handle)) != 0:
                    continue
                confidence = c_float()
                self.ocr_dll.GetOcrWordConfidence(word_handle, byref(confidence))
                words.append({"text": self._text(word_handle, self.ocr_dll.GetOcrWordContent),
                              "bounding_rect": self._box(word_handle, self.ocr_dll.GetOcrWordBoundingBox),
                              "confidence": float(confidence.value)})
            lines.append({"text": self._text(line_handle, self.ocr_dll.GetOcrLineContent),
                          "bounding_rect": self._box(line_handle, self.ocr_dll.GetOcrLineBoundingBox),
                          "words": words})
        angle = c_float()
        angle_value = float(angle.value) if self.ocr_dll.GetImageAngle(result, byref(angle)) == 0 else None
        return {"text": "\n".join(x["text"] or "" for x in lines), "text_angle": angle_value, "lines": lines}
