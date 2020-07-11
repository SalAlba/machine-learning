#!/bin/sh
APP="docker_ex2"
OUTPUT_PROT=9090
clear

echo "======================== START ========================"

echo '>>'
docker ps

echo '>>'
docker stop $APP

echo '>>'
docker rm $APP

echo '>>'
docker rmi $APP

echo '>>'
docker build -t $APP .

echo '>>'
docker run --name $APP -d -p $OUTPUT_PROT:5000 $APP

echo '>>'
docker ps

# echo '>>'
# docker exec -it $APP bash

echo "======================== END ========================"