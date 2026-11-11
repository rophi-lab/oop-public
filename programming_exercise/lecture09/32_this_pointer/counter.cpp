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
