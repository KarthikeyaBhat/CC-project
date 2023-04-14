# Follow Task-0 subtask-1

# syntax=docker/dockerfile:1

FROM python:3.8-alpine

COPY ./app/requirements.txt /app/requirements.txt
COPY . .
WORKDIR /app

RUN apk add --update \
&& pip install --upgrade pip  \
&& pip install -r requirements.txt \
&& rm -rf /var/cache/apk/*

COPY . .

CMD ["python3", "Exp.py"]