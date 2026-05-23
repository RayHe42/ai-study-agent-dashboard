from fastapi.testclient import TestClient

from study_agent.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_home_page():
    response = client.get("/")
    assert response.status_code == 200


def test_list_notes_empty():
    response = client.get("/api/notes/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_note():
    response = client.post(
        "/api/notes/",
        json={"title": "Test Note", "content": "Hello world"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Note"
    assert data["content"] == "Hello world"
    assert data["id"] is not None


def test_get_note():
    create_resp = client.post(
        "/api/notes/",
        json={"title": "Find Me", "content": "Some content"},
    )
    note_id = create_resp.json()["id"]

    response = client.get(f"/api/notes/{note_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Find Me"


def test_get_note_not_found():
    response = client.get("/api/notes/999")
    assert response.status_code == 404
