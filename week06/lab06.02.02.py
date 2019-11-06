import requests
import json

apiKey = 'f59b1cdb743ce0ab9b21a94ac246b02f06ee2d85'
url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne'
filename = 'repo_out.json'

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()

print(response.json())
print(response.status_code)

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)