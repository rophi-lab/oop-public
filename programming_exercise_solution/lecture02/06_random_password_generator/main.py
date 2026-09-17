"""
Exercise 06: Random Password Generator

Goal:
    Generate a random password of a given length that always contains at least
    one lowercase letter, one uppercase letter, and one digit.

Why this exercise?
    This teaches you to work with the `random` and `string` modules and to
    satisfy CONSTRAINTS while generating data. It is easy to generate a random
    string; it is a little harder to guarantee it always meets the rules. The
    common trick is: first force in one of each required character, then fill
    the rest randomly, and finally shuffle so the forced characters are not
    always at the front.

Useful tools:
    - string.ascii_lowercase / ascii_uppercase / digits -> character pools
    - random.choice(pool)   -> pick one random character from a pool
    - random.shuffle(list)  -> shuffle a list in place
    - "".join(list_of_chars) -> turn a list of characters back into a string

Tip:
    Build the password as a LIST of characters first (easy to shuffle), then
    join it into a string at the end. Import what you need:
        import random
        import string
    Assume length is at least 3 so one of each required character fits.

TODO:
    1. Guarantee at least one lowercase, one uppercase, and one digit.
    2. Fill the remaining characters randomly from all allowed characters.
    3. Shuffle and return the final password as a string of the given length.
"""

import random
import string


def random_password_generator(length):
    """
    Input: An integer length, e.g., 10 (assume length >= 3)
    Output: A string of a random password of the given length
    Characters to use: "a-z, A-Z, 0-9"
    Make sure the password contains:
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    Example:
    Input: 10
    Output: "aB1c2D3e4F"   # illustrative; your result will differ each run
    Hint: Use the random and string modules to pick and shuffle characters.
    """
    # TODO: generate and return a password that satisfies the requirements
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    all_characters = lowercase + uppercase + digits

    # Force one of each required character type first.
    password_characters = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
    ]

    # Fill the remaining length with random characters from the full pool.
    while len(password_characters) < length:
        password_characters.append(random.choice(all_characters))

    # Shuffle so the required characters are not always at the front.
    random.shuffle(password_characters)
    return "".join(password_characters)


length = 10
print(random_password_generator(length))
