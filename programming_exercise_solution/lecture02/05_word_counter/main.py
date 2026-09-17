"""
Exercise 05: Word Counter

Goal:
    Given a string of text, return a dictionary describing its words: the total
    number of words, the number of unique words, and how many times each word
    appears.

Why this exercise?
    Counting how often things occur is one of the most common tasks in
    programming (word frequencies, log analysis, tallying votes, ...). This is
    also your first taste of building a "frequency table" with a dictionary,
    where the key is the thing you are counting and the value is the count.

Useful tools:
    - text.split()            -> break a string into a list of words
    - len(words)              -> total number of words
    - set(words)              -> the collection of unique words
    - counts.get(word, 0) + 1 -> safely increment a count that may not exist yet

Tip:
    "total_words" counts every word including repeats, while "unique_words"
    counts each distinct word only once. len(set(words)) gives the latter.

TODO:
    1. Split the text into words.
    2. Count total words, unique words, and each word's frequency.
    3. Return them in one dictionary using the exact keys shown below.
"""


def count_words(text):
    """
    Input: A string of text, e.g., "hello world hello"
    Output: A dictionary with the following keys:
    - "total_words": the total number of words in the text
    - "unique_words": the number of unique words in the text
    - "word_frequency": a dictionary with the frequency of each word
    Example:
    Input: "hello world hello"
    Output: {
        "total_words": 3,
        "unique_words": 2,
        "word_frequency": {"hello": 2, "world": 1}
    }
    Hint: Use split() to break the text into words. Do not worry about
    punctuation in this exercise -- the sample text has none.
    """
    # TODO: count all words, unique words, and each word's frequency
    words = text.split()

    word_frequency = {}
    for word in words:
        # If the word is new, start at 0, then add 1.
        word_frequency[word] = word_frequency.get(word, 0) + 1

    return {
        "total_words": len(words),
        "unique_words": len(set(words)),
        "word_frequency": word_frequency,
    }


text = "hello world hello"
print(count_words(text))
