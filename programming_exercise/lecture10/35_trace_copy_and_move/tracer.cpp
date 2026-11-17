#include "tracer.hpp"

#include <iostream>
#include <utility>

Tracer::Tracer(std::string name)
    : name_(std::move(name))
{
    std::cout << "direct ctor   : " << name_ << '\n';
}

Tracer::Tracer(const Tracer& other)
    : name_(other.name_ + " (copy)")
{
    std::cout << "copy ctor     : " << name_ << " <- " << other.name_ << '\n';
}

Tracer::Tracer(Tracer&& other) noexcept
    : name_(std::move(other.name_))
{
    other.name_ = "<moved-from>";
    std::cout << "move ctor     : " << name_ << '\n';
}

Tracer& Tracer::operator=(const Tracer& other)
{
    if (this != &other) {
        name_ = other.name_ + " (copy-assigned)";
    }
    std::cout << "copy assign   : " << name_ << '\n';
    return *this;
}

Tracer& Tracer::operator=(Tracer&& other) noexcept
{
    if (this != &other) {
        name_ = std::move(other.name_);
        other.name_ = "<moved-from>";
    }
    std::cout << "move assign   : " << name_ << '\n';
    return *this;
}

Tracer::~Tracer()
{
    std::cout << "destructor    : " << name_ << '\n';
}

const std::string& Tracer::name() const
{
    return name_;
}
