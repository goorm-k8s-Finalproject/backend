FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y gcc

ENV PYTHONUNBUFFERED=0
ENV PYTHONIOENCODING=utf-8

WORKDIR /var/www

COPY . /var/www/backend

RUN pip install -r /var/www/backend/requirements.txt

EXPOSE 8000

WORKDIR /var/www/backend
