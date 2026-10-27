/*
Exercise 27: Temperature Converter

Goal:
    Ask the user for a Celsius temperature, convert it to Fahrenheit, and
    print the result with two decimal places.

Formula:
    Fahrenheit = Celsius * 9 / 5 + 32

Required function:
    double celsius_to_fahrenheit(double celsius);

Important:
    Write the formula carefully so you do NOT do integer division.
    Prefer writing:  celsius * 9.0 / 5.0 + 32.0
    (Using 9 / 5 alone would truncate to 1 in integer arithmetic.)

--------------------------------------------------------------------------------
TODO:
    1. Implement celsius_to_fahrenheit.
    2. In main: prompt for Celsius, call your function, print Fahrenheit
       with exactly two digits after the decimal point.

Example run:
    Enter Celsius temperature: 25
    Fahrenheit: 77.00

How to compile and run (from this folder):
    make
    ./temperature_converter
*/

#include <iomanip>
#include <iostream>

// TODO: convert Celsius to Fahrenheit and return the result.
double celsius_to_fahrenheit(double celsius)
{
}

int main()
{
    double celsius{};

    // TODO: prompt with "Enter Celsius temperature: " and read the value.

    // TODO: convert it using your function.

    // TODO: print  Fahrenheit: <value>  with exactly two decimal places.
    //       Hint: two manipulators from <iomanip>/<ios> work together here.

    return 0;
}
