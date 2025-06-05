from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_users():
    """
    It should return a list of items with status code 200.
    """
    response = client.get("/api/users")
    assert response.status_code == 200

def test_getUser():
    """
    It should return a specific item with status code 200 when ID exists.
    """
    id = "61beb66a-7823-4dc2-86c1-41293f56aa37"
    response = client.get(f"/api/users/{id}")
    assert response.status_code == 200

def test_create_user():
    """
    It should create a new item and return it with status code 200.
    """
    body = {"id": "61beb66a-7823-4dc2-86c1-41293f56aa37", "username": "jn ndagano", "email": "jndev@gmail.com", "password": "12345678"}
    response = client.post("/api/users/", json=body)
    assert response.status_code == 200
    assert response.json() == body