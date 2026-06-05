import requests

"""
Almost every AI system, web app, mobile app and agent:
    Sends requests
    Receives data
    Processes responses

    This is what APIs are about.


What we are doing today:
    Build a Python Program:
     Calls an API
     Receives data
     Displays useful information


API ANALOGY
    Think of an API as a waiter in a restaurant.

    
    You app wants some weather data
    The API goes to the server, gets the data and brings it back


Step 1: Install requests in your venv

What is requests?
    A poerful and user-friendly library for making HTTP requests in Python.
    It abstracts away the complexities of making requests behind a simple API, allowing you to send HTTP requests with a few lines of code.


    One of the most common HTTP methods is GET which is used to retrieve data from a server.  When you make a GET request, you are asking the server to send you some data.  
    The server will then respond with the requested data, which you can process and use in your application.
    To make a GET request using Requests, you can use the requests.get() function.
    This function takes the URL of the resource you want to access as an argument and returns a Response object that contains the server's response to your request.
"""

response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "language:python", "sort": "stars", "order": "desc"},
)


"""
What does line 40 mean?

We are making a GET request to the GitHub API to search for repositories.  
We are passing some parameters to the API to specify our search criteria.  
The parameters we are passing are:
q: This is the search query.  We are searching for repositories that are written in Python.
sort: This is the sorting criteria.  We are sorting the results by the number of stars the repositories have.
order: This is the sorting order.  We are sorting the results in descending order, which means that the repositories with the most stars will be at the top of the results.


If I wanted just one repository, ie the most starred Python repository, I could change the parameters to:
params={"q": "language:python", "sort": "stars", "order": "desc", "per_page": 1}
"""


print(
    response.status_code
)  # 200 means success, 404 means not found, 500 means server error, etc.
print(response.text)

# print(
#     response.json()
# )  # If the response is in JSON format, you can use the json() method


the_repo = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "language:python", "sort": "stars", "order": "desc", "per_page": 1},
)

print(the_repo.text)

"""
The response object contains useful information about the response from the server such as the status code, headers, and the content of the response. 
You can use this information to determine if your request was successful and to process the data returned by the server.

The response content can be accessed in various formats such as bytes(bytes are raw data - response.content), text (string representation of the response - response.text), and JSON (if the response is in JSON format - response.json()). 
You can use the appropriate method to access the content based on your needs.

You can customize requests by adding query parameters, headers and authentication. 
This allows you to interact with APIs that require specific parameters or authentication to access certain resources.
You can pass parameters using the params argument in the requests.get() function.
"""
