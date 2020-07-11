FROM python:3.6-alpine

ENV ENV_VARIABLE_FROM_DOCKER ENV_VARIABLE_FROM_DOCKER_BLA_BLA
RUN apk --update add bash vim

COPY app /app

COPY run_app.py run_app.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


ENTRYPOINT ["python"]
CMD ["run_app.py"]