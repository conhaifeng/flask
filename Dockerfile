# pull official base image
FROM python:3.8-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip3 install --upgrade pip
RUN pip3 install gunicorn

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

# copy project
COPY . /usr/src/app/
ENTRYPOINT ['gunicorn', '--config', 'config/gunicorn.conf', 'flask:app']