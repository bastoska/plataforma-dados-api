from pydantic import BaseModel
from datetime import datetime

class WorkloadBase(BaseModel):
    id: int
    workload_type: str
    name: str
    status: str
    created_at: datetime
    updated_at: datetime
    data_source_type: str
    data_source_location: str
    data_destination_type: str
    processing_type: str

# workload to be used in post (status, created_at, updated_at)
# are automatically created
class WorkloadCreate(BaseModel):
    workload_type: str
    name: str
    data_source_type: str
    data_source_location: str
    data_destination_type: str
    processing_type: str

class Workload(WorkloadBase):
    id: int

    class Config:
        orm_mode = True
