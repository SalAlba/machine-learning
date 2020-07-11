#!/bin/sh

clear

echo "======================== START ========================"

echo '>>'
docker ps

echo '>>'
docker stop my_docker_flask

echo '>>'
docker rm my_docker_flask

echo '>>'
docker rmi my_docker_flask

echo '>>'
docker build -t my_docker_flask .

echo '>>'
docker run --name my_docker_flask -d -p 8080:5000 my_docker_flask

echo '>>'
docker ps

# echo '>>'
# docker exec -it my_docker_flask bash

echo "======================== END ========================"