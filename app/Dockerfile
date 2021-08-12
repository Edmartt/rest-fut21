FROM python:3.7

WORKDIR /app

COPY requirements.txt /app

COPY wait-for-it.sh /app

RUN apt-get update && apt-get install gcc musl-dev

RUN pip install -r requirements.txt

COPY . .

#CMD flask init-db ; flask run
