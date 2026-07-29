"""
You can use if and else if you want only one of the clauses to be executed

You may have a case where you want one of many possible clauses to execute

elif statement is an else if statement that always follows an if statement or an elif statement

provides another condition that is checked only if all the previous conditions are False

has an elif keyword
a condition that evaluates to True or False
a colon
elif clause or elif block
"""

name = "Alice"
age = 33

if name == "Alice":
    print("Hi Alice")
elif age < 12:
    """
    The elif clause executes if name == 'Alice' is False and age < 12 is True

    If none of the conditions in both if and elif are True, then none of the clauses are executed

    In a chain of elif statements, only one or none of the clauses will be exceuted
    If one of the elif statement's condition is found to be True, the other elif statements are skipped.
    """
    print("You are not Alice, kiddo")
