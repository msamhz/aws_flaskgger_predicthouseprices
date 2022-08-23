## Self Guidance (AWS Trial Account)
---
1) git clone https://github.com/msamhz/aws_flaskgger_predicthouseprices.git

2) Cd into /aws_flaskgger_predicthouseprices/service

3) docker build -t predicthouse .

4) Docker run 

``TABLE_NAME=$(aws dynamodb list-tables | jq -r .TableNames[0])
docker run -d -p 8000:80 -e AWS_DEFAULT_REGION=$AWS_REGION -e DDB_TABLE_NAME=$TABLE_NAME predicthouse``

5) Check url with another terminal > Copy paste link (http format) 

6) Proceed to push into Repo (provided already created)

``MONO_ECR_REPOSITORY_URI=$(aws ecr describe-repositories | jq -r .repositories[].repositoryUri | grep mono)
docker tag predicthouse:latest $MONO_ECR_REPOSITORY_URI:latest
docker push $MONO_ECR_REPOSITORY_URI:latest``


---

### Navigating into AWS ### 

# To check for latest push into repo 
--> ECR --> repo --> check for latest image tag

Copy down URL (in order to set up in)

# To create task using image 
--> ECS --> Click Cluster link --> Create new task --> Create

1) Create task definition name 
2) network: awsvpc
3) Operating: Choose depending on dockerfile 
4) Requires compatabilities: Fargate 
5) Create Task execution role 
6) Set up task memory and CPU usage 
7) Add container 
  - Set up container name 
  - paste URL from latest image 
  - port mapping (if anny): 80 
  - env keys 
  
  #   Run task 
  --> actions --> run task 
  
  Launch type: Fargate 
  Cluster VPC: Need setup 
  Subnets: Need setup 
  Security groups: Create new security group
  Auto-assign public IP: Enabled 
  

# Assess IP from public IP address 
IP ADDRESS/apidocs
