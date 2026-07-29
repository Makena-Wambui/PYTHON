"""
The order of elif statements matters

The rest of the elif clauses are automatically skipped once a True condition has been found.
"""

name = "Carol"
age = 3000

if name == "Alice":
    print("Hi Alice")
elif age < 12:
    print("You are not Alice, kiddo")
elif age > 100:
    print("You are not Alice, grannie!")
elif age > 2000:  # True but skipped because the previous elif condition is True
    print("Unlike you, Alice is not a vamp!")
