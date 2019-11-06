import requests
import json

apiKey = '37134fea34fc11b5bdc5e82ad894109b3d141674'
url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne'
filename = 'repo_out.json'

file = open("pmg_test.txt", 'r')
#json.dump(repoJSON, file, indent=4)

response = requests.put(url, file, auth=('token',apiKey))
#response = requests.put(url, auth=('token',apiKey))


#repoJSON = response.json()

#print(response.json())
#print(response.status_code)
