/*
Exercise 26: Score Analyzer

Goal:
    Build a small program that reads a student name and five scores (0-100),
    then prints the average (two decimals) and a letter grade.

Why split into helper functions?
    - is_valid_score      -> checks whether ONE score is in range
    - calculate_average   -> averages the array of scores
    - determine_grade     -> turns an average into A/B/C/D/F
    - main                -> coordinates input, processing, and output

    main describes the overall flow; helpers handle individual tasks.

Grade rules:
    average >= 90 -> 'A'
    average >= 80 -> 'B'
    average >= 70 -> 'C'
    average >= 60 -> 'D'
    otherwise     -> 'F'

--------------------------------------------------------------------------------
TODO:
    1. Finish is_valid_score, calculate_average, and determine_grade.
    2. In main: read the name with getline, then read five valid scores.
       If input is bad or out of range, clear cin, ignore the rest of the
       line, and ask again (see the while loop scaffold).
    3. Print the student name, average (2 decimals), and grade.

Example run:
    Enter student name: Alice Kim
    Enter score 1: 90
    Enter score 2: 85
    Enter score 3: 92
    Enter score 4: 88
    Enter score 5: 95

    Student: Alice Kim
    Average: 90.00
    Grade: A

How to compile and run (from this folder):
    make
    ./score_analyzer
*/

#include <array>
#include <iomanip>
#include <iostream>
#include <limits>
#include <string>

// TODO: return true if score is between 0 and 100 (inclusive).
bool is_valid_score(int score)
{
}

// TODO: add up the scores and return their average.
// Hint: summing ints and dividing by an int gives you an int. Convert the
//       total to double before dividing so the fraction survives.
double calculate_average(std::array<int, 5> scores)
{
}

// TODO: return 'A', 'B', 'C', 'D', or 'F' using the grade rules above.
// Hint: check the highest cut-off first, then work downwards.
char determine_grade(double average)
{
}

int main()
{
    std::string student_name{};
    std::array<int, 5> scores{};

    // TODO: prompt with "Enter student name: " and read the whole line.

    for (std::size_t i{0}; i < scores.size(); ++i)
    {
        while (true)
        {
            std::cout << "Enter score " << i + 1 << ": ";

            // TODO: read into scores[i] and leave this loop only when the read
            //       SUCCEEDED and the value passes is_valid_score.
            //       Hint: `std::cin >> x` can itself be tested as a condition.
            //       Without this the loop below never ends.

            std::cout << "Enter a number from 0 to 100.\n";

            // Clear the fail state and throw away the rest of the line.
            std::cin.clear();
            std::cin.ignore(
                std::numeric_limits<std::streamsize>::max(),
                '\n'
            );
        }
    }

    // TODO: use your helper functions to get the average and the grade.

    // TODO: print the blank line, then the Student, Average, and Grade lines
    //       exactly as shown in the example run. The average needs two
    //       decimal places.

    return 0;
}
