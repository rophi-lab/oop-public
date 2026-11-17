#ifndef PLAYLIST_HPP
#define PLAYLIST_HPP

#include <string>
#include <vector>

/*
Exercise 34: The Rule of Zero

Goal:
    Build a class that copies correctly WITHOUT writing a single copy
    constructor, assignment operator, or destructor.

The Rule of Zero:
    If every member of your class already knows how to copy, move, and clean
    up after itself, then the special members the compiler generates for you
    do exactly the right thing. The best code here is no code at all.

    std::string and std::vector are members like that. Each one owns its own
    heap memory and handles copying and destruction internally, so a class
    assembled only from them inherits that correctness for free.

    Compare that with a class holding a raw pointer from new[]. The generated
    copy constructor would copy only the pointer, two objects would end up
    freeing the same memory, and you would be forced to write all five
    special members by hand.

--------------------------------------------------------------------------------
What Playlist needs (declare here, define in playlist.cpp):

    public
        explicit Playlist(const std::string& name);
            Store the name. explicit, so a string does not become a Playlist
            by itself.

        void add_song(const std::string& song);
            Append one song. push_back grows the vector at the back.

        void print() const;
            Print exactly:
                Playlist: <name>
                - <song>
                - <song>
            One song per line. No blank line after the last song.

    private
        std::string name_;
        std::vector<std::string> songs_;
            Already declared below. Both already copy and destroy themselves.

Rules:
    - Do NOT declare a copy constructor, copy assignment, move constructor,
      move assignment, or destructor anywhere. That restraint IS the exercise.

Hints:
    - A vector grows at the back with push_back.
    - print() does not change the object, so mark it const.
    - Loop over the songs without copying each one by using a const reference
      as the loop variable.
*/

class Playlist {
private:
    std::string name_;
    std::vector<std::string> songs_;

public:
    // TODO: declare the constructor, add_song, and print.
};

#endif  // PLAYLIST_HPP
