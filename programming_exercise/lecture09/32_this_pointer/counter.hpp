#ifndef COUNTER_HPP
#define COUNTER_HPP

#include <string>

/*
Exercise 32: The this Pointer

Goal:
    Learn what `this` is and three common ways to use it inside member
    functions.

What is this?
    Inside a non-static member function, `this` is a pointer to the object
    that the function was called on.

        Counter c;
        c.set_value(5);   // inside set_value, this == &c

    So:
        this->value_     means "the value_ member of THIS object"
        *this            means "the object itself" (a Counter&)

Common uses:
    1. Say explicitly that you mean a member, which matters when a parameter
       shares the member's name.
    2. Hand back the current object so calls can be CHAINED:
           c.reset().add(3).add(2);
       For that to work, the function's return type must be a reference to
       the class, and it must return the object itself.
    3. Ask whether two names refer to the same object by comparing addresses.

--------------------------------------------------------------------------------
What Counter needs (declare here, define in counter.cpp):

    public
        Counter(const std::string& name, int value);
            Already declared below.

        Counter& set_value(int value);
            Store value in the member. The parameter is also named value,
            so write this->value_ to mean the member.
        Counter& add(int amount);
            Increase the stored value by amount.
        Counter& reset();
            Set the stored value back to 0.
            Each of these three returns *this, not this, so calls can chain.
            main does not call reset(); it is still part of the class.

        bool is_same_object(const Counter& other) const;
            True only when this == &other. Compare addresses, not values.

        const std::string& get_name() const;
        int get_value() const;
        void print() const;
            Print one line:  [<name>] <value>

    private
        - the name (std::string) and the value (int)

The constructor and the data members are already written for you as a worked
example. Everything else is yours to add.

Hint:
    "Chainable" means the return type is Counter& rather than void.
*/

class Counter {
public:
    // WORKED EXAMPLE: declaration here, body in counter.cpp. Copy this shape
    // for the members below.
    Counter(const std::string& name, int value);

    // TODO: declare set_value, add, reset, is_same_object, get_name,
    //       get_value, and print.

private:
    std::string name_;
    int value_;
};

#endif  // COUNTER_HPP
