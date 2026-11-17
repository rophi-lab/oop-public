/*
Exercise 35: Tracing Copies, Moves, and Elision

Goal:
    Predict which special member runs for each line of main, then run the
    program and compare. This exercise is about reading, not writing: Tracer
    is already complete.

Things to think about before you run it:
    - direct construction   building an object straight from its arguments
    - copy construction     building one object from another lvalue
    - move construction     building from something the compiler may gut,
                            such as the result of std::move
    - copy elision          the compiler is allowed to build the object
                            directly in its final home and skip a copy/move
                            entirely, so a constructor call you expected may
                            simply never happen
    - destruction order     automatic objects die in reverse order of
                            construction, at the end of their scope

    Careful with std::move: it does not move anything by itself. It only
    hands the object over as something movable, and the constructor that
    receives it does the actual work.

The program prints one of these labels for each operation that actually runs:
    direct ctor   : <name>
    copy ctor     : <new name> <- <source name>
    move ctor     : <name>
    copy assign   : <name>
    move assign   : <name>
    destructor    : <name>
A moved-from Tracer is renamed <moved-from> before its destructor runs.

--------------------------------------------------------------------------------
TODO 1 -- predict, BEFORE compiling:
    Fill in the table below. For each line write which operation you expect,
    and how many Tracer objects are alive afterwards.

        Tracer first{"first"};              -> ...........................
        Tracer second{first};               -> ...........................
        Tracer third{std::move(first)};     -> ...........................
        Tracer fourth = create_tracer();    -> ...........................

    Then write the order you expect the destructors to run in:
        ...........................................................

TODO 2 -- run it:
        make
        ./tracer_lab
    Compare the real output with your prediction. Where you were wrong, work
    out why. Pay attention to what `first` is called when it is destroyed.

TODO 3 -- how many operations did create_tracer() cost?
    Look at the output for `fourth`. You wrote a whole function that builds a
    local object and returns it by value, yet you probably see far fewer
    operations than you predicted. That is copy elision.

    Now build a second version with elision switched off and compare:
        make noelide
        ./tracer_lab_noelide

    Write down, in a comment at the bottom of this file, which extra line(s)
    appear in the second run and which construction they belong to.

Note:
    Whether the return in create_tracer() costs a move at all depends on
    whether the compiler applies NRVO (named return value optimization), so
    do not be surprised if this differs between compilers.
*/

#include <utility>

#include "tracer.hpp"

Tracer create_tracer()
{
    Tracer result{"result"};
    return result;
}

int main()
{
    Tracer first{"first"};

    Tracer second{first};

    Tracer third{std::move(first)};

    Tracer fourth = create_tracer();

    return 0;
}

// TODO 3 answer -- what changed with -fno-elide-constructors?
//
