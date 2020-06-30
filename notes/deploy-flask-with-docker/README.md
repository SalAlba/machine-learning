---
slug: deploy-flask-with-docker
date: 2020-06-28
title: Deploy Flask With Docker
banner: ./images/flask-docker.jpeg
published: true
---

# Deploy Flask With Docker
In this post we will see how to use Docker to deploy Flask app on production, share our app with others and more :heart:.

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
- installed docker 🐋 on machine.

## Install Docker

### Linux
> ⚠️ TODO ...

### Windows
> ⚠️ TODO ...

### others 😩
> ⚠️ TODO ...

## Simple Flask Application [[1.2.]](#Resources)
Flask allow us to build application in very simple way just we need latest [Python](https://www.python.org/downloads/) and installed [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/#installation). Bellow example of basic Flask application.

``` python
# application.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return '{0} + {1} = {2}'.format(a, b, a+b)

# run the application ...
if __name__ == "__main__":
    app.run()

```

To run this application there are several ways covered on [flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart), I will use just the basic one show bellow.

``` bash
# bash

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

RUN adduser -D userAppliaction

WORKDIR /home/dirAppliaction

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn


COPY appliaction.py Dockerfile boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP appliaction.py

RUN chown -R appliaction:appliaction ./
USER appliaction

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]

```



## tl;dr
TODO ...

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