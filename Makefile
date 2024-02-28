up:
	docker-compose up

down:
	docker-compose down

makemigrations:
	docker-compose run --rm app sh -c "python manage.py makemigrations"

migrate:
	docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"

test:
	docker-compose run --rm app sh -c "python manage.py test"

flake8:
	docker-compose run --rm app sh -c "flake8"

superuser:
	docker-compose run --rm app sh -c "python manage.py createsuperuser"