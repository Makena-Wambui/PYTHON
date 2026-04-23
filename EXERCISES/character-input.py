'''
    Create a program that asks the user to enter their name and their age.
    Print out a message addressed to them that tells them the year that they will turn 100 years old. 
    Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year)
'''




"""
    To get user input, use input().
    Then store the input in a variable, and use it however you want
    What you get from the user will be a string, even if they enter a number

    You can turn the string into an integer using the int() function
    You can turn integers into strings using the str() function
"""


try:
    name = input('What is your name? ')
    age = int(input('What is your age? '))
    current_year = int(input("What is the current year? "))

    if age < 0:
        print('Age cannot be negative.')
    elif age >= 100:
        print('Hello, ' + name + 'You are already 100 years old or older!')
    else:
        year_turn_100 = current_year + (100 - age)
        print('Hello ' + name + '. ' + 'You will turn 100 years old in ' + str(year_turn_100))
except:
    print("Please enter valid values.")
