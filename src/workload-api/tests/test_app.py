import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from app.app import app
from app.models.workload import db

@pytest.fixture
def anyio_backend():
    return 'asyncio'

# @pytest.fixture(autouse=True)
# def setup_and_teardown_db():
#     # Clear the database before and after each test
#     db.drop_tables()
#     db.create_tables()

@pytest.mark.anyio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Running.."}

@pytest.mark.anyio
async def test_create_workload():
    workload = {
        "workload_type": "type1",
        "name": "Test Workload",
        "src_project": "project1",
        "src_dataset": "dataset1",
        "src_table": "table1",
        "src_column_name": "column1"
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/v1/workloads/", json=workload)
    assert response.status_code == 200
    data = response.json()
    assert data["workload_type"] == workload["workload_type"]
    assert data["name"] == workload["name"]
    assert data["src_project"] == workload["src_project"]
    assert data["src_dataset"] == workload["src_dataset"]
    assert data["src_table"] == workload["src_table"]
    assert data["src_column_name"] == workload["src_column_name"]
    assert data["status"] == "created"

@pytest.mark.anyio
async def test_create_workload_wrong_type():
    workload = {
        "workload_type": "type1",
        "name": "Test Workload",
        "src_project": "project1",
        "src_dataset": "dataset1",
        "src_table": "table1",
        "src_column_name": 123  # should be a string
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/v1/workloads/", json=workload)
    assert response.status_code == 422


@pytest.mark.anyio
async def test_create_workload_missing_field():
    workload = {
        "workload_type": "type1",
        "name": "Test Workload",
        "src_project": "project1",
        "src_dataset": "dataset1",
        "src_table": "table1",
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/v1/workloads/", json=workload)
    assert response.status_code == 422

@pytest.mark.anyio
async def test_read_workload():
    workload = {
        "workload_type": "type1",
        "name": "Test Workload",
        "src_project": "project1",
        "src_dataset": "dataset1",
        "src_table": "table1",
        "src_column_name": "column1"
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/v1/workloads/", json=workload)
    assert response.status_code == 200
    workload_id = response.json()["id"]
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(f"/api/v1/workloads/{workload_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == workload_id
    assert data["workload_type"] == workload["workload_type"]
    assert data["name"] == workload["name"]
    assert data["src_project"] == workload["src_project"]
    assert data["src_dataset"] == workload["src_dataset"]
    assert data["src_table"] == workload["src_table"]
    assert data["src_column_name"] == workload["src_column_name"]

@pytest.mark.anyio
async def test_read_all_workloads():
    workload = {
        "workload_type": "type1",
        "name": "Test Workload",
        "src_project": "project1",
        "src_dataset": "dataset1",
        "src_table": "table1",
        "src_column_name": "column1"
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        await ac.post("/api/v1/workloads/", json=workload)
        response = await ac.get("/api/v1/workloads/")
    assert response.status_code == 200
    data = response.json()
    assert type(data) == list

@pytest.mark.anyio
async def test_delete_workload():
    workload = {
        "workload_type": "type1",
        "name": "Test Workload",
        "src_project": "project1",
        "src_dataset": "dataset1",
        "src_table": "table1",
        "src_column_name": "column1"
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/v1/workloads/", json=workload)
    assert response.status_code == 200
    workload_id = response.json()["id"]
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete(f"/api/v1/workloads/{workload_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == workload_id
    assert data["workload_type"] == workload["workload_type"]
    assert data["name"] == workload["name"]
    assert data["src_project"] == workload["src_project"]
    assert data["src_dataset"] == workload["src_dataset"]
    assert data["src_table"] == workload["src_table"]
    assert data["src_column_name"] == workload["src_column_name"]
