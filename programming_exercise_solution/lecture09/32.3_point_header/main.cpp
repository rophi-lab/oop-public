/*
Exercise 32.3: A Class in Two Files

Goal:
    Put the class declaration in point.hpp and the function bodies in point.cpp.
    main only creates an object and calls the public functions.

Expected output:
    x: 3
    y: 4

How to compile and run (from this folder):
    make
    ./point_lab
*/

#include <iostream>

#include "point.hpp"

int main()
{
    Point point;

    // TODO: set the point to (3, 4), then print
    //         x: <value>
    //         y: <value>
    point.set(3, 4);
    std::cout << "x: " << point.get_x() << '\n';
    std::cout << "y: " << point.get_y() << '\n';

    return 0;
}
