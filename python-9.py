import base64
from github import Github
from pprint import pprint
username="madhavpreeth123"
g=Github()
user=g.get_user(username)
for repo in user.get_repos():
    print(repo,':',repo.url)
    
    
  ## output ##
  
Repository(full_name="madhavpreeth123/first") : https://api.github.com/repos/madhavpreeth123/first
Repository(full_name="madhavpreeth123/kesava-") : https://api.github.com/repos/madhavpreeth123/kesava-
Repository(full_name="madhavpreeth123/myrepo") : https://api.github.com/repos/madhavpreeth123/myrepo
Repository(full_name="madhavpreeth123/reposit") : https://api.github.com/repos/madhavpreeth123/reposit
Repository(full_name="madhavpreeth123/second") : https://api.github.com/repos/madhavpreeth123/second
Repository(full_name="madhavpreeth123/third") : https://api.github.com/repos/madhavpreeth123/third
Repository(full_name="madhavpreeth123/tusk") : https://api.github.com/repos/madhavpreeth123/tusk
