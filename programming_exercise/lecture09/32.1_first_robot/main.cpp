/*
Exercise 32.1: A First Class

In-class exercise. One file, one class, two objects.

Goal:
    A class describes data and behavior. Each object keeps its own data.
    main uses the object through its public functions.

What to build, in this file:
    class Robot
        private
            std::string name_;
        public
            void set_name(const std::string& name);
                Store the name.
            void introduce() const;
                Print one line:  I am <name>.

    main
        Create one robot named Atlas and one named Spot.
        Introduce each robot.

Rules:
    - name_ is private. main cannot write robot.name_.
    - introduce only reads the name, so it is const.

Expected output:
    I am Atlas.
    I am Spot.

How to compile and run (from this folder):
    make
    ./first_robot
*/

#include <iostream>
#include <string>

// TODO: define class Robot here.

int main()
{
    // TODO: create Atlas, set the name, and introduce that robot.

    // TODO: create Spot, set the name, and introduce that robot.

    return 0;
}
