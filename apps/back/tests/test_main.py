from fastapi.testclient import TestClient

from back.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"statut": "Serveur OK"}

