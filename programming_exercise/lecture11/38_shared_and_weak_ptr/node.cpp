#include "node.hpp"

#include <iostream>
#include <utility>

Node::Node(std::string name)
    : name_(std::move(name))
{
    std::cout << "created: " << name_ << '\n';
}

Node::~Node()
{
    std::cout << "destroyed: " << name_ << '\n';
}

const std::string& Node::name() const
{
    return name_;
}
