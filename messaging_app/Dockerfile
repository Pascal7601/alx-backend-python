FROM python:3.10-alpine

WORKDIR /app

RUN apk update \
    && apk add --no-cache \
    gcc \
    musl-dev \
    pkgconf \
    mariadb-connector-c-dev \
    && rm -rf /var/cache/apk/*

COPY Requirements.txt .

RUN pip install -r Requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

