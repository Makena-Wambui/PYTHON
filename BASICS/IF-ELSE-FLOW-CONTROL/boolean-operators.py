"""
There are three Boolean operators : and, or, not

They are used to compare Boolean values

Just like with comparison operators, they evaluate expressions down to a single Boolean value.

and operator always takes two Boolean values or expressions hence considered to be a binary Boolean operator
Evaluates an expression to True if both Boolean values are True
Otherwise evaluates to False
"""

print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False


"""
The or operator also always takes two Boolean values or expressions
Hence is also a bianary Boolean operator
Evaluates an expression to True if either of the two Boolean values is True
Evaluates to False if both are False
"""

print(True or True)  # True
print(True or False)  # True
print(False or False)  # False
print(False or True)  # True


"""
The not operator operates only on one Boolean value or expression
Hence it is a unary operator
Evaluates to the opposite Boolean value

You can also use multiple not operators
"""
print(not True)  # False
print(not False)  # True
print(not not False)  # False
print(not not not False)  # True
print(not not not not False)  # False
