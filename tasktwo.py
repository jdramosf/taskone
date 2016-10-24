import requests
import json

data = {"token": "4cf3ff970884c0176fc273c844a53db8"}

r = requests.post("http://challenge.code2040.org/api/reverse", params = json.dumps(data))

print(r)

new_string = "".join(r[i] for i in range(len(r) - 1, -1, -1))
print(new_string)

new_data = {"token": "4cf3ff970884c0176fc273c844a53db8", "string": new_string}

n = requests.post("http://challenge.code2040.org/api/reverse/validate", params = json.dumps(new_data))

print(n)