/*
Exercise 31: Basic Class and Object

Goal:
    Practice writing a C++ class with:
        - public, protected, and private members
        - separate .hpp (declarations) and .cpp (definitions)
        - creating objects and calling member functions

Access levels (quick guide):
    public     -- usable from anywhere (main, other classes, ...)
    protected  -- usable inside this class and classes that inherit from it
    private    -- usable ONLY inside this class

What to implement:
    1. bank_account.hpp / bank_account.cpp
           BankAccount with private owner_/balance_,
           public deposit/withdraw/getters/print,
           protected adjust_balance.
    2. savings_account.hpp / savings_account.cpp
           SavingsAccount inherits BankAccount,
           stores a private interest_rate_,
           apply_interest() uses protected adjust_balance.
    3. main.cpp below -- create objects and call the public API.

Rules:
    - From main, call only public members.
    - balance_ is private, and adjust_balance is protected. main cannot use either.
    - SavingsAccount may call adjust_balance, but it cannot use owner_ or balance_.
    - The program you hand in must compile. Part B stays commented out.

Expected output:
    Alice has $100
    Alice has $150
    withdraw ok: true
    Alice has $120
    Bob has $200
    Bob has $210

How to compile and run (from this folder):
    make
    ./bank_lab
*/

#include <iostream>

#include "bank_account.hpp"
#include "savings_account.hpp"

int main()
{
    // TODO: create a BankAccount for "Alice" starting at 100, and print it.

    // TODO: deposit 50, then print again (should show 150).

    // TODO: withdraw 30. Print  withdraw ok: <true or false>  using the
    //       bool that withdraw returned, then print the account again.
    //       Use std::boolalpha so the words true and false appear.
    //       Without it, C++ prints 1 and 0.

    // TODO: create a SavingsAccount for "Bob" starting at 200 with a 0.05
    //       interest rate. Print it, apply the interest, and print it again.

    // Part B (thinking question, not part of the output):
    // The finished program must compile, so leave these experiments commented out.
    //     alice.balance_ = 0;          // private: main cannot name this member
    //     alice.adjust_balance(-10);   // protected: main is not a derived class
    // Each line is rejected because of its access level.

    return 0;
}
