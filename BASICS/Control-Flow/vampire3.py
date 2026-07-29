"""
You can have an optional else statement after the last elif statement
Only one of the clauses will be executed.

If the conditions in each if and elif statement are False, then the else clause is executed

There is always exactly one if statement
Any necessary elif statements should follow the if statement
If you want to be sure that at least one clause is executed, close the structure with an else statement
"""

name = "Carol"
age = 3000

if name == "Alice":
    print("Hi Alice")
elif age < 12:
    print("You are not Alice, kiddo")
else:
    print("I dont know you!")
