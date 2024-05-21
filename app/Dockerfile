FROM python:3.10-slim-bullseye

RUN mkdir /app
WORKDIR /app

COPY ./src /app/src
COPY ./requirement.txt /app

RUN pip install -r requirement.txt

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
