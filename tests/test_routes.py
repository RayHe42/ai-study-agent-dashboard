import importlib

import pytest
from fastapi.testclient import TestClient


@pytest.fixture(autouse=True)
def setup_temp_db(tmp_path, monkeypatch):
    db_path = str(tmp_path / "test.db")
    monkeypatch.setenv("STUDY_AGENT_DATABASE_PATH", db_path)

    # Reload config so it picks up the temp path
    import study_agent.config
    importlib.reload(study_agent.config)

    # Create the table in the temp DB
    from study_agent.database import init_db
    init_db(db_path)

    yield


@pytest.fixture
def client(setup_temp_db):
    # Import app after config is patched;
    # routes/notes.py reads DATABASE_PATH lazily inside get_db()
    import study_agent.main
    importlib.reload(study_agent.main)

    from study_agent.main import app
    return TestClient(app)


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_list_notes_empty(client):
    response = client.get("/api/notes/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_note(client):
    response = client.post(
        "/api/notes/",
        json={"title": "Test Note", "content": "Hello world"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Note"
    assert data["content"] == "Hello world"
    assert data["id"] is not None


def test_get_note(client):
    create_resp = client.post(
        "/api/notes/",
        json={"title": "Find Me", "content": "Some content"},
    )
    note_id = create_resp.json()["id"]

    response = client.get(f"/api/notes/{note_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Find Me"


def test_get_note_not_found(client):
    response = client.get("/api/notes/999")
    assert response.status_code == 404


def test_update_note(client):
    create_resp = client.post(
        "/api/notes/",
        json={"title": "Old", "content": "Old content"},
    )
    note_id = create_resp.json()["id"]

    response = client.put(
        f"/api/notes/{note_id}",
        json={"title": "New", "content": "New content"},
    )
    assert response.status_code == 200
    assert response.json()["title"] == "New"
    assert response.json()["content"] == "New content"


def test_update_note_not_found(client):
    response = client.put(
        "/api/notes/999",
        json={"title": "X", "content": "Y"},
    )
    assert response.status_code == 404


def test_delete_note(client):
    create_resp = client.post(
        "/api/notes/",
        json={"title": "Delete Me", "content": "Bye"},
    )
    note_id = create_resp.json()["id"]

    response = client.delete(f"/api/notes/{note_id}")
    assert response.status_code == 204

    # Confirm it's gone
    response = client.get(f"/api/notes/{note_id}")
    assert response.status_code == 404


def test_delete_note_not_found(client):
    response = client.delete("/api/notes/999")
    assert response.status_code == 404
