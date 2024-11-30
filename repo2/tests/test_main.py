from fastapi.testclient import TestClient
from app.main import fastapi

client = TestClient(fastapi)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello from repo1!"
