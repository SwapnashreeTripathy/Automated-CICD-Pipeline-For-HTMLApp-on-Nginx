# Automate CICD-HTML Project Deployment to Nginx Server 

#### When there is any new commit pushed to the GitHub Main branch, automatically those new changes/commits will get deployed to your Production/main Server using Automation script & cronjob.

## Thought Process to build this project:


 1.	Create/Take a simple HTML project and push it to a GitHub repository.
 2.	Clone your GitHub Repo and Push this HTML project/index.html to your GitHub Main Branch.

       ``git clone https://github.com/SwapnashreeTripathy/CICDProject-HTML.git``<br>
   			 ``git add index.html``<br>
   			 ```git commit -m "new commit to github main repo"```<br>
   			 ``git push``<br>
      
3. Get the Recent Commit from GitHub Repo using a Python Script (Get_Commitids.py).

   * Import "REQUEST" library to  & "JSON" module.<br>
      REQUEST -- Used for sending HTTP requests to web services or APIs and handling/getting the Responses back.<br>
      JSON -- Use the json module to serialize Python objects (e.g., dictionaries or lists) into JSON format which is basically same as dictionary format in Python.<br>
      ```pip install requests```
     
   * Save your "REPO_OWNER" & "REPO_NAME" into these variables.<br>
   * Using GitHUB REST API Endpoint to access for accessing commit information of a GitHub repository.<br>
   * Connecting to this API using "request.get() method" to retrive the response from the server. And "Store the Response" in "response Variable".<br>
   * Using "response.json() to convert" the response of HTTP get request "into JSON Format" & Storing those in "commits Variable".<br>
   * Save only the "Latest Commit ID" or "0th Index" value into "commit_ids Varioable".<br>
     ("SHA" is the Key which stores Commit IDs)<br>
   * Write this Commit_id into a path in Linux Machine "/home/swapna/hvdevops/CICDProject-HTML/bash_script/Current_GitHub_Commits.txt file" 
     
     ![image](https://github.com/SwapnashreeTripathy/CICDProject-HTML/assets/139486876/a1b4b9a2-1e88-47e7-8cec-8875577164ea)
     
4. Write a Bash Script to Deploy the latest Code(only if there is new Commits present in GitHub) and start/restart Nginx as per the requirment.<br>
   * Move to html folder where the index.html is present in your server & get the "existing last commitid from your server" , save into a txt file.<br>
   * If the "latest commit_id from your Servers" is "same" as the "latest commit_id from your Github Repo", then print the same info & exit the script.<br>
   * But if the Condition dose not match, First "ZIP the existing CICDProject-HTML & Move it"  into another folder.<br>
     (For better use create the zip file name, with the current timestamp)<br>
   * Then, Move to the folder where "Index.html" is present & "PULL the new Commits from Github".<br>
   * Lastly check, if "Nginx is Active" on your server, if not then Restart the Nginx.<br>


     ![image](https://github.com/SwapnashreeTripathy/CICDProject-HTML/assets/139486876/1066eee9-361d-48d1-bebb-6744294ddc9e)

   
     ![image](https://github.com/SwapnashreeTripathy/CICDProject-HTML/assets/139486876/775784a6-df22-46ae-9163-c167ffa94f8e)

     ![image](https://github.com/SwapnashreeTripathy/CICDProject-HTML/assets/139486876/c1ac41f9-671b-4308-b7a7-05d2fcac3a17)

## Steps to RUN the Script:

  
  1.	Change the File permission of both the “.py” & “.sh” script to be Executable.
    
  3.	Change the File Owner and Group permission to ROOT, as we are using SUDO in our script file. So while running the “.sh” Script via Cronjob no password is required to fill. 
  4.	Add the Python Script to Bash Script, in order to have only one Cronjob scheduled. 
  5.	Create a Cronjob for the Bash Script to run in every 2 mins with root privileges.
  6.	To check if the cronjob is running or not, run the cat command for “/var/log/syslog”.
  7.	Also can view the last output of the bash script in the “output.log” file.  You would need to provide “read” File permission to view the log file.

   
      
      
   	

