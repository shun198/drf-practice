CONTAINER_NAME = app
PROJECT = test-proj
RUN_APP = docker-compose exec $(CONTAINER_NAME)
RUN_POETRY =  $(RUN_APP) poetry run
RUN_DJANGO = $(RUN_POETRY) python manage.py
RUN_PYTEST = $(RUN_POETRY) pytest

up:
	docker-compose up -d

build:
	docker-compose build

down:
	docker-compose down

loaddata:
	$(RUN_DJANGO) loaddata fixture.json

makemigrations:
	$(RUN_DJANGO) makemigrations

migrate:
	$(RUN_DJANGO) migrate

show_urls:
	$(RUN_DJANGO) show_urls

shell:
	$(RUN_DJANGO) debugsqlshell

superuser:
	$(RUN_DJANGO) createsuperuser

test:
	$(RUN_PYTEST)

test-cov:
	$(RUN_PYTEST) --cov=application/tests/

make_report:
	-@ $(RUN_PYTEST) --alluredir=allure-results
	sh send_results.sh
	echo "Generating test report. This may take a while..."
	curl -X GET "http://127.0.0.1:5050/allure-docker-service/generate-report?project_id=$(PROJECT)" -H  "accept: */*"
	echo "Successfully generated test report. Redirecting to allure server."
	open http://127.0.0.1:5050/allure-docker-service/projects/$(PROJECT)/reports/latest/index.html

show_report:
	open http://127.0.0.1:5050/allure-docker-service/projects/$(PROJECT)/reports/latest/index.html

format:
	$(RUN_POETRY) black .
	$(RUN_POETRY) isort .

update:
	$(RUN_APP) poetry update

db:
	docker exec -it db bash

