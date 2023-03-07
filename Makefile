run:
	python3 manage.py runserver

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

super:
	python3 manage.py createsuperuser

git:
	git add .
	git commit -m 'make commit'
	git push origin main

pip:
	pip install -r requirements.txt

test:
	python3 manage.py test
