"""
Comparison operators are also known as relational operators
They compare two values and evaluate down to a single Boolean value

== -> Equal To
!= -> Not Equal To
< -> Less Than
> -> Greater Than
<= -> Less Than Or Equal To
>= -> Greater Than Or Equal To

These operators can work with values of any data type

An int or a floating point value will never equal a string value

<, >, <= and >= operators only work properly with integers and floating point values

The equal to operator - == asks whether two values are the same as each other
The assignment operator - = puts the value on the right into the variable on the left
"""

print(42 == 42)  # True
print(42 == 99)  # False
print(2 != 3)  # True
print(2 != 2)  # False

print("hello" == "hello")  # True
print("hello" == "Hello")  # False
print("dog" == "cat")  # False
print("dog" != "cat")  # True
print(True == True)  # True
print(True != True)  # False
print(True != False)  # True
print(42 == 42.0)  # True
print(42 == "42")  # False
print(42 != "42")  # True

print(42 < 100)  # True
print(42 > 100)  # False
print(42 < 42)  # False
print(42 > 42)  # False

eggs = 42
print(eggs <= 42)  # True

my_age = 29
print(my_age >= 10)  # True

her_age = 35
print(her_age > my_age)  # True
