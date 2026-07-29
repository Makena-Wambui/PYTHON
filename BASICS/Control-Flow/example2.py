"""
Ask the user for two numbers:
    one number to check (call it num) and one number to divide by (check).
    If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

num = int(input("Please enter a number: "))
check = int(input("Please enter another number: "))

if num % 2 == 0:
    print("Your number is even")

    if num % 4 == 0:
        print("Your number is a multiple of 4")

else:
    print("Your number is odd and not a multiple of 4")


if num % check == 0:
    print(f"{check} is a factor of {num}")
else:
    print(f"{check} is not a factor of {num}")
