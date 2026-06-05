"""

I want my program to keep running.

Let the user choose actions repeatedly

Exit only when the user wants to.

We wrap our entire logic in a while loop that keeps running until the user types exit
"""


def to_upper(text):
    return text.upper()


def to_lower(text):
    return text.lower()


def count_words(text):
    return len(text.split())


def reversal(text):
    return text[::-1]


def count_chars(text):
    return len(text)


def remove_spaces(text):
    return text.strip()


# Map all choices to their respective functions using a dictionary
action_function = {
    1: to_upper,
    2: to_lower,
    3: count_words,
    4: reversal,
    5: count_chars,
    6: remove_spaces,
}
