from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def mock_query(mocker):
    mocker.patch(
        "app.routers.query.generate_response",
        return_value={
            "answer": "Mocked generated answer based on docs.",
            "contexts": ["Chunk 1", "Chunk 2"],
        },
    )

    response = client.post(
        "/api/v1/query", json={"prompt": "What is the project architecture?"}
    )
    return response


def test_query_success(mocker):
    response = mock_query(mocker)

    assert response.status_code == 200


def test_query_answer_returned(mocker):
    response = mock_query(mocker)
    data = response.json()

    assert "answer" in data


def test_query_contexts_returned(mocker):
    response = mock_query(mocker)
    data = response.json()

    assert "contexts" in data


def test_query_chunks_returned(mocker):
    response = mock_query(mocker)
    data = response.json()

    assert len(data["contexts"]) > 0


def test_query_missing_prompt():
    response = client.post("/api/v1/query", json={})

    assert response.status_code == 422
