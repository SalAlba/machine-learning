---
slug: deploy-flask-with-docker
date: 2020-06-28
title: Deploy Flask With Docker
banner: ./images/flask-docker.jpeg
published: true
---

# Deploy Flask With Docker
In this post we will see how to use Docker to deploy Flask app on production, share our app with others and more :heart:. Also I'm sending a huge thanks to [[m-godlewski]](https://github.com/m-godlewski).

> ⚠️ **TODO** What is Flask

> ⚠️ **TODO** What is Docker

> ⚠️ **TODO** What is Image

> ⚠️ **TODO** What is Container


> ⚠️**TODO** In this tutorial, you will create a Flask application and deploy it with Docker. This tutorial will also cover how to update an application after deployment.
## Table of contents

- [Prerequisites](#Prerequisites)
- [Install Docker](#install-docker)
- [Simple Flask Application](#simple-flask-application)
- [Build Image of Container](#build-image-of-container)
- [tl;dr](#)
- [Summarizing](#Summarizing)
- [Resources](#Resources)
- [TODO](#TODO)


## Prerequisites
+ Linux, Ubuntu 20. forget about windows 🤭.
+ Installed docker 🐋 on machine.

## Install Docker 

### Linux [[1]](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) [[2]](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)

There are many ways to install docker on ubuntu system check [official documentation](https://docs.docker.com/engine/install/ubuntu/) in this tutorial I will present installation using the repository.

```bash
$ sudo apt-get remove docker docker-engine docker.io containerd runc

$ sudo apt-get update

$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
   
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

$ sudo apt-key fingerprint 0EBFCD88

$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

$ sudo apt update


# Make sure you are about to install from the Docker repo instead of the default Ubuntu repo:
$ apt-cache policy docker-ce

$ sudo apt-get install docker-ce docker-ce-cli containerd.io

```

> Check if docker installed.

``` bash

$ sudo systemctl status docker
$ services docker status


● docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
     Active: active (running) since Fri 2020-07-10 14:09:27 CEST; 49s ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 28710 (dockerd)
      Tasks: 13
     Memory: 44.5M
     CGroup: /system.slice/docker.service
             └─28710 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock


```

> Check if docker is installed correctly by running the hello-world image.

``` bash
$ sudo docker run hello-world
```


### Windows
> ⚠️ TODO ...

### others 😩
> ⚠️ TODO ...

## Simple Flask Application [[1.2.]](#Resources)
Flask allow us to build application in very simple way just we need latest [Python](https://www.python.org/downloads/) and installed [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/#installation). Bellow example of basic Flask application.

``` python
# __init__.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!\n'

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return '{0} + {1} = {2}'.format(a, b, a+b)

# run the application ...
if __name__ == "__main__":
    app.run(host='0.0.0.0') # This important to get access into docker

```

To run this application there are several ways covered on [flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart), I will use just the basic one show bellow.

``` bash
$ python application.py
```

If every things goo well you should see logs printed on terminal like bellow telling, at which port application is listing.

```
 * Serving Flask app "application" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Build Image of Container
Whenever you start and want to deploy flask application to production, you must build image for container, the process is very easy just you have a special file called `Dockerfile`, this file will contain a set of rules for docker telling how  to build the specific image. So far so good bellow are example of `Dockerfile` for flask application

``` Dockerfile
# Dockerfile

FROM python:3.6-alpine

RUN apk --update add bash vim
ENV ENV_VARIABLE_FROM_DOCKER ENV_VARIABLE_VALUE

COPY __init__.py __init__.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["run_app.py"]
```

1. `FROM python:3.6-alpine` install python from [DockerHub](https://hub.docker.com/_/python).
2. `RUN apk --update add bash nano` install vim text editor, we can use it when we inside the container [see more](#).
3. `ENV ENV_VARIABLE_FROM_DOCKER ENV_VARIABLE_VALUE` environment variable for this docker image.
4. `COPY __init__.py __init__.py` copy the flask app, you can copy whole folder.
5. `COPY requirements.txt requirements.txt` copy the requirements file into docker.
6. `RUN pip install -r requirements.txt` install all required python package.
7. `ENTRYPOINT ["python"]` `CMD ["run_app.py"]` run flask app in container.


``` bash
# docker build -t <IMAGE_NAME> .

$ docker build -t my_image_name:latest .
```

1. Sets the name and tag for the new container image.
2. the dot `.` indicates the base directory where the container is to be built. This is the directory where the Dockerfile is located. 

check images list

``` bash
$ docker images -a

REPOSITORY          TAG                 IMAGE ID            CREATED              SIZE
my_image_name       latest              af73b3cf6a99        About a minute ago   110MB
```

``` bash
# docker run -p 8080:5000 -d --name <CONTAINER_NAME> <IMAGE_NAME>

$ docker run -p 8080:5000 -d --name my_container_name my_image_name
```
1. `-p` set ports.
2. `-d` the container runs as a foreground application, blocking your command prompt. 
3. `--name` name of the container


In terminal check if container app is running

``` bash
$ docker ps

CONTAINER ID        IMAGE               COMMAND               CREATED             STATUS              PORTS                    NAMES
d859fc976bff        my_container_name                 "python __init__.py"   8 seconds ago       Up 5 seconds        0.0.0.0:8080->5000/tcp   app

```
also check by curl or in browser

``` bash
$ curl 0.0.0.0:8080

Hello, World!
```


## tl;dr
List of docker examples [available here.](https://github.com/SalAlba/machine-learning/tree/master/notes/deploy-flask-with-docker/demo)

## Summarizing
### Advantage / Disadvantage ➕ ➖
TODO ... :blush:

### Notes
TODO ...

## Resources

1. [[1.1.] Book. Flask Web Development. Developing Web Applications with Python. 2nd](https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart)
2. [[1.2.] Flask Quick Start.](https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart)
3. [[1.3.] How To Build and Deploy a Flask Application Using Docker on Ubuntu 18.04.](https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04)
4. [[1.4.] The Flask Mega-Tutorial Part XIX: Deployment on Docker Containers.](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xix-deployment-on-docker-containers)

<!-- 
1. [[1.1.] MarkDown Template](https://gist.github.com/jonschlinkert/ac5d8122bfaaa394f896#sub-sub-heading-2)
2. [[1.2.] MarkDown TOC](https://github.com/jonschlinkert/markdown-toc/blob/master/README.md)
3. [[1.3.] Languages Supported by Github Flavored Markdown](http://www.rubycoloredglasses.com/2013/04/languages-supported-by-github-flavored-markdown/)
 -->

## TODO
...