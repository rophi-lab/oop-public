/*
Exercise 30: Pass and Return -- Value, Reference, const, Pointer

Goal:
    Compare how arguments are PASSED into functions and how results are
    RETURNED from functions.

Pass styles (caller -> function):
    by value          void f(int n)           copy; changes to n do NOT affect caller
    by reference      void f(int& n)          alias; can modify caller
    by const ref      void f(const int& n)    alias; read-only, no copy of big objects
    by pointer        void f(int* p)          address; can modify *p (check for nullptr)
    by const pointer  void f(const int* p)    address; read-only through *p

Return styles (function -> caller):
    by value          int f();                safe default; returns a copy
    by reference      int& f(int& n);         returns an alias (lifetime must outlive use)
    by const ref      const int& f(...);      read-only alias
    by pointer        int* f(int& n);         returns an address (&n)

Rule of thumb:
    - Prefer pass by const reference for reading without copying.
    - Prefer pass by reference (or pointer) when you need to modify.
    - Prefer return by value unless you intentionally return an alias/address
      to something that still exists after the function returns.

--------------------------------------------------------------------------------
TODO:
    Implement each function below, then call them from main as marked.
    Do NOT change the "DO NOT EDIT" prints -- fill the TODOs so the output matches.

Expected output:
    after pass_by_value: 10
    after pass_by_reference: 20
    print_by_const_ref: 20
    after pass_by_pointer: 40
    print_by_const_pointer: 40
    returned by value: 41
    after return_by_reference += 1: 41
    returned by const ref: 41
    returned by pointer: 41

How to compile and run (from this folder):
    make
    ./pass_and_return
*/

#include <iostream>

// TODO 1: PASS BY VALUE -- add 5 to n.
//         Afterwards, check in main that the caller's variable did NOT change.
void pass_by_value(int n)
{
}

// TODO 2: PASS BY REFERENCE -- double n in place so the caller sees it.
void pass_by_reference(int& n)
{
}

// TODO 3: PASS BY CONST REFERENCE -- print  print_by_const_ref: <n>
void print_by_const_ref(const int& n)
{
}

// TODO 4: PASS BY POINTER -- double the value p points at.
//         Guard against p being nullptr first.
void pass_by_pointer(int* p)
{
}

// TODO 5: PASS BY CONST POINTER -- print  print_by_const_pointer: <value>
//         Again, check for nullptr before following the pointer.
void print_by_const_pointer(const int* p)
{
}

// TODO 6: RETURN BY VALUE -- give back n + 1 as a copy.
int return_by_value(int n)
{
}

// TODO 7: RETURN BY REFERENCE -- give back n itself, so the caller can
//         assign through the result.
int& return_by_reference(int& n)
{
}

// TODO 8: RETURN BY CONST REFERENCE -- give back n as a read-only alias.
const int& return_by_const_ref(const int& n)
{
}

// TODO 9: RETURN BY POINTER -- give back where n lives in memory.
int* return_by_pointer(int& n)
{
}

int main()
{
    int score{10};

    // ---------------- PASS ----------------
    pass_by_value(score);
    std::cout << "after pass_by_value: " << score << '\n';  // still 10

    // TODO: call pass_by_reference so score becomes 20.
    std::cout << "after pass_by_reference: " << score << '\n';  // 20

    // TODO: call print_by_const_ref on score.

    // TODO: call pass_by_pointer so score becomes 40.
    //       Hint: this one wants an address, not the variable itself.
    std::cout << "after pass_by_pointer: " << score << '\n';  // 40

    // TODO: call print_by_const_pointer on score.

    // ---------------- RETURN ----------------
    // TODO: save what return_by_value(score) gives you and print
    //         returned by value: <value>
    //       score itself must stay at 40 here.

    // TODO: grab what return_by_reference(score) gives you as a reference,
    //       then add 1 through it. If you store it in a plain int instead,
    //       score will NOT change -- try both and see why.
    std::cout << "after return_by_reference += 1: " << score << '\n';

    // TODO: print  returned by const ref: <value>

    // TODO: keep what return_by_pointer(score) gives you, then print
    //         returned by pointer: <value it points at>

    return 0;
}
