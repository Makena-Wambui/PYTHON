"""
A Response is the object that contains the result of your request

We make the request to the Github API and store the return value in a variable,response, so we can have a closer look at the object's attributes and behaviours.

response is an instance of Response

We can use response to see alot of information about the results of your GET request.

The most common attributes of a Response object are:
- status_code: the HTTP status code returned by the server shows you the status of your request
    200 OK status means the request was successful and the server returned the requested data
    404 NOT FOUND status means the resource you were looking for could not be found on the server
"""

import requests

response = requests.get("https://api.github.com/everything")

print(response.status_code)


# You might want to use this information to make a decision.

status = response.status_code

# if status == 200:
#     print("Success!")
# else:
#     print("Error!")

"""
    If you use a Response object in a boolean context like a conditional statement, it will evaluate to True if the status code is less than 400, and False otherwise.

    We only use this convenient shorthand when we want to know whether the request was generally successful
"""


if response:
    # we check whether the status code of response is between 200 and 399
    print("Success!")
else:
    # if not we raise an Exception with an error message that includes the non success status code wrapped in an f string
    raise Exception(f"Non-success status code: {response.status_code}")
