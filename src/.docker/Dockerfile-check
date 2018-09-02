FROM python:3.6

RUN apt-get update
RUN apt-get install -y python-setuptools netcat

WORKDIR /code/src
COPY ./check .
RUN pip install -r requirements.txt