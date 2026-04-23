"""
We are building a simple command line program that:
    Takes user input

    Lets them choose an operation

    Outputs the result
"""

# Step 1: Ask for input:
text = input("Enter some text: ")
print("You entered: ", text)
# print(len(text))


"""
Step 2: Add one transformation for example let's make it uppercase
text = text.upper()
print("Result: ", text)
"""


# Step 3: Add multiple options - menu ie we make the program interactive
print("Choose an option:")
print("1: Uppercase")
print("2: Lowercase")
print("3: Count words")
print("4: Reverse")
print("5: Count characters")
print("6: Remove spaces")


choice = int(input("Enter number of operation you would like to perform: "))


# if choice in list(range(1, 7)):

#     if choice == 1:
#         print("Result: ", text.upper())
#     elif choice == 2:
#         print("Result: ", text.lower())
#     elif choice == 3:
#         words = text.split()
#         print(words)
#         print('Word count: ', len(words))


#         #     Reverse the string using string slicing

#         #     The syntax is [start:stop:step]

#         #     We leave start and stop empty and set step to -1, Python traverses the entire string backwards.
#     elif choice == 4:
#         text = text[::-1]
#         print("Result: ", text)

#     elif choice == 5:
#         number_of_chars = len(text)
#         print('Number of characters: ', number_of_chars)

#     elif choice == 6:
#         # Completely remove all spaces from a string, use the replace() function and replace the whitespace with an empty string
#         # text = text.replace(" ", "")

#         # Remove spaces from the beginning and end of string using strip()
#         # text = text.strip()

#         # Remove spaces only from the start/left using lstrip()
#         # Remove spaces only from the end/right using rstrip()
#         # text = text.rstrip()

#         # Collapse multiple consecutive spaces into a single space, use split then join back with a single space
#         "".join(text.split())
#         print("Space cleanup: ", text)
#         print(len(text))

# else:
#     print('Please enter a valid choice.')


# Lets turn the above logic into separate functions


def convert_to_uppercase(text):
    return text.upper()


def convert_to_lowercase(text):
    return text.lower()


def count_words(text):
    return len(text.split())


def reverse_string(text):
    return text[::-1]


def count_chars(text):
    return len(text)


def remove_spaces(text):
    return text.strip()


# Use a dictionary to map a choice to a function

actions = {
    1: convert_to_uppercase,
    2: convert_to_lowercase,
    3: count_words,
    4: reverse_string,
    5: count_chars,
    6: remove_spaces,
}


if choice in actions:
    # if choice == 1:
    #     print(convert_to_uppercase(text))

    # elif choice == 2:
    #     print(convert_to_lowercase(text))

    # elif choice == 3:
    #     print(count_words(text))

    # elif choice == 4:
    #     print(reverse_string(text))

    # elif choice == 5:
    #     print(count_chars(text))

    # elif choice == 6:
    #     print(remove_spaces(text))
    print(actions[choice](text))

else:
    print("Please choose a valid number.")
