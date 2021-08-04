FROM python:3.7

WORKDIR /app

COPY requirements.txt /app

ENV FLASK_RUN_HOST 0.0.0.0

ENV FLASK_ENV development

ENV API_KEY 1234

RUN apt-get update && apt-get install gcc musl-dev

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . .

CMD flask init-db ; flask run
