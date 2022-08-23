FROM python:3.8.8

WORKDIR /usr/src/app

#install dependencies
RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python docker_flask.py