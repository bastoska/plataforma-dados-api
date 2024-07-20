FROM python:3.11-slim

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /app

COPY app/ app/

EXPOSE 8080

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8080"]
