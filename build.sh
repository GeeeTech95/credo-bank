#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

export DEBUG=False
export PSYCOPG_DEBUG=1

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
#python manage.py migrate
#python manage.py loaddata dump.json

export DJANGO_SUPERUSER_EMAIL=admin1@credocapitalbank.com
export DJANGO_SUPERUSER_USERNAME=admin1
export DJANGO_SUPERUSER_PASSWORD=4$7QWQxn

#python manage.py createsuperuser --no-input




