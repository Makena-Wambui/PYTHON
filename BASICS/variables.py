"""
A variable is like a box in computer's memory where you can store a single value

For example if you want to use the result of an evaluated expression later on in your program, you can save it in a variable

You will store values in variables using an assignment statement
    This consists of a variable name, an equal sign called the assignment operator, and the value to be stored.
    The assignment statement spam = 42 - the variable named spam will have the integer value 42 stored in it.

A variable is initialized or created the first time a value is stored in it.
Afterwards, you can use it in expressions with other variables or values
When a variable is assigned a new value, the old value is forgotten - overwriting the variable

Use descriptive variable names so your code is readable
Variable naming conventions:
    Cannot have a space
    Can have letters, numbers or underscore. No hyphen
    Can not start with a number
    Can not have Python keywords like if, for, return

    current_balance / current-balance
    currentBalance / current Balance
"""

spam = 40

print(spam)

eggs = 2

print(eggs)

print(spam + eggs)

print(spam + eggs + spam)

spam = spam + 2
print(spam)  # overwritten spam

message = "Hello"

print(message)


message = "Goodbye"
print(message)

currentBalance = 1000
print(currentBalance)

account4 = 4000
print(account4)

# Can begin with an underscore
_42 = 42
print(_42)

TOTAL_SUM = 2000
print(TOTAL_SUM)

# No special characters - $
# TOTAL_$UM
# print(TOTAL_$UM)

hello = "Hello"
print(hello)

# No special characters in variable names ie ''
# 'hi' = "Hi stranger"
# print('hi')


"""
    Variable names are case sensitive.
    Spam, spam, SPAM, sPAM are all different variable names
    The convention is to start your variable names with lowercase letters instead of uppercase letters ie spam instead of Spam
"""
