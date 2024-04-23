.PHONY: help init startproject startapp superuser runserver makemigration migrate createsuperuser quick-migrate

BASEWORKDIR = src/
CMD = poetry run python manage.py

install:
	pip install -U poetry
	poetry config virtualenvs.create false
	poetry update --with test

migrations:
	./manage.py makemigrations

migrate:
	./manage.py migrate

runserver:
	./manage.py runserver

test:
	poetry run coverage run
	poetry run coverage report