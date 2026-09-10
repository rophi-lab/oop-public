"""
Exercise 07: Date and Time Practice

Goal:
    Given a date written as a string like "2026-12-31", return how many days
    from today until that date.

Why this exercise?
    Dates look like plain text, but you cannot do math on text. This exercise
    teaches the essential pattern of PARSING a string into a real `date`
    object, doing arithmetic on it, and reading the result. Subtracting two
    dates gives a `timedelta`, whose `.days` attribute is the answer.

Useful tools:
    - from datetime import date, datetime
    - datetime.strptime("2026-12-31", "%Y-%m-%d").date() -> parse the string
    - date.today()          -> today's date
    - date_b - date_a       -> a timedelta
    - timedelta.days        -> the whole number of days in that gap

Tip:
    Because the result depends on today's date, the exact number you print will
    change over time. That is expected. If the target date is today, the
    answer is 0; tomorrow is 1; yesterday is -1.

TODO:
    1. Convert the target_date string into a real date object.
    2. Subtract today's date from it and return the number of days.
"""


def days_until(target_date):
    """
    Input: A string of a date, e.g., "2026-12-31"
    Output: The number of days until the target date (negative if it is past)
    Example (suppose today is 2026-09-09):
    Input: "2026-09-09"
    Output: 0   # today
    Input: "2026-09-10"
    Output: 1   # tomorrow
    Input: "2026-09-08"
    Output: -1  # yesterday
    Hint: Parse the string with datetime, compare with date.today(), and
    use the .days attribute of the resulting timedelta.
    """
    # TODO: convert the string to a date and return the day difference
    return ...


# A date later this year so a typical run prints a positive number.
# Change it and re-run to see how the result moves with today's date.
target_date = "2026-12-31"
print(days_until(target_date))
