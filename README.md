# Steps

## Basic

1. make venv
2. activate venv
3. make script.py
4. test app: python script.py
5. make requirements.txt
6. make dockerfile
7. build docker image: `docker build --tag <image-name>:<tag-name> .`
   1. tag-name is optional: `docker build --tag <image-name> .`
8. view image: `docker images`
9. rename tag/ tag images: `docker tag <image-name>:<old-tag-name> <tag-name>:<new-tag-name>`
10. untag image: `docker rmi <image-name>:<tag-name>`
11. run image as container: `docker run <image-name>`
12. publish container to local/host machine: `docker run -p <host-port>:<container-port> <image-name>`
    1. host-port: port outside container
    2. container-port: port inside container

## Compose

1. Make `docker-compose.yml`
2. running the compose: `docker-compose up`
