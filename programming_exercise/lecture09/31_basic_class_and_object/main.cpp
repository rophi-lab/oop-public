/*
Exercise 31: Basic Class and Object

Goal:
    Practice writing a C++ class with:
        - public and private members
        - const member functions that only read the object
        - a header for the declaration and a source file for the definitions

Access levels:
    public   -- callable from main
    private  -- usable only inside BankAccount

What to implement:
    1. bank_account.hpp / bank_account.cpp
           BankAccount with private owner_ and balance_,
           and a public deposit, withdraw, getters, and print.
    2. main.cpp below -- create one account and call the public functions.

Rules:
    - From main, call only public members.
    - owner_ and balance_ are private. main cannot use them.
    - get_owner, get_balance, and print are const: they must not change the account.
    - The program you hand in must compile. Part B stays commented out.

Expected output:
    Alice has $100
    Alice has $150
    withdraw ok: true
    Alice has $120

How to compile and run (from this folder):
    make
    ./bank_lab
*/

#include <iostream>

#include "bank_account.hpp"

int main()
{
    // TODO: create a BankAccount for "Alice" starting at 100, and print it.

    // TODO: deposit 50, then print again (should show 150).

    // TODO: withdraw 30. Print  withdraw ok: <true or false>  using the
    //       bool that withdraw returned, then print the account again.
    //       Use std::boolalpha so the words true and false appear.
    //       Without it, C++ prints 1 and 0.

    // Part B (thinking question, not part of the output):
    // The finished program must compile, so leave this experiment commented out.
    //     alice.balance_ = 0;   // private: main cannot name this member

    return 0;
}
