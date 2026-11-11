#ifndef BANK_ACCOUNT_HPP
#define BANK_ACCOUNT_HPP

#include <string>

/*
Exercise 31: Basic Class and Object

Goal:
    Define a simple BankAccount class with a header and a source file,
    and practice two access levels plus const member functions:

        public   -> anyone can use (the class interface)
        private  -> only this class can use (the hidden data)
        const    -> a member function that only reads the object

File roles:
    bank_account.hpp  -> class declaration (what members exist)
    bank_account.cpp  -> member function definitions (how they work)
    main.cpp          -> create an object and call the public interface

--------------------------------------------------------------------------------
What BankAccount needs (declare here, define in bank_account.cpp):

    public
        BankAccount(const std::string& owner, double balance);
            Already declared below.
            const std::string& passes the name without copying it.

        void deposit(double amount);
            If amount is greater than 0, add it to the balance.
            Otherwise leave the balance unchanged.

        bool withdraw(double amount);
            If amount is greater than 0 and the balance can cover it,
            subtract it and return true.
            Otherwise leave the balance unchanged and return false.

        const std::string& get_owner() const;
        double get_balance() const;
            Read-only access. The const after the parameter list promises
            that these functions do not change the account.

        void print() const;
            Print one line:  <owner> has $<balance>
            The sample values are whole numbers, so the line is
            "Alice has $100", not "Alice has $100.00".

    private
        std::string owner_;
        double balance_;
            Already declared below. main cannot name these members.

The constructor and the private data are already written for you as a worked
example. Everything else is yours to add.

Hints:
    - A declaration ends with a semicolon; the body belongs in the .cpp file.
    - A const member function repeats const on its definition.
*/

class BankAccount {
public:
    // WORKED EXAMPLE: a declaration names the function and ends with a
    // semicolon -- the body lives in bank_account.cpp. Copy this pattern.
    BankAccount(const std::string& owner, double balance);

    // TODO: declare deposit, withdraw, get_owner, get_balance, and print.
    //       Mark the three read-only functions const.

private:
    // Given: the hidden data. Part B in main.cpp asks you to try reaching
    // these from outside the class and read the error you get.
    std::string owner_;
    double balance_;
};

#endif  // BANK_ACCOUNT_HPP
