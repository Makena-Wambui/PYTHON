"""
The if statement is the most common type of flow control statement.

An if statement's clause ie the block following the if statement will execute if the if statement's condition is True
If the condition is False the clause is skipped.
"""

name = "Alice"

# if statement starts with an if keyword
if (
    name == "Alice"
):  # Followed by a condition that evaluates to True or False and a colon
    print("Hi Alice")  # An indented block of code called the if block or if clause


if name == "Mary":
    print("Hi Mary")
