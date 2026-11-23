/*
Exercise 37: std::unique_ptr

Goal:
    Redo the memory management from Exercise 36 without writing a single
    new or delete, and watch ownership move from one pointer to another.

What a unique_ptr is:
    std::unique_ptr<T> is a pointer that OWNS what it points at. When it goes
    out of scope it deletes that object for you. Exactly one unique_ptr may
    own a given object at a time, which is where the name comes from.

    #include <memory> to use it.

Making one:
    auto p = std::make_unique<Resource>("engine");   // one object
    auto a = std::make_unique<int[]>(5);             // an array of 5 ints

    Prefer make_unique over writing new yourself; then your code contains no
    raw new at all.

Using one:
    p->use()        call a member, just like a raw pointer
    *p              the object itself
    p.get()         the raw pointer, when some old API demands one
    if (p)          true while p owns something, false when it is empty
    p.reset()       free what it owns right now, and become empty

Ownership is unique, so:
    - a unique_ptr CANNOT be copied; that would create a second owner
    - it CAN be moved with std::move, which transfers ownership and leaves
      the source empty
    - returning one from a function is the normal way to hand ownership back
      to the caller

--------------------------------------------------------------------------------
TODO -- work through main below in order:

    1. Make a unique_ptr<Resource> named "engine", then call use() on it.

    2. Move ownership into a second unique_ptr. Then print
           engine is empty: true
       An empty unique_ptr compares equal to nullptr. Print the bool with
       std::boolalpha, otherwise the line shows 1 instead of true.
       Call use() through the new owner to prove the object itself is untouched.

    3. Free it early with reset(), then print
           moved is empty: true
       Notice the released line appears at the reset, not at the end of main.

    4. Finish make_resource() below so it hands a new Resource back to the
       caller, then use it from main. The sensor stays alive until main
       ends, so its released line is the last line of the program.

    5. Make a unique_ptr to an array of 5 ints, fill element i with i * i,
       and print
           squares: 0 1 4 9 16
       You index it like a normal array. Note there is no delete[] anywhere.

Expected output:
    acquired: engine
    using: engine
    engine is empty: true
    using: engine
    released: engine
    moved is empty: true
    acquired: sensor
    using: sensor
    squares: 0 1 4 9 16
    released: sensor

Part B:
    The program you hand in must compile, so leave the copy line commented
    out. You may uncomment it, read the error, and comment it out again.
    Then answer in a comment: why does the library forbid this, and which
    single word turns the same line into legal code?

Count the deletes:
    When you are done, search this file and resource.cpp for the word
    "delete". You should find none, yet every resource is released.

How to compile and run (from this folder):
    make
    ./unique_ptr_lab
*/

#include <iostream>
#include <memory>
#include <utility>

#include "resource.hpp"

// TODO 4: return a unique_ptr<Resource> built from the given name.
//         Replace the line below.
std::unique_ptr<Resource> make_resource(const std::string& name)
{
    (void)name;
    return nullptr;
}

int main()
{
    // TODO 1: create the "engine" resource and use it.

    // TODO 2: move ownership into a second unique_ptr, report that the first
    //         one is now empty, and use the resource through the new owner.

    // TODO 3: release it early with reset(), then report that the owner is
    //         empty too.

    // TODO 4: get a "sensor" resource from make_resource and use it.

    // TODO 5: make an array of 5 ints, fill it with squares, and print them.

    // ---------- Part B ----------
    // Leave this commented out in the program you hand in.
    //
    // std::unique_ptr<Resource> second_owner = engine;

    return 0;
}
