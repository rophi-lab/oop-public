/*
Exercise 30: Pass and Return -- Value, Reference, const, Pointer

Goal:
    Compare how arguments are PASSED into functions and how results are
    RETURNED from functions.

Pass styles (caller -> function):
    by value          void f(int n)           copy; changes to n do NOT affect caller
    by reference      void f(int& n)          alias; can modify caller
    by const ref      void f(const int& n)    alias; read-only, no copy of big objects
    by pointer        void f(int* p)          address; can modify *p; do nothing if p is nullptr
    by pointer to const
                      void f(const int* p)    address; read-only through *p; do nothing if p is nullptr
                                              (const is before *: pointer to const, not int* const)

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
    Do not change the std::cout lines that are already written.
    Fill the TODOs so the output matches.

Expected output:
    after pass_by_value: 10
    after pass_by_reference: 20
    print_by_const_ref: 20
    after pass_by_pointer: 40
    print_by_pointer_to_const: 40
    returned by value: 41
    after return_by_reference += 1: 41
    returned by const ref: 41
    returned by pointer: 41

Why two lines say 41:
    return_by_value returns 40 + 1 and leaves score at 40.
    return_by_reference then adds 1 through an alias, so score becomes 41.
    The const-reference and pointer returns both observe that updated score.

How to compile and run (from this folder):
    make
    ./pass_and_return
*/

#include <iostream>

// TODO 1: PASS BY VALUE -- add 5 to n.
//         Afterwards, check in main that the caller's variable did NOT change.
void pass_by_value(int n)
{
    n += 5;
}

// TODO 2: PASS BY REFERENCE -- double n in place so the caller sees it.
void pass_by_reference(int& n)
{
    n *= 2;
}

// TODO 3: PASS BY CONST REFERENCE -- print  print_by_const_ref: <n>
void print_by_const_ref(const int& n)
{
    std::cout << "print_by_const_ref: " << n << '\n';
}

// TODO 4: PASS BY POINTER -- double the value p points at.
//         If p is nullptr, return without changing anything.
void pass_by_pointer(int* p)
{
    if (p != nullptr) {
        *p *= 2;
    }
}

// TODO 5: PASS BY POINTER TO CONST -- print  print_by_pointer_to_const: <value>
//         const int* is a pointer to const, not a const pointer (int* const).
//         If p is nullptr, return without printing.
void print_by_pointer_to_const(const int* p)
{
    if (p != nullptr) {
        std::cout << "print_by_pointer_to_const: " << *p << '\n';
    }
}

// TODO 6: RETURN BY VALUE -- give back n + 1 as a copy.
int return_by_value(int n)
{
    return n + 1;
}

// TODO 7: RETURN BY REFERENCE -- give back n itself, so the caller can
//         assign through the result.
int& return_by_reference(int& n)
{
    return n;
}

// TODO 8: RETURN BY CONST REFERENCE -- give back n as a read-only alias.
const int& return_by_const_ref(const int& n)
{
    return n;
}

// TODO 9: RETURN BY POINTER -- give back where n lives in memory.
int* return_by_pointer(int& n)
{
    return &n;
}

int main()
{
    int score{10};

    // ---------------- PASS ----------------
    pass_by_value(score);
    std::cout << "after pass_by_value: " << score << '\n';  // still 10

    // TODO: call pass_by_reference so score becomes 20.
    pass_by_reference(score);
    std::cout << "after pass_by_reference: " << score << '\n';  // 20

    // TODO: call print_by_const_ref on score.
    print_by_const_ref(score);

    // TODO: call pass_by_pointer so score becomes 40.
    //       Hint: this one wants an address, not the variable itself.
    pass_by_pointer(&score);
    std::cout << "after pass_by_pointer: " << score << '\n';  // 40

    // TODO: call print_by_pointer_to_const on score.
    //       Pass the address of score.
    print_by_pointer_to_const(&score);

    // ---------------- RETURN ----------------
    // TODO: save what return_by_value(score) gives you and print
    //         returned by value: <value>
    //       score itself must stay at 40 here.
    int by_value = return_by_value(score);
    std::cout << "returned by value: " << by_value << '\n';

    // TODO: bind an int& to return_by_reference(score), then add 1 through it.
    //       The submitted program must use a reference, or add 1 directly
    //       through the call. A plain int stores a copy, so score would
    //       stay 40 and the next line would not match.
    int& by_ref = return_by_reference(score);
    by_ref += 1;
    std::cout << "after return_by_reference += 1: " << score << '\n';

    // TODO: print  returned by const ref: <value>
    const int& by_const_ref = return_by_const_ref(score);
    std::cout << "returned by const ref: " << by_const_ref << '\n';

    // TODO: keep what return_by_pointer(score) gives you, then print
    //         returned by pointer: <value it points at>
    int* by_ptr = return_by_pointer(score);
    std::cout << "returned by pointer: " << *by_ptr << '\n';

    return 0;
}
