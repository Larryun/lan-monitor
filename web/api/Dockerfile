# use buster for compatibility on RPI
FROM python:3.6-buster

WORKDIR /usr/app/src

COPY ./lan_monitor /usr/app/src/lan_monitor
COPY ./web/api /usr/app/src/api
COPY ./requirements.txt /usr/app/src/api

RUN pip install -r ./api/requirements.txt &&\
    pip install ./lan_monitor

WORKDIR /usr/app/src/api
