import requests

# Make a request to an api
responseObj = requests.get("https://api.github.com")

# responseObj is a Response object that contains all the information about the response we got from the server
# We can parse the response content using the .json() method to get a Python dictionary

data = responseObj.json()

print(type(data))

print(data)

# Then we can interact with the data from the API via the dictionary keys and values
print(data["current_user_url"])
