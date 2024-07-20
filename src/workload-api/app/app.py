from http import HTTPStatus

from fastapi import FastAPI
from app.routers import workload

app = FastAPI()

app.include_router(workload.router, prefix="/api/v1", tags=["workloads"])

@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Olá Mundo!'}