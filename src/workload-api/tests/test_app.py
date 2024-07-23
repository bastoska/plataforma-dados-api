import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from app.app import app
from app.models.workload import db

@pytest.fixture
def client():
    return TestClient(app)

# @pytest.fixture(autouse=True)
# def setup_and_teardown_db():
#     # Clear the database before and after each test
#     db.drop_tables()
#     db.create_tables()

def test_read_root(client):
    """
    Test the root route
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Running.."}

def test_create_workload(client):
    """
    Teste the creation of a correct workload
    """
    workload = {
        "workload_type": "type1",
        "name": "Test Workload",
        "src_project": "project1",
        "src_dataset": "dataset1",
        "src_table": "table1",
        "src_column_name": "column1"
    }
    response = client.post("/api/v1/workloads/", json=workload)
    assert response.status_code == 200
    data = response.json()
    assert data["workload_type"] == workload["workload_type"]
    assert data["name"] == workload["name"]
    assert data["src_project"] == workload["src_project"]
    assert data["src_dataset"] == workload["src_dataset"]
    assert data["src_table"] == workload["src_table"]
    assert data["src_column_name"] == workload["src_column_name"]
    assert data["status"] == "created"

def test_create_workload_wrong_type(client):
    """
    Test the creation of a workload with a wrong field data type
    """
    workload = {
        "workload_type": "type1",
        "name": "Test Workload",
        "src_project": "project1",
        "src_dataset": "dataset1",
        "src_table": "table1",
        "src_column_name": 123  # should be a string
    }
    response = client.post("/api/v1/workloads/", json=workload)
    assert response.status_code == 422

def test_create_workload_missing_field(client):
    """
    Test the creation of a workload with missing required field
    """
    workload = {
        "workload_type": "type1",
        "name": "Test Workload",
        "src_project": "project1",
        "src_dataset": "dataset1",
        "src_table": "table1",
    }
    response = client.post("/api/v1/workloads/", json=workload)
    assert response.status_code == 422

def test_read_workload(client):
    """
    Test the read of a workload with a given ID
    """
    workload = {
        "workload_type": "type1",
        "name": "Test Workload",
        "src_project": "project1",
        "src_dataset": "dataset1",
        "src_table": "table1",
        "src_column_name": "column1"
    }
    ## creating a workload to get an id to request
    response = client.post("/api/v1/workloads/", json=workload)
    assert response.status_code == 200
    workload_id = response.json()["id"]

    ## getting the created workload with the given workload_id
    response = client.get(f"/api/v1/workloads/{workload_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == workload_id
    assert data["workload_type"] == workload["workload_type"]
    assert data["name"] == workload["name"]
    assert data["src_project"] == workload["src_project"]
    assert data["src_dataset"] == workload["src_dataset"]
    assert data["src_table"] == workload["src_table"]
    assert data["src_column_name"] == workload["src_column_name"]

def test_read_all_workloads(client):
    """
    Test the read all workloads
    """
    workload = {
        "workload_type": "type1",
        "name": "Test Workload",
        "src_project": "project1",
        "src_dataset": "dataset1",
        "src_table": "table1",
        "src_column_name": "column1"
    }
    client.post("/api/v1/workloads/", json=workload)
    response = client.get("/api/v1/workloads/")
    assert response.status_code == 200
    data = response.json()
    assert type(data) == list

def test_delete_workload(client):
    """
    Test the deletion of the given workload id
    """
    workload = {
        "workload_type": "type1",
        "name": "Test Workload",
        "src_project": "project1",
        "src_dataset": "dataset1",
        "src_table": "table1",
        "src_column_name": "column1"
    }
    ## we first create a workload to have an id to delete
    response = client.post("/api/v1/workloads/", json=workload)
    assert response.status_code == 200
    workload_id = response.json()["id"]

    ## deleting the given workload_id
    response = client.delete(f"/api/v1/workloads/{workload_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == workload_id
    assert data["workload_type"] == workload["workload_type"]
    assert data["name"] == workload["name"]
    assert data["src_project"] == workload["src_project"]
    assert data["src_dataset"] == workload["src_dataset"]
    assert data["src_table"] == workload["src_table"]
    assert data["src_column_name"] == workload["src_column_name"]


def test_create_nonexist_prj(client):
    """
    Test the deletion of a workload with a nonexistent google cloud project
    """
    workload = {
        "workload_type": "type1",
        "name": "Test Fail Project",
        "src_project": "telconet_missing_project",
        "src_dataset": "dataset1",
        "src_table": "table1",
        "src_column_name": "column1"
    }
    response = client.post("/api/v1/workloads/", json=workload)
    assert response.status_code == 404


def test_create_nonexist_dataset(client):
    """
    Test the deletion of a workload with a nonexistent BQ dataset
    """
    workload = {
        "workload_type": "type1",
        "name": "Test Fail Dataset",
        "src_project": "project1",
        "src_dataset": "telconet_missing_dataset",
        "src_table": "table1",
        "src_column_name": "column1"
    }
    response = client.post("/api/v1/workloads/", json=workload)
    assert response.status_code == 404


def test_create_nonexist_table(client):
    """
    Test the deletion of a workload with a nonexistent BQ table
    """
    workload = {
        "workload_type": "type1",
        "name": "Test Fail Table",
        "src_project": "project1",
        "src_dataset": "dataset1",
        "src_table": "telconet_missing_table",
        "src_column_name": "column1"
    }
    response = client.post("/api/v1/workloads/", json=workload)
    assert response.status_code == 404
    