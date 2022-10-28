FROM python:3.10.4-slim-buster
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN addgroup --gid 1024 dev
RUN useradd --create-home -g dev appuser

RUN apt-get update -y && \
    apt-get install build-essential -y --no-install-recommends && \
    pip install pipenv --no-cache-dir

# RUN pip install pipenv --no-cache-dir

USER appuser
RUN mkdir /home/appuser/app
WORKDIR /home/appuser/app

COPY docker/django/entrypoint.sh /home/appuser/app/
