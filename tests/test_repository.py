import pytest

from study_agent.database import get_connection, init_db
from study_agent import repository


@pytest.fixture
def conn(tmp_path):
    db_path = str(tmp_path / "test.db")
    init_db(db_path)
    c = get_connection(db_path)
    yield c
    c.close()


def test_insert_note(conn):
    note = repository.insert_note(conn, "Title", "Content")
    assert note["id"] is not None
    assert note["title"] == "Title"
    assert note["content"] == "Content"
    assert note["created_at"] is not None
    assert note["updated_at"] is not None


def test_select_all_notes_empty(conn):
    assert repository.select_all_notes(conn) == []


def test_select_all_notes(conn):
    repository.insert_note(conn, "A", "first")
    repository.insert_note(conn, "B", "second")
    notes = repository.select_all_notes(conn)
    assert len(notes) == 2
    assert notes[0]["title"] == "A"
    assert notes[1]["title"] == "B"


def test_select_note_by_id(conn):
    inserted = repository.insert_note(conn, "Title", "Content")
    found = repository.select_note_by_id(conn, inserted["id"])
    assert found is not None
    assert found["title"] == "Title"


def test_select_note_by_id_not_found(conn):
    assert repository.select_note_by_id(conn, 999) is None


def test_update_note(conn):
    inserted = repository.insert_note(conn, "Old", "Old content")
    updated = repository.update_note(conn, inserted["id"], "New", "New content")
    assert updated is not None
    assert updated["title"] == "New"
    assert updated["content"] == "New content"


def test_update_note_not_found(conn):
    assert repository.update_note(conn, 999, "X", "Y") is None


def test_delete_note(conn):
    inserted = repository.insert_note(conn, "Title", "Content")
    assert repository.delete_note(conn, inserted["id"]) is True
    assert repository.select_note_by_id(conn, inserted["id"]) is None


def test_delete_note_not_found(conn):
    assert repository.delete_note(conn, 999) is False
