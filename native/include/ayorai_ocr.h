#pragma once

#include <cstddef>

#ifdef _WIN32
#define AYORAI_API __declspec(dllexport)
#else
#define AYORAI_API
#endif

extern "C" {
AYORAI_API const char* ayorai_ocr_json(const unsigned char* image_bytes, std::size_t image_size);
AYORAI_API void ayorai_ocr_free(const char* json);
}
