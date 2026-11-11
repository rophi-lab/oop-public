/*
Exercise 32.2: const Member Functions

In-class exercise. One file. The class shell is already here.

Goal:
    Mark a member function const when it only reads the object.
    A const object can call const member functions, and nothing else.

What to finish:
    void increment();
        Add one to value_. This changes the object, so it is not const.
    int get_value() const;
        Return value_. Do not change it.

    main
        Increment one counter twice and print its value.
        Create a second counter that is const and print its value.
        Do not call increment on the const counter.

Expected output:
    clicks: 2
    untouched: 0

How to compile and run (from this folder):
    make
    ./const_counter
*/

#include <iostream>

class Counter {
public:
    void increment()
    {
        // TODO: add one to value_.
    }

    int get_value() const
    {
        // TODO: return value_. Replace the placeholder below.
        return 0;
    }

private:
    int value_{0};
};

int main()
{
    Counter clicks;

    // TODO: increment clicks twice, then print  clicks: <value>

    // TODO: create a const Counter named untouched and print
    //         untouched: <value>
    //       get_value is const, so a const object may call it.

    return 0;
}
