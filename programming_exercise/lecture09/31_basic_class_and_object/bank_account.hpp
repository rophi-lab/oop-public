#ifndef BANK_ACCOUNT_HPP
#define BANK_ACCOUNT_HPP

#include <string>

/*
Exercise 31: Basic Class and Object (public / protected / private)

Goal:
    Define a simple BankAccount class with separate header and source files,
    and practice the three access levels:

        public     -> anyone can use (the class "interface")
        protected  -> this class and DERIVED classes can use
        private    -> ONLY this class can use (the hidden data)

File roles:
    bank_account.hpp  -> class DECLARATION (what members exist)
    bank_account.cpp  -> member function DEFINITIONS (how they work)
    main.cpp          -> create objects and call the public interface

--------------------------------------------------------------------------------
What BankAccount needs (declare here, define in bank_account.cpp):

    public
        BankAccount(const std::string& owner, double balance);
            Already declared below.

        void deposit(double amount);
            If amount is greater than 0, add it to the balance.
            Otherwise leave the balance unchanged.

        bool withdraw(double amount);
            If amount is greater than 0 and the balance can cover it,
            subtract it and return true.
            Otherwise leave the balance unchanged and return false.

        const std::string& get_owner() const;
        double get_balance() const;
            Read-only access. Mark both functions const.

        void print() const;
            Print one line:  <owner> has $<balance>
            The sample values are whole numbers, so the line is
            "Alice has $100", not "Alice has $100.00".

    protected
        void adjust_balance(double delta);
            Add delta to the balance. delta may be negative.
            SavingsAccount calls this helper. Do not add extra checks here.

    private
        std::string owner_;
        double balance_;
            Already declared below.

The constructor and the private data are already written for you as a worked
example. Everything else is yours to add.

Hints:
    - Member functions that only read the object should be marked const.
    - Passing a std::string by const reference avoids copying it.
    - A declaration ends with a semicolon; the body belongs in the .cpp file.
*/

class BankAccount {
public:
    // WORKED EXAMPLE: a declaration names the function and ends with a
    // semicolon -- the body lives in bank_account.cpp. Copy this pattern.
    BankAccount(const std::string& owner, double balance);

    // TODO: declare deposit, withdraw, get_owner, get_balance, and print.

protected:
    // TODO: declare the helper that derived classes are allowed to use.

private:
    // Given: the hidden data. Part B in main.cpp asks you to try reaching
    // these from outside the class and read the error you get.
    std::string owner_;
    double balance_;
};

#endif  // BANK_ACCOUNT_HPP
