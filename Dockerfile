FROM python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .
WORKDIR /app/src

RUN python3 manage.py collectstatic
