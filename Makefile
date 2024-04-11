.PHONY: help init startproject startapp superuser runserver makemigration migrate createsuperuser quick-migrate

BASEWORKDIR = src/
CMD = poetry run python manage.py
PROJECT = $(shell basename "$(CURDIR)")

SETTINGS_LOCAL = $(PROJECT).settings.local
SETTINGS_PROD = $(PROJECT).settings.production
SETTINGS_DEV = $(PROJECT).settings.dev

define setting
	$(if $(filter $(1), prod), $(SETTINGS_PROD), $(if $(filter $(1), dev), $(SETTINGS_DEV), $(SETTINGS_LOCAL)))
endef

help:
	@echo ""
	@echo "Available commands:"
	@echo "  init: Install poetry dependencies and create .env file"
	@echo "  startproject: Create a new Django project"
	@echo "  startapp: Create a new Django app"
	@echo "  runserver: Run the server"
	@echo "  makemigration: Create a migration file"
	@echo "  migrate: Apply the migration"
	@echo "  createsuperuser: Create a superuser"
	@echo "  quick-migrate: Create a migration file and apply it"
	@echo "  help: Show this message"
	@echo ""

init:
	poetry install --no-root
	@echo "Poetry dependencies installed"
	@echo "Creating .env file"

startproject:
	@if [ ! -d $(BASEWORKDIR) ]; then mkdir -p $(BASEWORKDIR); fi	
	cd $(BASEWORKDIR) && poetry run django-admin startproject $(PROJECT) .
	@echo "Project $(project_name) created"

startapp:
	$(eval app_name := $(shell bash -c 'read -p "Enter app name: " pwd; echo $$pwd'))
	cd $(BASEWORKDIR) && $(CMD) startapp $(app_name)
	@echo "App $(app_name) created"

runserver:
	cd $(BASEWORKDIR) && $(CMD) runserver --settings=$(strip $(call setting,$(ENV)))

makemigration:
	cd $(BASEWORKDIR) && $(CMD) makemigrations --settings=$(strip $(call setting,$(ENV)))

migrate:
	cd $(BASEWORKDIR) && $(CMD) migrate --settings=$(strip $(call setting,$(ENV)))

createsuperuser:
	cd $(BASEWORKDIR) && $(CMD) createsuperuser --settings=$(strip $(call setting,$(ENV)))

quick-migrate:
	cd $(BASEWORKDIR) && $(CMD) makemigrations --settings=$(strip $(call setting,$(ENV))) && $(CMD) migrate --settings=$(strip $(call setting,$(ENV)))