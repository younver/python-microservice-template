from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health-check")
    assert response.status_code == 200

def test_endpoint():
    response = client.post("/endpoint", json={
        "some_field": "some_value"
        })
    assert response.status_code == 200
