#!/bin/bash

SRC_DIRECTORY="./lan-monitor"

rm -rf $SRC_DIRECTORY

git clone https://github.com/Larryun/lan-monitor

cp ./docker-compose.prod.yaml $SRC_DIRECTORY/
cp ./api.config.prod.yaml $SRC_DIRECTORY/web/api/instance/
cp ./config.prod.yaml $SRC_DIRECTORY/config/
cp ./.env.production.local $SRC_DIRECTORY/web/frontend/

cd $SRC_DIRECTORY

sudo docker-compose -f docker-compose.prod.yaml build
sudo docker-compose -f docker-compose.prod.yaml down
sudo docker-compose -f docker-compose.prod.yaml up -d