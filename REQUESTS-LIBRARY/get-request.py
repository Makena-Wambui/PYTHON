"""
HTTP Methods such as GET and POST specify the desired action to be performed when making an HTTP request.

GET - retrieves data from a server at the specified resource. GET requests should only retrieve data and should have no other effect on the data.

To make a GET request using Requests library, invoke requests.get() method. This method takes the URL of the resource as a parameter and returns a Response object.

You can make a GET request to the Github's REST API as shown below:
"""

import requests

response = requests.get("https://api.github.com")

print(
    response
)  # response is a Response object which contains the server's response to the HTTP request and contains several attributes and methods to access the response data, status code, headers, etc.
