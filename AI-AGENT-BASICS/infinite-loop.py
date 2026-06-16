"""
True is a Boolean value

True is always true

We use while True when we do not know in advance how many times something should happen

So instaed of limiting how many times something should happen, we use while True and let the user decide when to stop.
"""

while True:  # starts the infinite loop
    """
    We are saying, keep running the code below forever
    This code never stops on its own

    To stop this code from running infinitely, we use break
    """
    # print("Hello")
    answer = input("Type 'exit' to exit: ")  # asks the user for input
    # print(answer)

    if (
        answer == "exit"
    ):  # if the user types exit, we execute break, which immediately exits the loop
        break

    print(
        "You typed ", answer
    )  # if the user types anything else, it is printed on the screen

print(
    "The program ended."
)  # This part of the program continues as usual when the loop is terminated by break
