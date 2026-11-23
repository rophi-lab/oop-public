#ifndef NODE_HPP
#define NODE_HPP

#include <memory>
#include <string>

/*
Exercise 38: shared_ptr and weak_ptr

Node is written for you -- do NOT change it. It announces its own
construction and destruction, so the output shows exactly when the last
owner let go.

    constructor prints   created: <name>
    destructor  prints   destroyed: <name>

The two link members are public to keep the exercise short. `next` is a
STRONG link (it owns), `prev` is a WEAK link (it only observes).
*/

class Node {
public:
    explicit Node(std::string name);
    ~Node();

    const std::string& name() const;

    std::shared_ptr<Node> next;  // strong: keeps the other node alive
    std::weak_ptr<Node> prev;    // weak:   does not keep anything alive

private:
    std::string name_;
};

#endif  // NODE_HPP
