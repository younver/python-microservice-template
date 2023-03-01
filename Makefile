install:
	python3 -m pip install --upgrade pip &&\
		python3 -m pip install -r requirements.txt

unit-test:
	python3 -m pytest tests/unit_tests.py

test: unit-test

build:
	docker build -t microservice-template .

run:
	docker run -p 8000:8000 microservice-template

deploy:
	docker-compose up -d
