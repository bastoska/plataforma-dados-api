## GENERAL IMPORTS
from datetime import datetime

## FASTAPI IMPORTS
from fastapi import APIRouter, HTTPException


## LOCAL IMPORTS
from app.models.workload import Workload
from app.schemas import workload as schemas
from app.utils import SparkBigqueryCounter


router = APIRouter()
workload_model = Workload()

@router.post("/workloads/", response_model=schemas.Workload)
def create_workload(workload: schemas.WorkloadCreate):
    """
    Creates a new workload.
    """
    workload_data = workload.dict()

    spark_bq_counter = SparkBigqueryCounter(**workload_data)
    
    workload_data['id'] = len(workload_model.table) + 1
    workload_data['status'] = 'created'  # Default status
    workload_data['created_at'] = str(datetime.utcnow())
    workload_data['updated_at'] = str(datetime.utcnow())
    workload_model.insert(workload_data)
    return workload_data
    

@router.get("/workloads/{workload_id}", response_model=schemas.Workload)
def read_workload(workload_id: int):
    """
    Get a given workload.
    """
    db_workload = workload_model.get(workload_id=workload_id)
    if db_workload is None:
        raise HTTPException(status_code=404, detail="Workload not found")
    return db_workload


@router.delete("/workloads/{workload_id}", response_model=schemas.Workload)
def delete_workload(workload_id: int):
    """
    Delete the provided workload
    """
    db_workload = workload_model.get(workload_id=workload_id)
    if db_workload is None:
        raise HTTPException(status_code=404, detail="Workload not found")
    workload_model.delete(workload_id)
    return db_workload


@router.get("/workloads/", response_model=list[schemas.Workload])
def read_all_workloads():
    """
    Returns all workloads in a list
    """
    return workload_model.get_all()


## TODO: endpoints bellow aren't finished yet
# @router.get("/workloads/{workload_id}", response_model=schemas.Workload)
def get_wordcount_workload(workload_id: int):
    """
    Returns all counted workds for a given workload id.
    """
    pass
    