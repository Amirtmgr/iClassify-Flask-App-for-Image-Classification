FROM python:3.10-slim-buster

LABEL author="Amir Thapa Magar"
COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /app/app.py
COPY static /app/static
COPY utils /app/utils
COPY models /app/models

WORKDIR /app

#ENTRYPOINT [ "python3" ]
#CMD [ "app.py" ]

#EXPOSE 8085

RUN groupadd -r atm && useradd -r -g atm atm
RUN chown -R atm. /app

USER atm

# $PORT is set by Heroku
CMD gunicorn --log-level=debug --bind 0.0.0.0:$PORT -k gevent app:app

