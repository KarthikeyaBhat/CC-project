# Follow Task-0 subtask-1

# syntax=docker/dockerfile:1

FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apk add --update \
&& pip install --upgrade pip  \
&& pip install -r requirements.txt \
&& rm -rf /var/cache/apk/*

COPY . .

CMD ["python3", "app.py"]