FROM workload-api-requirements:1.0

WORKDIR /app

COPY app/ app/
COPY tests/ tests/
COPY pytest.ini pytest.ini

ENV PYTHONUNBUFFERED=1
EXPOSE 8080

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8080"]
