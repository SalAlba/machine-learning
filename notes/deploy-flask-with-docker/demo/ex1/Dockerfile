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