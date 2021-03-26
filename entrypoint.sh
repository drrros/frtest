#!/bin/sh

python manage.py collectstatic --noinput --clear
python manage.py migrate --noinput
exec "$@"
