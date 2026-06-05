# This program says hello and asks for my name

print(
    "Hello, and Welcome!"
)  # Displays the string value inside its parentheses on the screen

# Ask user for their name
print("What is your name?")

# You can also use print to print a blank line on the screen by passing it no arguments
print()

my_name = input(
    ">> "
)  # Waits for the user to type some text on the keyboard and press ENTER

# print(my_name)


print("It is good to meet you, " + my_name)

print("The length of your name is: ")

print(len(my_name))


# Ask for their age
print("What is your age?")
my_age = input(">> ")

# print(isinstance(my_age, str))


"""
The str() function can be passed an integer value like 29 and will return a string value version of the integer '29'
"""

print("You will be " + str(int(my_age) + 1) + " in a year!")


print("You will be " + str(29) + " in ten years")
