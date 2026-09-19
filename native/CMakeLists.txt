cmake_minimum_required(VERSION 3.20)
project(ayorai_ocr_native LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_library(ayorai_ocr SHARED src/ayorai_ocr.cpp)

target_include_directories(ayorai_ocr PRIVATE include)

if (WIN32)
  target_compile_definitions(ayorai_ocr PRIVATE NOMINMAX WIN32_LEAN_AND_MEAN)
endif()
