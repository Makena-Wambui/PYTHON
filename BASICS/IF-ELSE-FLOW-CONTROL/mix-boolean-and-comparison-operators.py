"""
Comparison operators evaluate to Boolean values, hence can be used in expressions with Boolean operators

NB: The Boolean operators and, or, not are called so because they operate on Boolean values True and False

4 < 5 expression is not a Boolean value but evaluates down to a Boolean value

You can also use multiple Boolean operators in an expression along the comparison operators.
Boolean operators also have an order of operations just like math operators
First any math and comparison operators evaluate,
    then the not operators
        then the and operators
            then the or operators
"""

print((4 < 5) and (5 < 6))  # True
print((4 < 5) and (9 < 6))  # False
print((1 == 2) or (2 == 2))  # True

spam = 4
print(2 + 2 == spam and not 2 + 2 == (spam + 1) and 4 == 2 + 2)
