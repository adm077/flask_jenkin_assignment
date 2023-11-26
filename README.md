# flask_jenkin_assignment

##1. Jenkins CI CD pipeline for flask application

Objective:
Set up a Jenkins pipeline that automates the testing and deployment of a simple Python web application.


Requirements:


1. Setup:

   - Install Jenkins on a virtual machine or use a cloud-based Jenkins service.

   - Configure Jenkins with Python and any necessary libraries.

I have launched an Ec2 instance on AWS and configured it with Java, Jenkins, pip and other dependencies.
![image](https://github.com/adm077/flask_jenkin_assignment/assets/139608052/8dc7c58d-c935-47b3-98ad-ce0242c41daf)

I have allowed Inbound rules
![image](https://github.com/adm077/flask_jenkin_assignment/assets/139608052/b60a9f2d-947b-4f9a-88bf-f5a7c3a89f26)

![image](https://github.com/adm077/flask_jenkin_assignment/assets/139608052/938192d7-d6bc-4639-9d9d-d25c30326768)


2. Source Code:

  - Fork the provided Python web application repository on GitHub (provide a link to a sample Python web application repository).

  - Clone the forked repository into your Jenkins server.

I have created a Job under Jenkins
![image](https://github.com/adm077/flask_jenkin_assignment/assets/139608052/9f2a01a3-4691-4347-ad94-c67bfff9f4d6)

3. Jenkins Pipeline:

   - Create a Jenkinsfile in the root of your Python application repository.

   - Define a pipeline with the following stages:

     - Build: Install dependencies using pip.

     - Test: Run unit tests using a testing framework like pytest.

     - Deploy: If tests pass, deploy the application to a staging environment.

``` Console Output
Started by user Israrul Haque
Running as SYSTEM
Building in workspace /var/lib/jenkins/workspace/flask_assignment
The recommended git tool is: NONE
No credentials specified
 > git rev-parse --resolve-git-dir /var/lib/jenkins/workspace/flask_assignment/.git # timeout=10
Fetching changes from the remote Git repository
 > git config remote.origin.url https://github.com/adm077/flask_jenkin_assignment # timeout=10
Fetching upstream changes from https://github.com/adm077/flask_jenkin_assignment
 > git --version # timeout=10
 > git --version # 'git version 2.34.1'
 > git fetch --tags --force --progress -- https://github.com/adm077/flask_jenkin_assignment +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git rev-parse refs/remotes/origin/main^{commit} # timeout=10
Checking out Revision c74aef852b4f31a4aadda7daf1636ef799497e0a (refs/remotes/origin/main)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f c74aef852b4f31a4aadda7daf1636ef799497e0a # timeout=10
Commit message: "Update app.py"
 > git rev-list --no-walk d9fb0125a59905b1c4d57fd7217e9ec8c7dbc6f8 # timeout=10
[flask_assignment] $ /bin/sh -xe /tmp/jenkins5713475323859548670.sh
+ echo /var/lib/jenkins/workspace/flask_assignment
/var/lib/jenkins/workspace/flask_assignment
+ pwd
/var/lib/jenkins/workspace/flask_assignment
+ whoami
jenkins
+ pip install -r requirements.txt
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: flask in /var/lib/jenkins/.local/lib/python3.10/site-packages (from -r requirements.txt (line 1)) (3.0.0)
Requirement already satisfied: blinker>=1.6.2 in /var/lib/jenkins/.local/lib/python3.10/site-packages (from flask->-r requirements.txt (line 1)) (1.7.0)
Requirement already satisfied: click>=8.1.3 in /var/lib/jenkins/.local/lib/python3.10/site-packages (from flask->-r requirements.txt (line 1)) (8.1.7)
Requirement already satisfied: Jinja2>=3.1.2 in /var/lib/jenkins/.local/lib/python3.10/site-packages (from flask->-r requirements.txt (line 1)) (3.1.2)
Requirement already satisfied: itsdangerous>=2.1.2 in /var/lib/jenkins/.local/lib/python3.10/site-packages (from flask->-r requirements.txt (line 1)) (2.1.2)
Requirement already satisfied: Werkzeug>=3.0.0 in /var/lib/jenkins/.local/lib/python3.10/site-packages (from flask->-r requirements.txt (line 1)) (3.0.1)
Requirement already satisfied: MarkupSafe>=2.0 in /var/lib/jenkins/.local/lib/python3.10/site-packages (from Jinja2>=3.1.2->flask->-r requirements.txt (line 1)) (2.1.3)
+ python3 app.py
Finished: SUCCESS

4. Triggers:

   - Configure the pipeline to trigger a new build whenever changes are pushed to the main branch of the repository.

Set the Build Triggers For triggering the new build whenever a new code is pushed in github
![image](https://github.com/adm077/flask_jenkin_assignment/assets/139608052/ed7b7ae4-f9f3-49d5-b1bf-c8c6e9ecd01d)


5. Notifications:

   - Set up a notification system to alert via email when the build process fails or succeeds.


6. Documentation:

   - Document the pipeline process and any prerequisites needed for the setup in a README.md file in the repository.


7. Submission:

   - Provide the URL to the GitHub repository with the Jenkinsfile and updated README.md.

   - Include screenshots of the Jenkins pipeline showing the build, test, and deployment stages.


Deliverables:

- Forked GitHub repository with Jenkinsfile.

- Documentation in README.md.

- Screenshots of the Jenkins pipeline execution.


#2. GitHub Actions CI/CD Pipeline Flask App

Objective:

Implement a CI/CD workflow using GitHub Actions for a Python application.


Requirements:


1. Setup:

   - Use a provided Python application repository on GitHub (provide a link to a sample Python application repository).

   - Ensure the repository has a main branch and a staging branch.


2. GitHub Actions Workflow:

   - Create a .github/workflows directory in your repository.

   - Inside the directory, create a YAML file to define the workflow.


3. Workflow Steps:

   - Define a workflow that performs the following jobs:

     - Install Dependencies: Install all necessary dependencies for the Python application using pip.

     - Run Tests: Execute the test suite using a framework like pytest.

     - Build: If tests pass, prepare the application for deployment.

     - Deploy to Staging: Deploy the application to a staging environment when changes are pushed to the staging branch.

     - Deploy to Production: Deploy the application to production when a release is tagged.


4. Environment Secrets:

   - Use GitHub Secrets to store sensitive information required for deployments (e.g., deployment keys, API tokens).


5. Documentation:

   - Update the README.md file with instructions on how the GitHub Actions workflow works and how to configure the necessary secrets.


6. Submission:

   - Provide the URL to the GitHub repository with the workflow file and updated README.md.

   - Include screenshots of the GitHub Actions workflow runs showing successful execution of all steps.

