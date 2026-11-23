#include "counter.hpp"

#include <iostream>

// WORKED EXAMPLE: note the Counter:: prefix and the initializer list.
Counter::Counter(const std::string& name, int value)
    : name_{name}, value_{value}
{
}

// TODO: define the remaining Counter members, following the pattern above.
//
// Reminders:
//   - For the chainable functions, the thing you hand back is the object
//     that `this` points at -- not the pointer itself.
//   - is_same_object compares addresses, so it needs the address of the
//     parameter rather than its value.
Counter& Counter::set_value(int value)
{
    this->value_ = value;
    return *this;
}

Counter& Counter::add(int amount)
{
    this->value_ += amount;
    return *this;
}

Counter& Counter::reset()
{
    this->value_ = 0;
    return *this;
}

bool Counter::is_same_object(const Counter& other) const
{
    return this == &other;
}

const std::string& Counter::get_name() const
{
    return name_;
}

int Counter::get_value() const
{
    return value_;
}

void Counter::print() const
{
    std::cout << '[' << name_ << "] " << value_ << '\n';
}
