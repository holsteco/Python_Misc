#
#
#

#imports
import requests
import json

#parameters for San Francisco
parameters = {"lat": 37.78, "lon": -122.41}

# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a python object.  Verify that it's a dictionary.
data = response.json()
print(type(data))
print(data)

# Print the status code of the response.
print(response.status_code)

# Headers is a dictionary
print(response.headers)

# Get the content-type from the dictionary
print(response.headers["content-type"])


# Get the response from the API endpoint.
response2 = requests.get("http://api.open-notify.org/astros.json")
data2 = response2.json()

# 9 people are currently in space.
print(data2["number"])
print(data2)