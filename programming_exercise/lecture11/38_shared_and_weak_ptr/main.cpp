/*
Exercise 38: std::shared_ptr and std::weak_ptr

Goal:
    In Exercise 37 exactly one unique_ptr owned each object. Here several
    owners share one object, and you learn what that costs.

std::shared_ptr<T>
    A pointer that shares ownership. Every shared_ptr aimed at the same
    object bumps a REFERENCE COUNT. The object is destroyed the moment the
    count reaches zero -- that is, when the last owner goes away.

        auto p = std::make_shared<Node>("a");   // count is 1
        auto q = p;                             // count is 2, no new object
        p.use_count()                           // ask what the count is
        p.reset()                               // this owner lets go

    Copying a shared_ptr is allowed and cheap; that is the whole difference
    from unique_ptr.

std::weak_ptr<T>
    A non-owning observer of a shared_ptr's object. It does NOT change the
    count and cannot keep anything alive.

        std::weak_ptr<Node> w = p;   // count unchanged
        w.expired()                  // true once the object is gone
        w.lock()                     // returns a shared_ptr: valid if the
                                     // object still lives, empty if not

    You cannot dereference a weak_ptr directly. Calling lock() is how you ask
    "is it still there?" and get a safe owner back in one step.

The problem weak_ptr exists to solve:
    If two objects hold shared_ptrs to each other, each keeps the other's
    count above zero forever. Neither is ever destroyed, even after every
    external owner is gone. That is a reference CYCLE, and it leaks. Making
    one of the two links weak breaks the cycle.

--------------------------------------------------------------------------------
TODO -- work through main below in order.

Expected output:
    created: engine
    count after create: 1
    count inside scope: 2
    count after scope: 1
    count with weak_ptr: 1
    lock succeeded, count: 2
    destroyed: engine
    expired after reset: true
    lock returns null: true
    --- cycle: two strong links ---
    created: A
    created: B
    A use_count: 2
    (nothing was destroyed when that scope ended)
    --- fixed: one weak link ---
    created: C
    created: D
    C use_count: 1
    destroyed: C
    destroyed: D
    (both were destroyed when that scope ended)

Read those last two blocks carefully. In the first, no "destroyed" line ever
appears: A and B leaked. In the second, both destroyed lines appear BEFORE
the closing message. C is destroyed before D: the local c is C's only owner,
and destroying C then releases D through next.

Part B -- see the leak for yourself:
        make asan
        ./shared_ptr_lab_asan
    The sanitizer reports a leak. Work out from its size and count which two
    objects it is complaining about, then answer in a comment: why can the
    sanitizer still see them as leaked even though the program used smart
    pointers everywhere?

How to compile and run (from this folder):
    make
    ./shared_ptr_lab
*/

#include <iostream>
#include <memory>

#include "node.hpp"

int main()
{
    std::cout << std::boolalpha;

    // ---------- Part 1: sharing and the reference count ----------
    // TODO: make a shared_ptr<Node> named "engine", then print
    //           count after create: <count>

    // TODO: open a nested scope { }. Inside it, copy the shared_ptr into a
    //       second variable and print
    //           count inside scope: <count>
    //       Notice no second node is created -- both point at the same one.

    // TODO: after the scope closes, print
    //           count after scope: <count>
    //       The copy let go when it went out of scope.

    // ---------- Part 2: observing without owning ----------
    // TODO: make a weak_ptr that watches the same node, then print
    //           count with weak_ptr: <count>
    //       Confirm for yourself that watching did not change the count.

    // TODO: lock() the weak_ptr inside an if statement so you only use the
    //       result when it is valid, and print
    //           lock succeeded, count: <count>
    //       Print the count of the shared_ptr that lock() returned.
    //       That temporary owner is why the count is one higher here.

    // TODO: let the last owner go with reset(). The destroyed line appears
    //       right here, not at the end of main. Then print
    //           expired after reset: <true or false>
    //           lock returns null: <true or false>

    // ---------- Part 3: a cycle that leaks ----------
    std::cout << "--- cycle: two strong links ---\n";
    {
        // TODO: create two shared nodes "A" and "B". Point A's next at B and
        //       B's next at A, so each one owns the other. Then print
        //           A use_count: <count>
        //       and ask yourself who the second owner is.
    }
    std::cout << "(nothing was destroyed when that scope ended)\n";

    // ---------- Part 4: the same shape, without the leak ----------
    std::cout << "--- fixed: one weak link ---\n";
    {
        // TODO: create two shared nodes "C" and "D". Point C's next at D as
        //       before, but make the link back from D a WEAK one by using
        //       its prev member instead. Then print
        //           C use_count: <count>
        //       Compare that number with Part 3 and explain the difference.
    }
    std::cout << "(both were destroyed when that scope ended)\n";

    return 0;
}
