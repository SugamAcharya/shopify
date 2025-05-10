#!/bin/bash
echo "Create migration"
python manage.oy makemigrations api
echo "------------------------------"


echo "Migrate"
python manage.py migrate
echo "-------------------------------"

echo "Start server"
python manage.py runserver