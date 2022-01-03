FROM python:3.6

WORKDIR /usr/app/src
ADD ./lan_monitor /usr/app/src/lan_monitor
ADD ./config /usr/app/src/

RUN python lan_monitor/setup.py install

#CMD ["python", "-u", "lan_monitor/main.py", "-c", "./config.dev.yaml", "-i", "5"]