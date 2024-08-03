FROM python:3.12-slim-bullseye

RUN apt-get update && apt-get install ffmpeg -y

ENV APP_HOME=/home/app/app/

RUN mkdir -p ${APP_HOME}

WORKDIR ${APP_HOME}

COPY requirements.freeze .
RUN pip3 install --no-cache-dir -r requirements.freeze

COPY app.py .
