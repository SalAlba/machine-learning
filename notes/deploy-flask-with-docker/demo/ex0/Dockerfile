FROM python:3.6-alpine

RUN apk --update add bash vim

COPY __init__.py __init__.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["__init__.py"]