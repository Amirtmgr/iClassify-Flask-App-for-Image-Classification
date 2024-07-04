FROM python:3.10-slim-buster

COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /app/app.py
COPY static /app/static
COPY utils /app/utils
COPY models /app/models

WORKDIR /app


RUN groupadd -r dev && useradd -r -g dev dev
RUN chown -R dev:dev /app

USER dev

# $PORT is set by Heroku
CMD gunicorn --log-level=debug --bind 0.0.0.0:$PORT -k gevent app:app

