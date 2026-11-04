/*
Exercise 29: Pointers, References, and const

Goal:
    Practice three related ideas in C++:
        1. references  -> another name for an existing object
        2. pointers    -> store the ADDRESS of an object
        3. const       -> promise not to change something through that name

Quick reminders:
    int x = 10;
    int& r = x;      // r is a reference to x (must be initialized; cannot reseat)
    int* p = &x;     // p holds the address of x
    *p = 20;         // dereference: change x through the pointer
    const int& cr = x;   // can read x through cr, but not assign to cr
    const int* cp = &x;  // pointer to const: can change cp, not *cp

Why pass by reference / const reference?
    - void set_to_zero(int& n)        -> modify the caller's variable
    - void print_value(const int& n)  -> read without copying; cannot modify

--------------------------------------------------------------------------------
TODO:
    1. Implement double_value: take an int by reference and double it in place.
    2. Implement print_score: take an int by const reference and print it.
       (Do NOT modify the parameter.)
    3. In main, finish the pointer section:
         - make pointer `p` point at `score`
         - print the value pointed to by p (*p)
         - set *p to 42 and show that `score` changed
       (You can also print `p` itself to see the raw address, but leave that
        out of the final program -- it is not part of the expected output.)
    4. Create a const int* named `cp` that points at score, and print *cp.
       (Do NOT try to assign through cp -- that should not compile.)

Expected output:
    before: 10
    after double_value: 20
    score via print_score: 20
    value via pointer: 20
    score after *p = 42: 42
    value via const pointer: 42

How to compile and run (from this folder):
    make
    ./pointer_ref_const
*/

#include <iostream>

// TODO 1: double n in place. Because n is a reference, assigning to it
//         changes the caller's variable.
void double_value(int& n)
{
}

// TODO 2: print  score via print_score: <n>
//         n is const here, so read it but do not assign to it.
void print_score(const int& n)
{
}

int main()
{
    int score{10};
    std::cout << "before: " << score << '\n';

    // TODO: call double_value so score becomes 20.
    std::cout << "after double_value: " << score << '\n';

    // TODO: call print_score.

    int* p{nullptr};
    // TODO 3: aim p at score, then print
    //           value via pointer: <the value p points to>
    //         Hint: one operator takes an address, another follows it.

    // TODO: change score to 42 by writing THROUGH p (do not touch score directly).
    std::cout << "score after *p = 42: " << score << '\n';

    // TODO 4: declare a pointer-to-const aimed at score and print
    //           value via const pointer: <value>
    //         Then try assigning through it, confirm it fails to compile,
    //         and comment that line back out.

    return 0;
}
