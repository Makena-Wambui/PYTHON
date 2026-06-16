import requests

"""
Foundation of Agents - to decide what API or function to call, and how to call it, based on the input and the context.

At a high level, an agent is a system that can perceive its environment, make decisions, and take actions to achieve specific goals. 
In the context of AI, agents can be designed to perform various tasks, such as answering questions, providing recommendations, or even controlling physical devices.

Input
  |
Decison
  |
Action
  |
Result


Input - Show me information about Octocat
Decison - User wants Github information about Octocat
Action - Call Github API to get information about Octocat
Result - Display the information about Octocat to the user


Input - Make this text uppercase
Decision - User wants text transformed to uppercase
Action - Call uppercase function
Result - return the transformed text to the user


In today's exercise:
    Create a program that can:
        Get Github user information
        Transform the text to uppercase
        Count words 
        Exit the program
    The program will decide what action to perform based on user's input.
    
"""


# Create functions
def get_github_user_info(username):
    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("\nGithub User Information: ")
        print("--------------------------")
        print("Name: ", data["name"])
        print("Id: ", data["id"])
        print("Location: ", data["location"])
        print("Repos: ", data["public_repos"])
    else:
        print("User Not Found.")


# get_github_user_info("Makena-Wambui")


def convert_to_uppercase(text):
    print("Text in uppercase: ", text.upper())


def count_words(text):
    print("Number of words in user input: ", len(text.split()))


# convert_to_uppercase("mom")
# count_words("I am extremely happy!")


# Add the Decision Loop
while True:
    print("\nDeveloper Assistant:")
    print("1. Github User Lookup")
    print("2. Uppercase Text")
    print("3. Count Words")
    print("4. Exit")

    option = input("Choose an option: ")

    if option == "1":
        userName = input("Enter Github User Name: ")

        get_github_user_info(userName)

    elif option == "2":
        text = input("Enter text: ")
        convert_to_uppercase(text)

    elif option == "3":
        text = input("Enter text: ")
        count_words(text)

    elif option == "4":
        print("Adios!")
        break

    else:
        print("Invalid Option")
