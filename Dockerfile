FROM python:3.10.9-slim-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y make libzbar0 libgl1-mesa-glx

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
