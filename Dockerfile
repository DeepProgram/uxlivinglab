# pull official base image
FROM python:3.12.4-slim-bookworm

# set working directory
RUN mkdir -p /usr/src/web
WORKDIR /usr/src/web

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

WORKDIR /usr/src/web/app

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install