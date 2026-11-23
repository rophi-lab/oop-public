#ifndef RESOURCE_HPP
#define RESOURCE_HPP

#include <string>

/*
Exercise 37: std::unique_ptr

Resource is written for you -- do NOT change it. It announces its own
construction and destruction, so the output tells you exactly when a
unique_ptr frees what it owns.

    constructor prints   acquired: <name>
    use()       prints   using: <name>
    destructor  prints   released: <name>
*/

class Resource {
public:
    explicit Resource(std::string name);
    ~Resource();

    void use() const;
    const std::string& name() const;

private:
    std::string name_;
};

#endif  // RESOURCE_HPP
