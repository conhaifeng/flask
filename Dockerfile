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
RUN pip3 install -r requirements.txt

EXPOSE 5000

# copy project
COPY . /usr/src/app/

# mk log file for gunicorn
RUN mkdir logs
RUN touch logs/access.log
RUN touch logs/error.log

ENTRYPOINT ["gunicorn", "--config", "config/gunicorn.conf.py", "app:app", "--preload"]