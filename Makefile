install:
	python3 -m pip install --upgrade pip &&\
		python3 -m pip install -r requirements.txt

unit-test:
	python3 -m pytest tests/unit_tests.py

test: unit-test

run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000

build:
	docker build -t microservice-template .

deploy:
	docker-compose up -d
