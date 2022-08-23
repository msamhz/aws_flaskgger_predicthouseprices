## Self-guidance on using aws 
---
1) git clone https://github.com/msamhz/aws_flaskgger_predicthouseprices.git

2) Cd into /aws_flaskgger_predicthouseprices/service

3) docker build -t predicthouse .

4) Docker run 

TABLE_NAME=$(aws dynamodb list-tables | jq -r .TableNames[0])
docker run -d -p 8000:80 -e AWS_DEFAULT_REGION=$AWS_REGION -e DDB_TABLE_NAME=$TABLE_NAME predicthouse

5) Check url with another terminal 
--> Copy paste link (http format) 

6) Once ok, push 

MONO_ECR_REPOSITORY_URI=$(aws ecr describe-repositories | jq -r .repositories[].repositoryUri | grep mono)
docker tag predicthouse:latest $MONO_ECR_REPOSITORY_URI:latest
docker push $MONO_ECR_REPOSITORY_URI:latest

---
