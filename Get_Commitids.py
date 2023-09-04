

#!/usr/bin/python3


import requests
import json 

REPO_OWNER = "SwapnashreeTripathy"   # Replace with the GitHub username or organization
REPO_NAME = "CICDProject-HTML"  # Replace with the repository name

# Make the API request and retrieve commit IDs
response = requests.get(f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/commits")
commits = response.json()

#get commit id only, commit_id is the value of SHA( which is a key as json respone we got)
commit_ids = [commit["sha"] for commit in commits]
print(commit_ids[0])


#Write Last Commit into Current_GitHub_Commits.txt file(define the path for the txt file)
dir_path = "/home/swapna/hvdevops/CICDProject-HTML/bash_script/"
file_path=f"{dir_path}/Current_GitHub_Commits.txt"
with open(file_path, 'w') as file:
	file.write(commit_ids[0])


'''to write into file path in another method
file = open(file_path,'w')
file.write(commit_ids[0])

file.close()'''

 
'''to READ the file_path 
    with open(file_path,'r') as file:
	file.content = file.read()
print(file.content)'''




'''#write all Commit_ids into a txt file
file=open('Current_GitHub_Commits.txt','w')
for c in commit_ids:
    entry= c+'\n'
    file.write(entry)
file.close()'''


