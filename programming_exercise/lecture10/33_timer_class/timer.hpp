#ifndef TIMER_HPP
#define TIMER_HPP

#include <string>

/*
Exercise 33: A Timer Class -- = delete and explicit

Goal:
    Write a small class that announces when it starts and when it finishes,
    then lock down two ways it could be misused.

Concept 1 -- = delete
    Writing            SomeClass() = delete;
    removes a function instead of defining it. Any attempt to use it becomes
    a COMPILE error rather than a run-time surprise. Use it to forbid an
    operation that makes no sense for your type.

Concept 2 -- explicit
    A constructor that takes one argument normally doubles as an implicit
    conversion, so  Timer t = some_string;  would quietly build a Timer out
    of a string. Marking the constructor explicit means the caller has to ask
    for it by name:  Timer t{some_string};

Why both here?
    A Timer with no name has nothing sensible to print, so default
    construction should be impossible. And a std::string is not a Timer, so
    it should never turn into one behind your back.

--------------------------------------------------------------------------------
What Timer needs (declare here, define in timer.cpp):

    public
        Timer() = delete;
            `Timer t;` must not compile.

        explicit Timer(const std::string& name);
            The only way to create a Timer. `explicit` rejects
            Timer t = std::string{"Nope"};
            Timer t{"Simulation"}; remains valid.

        ~Timer();
            The constructor prints    Start: <name>
            The destructor prints     End: <name>

    private
        std::string name_;
            Already declared below.

Hints:
    - A removed function still needs a declaration; you just say = delete
      where the semicolon would go.
    - Taking the name by const reference avoids copying it.
    - Both keywords belong in this header only, never on the definitions in
      the .cpp file.
*/

class Timer {
private:
    std::string name_;

public:
    // TODO: remove the default constructor, so `Timer t;` will not compile.

    // TODO: declare the constructor that takes the timer's name, and stop it
    //       from being used as an implicit conversion.

    // TODO: declare the destructor.
};

#endif  // TIMER_HPP
