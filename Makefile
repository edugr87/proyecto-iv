run:
	python manage.py runserver

test:
	python manage.py migrate
	cd weatherapp && python models.py
	cd weatherapp && python tests.py

install:
	pip install -r requirements.txt
