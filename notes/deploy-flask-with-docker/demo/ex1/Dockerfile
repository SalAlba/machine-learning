FROM python:3.6-alpine

RUN apk --update add bash vim
ENV STATIC_URL /static

COPY app /app
COPY run_app.py run_app.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


ENTRYPOINT ["python"]
CMD ["run_app.py"]