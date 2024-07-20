from fastapi import APIRouter, HTTPException
from datetime import datetime
from app.models.workload import Workload
from app.schemas import workload as schemas

router = APIRouter()
workload_model = Workload()

@router.post("/workloads/", response_model=schemas.Workload)
def create_workload(workload: schemas.WorkloadCreate):
    workload_data = workload.dict()
    workload_data['id'] = len(workload_model.table) + 1
    workload_data['status'] = 'created'  # Default status
    workload_data['created_at'] = str(datetime.utcnow())
    workload_data['updated_at'] = str(datetime.utcnow())
    workload_model.insert(workload_data)
    return workload_data
    

@router.get("/workloads/{workload_id}", response_model=schemas.Workload)
def read_workload(workload_id: int):
    db_workload = workload_model.get(workload_id=workload_id)
    if db_workload is None:
        raise HTTPException(status_code=404, detail="Workload not found")
    return db_workload


@router.delete("/workloads/{workload_id}", response_model=schemas.Workload)
def delete_workload(workload_id: int):
    db_workload = workload_model.get(workload_id=workload_id)
    if db_workload is None:
        raise HTTPException(status_code=404, detail="Workload not found")
    workload_model.delete(workload_id)
    return db_workload


@router.get("/workloads/", response_model=list[schemas.Workload])
def read_all_workloads():
    return workload_model.get_all()
