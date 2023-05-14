FROM python:3.8

WORKDIR "/src"

COPY requirements.txt .

COPY wait-for-it.sh .

RUN chmod +x wait-for-it.sh

RUN apt-get update && apt-get install gcc musl-dev

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

#CMD flask init-db; flask run
