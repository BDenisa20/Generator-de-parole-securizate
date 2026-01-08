FROM python:3.11-slim

WORKDIR /app

COPY . /app

ENTRYPOINT ["python", "main.py"]
CMD []