print(isinstance(20, int))


print(isinstance(str(20), str))

# The addition operator can only be used to add numbers together or concatenate strings together
# print("I am " + 40 + " years old") will throw a TypeError: can only concatenate str (not "int") to str

print("I am " + str(40) + " years old")

# str(), int() and float() will evaluate to the string, integer and floating point forms of the value you pass to them

# The input() function always returns a string even if the user entered a number

spam = input()

print(type(spam))

# The value stored inside spam is not the integer 101 but the string '101'
# If you want to do math using the value in spam, use the int() function to get its integer form,
# then store it as the variable's new value

spam = int(spam)
print(type(spam))

print(spam * 10 / 5)

# The round() function takes a float value and returns the nearest integer.
print(round(3.14))
