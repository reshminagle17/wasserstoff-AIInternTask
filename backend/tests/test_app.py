from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_get_answer():
    response = client.get("/get-answer?query=What is AI?") 
    assert response.status_code == 200 
    assert response.json() == {"query": "What is AI?", "response": "This is a mock answer from the document!"}
