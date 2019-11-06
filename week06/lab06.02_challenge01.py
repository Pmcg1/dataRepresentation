import requests
import json

apiKey = '82c7e8fcb3b7ac5f81babb532585415527d1c5ad'
url = 'https://api.github.com/repos/Pmcg1/data_rep_private'
filename = 'repo_out_PMG.json'

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()

print(response.json())
print(response.status_code)

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)