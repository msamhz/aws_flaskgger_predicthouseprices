# install base
FROM ubuntu:20.04

# Update all pip and python 
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
RUN pip3 install --upgrade pip

# install requirements first before creating the app folder 
COPY ./service/requirements.txt .
RUN pip3 install -r ./requirements.txt

# Copy only the service folder 
COPY ./service /appfolder

# set working directory into app folder 
WORKDIR /appfolder

# Set port to 80 
EXPOSE 80

# Run python3 for app.py
ENTRYPOINT ["python3"]
CMD ["app.py"]
