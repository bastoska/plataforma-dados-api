from pydantic import BaseModel, Field
from datetime import datetime

class WorkloadBase(BaseModel):
    id: int
    workload_type: str
    name: str
    status: str
    created_at: datetime
    updated_at: datetime
    src_project: str
    src_dataset: str
    src_table: str
    src_column_name: str

# workload to be used in post (status, created_at, updated_at)
# are automatically created
class WorkloadCreate(BaseModel):
    workload_type: str
    name: str
    src_project: str
    src_dataset: str
    src_table: str
    src_column_name: str

class Workload(WorkloadBase):
    id: int

    class Config:
        orm_mode = True
