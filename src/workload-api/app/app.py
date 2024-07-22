## GENERAL IMPORTS
from http import HTTPStatus

## FASTAPI IMPORTS
from fastapi import FastAPI

## LOCAL IMPORTS
from app.routers import workload
from app.config import API_PREFIX

## start app
app = FastAPI()

## add routes
app.include_router(workload.router, prefix=API_PREFIX, tags=["workloads"])

### -- route for testing purposes - check if API is alive
@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Running..'}