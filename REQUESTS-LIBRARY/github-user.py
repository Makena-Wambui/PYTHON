import requests

# Looking for github user data
response = requests.get("https://api.github.com/users/Makena-Wambui")

userData = response.json()

print(userData)


print(userData["login"])
