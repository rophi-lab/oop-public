/*
Exercise 25: Working with std::string

Goal:
    Practice the most common std::string operations: create, read, measure,
    concatenate, search, extract, and modify.

Useful std::string members (include <string>):
    - s.size() / s.length()   -> how many characters
    - s.empty()               -> true if the string has length 0
    - s[i]                    -> character at index i (0-based)
    - s + t                   -> concatenate two strings
    - s += t                  -> append to the end
    - s.substr(pos, count)    -> copy count characters starting at pos
    - s.find(needle)          -> index of needle, or std::string::npos if missing
    - s.push_back(ch)         -> add one character at the end

--------------------------------------------------------------------------------
TODO:
    Fill in each TODO below. Leave the includes and the declared
    `sentence` variable as they are.

    1. Read a full line of text into `sentence` with std::getline.
    2. Print how many characters are in the sentence.
    3. Print whether the sentence is empty, as the words true or false.
       Use the manipulator std::boolalpha. Without it, C++ prints 1 and 0.
       An empty line is only for this step.
    4. Print the first character and the last character.
       Assume the sentence is not empty for this step and the ones after it.
    5. Build a greeting string "Hello, " + sentence + "!" and print it.
    6. If the sentence contains the text "C++", print
           Found C++
       otherwise print
           No C++ found
       Use find(). A substring match is enough, so xC++y counts.
    7. Print the first three characters of the sentence using substr.
       Assume the user types at least three characters for this step.
    8. Append "!!!" to a copy of the sentence and print that copy.
       The original sentence must stay unchanged.

Example run:
    Enter a sentence: I love C++
    length: 10
    empty: false
    first: I
    last: +
    Hello, I love C++!
    Found C++
    first three: I l
    with bangs: I love C++!!!

How to compile and run (from this folder):
    make
    ./string_lab
*/
#include <iostream>
#include <string>

int main() {
    std::string sentence;

    // TODO 1: prompt with "Enter a sentence: " and read the whole line.


    // TODO 2: print  length: <number of characters>


    // TODO 3: print  empty: <true or false>
    //         Use std::boolalpha so the words true and false appear.
    //         Without it, C++ prints 1 and 0.
    //         An empty line is only for this step.


    // TODO 4: print the first and last characters on their own lines.
    //         Hint: the last character sits one before the size.
    //         Assume the sentence is not empty from here on.


    // TODO 5: build a greeting string of the form "Hello, <sentence>!"
    //         and print it.


    // TODO 6: report whether the sentence contains the text "C++".
    //         Hint: find() returns std::string::npos when there is no match.
    //         A substring match is enough, so xC++y counts.
    //         Print either  Found C++  or  No C++ found


    // TODO 7: print  first three: <first three characters>


    // TODO 8: copy the sentence, append "!!!" to the COPY, and print it as
    //         with bangs: <copy>       (the original must stay unchanged)

    return 0;
}

// Expected Output (for the example input "I love C++"):
// length: 10
// empty: false
// first: I
// last: +
// Hello, I love C++!
// Found C++
// first three: I l
// with bangs: I love C++!!!
