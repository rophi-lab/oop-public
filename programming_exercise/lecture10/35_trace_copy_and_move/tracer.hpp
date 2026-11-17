#ifndef TRACER_HPP
#define TRACER_HPP

#include <string>

/*
Exercise 35: Tracing Copies, Moves, and Elision

Tracer is written for you -- do NOT change it. Every special member announces
itself, so running a program tells you exactly which operations the compiler
chose.

The five special members plus the normal constructor:
    Tracer(std::string)        the ordinary ("direct") constructor
    Tracer(const Tracer&)      copy constructor
    Tracer(Tracer&&)           move constructor
    operator=(const Tracer&)   copy assignment
    operator=(Tracer&&)        move assignment
    ~Tracer()                  destructor

A moved-from Tracer renames itself to <moved-from>, so you can still tell the
two objects apart when their destructors run.
*/

class Tracer {
public:
    explicit Tracer(std::string name);

    Tracer(const Tracer& other);
    Tracer(Tracer&& other) noexcept;

    Tracer& operator=(const Tracer& other);
    Tracer& operator=(Tracer&& other) noexcept;

    ~Tracer();

    const std::string& name() const;

private:
    std::string name_;
};

#endif  // TRACER_HPP
