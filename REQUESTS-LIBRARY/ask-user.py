import requests

# prompt user for their github user name

userName = input("Enter your Github use name: ")

url = f"https://api.github.com/users/{userName}"

response = requests.get(url=url)

userData = response.json()

print("Name: ", userData["name"])
print("Location: ", userData["location"])
print("Repos: ", userData["public_repos"])
print("Followers: ", userData["followers"])
