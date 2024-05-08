#!/bin/sh

gunicorn --workers 2 --bind 0.0.0.0:5000 --timeout 60 --log-level debug $GUNICORN_APP
