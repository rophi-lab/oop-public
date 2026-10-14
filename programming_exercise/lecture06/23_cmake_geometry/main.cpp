/*
Exercise 23: Building with CMake (CMakeLists.txt)

Goal:
    Build the same style of multi-file C++ program as Exercise 22, but this
    time with CMake instead of a hand-written Makefile.

Why CMake?
    A Makefile lists exact compile/link commands for one platform.
    CMakeLists.txt describes the PROJECT (sources, targets, options).
    CMake then GENERATES a native build system for you (Makefiles on Linux,
    Visual Studio on Windows, Ninja, etc.).

Typical out-of-source workflow (keep build files out of your source folder):
    1. mkdir build
    2. cd build
    3. cmake ..              # configure: read CMakeLists.txt, generate build files
    4. cmake --build .       # compile and link
    5. ./geometry            # run (geometry.exe on Windows)
    6. To wipe the build:    # from the exercise folder
           rm -rf build      # or delete the build/ folder in Explorer

The C++ sources (geometry.hpp / geometry.cpp / main.cpp) are already finished.
Do NOT change them. Your job is CMakeLists.txt: describe the project so CMake
can generate a build system, then configure and build.

--------------------------------------------------------------------------------
TODO:
    1. Open CMakeLists.txt and complete every TODO line.
       Do NOT change the .hpp / .cpp files.
    2. From this folder, create a build directory and configure:
           mkdir build
           cd build
           cmake ..
    3. Build:
           cmake --build .
    4. Run the program and check the output below.
    5. Part B: temporarily remove geometry.cpp from add_executable in
       CMakeLists.txt, reconfigure + rebuild, observe the linker error,
       then put geometry.cpp back and rebuild successfully.

Expected program output:
    rectangle area: 12
    circle area: 28.2743
    (exact circle formatting may vary slightly)
*/

#include <iostream>
#include "geometry.hpp"

int main() {
    std::cout << "rectangle area: " << rectangle_area(3.0, 4.0) << "\n";
    std::cout << "circle area: " << circle_area(3.0) << "\n";
    return 0;
}
