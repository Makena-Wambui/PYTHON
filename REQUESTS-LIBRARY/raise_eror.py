"""
We might not want to check the response status code in an if statement
Instead, you want to use Requests built in capacities to raise an exception if the request was unsuccessful
We can do this using raise_for_status()

exceptions is a module in the requests library
It is where all the error classes live
It defines different types of exceptions/errors that can occur when making HTTP requests like:
    ConnectionError - network issues
    Timeout - server took too long to respond
    HTTPError - bad HTTP response status codes

HTTPError is a specific exception class from exceptions module
HTTPError is raised when the server responds with a bad status code
It is raised when you call response.raise_for_status() and the HTTP response status code shows an eror like 404 or 500


When you visit https://api.github.com, Github is saying "These are the services and information I expose to developers, you can use this API to interact with my services"

The response is just JSON data that describes Github's API endpoints
"""

import requests  # requests for making HTTP requests
from requests.exceptions import (
    HTTPError,
)  # import HTTP Error so we can catch it specifically when a request fails due to a bad HTTP status code

# the first url is valid but the second one is invalid and will trigger an error
URLS = ["http://api.github.com", "http://api.github.com/invalid"]


for url in URLS:
    # Make a GET request
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check the response
        # if status code is below 400, no HTTPError
        # Otherwise HTTPError is raised
    except (
        HTTPError
    ) as httpErr:  # If there is an HTTPError like 404, it is captured here
        print(f"HTTPError occured: {httpErr}")
    except (
        Exception
    ) as err:  # any other error like network issues, invalid URL format are captured here
        print(f"Error: {err}")
    else:
        print("Success!")  # will only run if no exception was raised
