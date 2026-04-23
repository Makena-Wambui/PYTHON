
# Ask the user for a string.
# Print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)
# For example: mom, radar, level

# Solution done using string slicing


your_string = input("Enter a string: ")

#print(your_string)


#convert your_string to a str
your_string = str(your_string)


# reverse the string
reversed_str = your_string[::-1]
print(reversed_str)

if (your_string == reversed_str):
    print("Your string is a palindrome.")
else:
    print("Your string is not a palindrome.")
