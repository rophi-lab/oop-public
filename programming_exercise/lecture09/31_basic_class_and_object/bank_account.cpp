#include "bank_account.hpp"

#include <iostream>

// WORKED EXAMPLE: study this pattern, then write the others like it.
//   - Outside the class every definition carries the BankAccount:: prefix.
//   - A constructor can set its members in an initializer list, written
//     after a colon and before the body.
BankAccount::BankAccount(const std::string& owner, double balance)
    : owner_{owner}, balance_{balance}
{
}

// TODO: define deposit, withdraw, get_owner, get_balance, and print,
//       following the pattern above.
//
// Reminders:
//   - Definitions of const member functions repeat the const.
//   - Do not repeat the words public or private in this file.
//     The header already decided who may call what.
