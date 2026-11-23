#include "resource.hpp"

#include <iostream>
#include <utility>

Resource::Resource(std::string name)
    : name_(std::move(name))
{
    std::cout << "acquired: " << name_ << '\n';
}

Resource::~Resource()
{
    std::cout << "released: " << name_ << '\n';
}

void Resource::use() const
{
    std::cout << "using: " << name_ << '\n';
}

const std::string& Resource::name() const
{
    return name_;
}
