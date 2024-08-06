## Requirements
- Python 3.6
- Django 3.1
- Django REST Framework

## Installation
python -m venv env

## Install Packages
pip install -r requirements.txt

## Run Migration
python manage.py migrate

## Run Server
python manage.py runserver

## API Doc
http://127.0.0.1:8000/api/schema/swagger-ui/

## Run test
pytest

## Run test with coveration
pytest --cov

## docker

### How to Build
docker-compose up

### Run migrations
docker-compose exec web python manage.py migrate

### Run test
docker-compose exec web pytest

## API Doc
http://127.0.0.1:8000/api/schema/swagger-ui/
