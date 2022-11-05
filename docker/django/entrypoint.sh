#!/bin/sh

pipenv install
pipenv run python django/manage.py createschema
pipenv run python django/manage.py makemigrations
pipenv run python django/manage.py migrate
pipenv run python django/manage.py initialize -f
pipenv run uwsgi --ini uwsgi.ini
