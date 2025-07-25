# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY src/app.py .

CMD ["python", "app.py"]
