---
slug: deploy-flask-with-docker
date: 2020-06-28
title: Deploy Flask With Docker
banner: ./images/flask-docker.jpeg
published: true
---

# Deploy Flask With Docker
In this post we will see how to use Docker to deploy Flask app on production, share our app with others and more :heart:.

> ⚠️ TODO What is docker

> ⚠️ TODO What is Flask

## Table of contents

- [Prerequisites](#Prerequisites)
- [Install Docker](#install-docker)
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

## Build Image of Container
Whenever you start and want to deploy flask application to production, you must build container image, the process is very easy just you have a special file called `Dockerfile`, this file will contain a set of rules for docker allowing to build the specific image. So far so good bellow are example of `Dockerfile` for flask application

``` Dockerfile
# Dockerfile

FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt

```



## tl;dr
TODO ...

## Summarizing
### Advantage / Disadvantage ➕ ➖
TODO ... :blush:

### Notes
TODO ...

## Resources
1. [[1.1.] MarkDown Template](https://gist.github.com/jonschlinkert/ac5d8122bfaaa394f896#sub-sub-heading-2)
2. [[1.2.] MarkDown TOC](https://github.com/jonschlinkert/markdown-toc/blob/master/README.md)
3. [[1.3.] Languages Supported by Github Flavored Markdown](http://www.rubycoloredglasses.com/2013/04/languages-supported-by-github-flavored-markdown/)

## TODO
...