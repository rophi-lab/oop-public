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
#include <iomanip>
#include <string>

int main() {
    // TODO: declare variables for the name, the width, and the height.
    std::string name;
    double width{};
    double height{};

    // TODO: prompt for the name and read the WHOLE line.
    //       Hint: >> stops at the first space, so it cannot read "Alice Kim".
    std::cout << "Enter your name: ";
    std::getline(std::cin, name);

    // TODO: prompt for width, then height, and read them as doubles.
    std::cout << "Enter width: ";
    std::cin >> width;
    std::cout << "Enter height: ";
    std::cin >> height;

    // TODO: compute the area.
    double area = width * height;

    // TODO: print the blank line, the greeting, and the area.
    //       Hint: two manipulators work together to force exactly two
    //       decimals -- one fixes the notation, one sets the precision.
    std::cout << '\n';
    std::cout << "Hello, " << name << "!\n";
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "The area is " << area << ".\n";

    return 0;
}
