FROM python:3.11.0-slim-bullseye

ADD requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /app

ENTRYPOINT ["python",  "/app/scrape.py"]