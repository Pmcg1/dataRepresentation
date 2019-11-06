from github import Github
import requests

g = Github("37134fea34fc11b5bdc5e82ad894109b3d141674")

for repo in g.get_user().get_repos():
    print(repo.name)

repo = g.get_repo("datarepresentationstudent/aPrivateOne")
#print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print(urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
print(contentOfFile)

newContents = contentOfFile + " more stuff \n"
print(newContents)

gitHubResponse=repo.update_file(fileInfo.path, "updated by prog", newContents, fileInfo.sha)
print(gitHubResponse)