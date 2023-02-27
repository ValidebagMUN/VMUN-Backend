#!/bin/zsh

export COMPOSE_FILE=production.yml

docker-compose build

docker-compose up -d

docker-compose run --rm django python manage.py migrate
