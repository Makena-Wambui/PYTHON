# This is a simple example of how to read a file and compare it to user input.
# First, we open the file that contains the secret password.  We call the open() function and pass it the name of the file we want to open.  This returns a file object that we can use to read the contents of the file.
password_file = open("SecretPasswordFile.txt")

# Next, we read the contents of the file using the read() method of the file object.  This returns a string that contains the contents of the file.  We store this string in a variable called secret_password.
secret_password = password_file.read()

# print(secret_password)

print("Enter your password:")

# Prompt the user to enter their password using the input() function.  This function waits for the user to type something and then returns that input as a string.  We store this string in a variable called typed_password.
typed_password = input()


# Finally, we compare the typed password to the secret password using an if statement.  If the two passwords match, we print "Access Granted".  If they do not match, we print "Access Denied".

if typed_password == secret_password:
    print("Access Granted")
else:
    print("Access Denied")
