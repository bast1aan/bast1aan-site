FROM python:3.12-slim

COPY ./requirements.txt /

RUN groupadd -r bast1aan
RUN useradd -r -g bast1aan bast1aan

RUN pip install -r /requirements.txt

COPY . /srv/bast1aan-site

WORKDIR /srv/bast1aan-site

USER bast1aan

ENV GUNICORN_APP=bast1aan.site.app:app

ENTRYPOINT ./entrypoint.sh
