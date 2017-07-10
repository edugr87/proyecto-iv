run:
	python manage.py runserver

test:
 cd weatherapp && python tests.py

install:
	pip install -r requirements.txt
