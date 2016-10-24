# Import libraries
import requests
import json

# Create the dictionary with the values for token and github
data = {"token": "4cf3ff970884c0176fc273c844a53db8", "github": "https://github.com/jdramosf/taskone.git"}

# Convert dictionary to JSON format
json_data = json.dumps(data)

# Make the HTTP POST request to the URL using the data in the json_data variable
r = requests.post("http://challenge.code2040.org/api/register", json_data)

# Print the response
print(r)