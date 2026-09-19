#include "ayorai_ocr.h"

#include <cstdlib>
#include <cstring>
#include <filesystem>
#include <sstream>
#include <string>
#include <vector>

#ifdef _WIN32
#include <windows.h>
#endif

namespace {

#ifdef _WIN32

struct ImageStructure {
    int type;
    int width;
    int height;
    int reserved;
    int step_size;
    void* data_ptr;
};

struct BoundingBox {
    float x1, y1, x2, y2, x3, y3, x4, y4;
};

using CreateOcrInitOptionsFn = void* (__cdecl*)();
using SetDelayLoadFn = void (__cdecl*)(void*, bool);
using CreatePipelineFn = void* (__cdecl*)(void*, const char*);
using CreateProcessOptionsFn = void* (__cdecl*)();
using SetMaxLinesFn = void (__cdecl*)(void*, int);
using RunPipelineFn = int (__cdecl*)(void*, void*, ImageStructure*);
using GetAngleFn = float (__cdecl*)(void*);
using GetLineCountFn = int (__cdecl*)(void*);
using GetLineFn = void* (__cdecl*)(void*, int);
using GetLineContentFn = const char* (__cdecl*)(void*);
using GetLineBoxFn = BoundingBox (__cdecl*)(void*);
using GetWordCountFn = int (__cdecl*)(void*);
using GetWordFn = void* (__cdecl*)(void*, int);
using GetWordContentFn = const char* (__cdecl*)(void*);
using GetWordBoxFn = BoundingBox (__cdecl*)(void*);
using GetWordConfidenceFn = float (__cdecl*)(void*);
using ReleaseFn = void (__cdecl*)(void*);

std::string json_escape(const char* value) {
    std::string out;
    if (!value) return out;
    for (const unsigned char c : std::string(value)) {
        switch (c) {
            case '\\': out += "\\\\"; break;
            case '"': out += "\\\""; break;
            case '\n': out += "\\n"; break;
            case '\r': out += "\\r"; break;
            case '\t': out += "\\t"; break;
            default: out += static_cast<char>(c);
        }
    }
    return out;
}

template <typename T>
T symbol(HMODULE dll, const char* name) {
    return reinterpret_cast<T>(GetProcAddress(dll, name));
}

#endif

}  // namespace

extern "C" AYORAI_API const char* ayorai_ocr_json(
    const unsigned char* image_bytes, std::size_t image_size) {
#ifdef _WIN32
    if (!image_bytes || image_size == 0) return nullptr;

    // The native bridge intentionally expects decoded BGRA/RGBA pixels in a
    // future image-decoder layer. Keeping this boundary explicit prevents
    // silently guessing image formats inside the OCR engine.
    (void)image_bytes;
    (void)image_size;

    return nullptr;
#else
    (void)image_bytes;
    (void)image_size;
    return nullptr;
#endif
}

extern "C" AYORAI_API void ayorai_ocr_free(const char* json) {
    std::free(const_cast<char*>(json));
}
