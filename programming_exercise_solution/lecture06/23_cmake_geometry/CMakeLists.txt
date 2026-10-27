# Exercise 23: CMakeLists.txt
#
# The C++ sources are already finished. Do not change them.
# Fill in the TODOs below, then from this folder run:
#     mkdir build
#     cd build
#     cmake ..
#     cmake --build .
#
# Every CMake command has the form:  command_name(arguments)
# Look up any command you are unsure about at https://cmake.org/cmake/help/latest/


# TODO 1: state the minimum CMake version this project needs (3.10 is fine).
#         Command to use: cmake_minimum_required
cmake_minimum_required(VERSION 3.10)


# TODO 2: give the project a name and tell CMake it is a C++ project.
#         Command to use: project   (pass LANGUAGES CXX)
project(geometry LANGUAGES CXX)


# TODO 3: ask for C++17 and make it mandatory.
#         Variables to set: CMAKE_CXX_STANDARD and CMAKE_CXX_STANDARD_REQUIRED
#         Command to use: set
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)


# TODO 4: turn on the usual gcc/clang warnings (-Wall -Wextra -Wpedantic).
#         Command to use: add_compile_options
#         (MSVC ignores these flags; that is fine for this exercise.)
add_compile_options(-Wall -Wextra -Wpedantic)


# TODO 5: build an executable called "geometry" from the project's .cpp files.
#         Command to use: add_executable
#
#         Part B: once it works, list ONLY main.cpp here, rebuild, and read the
#         error. Which stage fails -- compiling or linking? Then restore the
#         missing source file.
add_executable(geometry main.cpp geometry.cpp)
