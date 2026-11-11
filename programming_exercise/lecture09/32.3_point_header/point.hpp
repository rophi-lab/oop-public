#ifndef POINT_HPP
#define POINT_HPP

/*
Exercise 32.3: A Class in Two Files

In-class exercise. The class declaration lives here.
The function bodies live in point.cpp.

What Point needs:
    public
        void set(int x, int y);
            Store both coordinates.
        int get_x() const;
        int get_y() const;
            Read one coordinate. These do not change the point.

    private
        int x_{0};
        int y_{0};
            Already declared below.

The include guard at the top of this file stops the class from being
defined twice when more than one .cpp file includes it.
*/

class Point {
public:
    // TODO: declare set, get_x, and get_y.
    //       A declaration ends with a semicolon.
    //       get_x and get_y are const.

private:
    int x_{0};
    int y_{0};
};

#endif  // POINT_HPP
