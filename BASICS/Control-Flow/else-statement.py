"""
if clause can optionally be followed by an else statement

else clause is executed only when the if statement's condition is False

else statement does not have a condition
"""

name = "Mary"

if name == "Alice":
    print("Hi Alice")
else:  # else statement begins with an else keyword, has no condition and ends with a colon
    print("Hi stranger")  # This is the else block or else clause
