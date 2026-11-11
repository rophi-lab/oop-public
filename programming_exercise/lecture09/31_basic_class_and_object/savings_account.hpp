#ifndef SAVINGS_ACCOUNT_HPP
#define SAVINGS_ACCOUNT_HPP

#include "bank_account.hpp"

/*
SavingsAccount is a DERIVED class: it inherits from BankAccount.

It may use the protected member adjust_balance, but it cannot touch the
private data of BankAccount directly.

What SavingsAccount needs (declare here, define in savings_account.cpp):

    public
        SavingsAccount(const std::string& owner, double balance,
                       double interest_rate);

        void apply_interest();
            Increase the balance by get_balance() * interest_rate_.
            The balance is private in BankAccount, so read it with
            get_balance() and change it with adjust_balance.

    private
        double interest_rate_;
*/

class SavingsAccount : public BankAccount {
public:
    // TODO: declare the constructor and apply_interest.

private:
    // TODO: declare the interest rate.
};

#endif  // SAVINGS_ACCOUNT_HPP
