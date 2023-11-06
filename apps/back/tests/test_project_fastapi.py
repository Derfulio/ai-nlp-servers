from fastapi.testclient import TestClient
from back.main import app, ModelName

client = TestClient(app)


def test_nlp_back_server():
    model_names = [model.value for model in ModelName]
    assert model_names
    response = client.get("/models")
    assert response.status_code == 200
    assert response.json() == model_names
    articles = [
        {"text": "Ceci est un document"},
        {"text": "Ceci est un autre document"},
    ]
    data = {"articles": articles, "model": model_names[0]}
    response = client.post("/process/", json=data)
    assert response.status_code == 200
    result = response.json()["result"]
    assert len(result) == len(articles)
    assert [{"text": entry["text"]} for entry in result] == articles
    assert all("ents" in entry for entry in result)
