/*
Exercise 22: Multi-File Geometry Program (Makefile)

Goal:
    The C++ sources in this folder are already finished. Your job is the
    Makefile: compile the two translation units, link them into a program,
    and then break the link step on purpose so you can read a LINKER error.

Why a Makefile?
    - geometry.hpp  -> DECLARATIONS (already done; the "interface")
    - geometry.cpp  -> DEFINITIONS  (already done; the "implementation")
    - main.cpp      -> this file; CALLS the geometry functions (already done)
    - Makefile      -> YOU write this; recipes to compile, link, and clean

    The compiler can check main.cpp against the declarations in the header.
    The linker then stitches the object files together. If a definition is
    missing, compilation of main.cpp may still succeed -- but linking fails.

--------------------------------------------------------------------------------
TODO:
    1. Open Makefile and complete every TODO.
    2. Run:  make
           then run the program (./geometry on Linux/macOS, or geometry.exe).
    3. Intentionally break linking (see Part B below) and explain the error.
    4. Do NOT change the .hpp / .cpp files.

Part B -- observe a linker error:
    1. Temporarily drop geometry.o from OBJECTS (leave only main.o).
    2. Run:  make clean && make
    3. Read the linker error. Notice that the COMPILER may still succeed;
       the LINKER fails because rectangle_area / circle_area have no
       definition to link against.
    4. Put geometry.o back and run make clean && make again so everything
       works.

Expected program output (when everything is linked correctly):
    rectangle area: 12
    circle area: 28.2743
    (exact circle formatting may vary slightly)
*/

#include <iostream>
#include "geometry.hpp"

int main() {
    std::cout << "rectangle area: " << rectangle_area(3.0, 4.0) << '\n';
    std::cout << "circle area: " << circle_area(3.0) << '\n';
    return 0;
}
