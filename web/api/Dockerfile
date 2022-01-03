FROM python:3.6

WORKDIR /usr/app/src

ADD ./lan_monitor /usr/app/src/lan_monitor
ADD ./web/api /usr/app/src/api
ADD ./requirements.txt /usr/app/src/api

RUN pip install -r ./api/requirements.txt &&\
    pip install ./lan_monitor

WORKDIR /usr/app/src/api
