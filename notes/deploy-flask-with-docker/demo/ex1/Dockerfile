FROM python:3.6-alpine

RUN apk --update add bash vim
ENV ENV_VARIABLE_FROM_DOCKER "Hello, World!"

COPY app /app
COPY run_app.py run_app.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


ENTRYPOINT ["python"]
CMD ["run_app.py"]