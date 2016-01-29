#!/usr/bin/env bash

init() {
    python manage.py makemigrations
    python manage.py migrate
}

rundev() {
    init
    python manage.py runserver 0.0.0.0:8000
}

runprod() {
    init
    uwsgi --ini deploy/uwsgi/miracle.ini
}

case "$1" in
    dev)  rundev;;
    prod) runprod;;
    *) "$@";;
esac
