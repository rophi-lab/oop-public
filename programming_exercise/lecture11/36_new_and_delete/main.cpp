/*
Exercise 36: new and delete

Goal:
    Part 1 and 2 make you manage heap memory by hand. Part 3 hands the same
    job to a class, so the cleanup happens whether you remember it or not.

Expected output:
    value: 42
    numbers: 0 1 4 9 16
    buffer size=3 [0, 0, 0]
    buffer size=3 [10, 20, 30]
    IntBuffer: freed 3 ints

    Notice the last line. You never wrote a delete for the buffer -- its
    destructor ran on its own when main ended.

How to compile and run (from this folder):
    make
    ./memory_lab
*/

#include <iostream>

#include "int_buffer.hpp"

int main()
{
    // ---------- Part 1: a single object on the heap ----------
    // TODO: allocate one int holding 42, print
    //           value: 42
    //       then release it and set your pointer to nullptr.

    // ---------- Part 2: an array on the heap ----------
    // TODO: allocate an array of 5 ints. Put i * i into element i, then print
    //       them separated by single spaces on one line:
    //           numbers: 0 1 4 9 16
    //       Then release the array with delete[] and set the pointer to
    //       nullptr. An array does not use the same delete as a single object.

    // ---------- Part 3: let a class own the memory ----------
    // TODO: create an IntBuffer holding 3 ints and print it with the label
    //       "buffer". It should start out all zeros.

    // TODO: set the three elements to 10, 20 and 30, then print it again.
    //       Do NOT write a delete for this one -- that is the whole point.

    // ---------- Part 4: why copying is forbidden ----------
    // The program you hand in must compile, so leave this line commented out.
    // You may uncomment it, read the error, and comment it out again.
    // Then answer in a comment: if the copy WERE allowed and both objects
    // held the same pointer, what would go wrong at the end of main?
    //
    // IntBuffer copy{buffer};

    return 0;
}
