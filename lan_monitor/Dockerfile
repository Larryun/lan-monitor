#FROM python:3.6

# use buster for compatibility on RPI
FROM python:3.6-buster

WORKDIR /usr/app/src
COPY ./lan_monitor /usr/app/src/lan_monitor
COPY ./config /usr/app/src/

#RUN python lan_monitor/setup.py install
RUN pip install ./lan_monitor

#CMD ["python", "-u", "lan_monitor/main.py", "-c", "./config.dev.yaml", "-i", "5"]