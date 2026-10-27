/*
Exercise 24: Input and Output Checkpoint

Goal:
    Practice reading input from the user and printing formatted output.

What you will use:
    - std::cout and std::cin          -> print and read
    - std::getline                    -> read a full name (may contain spaces)
    - std::fixed and std::setprecision -> control decimal places
      (include <iomanip> for these)

--------------------------------------------------------------------------------
TODO:
    1. Ask the user for their name, the rectangle width, and the rectangle height.
    2. Print a greeting that uses the name.
    3. Compute the rectangle area (width * height).
    4. Print the area with exactly two digits after the decimal point.

Rules:
    - Match the prompts and output format shown below.
    - The area line must always show two decimal places (e.g. 7.00, not 7).

Example run:
    Enter your name: Alice Kim
    Enter width: 3.5
    Enter height: 2.0

    Hello, Alice Kim!
    The area is 7.00.

How to compile and run (from this folder):
    make
    ./rectangle_area
*/

#include <iostream>
// TODO: add the headers you need. <string> gives you std::string, and the
//       decimal-place manipulators live in <iomanip>.

int main() {
    // TODO: declare variables for the name, the width, and the height.

    // TODO: prompt for the name and read the WHOLE line.
    //       Hint: >> stops at the first space, so it cannot read "Alice Kim".

    // TODO: prompt for width, then height, and read them as doubles.

    // TODO: compute the area.

    // TODO: print the blank line, the greeting, and the area.
    //       Hint: two manipulators work together to force exactly two
    //       decimals -- one fixes the notation, one sets the precision.

    return 0;
}
