from fastapi.testclient import TestClient
from base_fast_api_package.api.api import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_get_jobs():
    response = client.get("/jobs")
    assert response.status_code == 200
    assert response.json() == {"jobs": ["job1", "job2", "job3"]}
