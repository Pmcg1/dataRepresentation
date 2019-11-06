import requests
import json

apiKey = '37134fea34fc11b5bdc5e82ad894109b3d141674'
url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne'
filename = 'repo_out2.json'

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()

print(response.json())
print(response.status_code)

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)