/*
Exercise 28: Number Statistics

Goal:
    Read five integers into a std::array<int, 5> and print summary statistics.

Print:
    - the sum
    - the average (two decimal places)
    - the minimum value
    - the maximum value
    - the number of positive values (> 0)

Suggested helper functions:
    int calculate_sum(std::array<int, 5> values);
    int find_minimum(std::array<int, 5> values);
    int find_maximum(std::array<int, 5> values);

You may also write helpers for average and counting positives if you like,
or compute those directly in main.

--------------------------------------------------------------------------------
TODO:
    1. Implement calculate_sum, find_minimum, and find_maximum.
    2. In main: read five integers into the array.
    3. Print all five statistics listed above.

Example run:
    Enter value 1: 3
    Enter value 2: -1
    Enter value 3: 7
    Enter value 4: 0
    Enter value 5: 4

    Sum: 13
    Average: 2.60
    Minimum: -1
    Maximum: 7
    Positive count: 3

How to compile and run (from this folder):
    make
    ./number_statistics
*/

#include <array>
#include <iomanip>
#include <iostream>

// TODO: return the sum of all five values.
// Hint: a range-based for loop (for (int value : values)) reads each element.
int calculate_sum(std::array<int, 5> values)
{
}

// TODO: return the smallest value in the array.
// Hint: start from the first element, then compare against the rest.
int find_minimum(std::array<int, 5> values)
{
}

// TODO: return the largest value in the array.
int find_maximum(std::array<int, 5> values)
{
}

int main()
{
    std::array<int, 5> values{};

    // TODO: prompt "Enter value 1: " ... "Enter value 5: " and read each one
    //       into the array. A loop over values.size() keeps this short.

    // TODO: work out the five statistics.
    //       - sum, minimum, maximum come from your helper functions
    //       - the average is the sum divided by how many values there are
    //         (watch out for integer division)
    //       - count how many values are greater than zero

    // TODO: print the blank line and the five result lines exactly as shown
    //       in the example run. Only the average needs two decimal places.

    return 0;
}
