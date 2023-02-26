install:
	python3 -m pip install --upgrade pip &&\
		python3 -m pip install -r requirements.txt

test:
	python3 -m pytest app/tests/unit_tests.py

build:
	docker build -t microservice-template .

run:
	docker run -p 8000:8000 microservice-template

deploy:
	# todo

all: install test build
