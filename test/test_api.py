from fastapi.testclient import TestClient
from base_fast_api_package.api.api import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
