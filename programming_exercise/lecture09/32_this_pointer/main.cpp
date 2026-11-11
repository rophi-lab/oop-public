/*
Exercise 32: The this Pointer

Goal:
    Practice three uses of the this pointer inside member functions:
        1. this->member   -- talk about the current object's data
        2. return *this   -- enable method chaining
        3. this == &other -- check whether two names refer to the same object

Implement Counter in counter.hpp / counter.cpp, then finish main below.

Expected output:
    [alpha] 0
    [alpha] 5
    [alpha] 10
    same object (alpha vs alpha): true
    same object (alpha vs beta): false

How to compile and run (from this folder):
    make
    ./this_lab
*/

#include <iostream>

#include "counter.hpp"

int main()
{
    // TODO: create a Counter named "alpha" starting at 0, and print it.

    // TODO: set its value to 5, then print it.

    // TODO: add 3 and then add 2 in a SINGLE chained statement, then print.
    //       If chaining does not compile, revisit what add() returns.

    // TODO: create a second Counter named "beta" starting at 99.

    // TODO: print
    //         same object (alpha vs alpha): <result>
    //         same object (alpha vs beta): <result>
    //       The words alpha and beta are the object names, not variables
    //       called a and b.
    //       Use std::boolalpha so the words true and false appear.
    //       Without it, C++ prints 1 and 0.

    return 0;
}
