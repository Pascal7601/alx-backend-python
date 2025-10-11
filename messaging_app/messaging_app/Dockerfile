FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r Requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

