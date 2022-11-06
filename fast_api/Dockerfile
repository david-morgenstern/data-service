FROM python:3.11.0-slim-bullseye

ADD requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /app

EXPOSE 8080

CMD uvicorn --app-dir /app app:app --reload --port 8080 --host 0.0.0.0
