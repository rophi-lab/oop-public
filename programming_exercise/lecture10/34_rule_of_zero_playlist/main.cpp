/*
Exercise 34: The Rule of Zero

Goal:
    Implement Playlist in playlist.hpp / playlist.cpp, copy a playlist, change
    the copy, and confirm the original was not touched -- all without writing
    any copy, move, or destructor code yourself.

Expected output:
    Playlist: Favorites
    - Song A
    - Song B
    Playlist: Favorites
    - Song A
    - Song B
    - Song C

    The first block is the original and the second is the copy. The original
    still has two songs, which proves the compiler-generated copy constructor
    made a genuine deep copy: the two vectors are separate.

How to compile and run (from this folder):
    make
    ./playlist_lab
*/

#include <iostream>

#include "playlist.hpp"

int main()
{
    // TODO: create a Playlist named "Favorites" and add "Song A" and "Song B".

    // TODO: copy-construct a second playlist from the first, then add
    //       "Song C" to the copy only:
    //           Playlist copy{favorites};
    //       That calls the compiler-generated copy constructor.
    //       Playlist copy = favorites; does the same thing, because the
    //       object is being created. It is not assignment.
    //       There is no default constructor, so Playlist copy; will not compile.

    // TODO: print the original first, then the copy, and check the output
    //       against the expected block above.

    // TODO (written answer): why does this class need no custom copy, move,
    // or destructor? Answer in a sentence or two right here as a comment.
    // Think about what name_ and songs_ each do when they are copied.

    return 0;
}
