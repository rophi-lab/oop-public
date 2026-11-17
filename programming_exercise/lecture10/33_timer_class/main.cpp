/*
Exercise 33: A Timer Class

Goal:
    Implement Timer in timer.hpp / timer.cpp so that it prints when it is
    created and when it is destroyed, and so that the two misuses in Part B
    are rejected by the compiler.

Expected output:
    Start: Simulation
    End: Simulation

    Notice there is nothing between those two lines: the End line appears
    when timer reaches the end of main and is destroyed.

How to compile and run (from this folder):
    make
    ./timer_lab
*/

#include <string>

#include "timer.hpp"

int main()
{
    Timer timer{"Simulation"};

    // Part B -- the program you hand in must compile, so leave both lines
    // commented out. You may uncomment one at a time, read the error, and
    // comment it out again.
    //
    // Timer no_name;                         // deleted default constructor
    // Timer implicit = std::string{"Nope"};  // explicit blocks this conversion

    return 0;
}
