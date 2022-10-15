
build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

rebuild:
	make down build up

precommit-install:
	pip3 install pre-commit
	pre-commit install

lint:
	pre-commit run --all-files

makemigrations:
	docker-compose run --rm --no-deps app python src/manage.py makemigrations

migrate:
	docker-compose run --rm --no-deps app python src/manage.py migrate

test:
	docker-compose run --rm --no-deps app pytest -s -c src/pytest.ini

test-cov:
	docker-compose run --rm --no-deps app pytest --cov -c src/pytest.ini
