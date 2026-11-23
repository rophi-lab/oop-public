#include "point.hpp"

// TODO: define set, get_x, and get_y.
//       Each definition starts with Point::
//       Repeat const on get_x and get_y.
void Point::set(int x, int y)
{
    x_ = x;
    y_ = y;
}

int Point::get_x() const
{
    return x_;
}

int Point::get_y() const
{
    return y_;
}
