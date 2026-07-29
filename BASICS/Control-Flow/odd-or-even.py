# Ask the user for a number
num = int(input("Please enter a number >> "))

print(type(num))

# Depending on whether the number is even or odd, print out an appropriate message to the user

# if we divide a number by 2 and the remainder is 0, it is even so we use the modulus operator

if num % 2 == 0:
    print("Your number is even")

    if num % 4 == 0:
        print("Your number is a multiple of 4")

else:
    print("Your number is odd and not a multiple of 4")
