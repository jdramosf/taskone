# Import libraries
import requests
import json

# Create the dictionary with the values for token and github
data = {"token": "4cf3ff970884c0176fc273c844a53db8", "github": "https://github.com/jdramosf/taskone.git"}

# Make the HTTP POST request to the URL using the data in the data variable
r = requests.post("http://challenge.code2040.org/api/register", params = data)

# Print the response
print(r)